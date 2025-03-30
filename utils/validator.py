import json

from assertpy import assert_that
from _operator import itemgetter

from endpoints.v2.controller_catalog import V2_GET_DATA_ASSET
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_explorer import (
    V2_GET_EXECUTE_SQL_IN_SESSION_JDBC,
    V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS,
)
from endpoints.v2.controller_hoot import (
    V2_GET_DATA_PREVIEW_1,
    V2_GET_HOOT,
    V2_GET_RULES_DATA_PREVIEW_PAGING,
    V2_GET_SQL_RESULT,
    V2_GET_TABLE_STATS,
)
from endpoints.v2.controller_owl_options import V2_OWL_OPTIONS_GET
from endpoints.v2.controller_profile import (
    V2_GET_DATA_HISTOGRAM,
    V2_GET_DATASET_CORR,
    V2_GET_PROFILE_DELTA,
)
from endpoints.v3.dataset_def_api import V3_DATASETDEFS_DATASET, V3_DATASETDEFS_HOST
from endpoints.v3.rule_api import (
    V3_RULES,
    V3_RULES_DATASET,
    V3_RULES_RUN,
)
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper

helper = BaseHelper()


def validate_job_timezone(api_utils, dataset, run_id=PROD_RUN_ID, expected="UTC"):
    payload = {"dataset": dataset, "runId": run_id}
    hoot = api_utils.get(V2_GET_HOOT, payload)
    asset = api_utils.get(V2_GET_DATA_ASSET, payload)

    assert_that(hoot, "Time zone did not return in hoot call").contains_key("timeZone")
    assert_that(hoot["timeZone"], "Unexpected time zone").is_equal_to(expected)

    assert_that(asset, "Time zone did not return in data asset call").contains_key("timeZone")
    assert_that(asset["timeZone"], "Unexpected time zone").is_equal_to(expected)


def validate_array_dict(expected_data, found_data, custom_msg="", stringify=False):
    """Validate the data in an array of dictionaries"""
    for i, expected_item in enumerate(expected_data):
        for key, value in expected_item.items():
            msg = (
                f"{custom_msg} For {key}, found: {found_data[i][key]}, "
                f"but expected: {expected_item}",
            )
            if stringify:  # Change format to strings so #2 = string '2'
                assert_that(str(found_data[i][key]), msg).is_equal_to(str(value))
            else:
                assert_that(found_data[i][key], msg).is_equal_to(value)


def validate_explorer_data_preview_schema(
    api_utils, connection_name, table, columns, expected_schema_preview
):
    """Validate data preview schema preview for a table in explorer.
    Expected results are the output of /v2/getlistdataschemapreviewdbtablebycols"""
    connection_details = api_utils.get(
        V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection_name}
    )

    schema_preview_params = {
        "table": table,
        "aliasname": connection_name,
        "hostname": connection_details["hostname"],
        "drivername": connection_details["drivername"],
        "cols": columns,
    }
    schema_preview = api_utils.post(
        V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS, params=schema_preview_params
    )

    expected_schema_preview_length = len(expected_schema_preview)
    schema_preview_length = len(schema_preview)
    assert_that(
        schema_preview_length,
        "Schema preview has unexpected number of records"
        f"Expected: {expected_schema_preview_length}  "
        f"Found: {schema_preview_length}",
    ).is_equal_to(expected_schema_preview_length)

    # Iterate through schema data as data returned in a list of dictionaries in dictionaries.
    # Iterate through expected data instead of returned to handle duplicate rows being returned
    # erroneously.  Potential refactor to extract data and do more specific assertions.
    for expected_row in expected_schema_preview:
        assert_that(
            schema_preview, f"Expected data {expected_row} not found in {schema_preview}"
        ).contains(expected_row)


