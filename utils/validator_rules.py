import json
import time
from _operator import itemgetter

from assertpy import assert_that, soft_assertions

from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_hoot import V2_GET_DATASET_SCAN, V2_GET_ISSUE_COUNTS
from endpoints.v2.controller_rule import V2_GET_RULE_BREAKS, V2_GET_RULE_OUTPUT2
from endpoints.v3.dataset_def_api import V3_DATASETDEFS_DATASET
from endpoints.v3.job_api import V3_JOBS_DATASET_RUNDATE_BREAKS_RULES
from endpoints.v3.rule_api import (
    V3_RULES,
    V3_RULES_DATASET_RULENAME_RUNID_BREAKS,
    V3_RULES_VALIDATE,
)
from utils.helper import BaseHelper
from utils.helper_break_records import BreakRecordsHelper
from utils.validator import (
    validate_downloaded_break_records_csv,
    validate_downloaded_break_records_json,
)
from utils.validator_pushdown_archived_breaks import (
    validate_pushdown_archived_break_records_count,
    validate_pushdown_archived_break_records_data,
    validate_pushdown_archived_break_records_query,
    validate_pushdown_archived_break_records_query_output,
)

breaks_helper = BreakRecordsHelper()
helper = BaseHelper()


def validate_rule_breaks(api_utils, dataset, run_id, expected_rule_breaks):
    """Validates rule breaks for a given dataset and runId.
    Expected rule breaks is from output of /v3/rules/{dataset}/breaks or /v2/getrulebreaks
    depending on the state of the use_v2_api parameter"""
    # Pullup rule break records have no unique key
    # Do not assume order returned is guaranteed
    # Sort lists by everything except runId and verify by index
    expected_rule_breaks_sorted = sorted(
        expected_rule_breaks, key=itemgetter("dataset", "ruleNm", "linkId")
    )
    # Extract the run date from the first 10 characters of the runId
    run_date = run_id[0:10]
    get_rule_break_params = {
        "dataset": dataset,
        "runDate": run_date,
    }
    rule_breaks = api_utils.get(
        V3_RULES + "/" + dataset + "/breaks",
        params=get_rule_break_params,
    )

    rule_breaks_sorted = sorted(rule_breaks, key=itemgetter("dataset", "ruleNm", "linkId"))

    assert_that(
        len(rule_breaks_sorted),
        f"Unexpected number of rule breaks detected.  "
        f"Expected: {len(expected_rule_breaks_sorted)} "
        f"Actual: {len(rule_breaks_sorted)}",
    ).is_equal_to(len(expected_rule_breaks_sorted))

    expected_run_id = run_id  # runId from the job run under test
    for index, expected_rule_break_record in enumerate(expected_rule_breaks_sorted, start=0):
        for key in expected_rule_break_record:
            if key == "runId":
                assert_that(
                    rule_breaks_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id}  "
                    f"Found: {expected_rule_break_record[key]} "
                    f"in {rule_breaks_sorted[index]}",
                ).is_equal_to(expected_run_id)
            else:
                assert_that(
                    rule_breaks_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_rule_break_record[key]}  "
                    f"Found: {rule_breaks_sorted[index][key]} "
                    f"in {rule_breaks_sorted[index]}",
                ).is_equal_to(expected_rule_break_record[key])
        assert_that(
            len(rule_breaks_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_rule_break_record)}  "
            f"Found: {len(rule_breaks_sorted[index])} "
            f"in {rule_breaks_sorted[index]}",
        ).is_equal_to(len(expected_rule_break_record))


