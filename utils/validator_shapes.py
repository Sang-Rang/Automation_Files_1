import copy
from _operator import itemgetter

from assertpy import assert_that, soft_assertions

from endpoints.v2.controller_admin import V2_GET_ADMIN_CONFIG
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_hoot import (
    V2_GET_DATA_SHAPES,
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
)
from utils.helper import BaseHelper
from utils.helper_break_records import BreakRecordsHelper
from utils.validator_pushdown_archived_breaks import (
    validate_pushdown_archived_break_records_count,
    validate_pushdown_archived_break_records_data,
    validate_pushdown_archived_break_records_query,
    validate_pushdown_archived_break_records_query_output,
)

breaks_helper = BreakRecordsHelper()
helper = BaseHelper()


def validate_shapes_findings(
    api_utils, dataset_defs, run_id, expected_shapes, compare_link_ds_to_nolink_ds=False
):
    """Validates shapes findings for a given dataset and runId.
    Expected shapes is from output of /v2/getdatashapes"""
    expected_shapes_findings = expected_shapes["data"]
    expected_shapes_count = len(expected_shapes_findings)
    dataset = dataset_defs["dataset"]
    shapes_findings = api_utils.get(
        V2_GET_DATA_SHAPES,
        params={"dataset": dataset, "runId": run_id},
    )["data"]

    validate_shapes_count(api_utils, dataset, run_id, expected_shapes_count)
    validate_shapes_score(api_utils, dataset, run_id)
    validate_shapes_details(
        dataset_defs,
        run_id,
        expected_shapes_count,
        expected_shapes_findings,
        shapes_findings,
        compare_link_ds_to_nolink_ds,
    )


def validate_shapes_count(api_utils, dataset, run_id, expected_shapes_count):
    """
    Verify the count of shapes findings displayed on the Shapes tab of the finding page
    :param api_utils: api_utils
    :param dataset: The dataset to validate
    :param run_id: The runId to validate
    :param expected_shapes_count: The expected count of shapes findings
    """
    issue_type = "SHAPE"
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_count_shapes_count = issue_count_response[issue_type]

    sleep_interval = 1
    timeout = 10
    issue_count_shapes_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_shapes_count,
        expected_shapes_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_shapes_count,
        f"Expected shapes count to be: {expected_shapes_count}  "
        f"Actual: {issue_count_shapes_count}",
    ).is_equal_to(expected_shapes_count)


def validate_shapes_score(api_utils, dataset, run_id):
    issue_count_response = api_utils.get(
        V2_GET_ISSUE_COUNTS, params={"dataset": dataset, "runId": run_id}
    )
    issue_type = "SHAPE"
    issue_count_shapes_count = issue_count_response[issue_type]

    dataset_scoring = api_utils.get(
        V2_GET_DATASET_SCORING, params={"dataset": dataset, "runId": run_id}
    )
    shapes_score = dataset_scoring["datashapeTotalScore"]

    shapes_score_per_finding = dataset_scoring["datashapeScore"]
    expected_shapes_score = issue_count_shapes_count * shapes_score_per_finding
    assert_that(
        shapes_score,
        f"Expected shapes score to be: {expected_shapes_score}  Actual: {shapes_score}",
    ).is_equal_to(expected_shapes_score)