def validate_explorer_data_preview_sql(api_utils, connection, query, limit, expected_data_preview):
    """Validate data preview sql result for a table in explorer.
    Use a query with an order by clause that includes a unique key.
    Expected results are the output of /v2/getsqlresult"""
    get_sql_result_params = {
        "sql": query,
        "cxn": connection,
        "limit": limit,
    }
    data_preview = api_utils.post(V2_GET_SQL_RESULT, params=get_sql_result_params)

    expected_data_preview_length = len(expected_data_preview)
    data_preview_length = len(data_preview)
    assert_that(
        data_preview_length,
        "Data preview has unexpected structure. "
        f"Expected: {expected_data_preview_length} elements. "
        f"Found: {data_preview_length}",
    ).is_equal_to(expected_data_preview_length)

    expected_data_preview_rows_length = len(expected_data_preview["rows"])
    data_preview_rows_length = len(data_preview["rows"])
    assert_that(
        data_preview_rows_length,
        "Data preview has unexpected number of records. "
        f"Expected: {expected_data_preview_rows_length}  "
        f"Found: {data_preview_rows_length}",
    ).is_equal_to(expected_data_preview_rows_length)

    expected_data_preview_schema_length = len(expected_data_preview["schema"])
    data_preview_schema_length = len(data_preview["schema"])
    assert_that(
        data_preview_schema_length,
        "Data preview has unexpected number of schema elements. "
        f"Expected: {expected_data_preview_schema_length}  "
        f"Found: {data_preview_schema_length}",
    ).is_equal_to(expected_data_preview_schema_length)

    # Iterate through preview data as data is returned in a list of dictionaries in dictionaries.
    # Iterate through expected data instead of returned to handle duplicate rows being returned
    # erroneously.  Potential refactor to extract data and do more specific assertions.
    for expected_row in expected_data_preview["rows"]:
        assert_that(
            data_preview["rows"], f"Expected data {expected_row} not found in {data_preview}"
        ).contains(expected_row)

    for expected_schema_element in expected_data_preview["schema"]:
        assert_that(
            data_preview["schema"],
            f"Expected schema element {expected_schema_element} not found in {data_preview}",
        ).contains(expected_schema_element)

    expected_data_preview_exception = expected_data_preview["exception"]
    data_preview_exception = data_preview["exception"]
    assert_that(
        data_preview_exception,
        f"Expected exception to be: {expected_data_preview_exception}  "
        f"Found: {data_preview_exception} in {data_preview}.",
    ).is_equal_to(expected_data_preview_exception)

    expected_data_preview_row_count = expected_data_preview["rowCount"]
    data_preview_row_count = data_preview["rowCount"]
    assert_that(
        data_preview_row_count,
        f"Expected row count to be: {expected_data_preview_row_count}  "
        f"Found: {data_preview_row_count} in {data_preview}.",
    ).is_equal_to(expected_data_preview_row_count)


def validate_finding_page_data_preview(api_utils, dataset, run_id, expected_preview_data):
    """Validate data preview on finding page.
    Expected results are the output of /v2/getdatapreview1"""
    data_preview_params = {"dataset": dataset, "runId": run_id}
    preview_data = api_utils.get(V2_GET_DATA_PREVIEW_1, params=data_preview_params)

    validate_finding_page_data_preview_rows(expected_preview_data, preview_data)
    validate_finding_page_data_preview_schema(expected_preview_data, preview_data)


def validate_finding_page_data_preview_rows(expected_preview_data, preview_data):
    """Validate rows returned in finding page data preview
    Expected results are the output of /v2/getdatapreview1"""
    expected_row_count = len(expected_preview_data["rows"])
    row_count = len(preview_data["rows"])
    assert_that(
        row_count, f"Expected {expected_row_count} rows.  Found {row_count} rows"
    ).is_equal_to(expected_row_count)

    # Iterate through preview data records as data returned is a list of lists of dictionaries.
    # Iterate through expected data instead of returned to handle duplicate rows being returned
    # erroneously.  Potential refactor to extract data and do more specific assertions.
    for row in expected_preview_data["rows"]:
        assert_that(preview_data["rows"], f"Expected row {row} not found").contains(row)