def validate_rule_breaks_v2(api_utils, dataset, run_id, expected_rule_breaks):
    """Validates rule breaks for a given dataset and runId.
    Expected rule breaks is from output of /v2/getrulebreaks"""
    # Pullup rule break records have no unique key
    # Do not assume order returned is guaranteed
    # Sort lists by everything except runId/runIdStr and verify by index
    expected_rule_breaks_sorted = sorted(
        expected_rule_breaks, key=itemgetter("dataset", "ruleNm", "linkId")
    )
    # Extract the run date from the first 10 characters of the runId
    run_date = run_id[0:10]
    get_rule_break_params = {"dataset": dataset, "runId": run_id}
    rule_breaks = api_utils.get(
        V2_GET_RULE_BREAKS,
        params=get_rule_break_params,
    )

    rule_breaks_sorted = sorted(rule_breaks, key=itemgetter("dataset", "ruleNm", "linkId"))

    assert_that(
        len(rule_breaks_sorted),
        f"Unexpected number of rule breaks detected.  "
        f"Expected: {len(expected_rule_breaks_sorted)} "
        f"Actual: {len(rule_breaks_sorted)}",
    ).is_equal_to(len(expected_rule_breaks_sorted))

    expected_run_id = run_id  # runId from the job run under test
    expected_run_id_str = run_date + " 00:00:00"  # runIdStr for V2 test
    for index, expected_rule_break_record in enumerate(expected_rule_breaks_sorted, start=0):
        for key in expected_rule_break_record:
            if key == "runId":
                assert_that(
                    rule_breaks_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id}  "
                    f"Found: {expected_rule_break_record[key]} "
                    f"in {rule_breaks_sorted[index]}",
                ).is_equal_to(expected_run_id)
            elif key == "runIdStr":
                assert_that(
                    rule_breaks_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id}  "
                    f"Found: {expected_rule_break_record[key]} "
                    f"in {rule_breaks_sorted[index]}",
                ).is_equal_to(expected_run_id_str)
            else:
                assert_that(
                    rule_breaks_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_rule_break_record[key]}  "
                    f"Found: {rule_breaks_sorted[index][key]} "
                    f"in {rule_breaks_sorted[index]}",
                ).is_equal_to(expected_rule_break_record[key])
        assert_that(
            len(rule_breaks_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_rule_break_record)}  "
            f"Found: {len(rule_breaks_sorted[index])} "
            f"in {rule_breaks_sorted[index]}",
        ).is_equal_to(len(expected_rule_break_record))


def validate_rules_findings(
    api_utils,
    dataset,
    run_id,
    expected_rules_findings,
    compare_link_ds_to_nolink_ds=False,
    skip_exception_msg_check=False,
):
    """Validates rule output for a given dataset and runId.
    Expected rules findings is from output of /v2/getruleoutput2"""
    expected_rules_output = expected_rules_findings["data"]
    expected_rule_count = len(expected_rules_output)
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    rule_output_list = api_utils.get(V2_GET_RULE_OUTPUT2, params=dataset_and_runid)["data"]

    validate_rules_count(api_utils, dataset_and_runid, expected_rule_count)
    validate_rules_score(api_utils, dataset_and_runid, rule_output_list)
    validate_rules_findings_details(
        expected_rules_output,
        rule_output_list,
        run_id,
        compare_link_ds_to_nolink_ds,
        skip_exception_msg_check,
    )


def validate_rules_count(api_utils, dataset_and_runid, expected_rules_count):
    """
    Verify the count of rules findings displayed on the Rules tab of the finding page
    :param api_utils: api_utils
    :param dataset_and_runid: A dictionary containing dataset and runId
    :param expected_rules_count: The expected count of rules findings
    """
    issue_type = "RULE"
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_count_rule_count = issue_count_response[issue_type]

    sleep_interval = 1
    timeout = 10
    issue_count_rule_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_rule_count,
        expected_rules_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_rule_count,
        f"Expected {expected_rules_count} rules, found {issue_count_rule_count} rules.",
    ).is_equal_to(expected_rules_count)


def validate_rules_score(api_utils, dataset_and_runid_params, rule_output_list):
    max_valid_rules_score = 100

    # Verify score shown in rule tab
    dataset_scan_response = api_utils.get(V2_GET_DATASET_SCAN, params=dataset_and_runid_params)
    visible_rule_score = dataset_scan_response["scoreRule"]

    total_rule_score = 0
    for rule_output in rule_output_list:
        total_rule_score += rule_output["score"]
    expected_rule_score = min(total_rule_score, max_valid_rules_score)

    # Delays of less than 1 second are intermittently seen for rule scores
    # to be retrieved on S3 to JDBC test and possibly others
    # Retry for a short time if the score is too low
    sleep_interval = 1
    timeout = 3  # Maximum wait time in seconds
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < timeout and visible_rule_score < expected_rule_score:
        time.sleep(sleep_interval)
        dataset_scan_response = api_utils.get(V2_GET_DATASET_SCAN, params=dataset_and_runid_params)
        elapsed_time = time.time() - start_time
        visible_rule_score = dataset_scan_response["scoreRule"]
    assert_that(
        visible_rule_score,
        f"Expected rule score to be: {expected_rule_score}  Actual: {visible_rule_score}",
    ).is_equal_to(expected_rule_score)


