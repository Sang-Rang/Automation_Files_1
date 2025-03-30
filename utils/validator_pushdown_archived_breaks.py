from _operator import itemgetter
from assertpy import assert_that

from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v3.job_api import (
    V3_JOBS_DATASET_RUNDATE_BREAKS_DUPES,
    V3_JOBS_DATASET_RUNDATE_BREAKS_OUTLIERS,
    V3_JOBS_DATASET_RUNDATE_BREAKS_RULES,
    V3_JOBS_DATASET_RUNDATE_BREAKS_SHAPES,
)
from utils.helper import BaseHelper
from utils.helper_break_records import BreakRecordsHelper

breaks_helper = BreakRecordsHelper()
helper = BaseHelper()


def validate_pushdown_archived_break_records_count(breaks, expected_breaks, run_id):
    expected_break_count = len(expected_breaks)
    break_count = len(breaks)
    assert_that(
        break_count,
        f"Expected archived break record count to be: {expected_break_count} for runId {run_id} "
        f"Actual: {break_count}",
    ).is_equal_to(expected_break_count)


def validate_pushdown_archived_break_records_data(
    breaks, expected_breaks, expected_run_id, validated_keys
):
    """Verify specified fields of records stored in archived break records tables match
    expected values."""
    expected_breaks_sorted = sorted(expected_breaks, key=itemgetter(*validated_keys))
    breaks_sorted = sorted(breaks, key=itemgetter(*validated_keys))
    for index, expected_break in enumerate(expected_breaks_sorted):
        for key in validated_keys:
            if key == "run_id":
                assert_that(
                    breaks_sorted[index][key],
                    f"Expected {key} to be: {expected_run_id}  "
                    f"Found: {breaks_sorted[index][key]} "
                    f"in {breaks_sorted[index]}",
                ).is_equal_to(expected_run_id)
            else:
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


def validate_pushdown_archived_break_records_query_output(breaks, expected_breaks):
    """Verify records returned by the query stored in the collibra_dq_breaks table returns
    expected results."""
    assert_that(
        len(breaks),
        f"Expected query response record count: {len(expected_breaks)}  Found: {len(breaks)} "
        f"in {breaks}",
    ).is_equal_to(len(expected_breaks))

    for expected_break_record in expected_breaks:
        assert_that(breaks, "Expected break record not found in query output.").contains(
            expected_break_record
        )


def validate_pushdown_archived_break_records_query(
    api_utils,
    dataset,
    run_date,
    finding_type,
    expected_break_records_query,
):
    """
    Verify that the break records query retrieved through the API matches the expected query.
    :param api_utils: API Utils
    :param dataset: The dataset to validate
    :param run_date: The run date to validate
    :param finding_type: The finding type for query retrieval
    :param expected_break_records_query: The expected query for comparison
    :return:
    """
    if finding_type == "DUPES":
        break_records_query = api_utils.get(
            V3_JOBS_DATASET_RUNDATE_BREAKS_DUPES.format(dataset=dataset, runDate=run_date),
            params={"format": "SQL"},
            return_json=False,
        ).text
    elif finding_type == "OUTLIERS":
        break_records_query = api_utils.get(
            V3_JOBS_DATASET_RUNDATE_BREAKS_OUTLIERS.format(dataset=dataset, runDate=run_date),
            params={"format": "SQL"},
            return_json=False,
        ).text
    elif finding_type == "RULES":
        break_records_query = api_utils.get(
            V3_JOBS_DATASET_RUNDATE_BREAKS_RULES.format(dataset=dataset, runDate=run_date),
            params={"format": "SQL"},
            return_json=False,
        ).text
    elif finding_type == "SHAPES":
        break_records_query = api_utils.get(
            V3_JOBS_DATASET_RUNDATE_BREAKS_SHAPES.format(dataset=dataset, runDate=run_date),
            params={"format": "SQL"},
            return_json=False,
        ).text
    else:
        raise ValueError(f"Finding type {finding_type} not supported for API query retrieval.")

    assert_that(
        break_records_query,
        "Query retrieved from API does not match the expected query.",
    ).is_equal_to(expected_break_records_query)

def validate_pushdown_archived_break_records_single_rule_query_results(
        api_utils,
        dataset,
        run_id,
        connection,
        rule_name,
        expected_query_results,
        write_sql_out=False,
):
    run_date = run_id[0:10]
    connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
    limit_value = breaks_helper.get_unlimited_query_limit_value(connection_details)
    rule_archive_breaks_query = api_utils.get(
        V3_JOBS_DATASET_RUNDATE_BREAKS_RULES.format(dataset=dataset, runDate=run_date),
        params={"format": "SQL", "ruleName": rule_name},
        return_json=False,
    ).text

    queried_rule_break_records = BaseHelper.run_query_and_extract_result(
        api_utils, rule_archive_breaks_query, connection, limit=limit_value
    )
    if write_sql_out:
        print(
            str(len(queried_rule_break_records)) + " queried break records found for runId "
            + run_id + " and rule " + rule_name + "."
        )
        print(queried_rule_break_records)
    else:
        validate_pushdown_archived_break_records_query_output(
            queried_rule_break_records,
            expected_query_results,
        )