def validate_finding_page_data_preview_schema(expected_preview_data, preview_data):
    """Validate schema information returned in finding page data preview
    Expected results are the output of /v2/getdatapreview1"""
    expected_column_count = len(expected_preview_data["schema"])
    column_count = len(preview_data["schema"])
    assert_that(
        column_count, f"Expected {expected_column_count} columns.  Found {column_count} columns."
    ).is_equal_to(expected_column_count)

    expected_preview_data_schema_dict = {
        expected_column["name"]: expected_column
        for expected_column in expected_preview_data["schema"]
    }
    preview_data_schema_dict = {column["name"]: column for column in preview_data["schema"]}
    for column_name in expected_preview_data_schema_dict.keys():
        if preview_data_schema_dict[column_name]:
            for key in expected_preview_data_schema_dict[column_name]:
                assert_that(
                    preview_data_schema_dict[column_name][key],
                    f"Expected {key} to be "
                    f"{expected_preview_data_schema_dict[column_name][key]} "
                    f"but found {preview_data_schema_dict[column_name][key]} "
                    f"in {preview_data_schema_dict[column_name]}",
                ).is_equal_to(expected_preview_data_schema_dict[column_name][key])
            assert_that(
                len(preview_data_schema_dict[column_name]),
                f"Key count does not match expected for column {column_name}. "
                f"Expected number of keys: {len(expected_preview_data_schema_dict[column_name])}  "
                f"Found: {len(preview_data_schema_dict[column_name])} "
                f"in {preview_data_schema_dict[column_name]}",
            ).is_equal_to(len(expected_preview_data_schema_dict[column_name]))
        else:
            raise AssertionError(f"Rule {preview_data_schema_dict[column_name]} not found.")


def compare_dicts_are_equal(dict1, dict2, excluded_keys=None, ignore_order=False):
    """Compare 2 dictionaries while excluding a specific keys from comparison,
     order can be ignored optionally"""
    for key, value1 in dict1.items():
        if excluded_keys and key in excluded_keys:
            continue
        value2 = dict2.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            compare_dicts_are_equal(value1, value2, excluded_keys, ignore_order)
        elif isinstance(value1, list) and isinstance(value2, list):
            compare_lists_are_equal(value1, value2, excluded_keys, ignore_order)
        else:
            assert value1 == value2, f"Key '{key}' has different values: {value1} != {value2}"
    for key, value2 in dict2.items():
        if excluded_keys and key in excluded_keys:
            continue
        value1 = dict1.get(key)
        if isinstance(value1, dict) and isinstance(value2, dict):
            compare_dicts_are_equal(value1, value2, excluded_keys, ignore_order)
        elif isinstance(value1, list) and isinstance(value2, list):
            compare_lists_are_equal(value1, value2, excluded_keys, ignore_order)
        else:
            assert value1 == value2, f"Key '{key}' has different values: {value1} != {value2}"


def compare_lists_are_equal(list1, list2, excluded_keys=None, ignore_order=False):
    """Compare 2 lists while excluding specified keys from comparison,
    order can be ignored optionally"""
    assert len(list1) == len(list2), "Lists have different lengths"
    if ignore_order:
        sorted1 = sorted(list1, key=lambda x: sorted(x.items()) if isinstance(x, dict) else x)
        sorted2 = sorted(list2, key=lambda x: sorted(x.items()) if isinstance(x, dict) else x)
    else:
        sorted1, sorted2 = list1, list2

    for item1, item2 in zip(sorted1, sorted2):
        if isinstance(item1, dict) and isinstance(item2, dict):
            compare_dicts_are_equal(item1, item2, excluded_keys, ignore_order)
        else:
            assert item1 == item2, f"List items are different: {item1} != {item2}"


def validate_profile_tab_details(api_utils, ds_name, run_id, expected_data):
    """Validate the data on the profiles page > profile tab"""
    # Expected data from: /v2/getprofiledeltasbyrunid

    # Results are an array of objects, and each object contains an object for:
    #   baseline, datasetField, historicalSchema, and currentSchema
    profile = api_utils.get(V2_GET_PROFILE_DELTA, {"dataset": ds_name, "runId": run_id})

    sorted_profile = sorted(profile, key=lambda x: x["colName"])
    sorted_expected = sorted(expected_data, key=lambda x: x["colName"])

    for i, expected_item in enumerate(sorted_expected):
        for key, value in expected_item.items():
            baseline = expected_item["baseline"]
            dataset_field = expected_item["datasetField"]
            historical_schema = expected_item["historicalSchema"]
            current_schema = expected_item["currentSchema"]

            # Validate all non-object data
            if key not in ["baseline", "datasetField", "historicalSchema", "currentSchema"]:
                assert_that(
                    sorted_profile[i][key], f"Profile data failure for key {key}"
                ).is_equal_to(value)

            compare_dicts_are_equal(baseline, sorted_profile[i]["baseline"])
            compare_dicts_are_equal(dataset_field, sorted_profile[i]["datasetField"], ["updtTs"])
            compare_dicts_are_equal(
                historical_schema, sorted_profile[i]["historicalSchema"], ["updatedAt"]
            )
            compare_dicts_are_equal(
                current_schema, sorted_profile[i]["currentSchema"], ["updatedAt"]
            )
    assert_that(len(sorted_profile), "Found unexpected profile tab data").is_equal_to(
        len(sorted_expected)
    )