def validate_rules_findings_details(
    expected_rules_findings,
    rule_output_list,
    run_id,
    compare_link_ds_to_nolink_ds=False,
    skip_exception_msg_check=False,
):
    expected_rule_detail_count = len(expected_rules_findings)
    rule_detail_count = len(rule_output_list)
    assert_that(
        rule_detail_count,
        f"Rule output does not contain the expected number of rules. "
        f"Expected rule output count: {expected_rule_detail_count}, "
        f"Actual rule output count: {rule_detail_count}, "
        f"Expected rule output: {expected_rules_findings}, "
        f"Actual rule output: {rule_output_list}",
    ).is_equal_to(expected_rule_detail_count)
    # Verify details of rule output
    # More data is returned than is validated
    # Only validate data that should be the same from run to run
    # (no unique ids, values that differ from instance to instance...)
    # Only data returned by one API is validated
    # "Records" value is calculated in UI backend from percent thus unavailable
    # "isActive" value in the UI returned by other APIs and not validated here
    expected_run_id = run_id  # runId from the job run under test
    expected_rule_output_dict = {
        expected_rule_output["ruleNm"]: expected_rule_output
        for expected_rule_output in expected_rules_findings
    }
    rule_output_dict = {rule_output["ruleNm"]: rule_output for rule_output in rule_output_list}
    validated_keys = [
        "dataset",
        "runId",
        "ruleNm",
        "ruleType",
        "ruleValue",
        "score",
        "perc",
        "exception",
        "breakMsg",
        "dimId",
        "dimName",
        "ruleCondition",
        "totalCount",
        "rowsBreaking",
        "tolerance",
    ]
    # These values will be different when comparing a dataset which has archive break records
    # enabled to a different dataset which does not.
    if compare_link_ds_to_nolink_ds:
        validated_keys.remove("dataset")
        validated_keys.remove("ruleValue")
        validated_keys.remove("ruleCondition")
    if skip_exception_msg_check:
        validated_keys.remove("exception")
    for rule_name in expected_rule_output_dict.keys():
        if rule_output_dict[rule_name]:
            for key in validated_keys:
                if key == "runId":
                    assert_that(
                        rule_output_dict[rule_name][key],
                        f"Expected {key} to be "
                        f"{expected_run_id} "
                        f"but found {rule_output_dict[rule_name][key]} "
                        f"in {rule_output_dict[rule_name]}",
                    ).is_equal_to(expected_run_id)
                else:
                    assert_that(
                        rule_output_dict[rule_name][key],
                        f"Expected {key} to be "
                        f"{expected_rule_output_dict[rule_name][key]} "
                        f"but found {rule_output_dict[rule_name][key]} "
                        f"in {rule_output_dict[rule_name]}",
                    ).is_equal_to(expected_rule_output_dict[rule_name][key])
            assert_that(
                len(rule_output_dict[rule_name]),
                "Key count does not match expected. "
                "Expected number of keys: "
                f"{len(expected_rule_output_dict[rule_name])}  "
                f"Found: {len(rule_output_dict[rule_name])} "
                f"in {rule_output_dict[rule_name]}",
            ).is_equal_to(len(expected_rule_output_dict[rule_name]))
        else:
            raise AssertionError(f"Rule {expected_rule_output_dict[rule_name]} not found.")