def validate_shapes_details(
    dataset_defs,
    run_id,
    expected_shapes_count,
    expected_shapes_findings,
    shapes_findings,
    compare_link_ds_to_nolink_ds=False,
):
    # Shapes findings have no unique values that are consistent between runs
    # Verify length of expected and actual lists
    # Sort by all relevant keys and iterate through
    shapes_count = len(shapes_findings)
    assert_that(
        shapes_count,
        f"Expected shapes findings to have count: {expected_shapes_count}  "
        f"Actual count: {shapes_count}",
    ).is_equal_to(expected_shapes_count)

    # Validate each relevant column in the sorted lists
    # Include runId as well as sorted columns
    # Validate that none of the returned values exceed settings
    validated_keys = [
        "dataset",
        "runId",
        "colName",
        "colFormat",
        "colFormatCnt",
        "linkId",
        "percent",
        "rowCountTotal",
        "definedSchema",
        "shapePerColumn",
    ]
    # These values will be different when comparing a dataset which has archive break records
    # enabled to a different dataset which does not.
    if compare_link_ds_to_nolink_ds:
        validated_keys.remove("dataset")
        validated_keys.remove("linkId")

    # Sort on relevant keys
    sort_keys = copy.deepcopy(validated_keys)
    sort_keys.remove("runId")
    expected_shapes_findings_sorted = sorted(
        expected_shapes_findings,
        key=itemgetter(*sort_keys),
    )
    shapes_findings_sorted = sorted(
        shapes_findings,
        key=itemgetter(*sort_keys),
    )
    expected_run_id = run_id  # runId from the job run under test
    occurrences_limit = float(dataset_defs["profile"]["shapeSensitivity"])
    format_per_col_limit = int(dataset_defs["profile"]["shapeMaxPerCol"])
    character_length_limit = int(dataset_defs["profile"]["shapeMaxColSize"])
    for index, expected_shapes_finding in enumerate(expected_shapes_findings_sorted, start=0):
        for key in validated_keys:
            if key == "runId":
                assert_that(
                    shapes_findings_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id}  "
                    f"Found: {shapes_findings_sorted[index][key]} "
                    f"in {shapes_findings_sorted[index]}",
                ).is_equal_to(expected_run_id)
            else:
                assert_that(
                    shapes_findings_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_shapes_finding[key]}  "
                    f"Found: {shapes_findings_sorted[index][key]} "
                    f"in {shapes_findings_sorted[index]}",
                ).is_equal_to(expected_shapes_finding[key])
        with soft_assertions():
            assert_that(
                shapes_findings_sorted[index]["percent"],
                "Occurrences exceed specified setting. "
                f"Expected percent to be less than {occurrences_limit}  "
                f"Found: {shapes_findings_sorted[index]['percent']} "
                f"in {shapes_findings_sorted[index]}",
            ).is_less_than_or_equal_to(occurrences_limit)
            assert_that(
                shapes_findings_sorted[index]["shapePerColumn"],
                "Shapes per column exceeds specified setting. "
                "Expected shapePerColumn "
                f"to be less than {format_per_col_limit}  "
                f"Found: {shapes_findings_sorted[index]['shapePerColumn']} "
                f"in {shapes_findings_sorted[index]}",
            ).is_less_than_or_equal_to(format_per_col_limit)
            assert_that(
                len(shapes_findings_sorted[index]["colFormat"]),
                "Shape length exceeds specified setting. Expected length of: "
                f"{shapes_findings_sorted[index]['colFormat']} "
                f"to be less than {character_length_limit}  "
                "Length found was: "
                f"{len(shapes_findings_sorted[index]['colFormat'])} "
                f"in {shapes_findings_sorted[index]}",
            ).is_less_than_or_equal_to(character_length_limit)
        assert_that(
            len(shapes_findings_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_shapes_finding)}  "
            f"Found: {len(shapes_findings_sorted[index])} "
            f"in {shapes_findings_sorted[index]}",
        ).is_equal_to(len(expected_shapes_finding))


def validate_shapes_limit(api_utils, dataset, run_id):
    """Verify shapes findings are properly limited as configured"""
    shapes_findings = api_utils.get(
        V2_GET_DATA_SHAPES,
        params={"dataset": dataset, "runId": run_id},
    )["data"]

    admin_limits = api_utils.get(V2_GET_ADMIN_CONFIG)
    shapes_storage_limit = 0
    shapes_display_limit = 0
    for setting in admin_limits:
        if setting["colNm"] == "datashapelimit":
            shapes_storage_limit = int(setting["colValue"])
        if setting["colNm"] == "datashapelimitui":
            shapes_display_limit = int(setting["colValue"])

    validate_shapes_count(api_utils, dataset, run_id, shapes_storage_limit)
    validate_shapes_score(api_utils, dataset, run_id)

    expected_shapes_detail_count = min(shapes_storage_limit, shapes_display_limit)
    shapes_detail_count = len(shapes_findings)
    assert_that(
        shapes_detail_count,
        f"Expected {expected_shapes_detail_count} shapes records displayed.  "
        f"Found: {shapes_detail_count}",
    ).is_equal_to(expected_shapes_detail_count)


def validate_pushdown_shapes_archived_break_records(
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
    :param expected_breaks: list, expected break records from collibra_dq_shapes extracted from
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
    query_validation_finding_type = "SHAPES"
    run_date = run_id[0:10]
    validated_keys = [
        "dataset",
        "run_id",
        "column_name",
        "shape_value",
        "shape_count",
        "shape_rate",
        "shape_length",
        "shape_type",
        "link_id",
    ]

    database_brand = connection_details["dbBrandName"]
    if database_brand == "BIGQUERY":
        breaks_queries = breaks_helper.build_bigquery_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "DATABRICKS":
        breaks_queries = breaks_helper.build_databricks_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SAP":
        breaks_queries = breaks_helper.build_saphana_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SNOWFLAKE":
        breaks_queries = breaks_helper.build_snowflake_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "TRINO":
        breaks_queries = breaks_helper.build_trino_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    else:
        raise ValueError(f"No shapes query support for: {database_brand}.")

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