def validate_histogram_tab_details(api_utils, ds_name, run_id, expected_data):
    """Validate the data on the profiles page > histogram tab"""
    # Expected data from: /v2/getdatahistogram
    histogram = api_utils.get(V2_GET_DATA_HISTOGRAM, {"dataset": ds_name, "runId": run_id})

    sorted_histogram = dict(sorted(histogram.items(), key=lambda x: x))
    sorted_expected = dict(sorted(expected_data.items(), key=lambda x: x))

    for category in sorted_expected:
        found_category = sorted_histogram[category]
        expected_category = sorted_expected[category]

        for key, value in expected_category.items():
            assert_that(value, f"Histogram data failure for {key}").is_equal_to(found_category[key])

    assert_that(len(sorted_histogram), "Found unexpected histogram data").is_equal_to(
        len(sorted_expected)
    )


def validate_correlation_tab_details(api_utils, ds_name, run_id, expected_data):
    """Validate the data on the profiles page > correlation tab"""
    # Expected data from: /v2/getdatasetcorr
    correlation = api_utils.get(V2_GET_DATASET_CORR, params={"dataset": ds_name, "runid": run_id})

    # Non-object data
    assert_that(expected_data["xAxisLabels"], "Correlation xAxisLabels failed").is_equal_to(
        correlation["xAxisLabels"]
    )
    assert_that(expected_data["yAxisLabels"], "Correlation yAxisLabels failed").is_equal_to(
        correlation["yAxisLabels"]
    )
    assert_that(expected_data["title"], "Correlation title failed").is_equal_to(
        correlation["title"]
    )
    assert_that(expected_data["lookup"], "Correlation lookup failed").is_equal_to(
        correlation["lookup"]
    )
    assert_that(expected_data["groupId"], "Correlation groupId failed").is_equal_to(
        correlation["groupId"]
    )

    # Object data
    compare_lists_are_equal(expected_data["relationships"], correlation["relationships"], None)
    compare_lists_are_equal(expected_data["labels"], correlation["labels"], None)

    for i, item in enumerate(expected_data["series"]):
        compare_lists_are_equal(item, correlation["series"][i], None)

    assert_that(len(correlation), "Found unexpected correlation data").is_equal_to(
        len(expected_data)
    )


def validate_rule_result_preview(api_utils, dataset, rule_def, expected_result_preview):
    """
    Retrieve and validate rule result preview.  Validates both pull up and pushdown datasets.
    Rules must be of supported types for each connection type.
    :param api_utils: API Utils
    :param dataset: The dataset for the rule to be validated
    :param rule_def: Definition of the rule to be validated
    :param expected_result_preview: Expected output for the rule result preview
    :return:
    """
    dataset_defs = api_utils.get(V3_DATASETDEFS_DATASET.format(dataset=dataset))
    connection_type = dataset_defs["connectionType"]
    filter_query = rule_def["filterQuery"]
    rule_name = rule_def["ruleNm"]
    rule_type = rule_def["ruleType"]
    rule_value = rule_def["ruleValue"]
    api_utils.delete(V3_RULES_DATASET.format(dataset=dataset), return_json=False)
    api_utils.post(V3_RULES, data=json.dumps(rule_def))

    if connection_type == "PULLUP":
        connection = dataset_defs["load"]["connectionName"]
        validation_query = rule_value
        if filter_query not in ("", None):
            validation_query = rule_value + " \u001F " + filter_query
        if rule_type in ["SQLF", "SQLG"]:
            execute_sql_params = {
                "connectionalias": connection,
                "datasetName": dataset,
                "sql": validation_query,
                "ruleType": rule_type,
            }
            result_preview = api_utils.get(
                V2_GET_EXECUTE_SQL_IN_SESSION_JDBC, params=execute_sql_params
            )
            compare_lists_are_equal(result_preview, expected_result_preview, None)
        elif rule_type == "NATIVE":
            get_sql_result_params = {"sql": rule_value, "cxn": connection}
            result_preview = api_utils.post(V2_GET_SQL_RESULT, params=get_sql_result_params)
            compare_dicts_are_equal(result_preview, expected_result_preview, None)
        else:
            raise ValueError(f"Results preview validation not supported for rule type: {rule_type}")
    elif connection_type == "PUSHDOWN":
        connection = dataset_defs["pushdown"]["connectionName"]
        if rule_type in ["SQLF", "SQLG"]:
            execute_sql_params = {
                "dataset": dataset,
                "connectionAlias": connection,
                "ruleName": rule_name,
                "ruleValue": rule_value,
                "ruleType": rule_type,
                "filterQuery": filter_query,
            }
            result_preview = api_utils.post(V3_RULES_RUN, params=execute_sql_params)
            compare_dicts_are_equal(result_preview, expected_result_preview, None)
        else:
            raise ValueError(f"Results preview validation not supported for rule type: {rule_type}")
    else:
        raise ValueError(f"Connection type {connection_type} not supported for validation.")