def validate_pushdown_rules_archived_break_records(
    api_utils,
    connection,
    dataset,
    run_id,
    expected_breaks,
    expected_queried_break_records,
    write_sql_out=False,
):
    """
    Validate pushdown shapes archived break records
    :param api_utils: str, api_utils
    :param connection: str, connection name
    :param dataset: str, dataset name
    :param run_id: str, runId
    :param expected_breaks: list, expected break records from collibra_dq_rules extracted from
    the output of /v2/getsqlresult using the extract_sql_result_from_data_preview helper method
    :param expected_queried_break_records: list, expected break records from the query written to
    collibra_dq_breaks for the dataset.  Submitted as extracted from the output of /v2/getsqlresult
    using the extract_sql_result_from_data_preview helper method
    :param write_sql_out: bool, If True, write the extracted SQL output to the console instead of
    validating.  This is useful for writing new tests or updating existing tests' expected results.
    :return:

    Example of using kwargs in tests:
    kwargs = {"timeout:5", "proxies": {"http:" "proxy.example.com"}}
    response = get(endpoint, params, **kwargs)
    """
    connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
    expected_run_id = run_id
    query_validation_finding_type = "RULES"
    run_date = run_id[0:10]
    validated_keys = [
        "dataset",
        "run_id",
        "rule_name",
        "link_id",
    ]

    database_brand = connection_details["dbBrandName"]
    if database_brand == "ATHENA":
        breaks_queries = breaks_helper.build_athena_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "BIGQUERY":
        breaks_queries = breaks_helper.build_bigquery_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "DATABRICKS":
        breaks_queries = (
            breaks_helper.build_databricks_pushdown_archived_rules_break_record_sql_statements(
                api_utils, connection, dataset, run_id
            )
        )
    elif database_brand == "REDSHIFT":
        breaks_queries = breaks_helper.build_redshift_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SAP":
        breaks_queries = breaks_helper.build_saphana_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SNOWFLAKE":
        breaks_queries = breaks_helper.build_snowflake_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SQLSERVER":
        breaks_queries = breaks_helper.build_sqlserver_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "TRINO":
        breaks_queries = breaks_helper.build_trino_pushdown_archived_rules_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    else:
        raise ValueError(f"No rules query support for: {database_brand}.")

    # Write processed sql output to the console instead of validating
    # when adding new tests' expected results to the repo
    break_records = breaks_helper.get_pushdown_archived_breaks(
        api_utils, connection_details, run_id, breaks_queries, write_sql_out
    )

    if not write_sql_out:
        validate_pushdown_archived_break_records_count(
            break_records["breaks"],
            expected_breaks,
            run_id,
        )
        validate_pushdown_archived_break_records_data(
            break_records["breaks"],
            expected_breaks,
            expected_run_id,
            validated_keys,
        )
        validate_pushdown_archived_break_records_query_output(
            break_records["queried_break_records"],
            expected_queried_break_records,
        )

    query_limit_value = breaks_helper.get_unlimited_query_limit_value(connection_details)
    break_records_query = helper.run_query_and_extract_result(
        api_utils,
        breaks_queries["recordQuery"],
        connection,
        limit=query_limit_value,
    )[0]["query"]

    validate_pushdown_archived_break_records_query(
        api_utils,
        dataset,
        run_date,
        query_validation_finding_type,
        break_records_query,
    )


def validate_pushdown_rule_validation(
    api_utils,
    dataset_defs,
    rule_definition,
    expected_rule_output=None,
    expect_error=False,
):
    """Validate the response from validating the syntax of a rule for a pushdown dataset.
    Supports SQLF and SQLG rule types."""
    connection = dataset_defs["pushdown"]["connectionName"]
    connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
    rule_name = rule_definition["ruleNm"]

    rule_validation_params = {
        "ruleType": rule_definition["ruleType"],
        "ruleValue": rule_definition["ruleValue"],
        "filterQuery": rule_definition["filterQuery"],
    }
    rule_validation_endpoint = V3_RULES_VALIDATE.format(dataset=dataset_defs["dataset"])
    validation_response = api_utils.post(
        rule_validation_endpoint,
        params=rule_validation_params,
        return_json=False,
    )

    if connection_details["dbBrandName"] == "BIGQUERY":
        if not expected_rule_output:
            raise ValueError("No expected rule output supplied for BigQuery rule validation.")
        expected_bigquery_responses = helper.build_pushdown_bigquery_rule_validation_response(
            dataset_defs, rule_definition, expected_rule_output
        )
        expected_status_code = expected_bigquery_responses["expected_status_code"]
        expected_message = expected_bigquery_responses["expected_message"]
    elif expect_error:
        expected_status_code = 400
        expected_message = "Syntax error in rule:" + rule_definition["ruleValue"] + "."
    else:
        expected_status_code = 200
        expected_message = "Syntax of rule " + rule_definition["ruleValue"] + " is correct."

    with soft_assertions():
        assert_that(
            validation_response.status_code, f"Unexpected status code for rule {rule_name}."
        ).is_equal_to(expected_status_code)
        assert_that(
            validation_response.content.decode("utf-8"), f"Unexpected message for rule {rule_name}."
        ).is_equal_to(expected_message)


