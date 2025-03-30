from _operator import itemgetter

from assertpy import assert_that

from endpoints.v2.controller_admin import V2_GET_ADMIN_CONFIG
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_hoot import (
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
    V2_GET_OBSERVATION_DETAILS_2,
)
from endpoints.v3.dataset_def_api import V3_DATASETDEFS_DATASET
from utils.helper import BaseHelper
from utils.helper_break_records import BreakRecordsHelper
from utils.validator_pushdown_archived_breaks import (
    validate_pushdown_archived_break_records_count,
    validate_pushdown_archived_break_records_data,
    validate_pushdown_archived_break_records_query,
)

breaks_helper = BreakRecordsHelper()
helper = BaseHelper()


def validate_dupes_findings(
    api_utils,
    dataset,
    run_id,
    expected_dupes_findings,
    compare_link_ds_to_nolink_ds=False,
):
    """
    Validate dupes findings for a given dataset and runId.
    :param api_utils: APIUtils
    :param dataset: The name of the dataset to validate
    :param run_id: The runId to validate
    :param expected_dupes_findings: Expected output of /v2/getobservationdetails2 using the
    specified dataset and runId
    :param compare_link_ds_to_nolink_ds: Boolean indicating whether we are comparing records from
    a dataset with archive breaks enabled to a dataset without archive breaks enabled.  When true,
    some validations are altered to account for expected differences in outputs.
    :return:
    """
    # Dupe detection returns two records for each finding
    # The two values determined to be dupes are both returned
    records_per_dupe = 2
    expected_dupes = expected_dupes_findings[0]["data"]
    expected_dupe_count = len(expected_dupes) / records_per_dupe

    get_observation_details_params = {
        "dataset": dataset,
        "runId": run_id,
        "type": "DUPE",
    }
    # Use index 0 which works at least as long as no other observation
    # types are present
    # Revisit to handle a more complex case if needed
    dupe_findings = api_utils.get(
        V2_GET_OBSERVATION_DETAILS_2, params=get_observation_details_params
    )[0]

    dataset_defs = api_utils.get(V3_DATASETDEFS_DATASET.format(dataset=dataset))

    if dataset_defs["connectionType"] == "PUSHDOWN":
        dupes_archive_breaks_enabled = dataset_defs["pushdown"]["sourceBreakDupes"]
    elif dataset_defs["connectionType"] == "PULLUP":
        dupes_archive_breaks_enabled = dataset_defs["load"]["archiveBreaks"]
    else:
        dupes_archive_breaks_enabled = False

    validate_dupes_count(api_utils, dataset, expected_dupe_count, run_id)
    validate_dupes_score(api_utils, dataset, run_id)
    validate_dupes_details(
        dupe_findings,
        expected_dupes,
        expected_dupes_findings,
        dupes_archive_breaks_enabled,
        dataset_defs,
        compare_link_ds_to_nolink_ds,
    )


def validate_dupes_count(api_utils, dataset, expected_dupe_count, run_id):
    """
    Verify the count of dupes findings displayed on the Dupes tab of the finding page
    :param api_utils: api_utils
    :param dataset: The dataset to validate
    :param expected_dupe_count: The expected count of dupes findings
    :param run_id: The runId to validate
    """
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    issue_type = "DUPE"
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_count_dupe_count = issue_count_response[issue_type]

    sleep_interval = 1
    timeout = 10
    issue_count_dupe_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_dupe_count,
        expected_dupe_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_dupe_count,
        f"Expected dupe count to be: {expected_dupe_count}  Actual: {issue_count_dupe_count}",
    ).is_equal_to(expected_dupe_count)