def validate_rule_data_preview(api_utils, dataset, run_id, rule_name, expected_rule_data_preview):
    rule_data_preview_params = {
        "dataset": dataset,
        "runId": run_id,
        "rowkey": rule_name,
        "length": expected_rule_data_preview["recordsTotal"],
        "start": 0,
        "draw": 1,
    }

    rule_data_preview_response = api_utils.get(
        V2_GET_RULES_DATA_PREVIEW_PAGING, params=rule_data_preview_params
    )

    compare_dicts_are_equal(
        rule_data_preview_response,
        expected_rule_data_preview,
    )


def validate_downloaded_break_records_csv(
    findings_text,
    expected_findings,
    write_rule_output=False,
):
    """
    Validate break records downloaded in csv format.
    :param findings_text: String containing returned records from the application
    :param expected_findings: List containing expected records with csv rows represented as
    individual members of the list
    :param write_rule_output: Boolean used to turn on writing records to the console instead of
    validating.  This improves efficiency when writing new tests as the test writer can enable this
    flag and the system will export results that can be stored with little modification.
    :return:
    """
    expected_header_line = expected_findings[0]
    expected_findings.remove(expected_findings[0])
    expected_break_lines_sorted = sorted(expected_findings)
    expected_findings_sorted = [expected_header_line]
    for index, line in enumerate(expected_break_lines_sorted, start=0):
        expected_findings_sorted.append(line)

    break_lines = findings_text.splitlines()
    header_line = break_lines[0]
    break_lines.remove(break_lines[0])
    rule_break_lines_sorted = sorted(break_lines)
    rule_break_output_sorted = [header_line]
    for index, line in enumerate(rule_break_lines_sorted, start=0):
        rule_break_output_sorted.append(line)

    if write_rule_output:
        print("Downloaded CSV Rule breaks:")
        print(rule_break_output_sorted)
    else:
        findings_count = len(rule_break_output_sorted)
        expected_findings_count = len(expected_findings_sorted)
        assert_that(
            findings_count,
            f"Expected {expected_findings_count} records returned.  "
            f"Found: {findings_count} in {rule_break_output_sorted}",
        ).is_equal_to(expected_findings_count)
        for index, expected_finding in enumerate(expected_findings_sorted, start=0):
            assert_that(
                rule_break_output_sorted[index],
                f"Expected: {expected_finding} "
                f"Found {rule_break_output_sorted[index]} in {rule_break_output_sorted}",
            ).is_equal_to(expected_finding)


def validate_downloaded_break_records_json(
    findings_json,
    expected_findings_json,
):
    """
    Validate break records downloaded in JSON format
    :param findings_json: String with json to be validated
    :param expected_findings_json: String with json representing expected results
    :return:
    """
    # Assumption: All records have the same keys so any one of them will do to determine keys
    keys = expected_findings_json[0].keys()
    findings_sorted = sorted(findings_json, key=itemgetter(*keys))
    expected_findings_sorted = sorted(expected_findings_json, key=itemgetter(*keys))

    findings_count = len(findings_sorted)
    expected_findings_count = len(expected_findings_sorted)

    assert_that(
        findings_count,
        f"Expected {expected_findings_count} records.  "
        f"Found {findings_count} in {expected_findings_sorted}",
    ).is_equal_to(expected_findings_count)

    for index, expected_finding in enumerate(expected_findings_sorted, start=0):
        for key in expected_finding:
            assert_that(
                findings_sorted[index][key],
                f"Expected {key} to be: {expected_finding[key]} "
                f"Found: {findings_sorted[index][key]} in {findings_sorted[index]}",
            ).is_equal_to(expected_finding[key])
        assert_that(
            len(findings_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_finding)} "
            f"Found: {len(findings_sorted[index])} "
            f"in {findings_sorted[index]}",
        ).is_equal_to(len(expected_finding))