# pylint: disable-next=too-many-arguments
def validate_downloaded_job_rule_breaks(
    api_utils,
    dataset,
    run_date,
    response_format,
    expected_rule_breaks,
    limit=0,
    rule_name=None,
    write_rule_output=False,
):
    """
    Retrieve and validate rule break records from the specified dataset run.  Returns rule breaks
    for all rules on the dataset.
    :param api_utils: API Utils
    :param dataset: The dataset to be validated
    :param run_date: The dataset run date to be validated
    :param response_format: String indicating CSV or JSON
    :param expected_rule_breaks: Expected system output
    :param limit: Limit on the number of records returned.  Default to 0 which indicates no limit.
    :param rule_name: The rule name for which to download breaks.  Default to null which downloads
    all rule breaks for the dataset.
    :param write_rule_output: Boolean used to turn on writing records to the console instead of
    validating.  This improves efficiency when writing new tests as the test writer can enable this
    flag and the system will export results that can be stored with little modification.
    :return:
    """
    dataset_details = api_utils.get(V3_DATASETDEFS_DATASET.format(dataset=dataset))
    breaks_output = api_utils.get(
        V3_JOBS_DATASET_RUNDATE_BREAKS_RULES.format(
            dataset=dataset,
            runDate=run_date,
        ),
        params={"format": response_format, "limit": limit, "ruleName": rule_name},
        return_json=False,
    )
    rule_breaks = breaks_output.text
    if response_format == "CSV":
        validate_downloaded_break_records_csv(rule_breaks, expected_rule_breaks, write_rule_output)
    elif response_format == "JSON":
        rule_breaks_json = json.loads(breaks_output.text)
        if write_rule_output:
            print("Downloaded JSON Rule breaks:")
            print(rule_breaks_json)
        elif (
            dataset_details["connectionType"] == "PUSHDOWN"
            and dataset_details["pushdown"]["sourceBreakRules"] is True
        ):
            rule_breaks_json_list = list(rule_breaks_json["Rules"])
            expected_rule_breaks_list = list(expected_rule_breaks["Rules"])
            validate_downloaded_break_records_json(rule_breaks_json_list, expected_rule_breaks_list)
        else:
            validate_downloaded_break_records_json(rule_breaks_json, expected_rule_breaks)
    else:
        raise ValueError(f"Download breaks format not supported: {response_format}")


def validate_downloaded_rule_breaks(
    api_utils,
    dataset,
    run_id,
    rule_name,
    expected_rule_breaks,
    limit=0,
    write_rule_output=False,
):
    """
    Retrieve and validate rule break records from the specified dataset run.  Returns rule breaks
    for only the rule specified.
    :param api_utils: API Utils
    :param dataset: The dataset to be validated
    :param run_id: The dataset runId to validate
    :param rule_name: The rule name to be validated
    :param expected_rule_breaks: Expected system output
    :param limit: Limit on the number of records returned.  Default to 0 which indicates no limit.
    :param write_rule_output: Boolean used to turn on writing records to the console instead of
    validating.  This improves efficiency when writing new tests as the test writer can enable this
    flag and the system will export results that can be stored with little modification.
    :return:
    """
    breaks_output = api_utils.get(
        V3_RULES_DATASET_RULENAME_RUNID_BREAKS.format(
            dataset=dataset,
            ruleName=rule_name,
            runId=run_id,
        ),
        params={"limit": limit},
        return_json=False,
    )
    rule_breaks = breaks_output.text
    validate_downloaded_break_records_csv(rule_breaks, expected_rule_breaks, write_rule_output)