def validate_dupes_score(api_utils, dataset, run_id):
    """
    Validate the dupes score shown on the finding page.
    :param api_utils: APIUtils
    :param dataset: The dataset to validate
    :param run_id: The runId to validate
    :return:
    """
    issue_type = "DUPE"
    params_dataset_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=params_dataset_runid)
    dataset_scoring = api_utils.get(V2_GET_DATASET_SCORING, params=params_dataset_runid)
    dupe_score_per_finding = dataset_scoring["dupeScore"]
    visible_dupe_score = dataset_scoring["dupeTotalScore"]
    dupe_finding_count = issue_count_response[issue_type]
    total_dupe_score = dupe_finding_count * dupe_score_per_finding

    expected_dupe_score = total_dupe_score
    assert_that(
        visible_dupe_score,
        f"Expected dupe score to be: {expected_dupe_score}  Actual: {visible_dupe_score}",
    ).is_equal_to(expected_dupe_score)


def validate_dupes_details(
    dupe_findings,
    expected_dupes,
    expected_dupes_findings,
    dupes_archive_breaks_enabled,
    dataset_defs,
    compare_link_ds_to_nolink_ds=False,
):
    """
    Validate the dupes details presented on the finding page.
    :param dupe_findings: The output of /v2/getobservationdetails2 for the dataset under test
    :param expected_dupes: The portion of the /v2/getobservationdetails2 output which contains
    dupes details
    :param expected_dupes_findings: Expected dupes output including dupes details and columns
    :param dupes_archive_breaks_enabled: Boolean indicating whether archive break records is enabled
    :param dataset_defs: The dataset definition which contains configuration used in validations
    :param compare_link_ds_to_nolink_ds: Boolean indicating whether we are comparing records from
    a dataset with archive breaks enabled to a dataset without archive breaks enabled
    :return:
    """
    ignore_case = dataset_defs["dupe"]["ignoreCase"]
    included_columns = dataset_defs["dupe"]["include"]
    excluded_columns = dataset_defs["dupe"]["exclude"]
    score_lower_bound = float(dataset_defs["dupe"]["lowerBound"])
    score_upper_bound = float(dataset_defs["dupe"]["upperBound"])
    is_dupes_exact_match = bool(dataset_defs["dupe"]["depth"] == 0)
    exact_match_score = "100"
    max_displayed_dupe_detail_count = 2

    # Columns returned vary depending on which columns contain detected dupes
    expected_column_count = len(expected_dupes_findings[0]["columns"])
    actual_column_count = len(dupe_findings["columns"])
    if compare_link_ds_to_nolink_ds:
        if dataset_defs["pushdown"]["sourceBreakDupes"]:
            actual_column_count -= len(excluded_columns)
        # owl_id is not returned in archive breaks and is not necessary to validate
        owl_id_column = {"data": "owl_id", "name": "owl_id", "title": "owl_id"}
        if (
            dupes_archive_breaks_enabled
            and owl_id_column in expected_dupes_findings[0]["columns"]
            and owl_id_column not in dupe_findings["columns"]
        ):
            expected_column_count -= 1
    assert_that(
        actual_column_count,
        f"Expected {expected_column_count} columns.  Found {actual_column_count} columns.",
    ).is_equal_to(expected_column_count)
    # Some columns' values vary from run to run.  Exclude those for validation.
    validation_columns = []
    for column in expected_dupes_findings[0]["columns"]:
        if column["name"] not in [
            "assignment_id",
            "assignment_uuid",
            "item_key",
            "owl_id",
            "item_value",
        ]:
            validation_columns.append(column["name"])
    dupes = dupe_findings["data"]
    expected_dupes_count_pre_processing = len(expected_dupes)
    dupes_count_pre_processing = len(dupes)
    assert_that(
        dupes_count_pre_processing,
        f"Expected {expected_dupes_count_pre_processing} dupes.  "
        f"Found {dupes_count_pre_processing} dupes.",
    ).is_equal_to(expected_dupes_count_pre_processing)

    expected_dupes = helper.prepare_dupe_list_for_validation(
        expected_dupes, ignore_case, included_columns, max_displayed_dupe_detail_count
    )
    dupes = helper.prepare_dupe_list_for_validation(
        dupes, ignore_case, included_columns, max_displayed_dupe_detail_count
    )

    expected_dupes_sorted = helper.filter_dupes_occurs(
        dupes_archive_breaks_enabled,
        compare_link_ds_to_nolink_ds,
        expected_dupes,
    )
    dupes_sorted = helper.filter_dupes_occurs(
        dupes_archive_breaks_enabled,
        compare_link_ds_to_nolink_ds,
        dupes,
    )
    expected_dupes_sorted = sorted(expected_dupes_sorted, key=itemgetter(*validation_columns))
    dupes_sorted = sorted(dupes_sorted, key=itemgetter(*validation_columns))
    expected_dupe_detail_count = len(expected_dupes_sorted)
    dupe_detail_count = len(dupes_sorted)
    assert_that(
        dupe_detail_count,
        f"Expected {expected_dupe_detail_count} dupes.  Found {dupe_detail_count} dupes.",
    ).is_equal_to(expected_dupe_detail_count)
    # Validate each relevant column in the sorted lists
    for index, expected_dupe in enumerate(expected_dupes_sorted, start=0):
        for column in validation_columns:
            assert_that(
                dupes_sorted[index][column],
                f"Expected {column} "
                f"to be: {expected_dupe[column]}  "
                f"Found: {dupes_sorted[index][column]} "
                f"in {dupes_sorted[index]}",
            ).is_equal_to(expected_dupe[column])
            if column == "score":
                if is_dupes_exact_match:
                    assert_that(
                        dupes_sorted[index][column],
                        f"Expected {column} to be: {exact_match_score}  "
                        f"Found: {dupes_sorted[index][column]} "
                        f"in {dupes_sorted[index]}",
                    ).is_equal_to(exact_match_score)
                else:
                    assert_that(
                        float(dupes_sorted[index][column]),
                        f"Expected {column} to be between: "
                        f"{score_lower_bound} and {score_upper_bound}"
                        f"Found: {dupes_sorted[index][column]} "
                        f"in {dupes_sorted[index]}",
                    ).is_between(score_lower_bound, score_upper_bound)
        if not compare_link_ds_to_nolink_ds:
            assert_that(
                len(dupes_sorted[index]),
                "Key count does not match expected. "
                f"Expected number of keys: {len(expected_dupe)}  "
                f"Found: {len(dupes_sorted[index])} "
                f"in {dupes_sorted[index]}",
            ).is_equal_to(len(expected_dupe))


