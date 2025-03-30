import copy
from _operator import itemgetter

from assertpy import assert_that

from endpoints.v2.controller_admin import V2_GET_ADMIN_CONFIG
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_hoot import (
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
    V2_GET_OUTLIER,
)
from endpoints.v2.controller_outlier_opt import V2_OUTLIER_OPT
from utils.helper import BaseHelper
from utils.helper_break_records import BreakRecordsHelper
from utils.validator_pushdown_archived_breaks import (
    validate_pushdown_archived_break_records_count,
    validate_pushdown_archived_break_records_data,
    validate_pushdown_archived_break_records_query,
)

breaks_helper = BreakRecordsHelper()
helper = BaseHelper()


def validate_pushdown_outliers_archived_break_records(
    api_utils,
    connection,
    dataset,
    run_id,
    expected_breaks,
    expected_queried_break_records,
    write_sql_out=False,
):
    """
    Validate pushdown outliers archived break records
    :param api_utils: str, api_utils
    :param connection: str, connection name
    :param dataset: str, dataset name
    :param run_id: str, runId
    :param expected_breaks: list, expected break records from collibra_dq_outliers extracted from
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
    query_validation_finding_type = "OUTLIERS"
    run_date = run_id[0:10]
    validated_keys = [
        "dataset",
        "run_id",
        "key_column",
        "key_value",
        "value_column",
        "value",
        "date_value",
        "type",
        "median",
        "lb",
        "ub",
        "confidence",
        "cnt",
        "link_id",
        "is_outlier",
        "is_historical",
        "is_topn",
        "is_botn",
        "source_date",
        "frequency",
        "percentile",
    ]

    database_brand = connection_details["dbBrandName"]
    if database_brand == "BIGQUERY":
        breaks_queries = breaks_helper.build_bigquery_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "DATABRICKS":
        breaks_queries = breaks_helper.build_databricks_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SNOWFLAKE":
        breaks_queries = breaks_helper.build_snowflake_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "TRINO":
        breaks_queries = breaks_helper.build_trino_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SAP":
        breaks_queries = breaks_helper.build_saphana_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    else:
        raise ValueError(f"No outliers query support for {database_brand}.")

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
        validate_pushdown_outliers_archived_break_records_query_output(
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


def validate_pushdown_outliers_archived_break_records_query_output(breaks, expected_breaks):
    assert_that(
        len(breaks),
        f"Expected query response record count: {len(expected_breaks)}  Found: {len(breaks)} "
        f"in {breaks}",
    ).is_equal_to(len(expected_breaks))

    for break_record in breaks:
        del break_record["id"]

    for expected_break_record in expected_breaks:
        del expected_break_record["id"]
        assert_that(breaks, "Expected break record not found in query output.").contains(
            expected_break_record
        )


def validate_outliers_findings_not_present(api_utils, dataset_defs, run_id):
    """Validate no outliers findings are discovered for a dataset run."""
    expected_outliers = []
    dataset = dataset_defs["dataset"]
    params_dataset_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    outliers = api_utils.get(V2_GET_OUTLIER, params=params_dataset_runid)["data"]

    validate_outliers_config_count(api_utils, dataset_defs)
    validate_outliers_count(api_utils, expected_outliers, params_dataset_runid)
    validate_outliers_score(api_utils, outliers, params_dataset_runid)
    expected_outlier_count = len(expected_outliers)
    outlier_count = len(outliers)
    assert_that(
        outlier_count,
        f"Expected no outliers, found {outlier_count} for runId {run_id} in {outliers}",
    ).is_equal_to(expected_outlier_count)


def validate_outliers_findings(
    api_utils,
    dataset_defs,
    run_id,
    expected_outlier_findings,
    validate_details=True,
    compare_link_ds_to_nolink_ds=False,
):
    """Validate outlier findings for a given dataset and runId.  Expected outlier findings is from
    output of /v2/getoutlier.  Validate details by default; however allow for skipping this step
    to accommodate older tests that were not designed for detailed analysis.
    Default to comparing all values; however, setting the option to
    compare a dataset with linkId to one without will allow comparisons between outlier
    configurations with and without archive break records enabled."""
    dataset = dataset_defs["dataset"]
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    expected_outliers = expected_outlier_findings["data"]
    outliers = api_utils.get(V2_GET_OUTLIER, params=dataset_and_runid)["data"]

    validate_outliers_config_count(api_utils, dataset_defs)
    validate_outliers_count(api_utils, expected_outliers, dataset_and_runid)
    validate_outliers_score(api_utils, outliers, dataset_and_runid)
    if validate_details:
        validate_outliers_details(expected_outliers, outliers, run_id, compare_link_ds_to_nolink_ds)


def validate_outliers_config_count(api_utils, dataset_defs):
    """Validate that the expected number of outlier configurations are present for a dataset."""
    dataset = dataset_defs["dataset"]
    expected_outlier_config_count = len(dataset_defs["outliers"])

    outlier_configs_response = api_utils.get(
        V2_OUTLIER_OPT, params={"dataset": dataset}, return_json=False
    )
    outlier_configs = outlier_configs_response.json()
    outlier_config_count = len(outlier_configs["result"])

    assert_that(
        outlier_config_count,
        f"Expected outlier configuration count of {expected_outlier_config_count} "
        f"for dataset {dataset}. Found: {outlier_config_count} in: {outlier_configs}.",
    ).is_equal_to(expected_outlier_config_count)


def validate_outliers_count(api_utils, expected_outliers, dataset_and_runid):
    """
    :param api_utils: api_utils
    :param expected_outliers: The expected count of outliers findings
    :param dataset_and_runid: A dictionary containing dataset and runId
    :return:
    """
    expected_outlier_count = len(expected_outliers)
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_type = "OUTLIER"
    issue_count_outlier_count = issue_count_response[issue_type]
    run_id = dataset_and_runid["runId"]

    sleep_interval = 1
    timeout = 10
    issue_count_outlier_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_outlier_count,
        expected_outlier_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_outlier_count,
        f"Expected outlier count to be: {expected_outlier_count} for runId {run_id}. "
        f"Actual: {issue_count_outlier_count}",
    ).is_equal_to(expected_outlier_count)


def validate_outliers_score(api_utils, outlier_findings, params_dataset_runid):
    """Validate outlier score displayed on the finding page."""
    max_valid_outlier_score = 100
    run_id = params_dataset_runid["runId"]
    admin_config = api_utils.get(V2_GET_ADMIN_CONFIG)
    categorical_outlier_score_per_finding = None
    for setting in admin_config:
        if setting["colNm"] == "categoricalscore":
            categorical_outlier_score_per_finding = float(setting["colValue"])
            break
    if categorical_outlier_score_per_finding is None:
        raise ValueError("No categoricalscore present in configuration settings")
    dataset_scoring = api_utils.get(V2_GET_DATASET_SCORING, params=params_dataset_runid)
    numerical_outlier_score_per_finding = dataset_scoring["outlierScore"]
    visible_outlier_score = dataset_scoring["outlierTotalScore"]
    total_outlier_score = 0
    for outlier in outlier_findings:
        outlier_type = outlier["obsType"]
        if outlier_type == "OUTLIER_NUMERICAL":
            total_outlier_score += outlier["outCount"] * numerical_outlier_score_per_finding
        elif outlier_type == "OUTLIER_CATEGORICAL":
            total_outlier_score += categorical_outlier_score_per_finding
        else:
            raise ValueError(f"No support for score validation of outlier type: {outlier_type}")
    expected_outlier_score = min(total_outlier_score, max_valid_outlier_score)
    assert_that(
        visible_outlier_score,
        f"Expected outliers score to be: {expected_outlier_score} for runId {run_id}. "
        f"Actual: {visible_outlier_score}",
    ).is_equal_to(expected_outlier_score)


def validate_outliers_details(
    expected_outliers, outliers, run_id, compare_link_ds_to_nolink_ds=False
):
    """Validate outlier findings details displayed on the finding page."""
    # Outlier findings have no unique values that are consistent between runs
    # Verify length of expected and actual lists
    # Sort by all validated keys and iterate through
    expected_outlier_count = len(expected_outliers)
    actual_outlier_count = len(outliers)
    assert_that(
        expected_outlier_count,
        f"Expected outlier findings to have count: {expected_outlier_count}  "
        f"Actual count: {actual_outlier_count}",
    ).is_equal_to(actual_outlier_count)

    validated_keys = [
        "dataset",
        "runId",
        "outKeyColumn",
        "outColumn",
        "outValue",
        "obsSubType",
        "outMedian",
        "outCount",
        "keyArr",
        "lb",
        "ub",
        "confidence",
        "linkId",
        "linkIdArr",
        "obsType",
    ]
    sort_keys = copy.deepcopy(validated_keys)
    sort_keys.remove("runId")
    sort_keys.remove("linkId")
    sort_keys.remove("linkIdArr")

    expected_outliers_sorted = sorted(
        expected_outliers,
        key=itemgetter(*sort_keys),
    )
    outliers_sorted = sorted(
        outliers,
        key=itemgetter(*sort_keys),
    )
    # These values will be different when comparing a dataset which has archive break records
    # enabled to a different dataset which does not.
    if compare_link_ds_to_nolink_ds:
        validated_keys.remove("dataset")
        validated_keys.remove("linkId")
        validated_keys.remove("linkIdArr")

    expected_run_id = run_id  # runId from the job run under test
    for index, expected_outlier_finding in enumerate(expected_outliers_sorted, start=0):
        for key in validated_keys:
            if key == "runId":
                assert_that(
                    outliers_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id} "
                    f"Found: {outliers_sorted[index][key]} "
                    f"in {outliers_sorted[index]}",
                ).is_equal_to(expected_run_id)
            # Link id values reported can vary when multiple rows are returned for one outlier value
            elif key in ["linkId", "linkIdArr"] and expected_outlier_finding["outCount"] > 1:
                pass
            elif key == "linkId":
                assert_that(
                    outliers_sorted[index][key],
                    f"Expected {key} to be empty "
                    f"Found: {outliers_sorted[index][key]} "
                    f"in {outliers_sorted[index]}",
                ).is_empty()
            elif key == "linkIdArr":
                assert_that(
                    outliers_sorted[index][key],
                    f"Expected {key} to be empty "
                    f"Found: {outliers_sorted[index][key]} "
                    f"in {outliers_sorted[index]}",
                ).is_equal_to([""])
            else:
                assert_that(
                    outliers_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_outlier_finding[key]} for runId {run_id} "
                    f"Found: {outliers_sorted[index][key]} "
                    f"in {outliers_sorted[index]}",
                ).is_equal_to(expected_outlier_finding[key])
        assert_that(
            len(outliers_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_outlier_finding)} "
            f"Found: {len(outliers_sorted[index])} for runId {run_id} "
            f"in {outliers_sorted[index]}",
        ).is_equal_to(len(expected_outlier_finding))