def run_and_validate_pd_job(
    api_utils,
    dataset_defs,
    expected_run_id=None,
    expected_run_id_end=None,
    expected_row_count=None,
):
    """
    Run a pushdown job to create/update a dataset.  Validate the process completes as
    expected.  Optional validation of runId, runIdEnd, and row count.
    :param api_utils: API Utils
    :param dataset_defs: Dataset definition for the pushdown dataset to be generated
    :param expected_run_id: Optional parameter.  If present, validate this runId is returned by
    the DQ job.
    :param expected_run_id_end: Optional parameter.  If present, validate this runIdEnd
    is returned by the DQ job.
    :param expected_row_count: Optional parameter.  If present, validate this number of rows
    are returned in the dataset
    :return:
    """
    job_response = helper.run_pushdown_job(api_utils, dataset_defs)
    job_status = job_response["status"]

    expected_job_status = "FINISHED"
    assert_that(
        job_status,
        f"Unexpected job status. Expected status: {expected_job_status}, "
        f"Found status: {job_status} in {job_response}",
    ).is_equal_to(expected_job_status)

    dataset_details = api_utils.get(V2_OWL_OPTIONS_GET, params={"dataset": dataset_defs["dataset"]})
    dataset_run_id = dataset_details["result"]["runId"]
    dataset_run_id_end = dataset_details["result"]["runIdEnd"]

    if expected_run_id:
        assert_that(
            dataset_run_id,
            f"Unexpected runId value.  Expected: {expected_run_id} "
            f"Found: {dataset_run_id} in {dataset_details}",
        ).is_equal_to(expected_run_id)

    if expected_run_id_end:
        assert_that(
            dataset_run_id_end,
            f"Unexpected runIdEnd value.  Expected: {expected_run_id_end} "
            f"Found: {dataset_run_id_end} in {dataset_details}",
        ).is_equal_to(expected_run_id_end)

    if expected_row_count:
        table_stats = api_utils.get(
            V2_GET_TABLE_STATS,
            params={"dataset": dataset_defs["dataset"], "runId": dataset_run_id, "sense": 3},
        )
        stats_row_count = table_stats["rows"]

        assert_that(
            stats_row_count,
            f"Expected row count to be {expected_row_count}, "
            f"found {stats_row_count} in {table_stats}",
        ).is_equal_to(expected_row_count)


def validate_dataset_metatags(api_utils, dataset_name, dataset_metatags):
    """
    This function validates whether the metadata tags (metaTags) of a dataset match the
     expected values.
    :param api_utils: API Utils
    :param dataset_name: Name of the dataset whose metadata needs validation
    :param dataset_metatags: Expected metadata tags that should be present in the dataset.
    :return:
    """
    dataset_def = api_utils.get(V3_DATASETDEFS_DATASET.format(dataset=dataset_name))
    assert_that(
        dataset_def["metaTags"], "MetaTags are not added to the dataset correctly."
    ).is_equal_to(dataset_metatags)


def validate_bulk_actions_manage_hosts(api_utils, parameters, expected_message):
    """
    send a PATCH request to update dataset definitions for hosts and
    validate the response against an expected error message.
    :param api_utils: API Utils
    :param parameters: the request parameters (host & datasets) to update dataset definitions
    :param expected_message: Expected error response from the API.
        If a string, it verifies that the API response contains the expected error message.
        If a dictionary, it verifies that the entire response matches the expected dictionary.
    :return:
    """
    response = api_utils.patch(V3_DATASETDEFS_HOST, params=parameters)
    if isinstance(expected_message, str):
        assert_that(response["message"], "Invalid Error Message").is_equal_to(expected_message)
    else:
        assert_that(response, "Invalid Error Message").is_equal_to(expected_message)