def validate_dupes_limit(api_utils, dataset, run_id):
    # Dupe detection returns two records for each finding
    # The two values determined to be dupes are both returned
    records_per_dupe = 2
    dupe_findings = api_utils.get(
        V2_GET_OBSERVATION_DETAILS_2,
        params={
            "dataset": dataset,
            "runId": run_id,
            "type": "DUPE",
        },
    )[0]
    dupes = dupe_findings["data"]

    admin_limits = api_utils.get(V2_GET_ADMIN_CONFIG)
    dupe_storage_limit = 0
    dupe_display_limit = 0
    for setting in admin_limits:
        if setting["colNm"] == "dupelimit":
            dupe_storage_limit = int(setting["colValue"])
        if setting["colNm"] == "dupelimitui":
            dupe_display_limit = int(setting["colValue"])

    validate_dupes_count(api_utils, dataset, dupe_storage_limit, run_id)
    validate_dupes_score(api_utils, dataset, run_id)

    expected_dupe_detail_count = min(dupe_storage_limit, dupe_display_limit)
    dupe_detail_count = len(dupes) / records_per_dupe
    assert_that(
        dupe_detail_count,
        f"Expected {expected_dupe_detail_count} dupe detail records.  Found: {dupe_detail_count}",
    ).is_equal_to(expected_dupe_detail_count)


def validate_pushdown_dupes_archived_break_records(
    api_utils,
    dataset_defs,
    run_id,
    expected_breaks,
    expected_queried_break_records,
    write_sql_out=False,
):
    """
    Validate pushdown outliers archived break records
    :param api_utils: str, api_utils
    :param dataset_defs: dict, dataset definition from which information necessary for validation
    will be extracted.  Use dataset_defs since it is already available rather than create a separate
    list of necessary parameters or add more parameters to the validation function.
    :param run_id: str, The runId for validation.
    :param expected_breaks: list, expected break records from collibra_dq_dupes extracted from
    the output of /v2/getsqlresult using the extract_sql_result_from_data_preview helper method
    :param expected_queried_break_records: list, expected break records from the query written to
    collibra_dq_breaks for the dataset.  Submitted as extracted from the output of /v2/getsqlresult
    using the extract_sql_result_from_data_preview helper method.
    :param write_sql_out: bool, If True, write the extracted SQL output to the console instead of
    validating.  This is useful for writing new tests or updating existing tests' expected results.
    :return:

    Example of using kwargs in tests:
    kwargs = {"timeout:5", "proxies": {"http:" "proxy.example.com"}}
    response = get(endpoint, params, **kwargs)
    """
    connection = dataset_defs["pushdown"]["connectionName"]
    dataset = dataset_defs["dataset"]
    table_columns = dataset_defs["dupe"]["include"] + dataset_defs["dupe"]["exclude"]
    connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
    expected_run_id = run_id
    query_validation_finding_type = "DUPES"
    run_date = run_id[0:10]
    validated_keys = [
        "dataset",
        "run_id",
        "dupe1",
        "dupe1_link_id",
        "dupe2",
        "dupe2_link_id",
        "score",
    ]
    query_validated_keys = table_columns + [
        "dupe1",
        "dupe2",
        "score",
    ]

    database_brand = connection_details["dbBrandName"]
    if database_brand == "BIGQUERY":
        breaks_queries = breaks_helper.build_bigquery_pushdown_archived_dupes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "DATABRICKS":
        breaks_queries = breaks_helper.build_databricks_pushdown_archived_dupes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SAP":
        breaks_queries = breaks_helper.build_saphana_pushdown_archived_dupes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "SNOWFLAKE":
        breaks_queries = breaks_helper.build_snowflake_pushdown_archived_dupes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    elif database_brand == "TRINO":
        breaks_queries = breaks_helper.build_trino_pushdown_archived_dupes_break_record_sql(
            api_utils, connection, dataset, run_id
        )
    else:
        raise ValueError(f"No dupes query support for {database_brand}.")

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
        validate_pushdown_archived_dupes_break_records_query_output(
            break_records["queried_break_records"],
            expected_queried_break_records,
            query_validated_keys,
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


def validate_pushdown_archived_dupes_break_records_query_output(
    breaks, expected_breaks, query_validated_keys
):
    """Verify records returned by the query stored in the collibra_dq_breaks table returns
    expected results."""
    assert_that(
        len(breaks),
        f"Expected query response record count: {len(expected_breaks)}  Found: {len(breaks)} "
        f"in {breaks}",
    ).is_equal_to(len(expected_breaks))

    expected_breaks_sorted = sorted(expected_breaks, key=itemgetter(*query_validated_keys))
    breaks_sorted = sorted(breaks, key=itemgetter(*query_validated_keys))
    for index, expected_break in enumerate(expected_breaks_sorted):
        for key in query_validated_keys:
            assert_that(
                breaks_sorted[index][key],
                f"Expected {key} to be: {expected_break[key]}  "
                f"Found: {breaks_sorted[index][key]} "
                f"in {breaks_sorted[index]}",
            ).is_equal_to(expected_break[key])
        assert_that(
            len(breaks_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_break)}  "
            f"Found: {len(breaks_sorted[index])} in {breaks_sorted[index]}",
        ).is_equal_to(len(expected_break))
