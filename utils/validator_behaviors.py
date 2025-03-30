from assertpy import assert_that

from endpoints.v2.controller_hoot import (
    V2_GET_TABLE_STATS,
    V2_GET_DATASET_SCORING,
    V2_BEHAVIOR_DETAILS,
)


def validate_behavior_findings_overview(api_utils, dataset, run_id, expected_table_stats):
    """Validate behavior findings overview on finding page.
    Currently only supports row count finding type.
    Expected table stats is output from /v2/gettablestats"""
    table_stats_params = {"dataset": dataset, "runId": run_id, "sense": 3}
    table_stats = api_utils.get(V2_GET_TABLE_STATS, table_stats_params)

    validate_behavior_count(expected_table_stats, table_stats)
    validate_behavior_score(api_utils, dataset, run_id, expected_table_stats)

    if "Row Count__ROW_COUNT" in expected_table_stats["dqItems"]:
        validate_row_count_findings_summary(api_utils, dataset, run_id, expected_table_stats)


def validate_behavior_count(expected_table_stats, table_stats):
    """Verify the correct number of behavior findings are reported."""
    expected_behavior_finding_count = len(expected_table_stats["dqItems"])
    behavior_finding_count = len(table_stats["dqItems"])
    assert_that(
        behavior_finding_count,
        f"Expected behavior score to be: {expected_behavior_finding_count}  "
        f"Actual: {behavior_finding_count}",
    ).is_equal_to(expected_behavior_finding_count)


def validate_behavior_score(api_utils, dataset, run_id, expected_table_stats):
    """Validate the behavior score displayed on the finding page."""
    max_valid_behavior_score = 100
    total_behavior_score = 0
    params_dataset_runid = {"dataset": dataset, "runId": run_id}

    for item in expected_table_stats["dqItems"]:
        total_behavior_score += expected_table_stats["dqItems"][item]["score"]
    expected_behavior_score = min(total_behavior_score, max_valid_behavior_score)

    dataset_scoring = api_utils.get(V2_GET_DATASET_SCORING, params=params_dataset_runid)
    visible_behavior_score = dataset_scoring["behaviorTotalScore"]

    assert_that(
        visible_behavior_score,
        f"Expected behavior score to be: {expected_behavior_score}  "
        f"Actual: {visible_behavior_score}",
    ).is_equal_to(expected_behavior_score)


def validate_row_count_findings_summary(api_utils, dataset, run_id, expected_table_stats):
    """Validate the details of row count findings listed on the finding page."""
    table_stats_params = {"dataset": dataset, "runId": run_id, "sense": 3}
    table_stats = api_utils.get(V2_GET_TABLE_STATS, params=table_stats_params)
    expected_row_count_data = expected_table_stats["dqItems"]["Row Count__ROW_COUNT"]
    row_count_data = table_stats["dqItems"]["Row Count__ROW_COUNT"]

    validated_keys = [
        "key",
        "name",
        "stndDev",
        "zscore",
        "mean",
        "value",
        "score",
        "perChange",
        "deltaPerChange",
        "verbose",
        "type",
        "linkId",
        "dqType",
        "lbAbs",
        "ubAbs",
        "lbZscore",
        "ubZscore",
        "rangeChart",
        "chartType",
        "chartHistory",
        "chartHistoryRange",
        "chartHistoryPassFail",
        "chartHistoryPassFailString",
        "chartHistoryMean",
        "passFail",
        "isManual",
        "isRootCause",
        "status",
        "adaptiveTier",
    ]

    for key in validated_keys:
        assert_that(
            row_count_data[key],
            f"Expected {key} to be: {expected_row_count_data[key]}  Found: {row_count_data[key]} "
            f"in {row_count_data}",
        ).is_equal_to(expected_row_count_data[key])

    row_count_data_key_count = len(row_count_data)
    expected_row_count_data_key_count = len(expected_row_count_data)
    assert_that(
        row_count_data_key_count,
        "Key count does not match expected. "
        f"Expected number of keys: {expected_row_count_data_key_count}  "
        f"Found: {row_count_data_key_count} "
        f"in {row_count_data}",
    ).is_equal_to(expected_row_count_data_key_count)


def validate_row_count_findings_details(api_utils, dataset, run_id, expected_row_count_details):
    """Validate the details of row count findings listed on the row count detail page.
    Expected row count details is output from /v2/behavior-details."""
    row_count_details_params = {
        "dataset": dataset,
        "runId": run_id,
        "field": "Row Count",
        "issueType": "ROW_COUNT",
    }
    row_count_details = api_utils.get(V2_BEHAVIOR_DETAILS, params=row_count_details_params)

    validated_keys = {
        "key",
        "name",
        "stndDev",
        "zscore",
        "mean",
        "value",
        "score",
        "perChange",
        "deltaPerChange",
        "verbose",
        "type",
        "linkId",
        "dqType",
        "lbAbs",
        "ubAbs",
        "lbZscore",
        "ubZscore",
        "rangeChart",
        "chartType",
        "chartHistory",
        "chartHistoryRange",
        "chartHistoryPassFail",
        "chartHistoryPassFailString",
        "chartHistoryMean",
        "passFail",
        "isManual",
        "isRootCause",
        "status",
        "adaptiveTier",
        "neverNegative",
    }

    for key in validated_keys:
        assert_that(
            row_count_details[key],
            f"Expected {key} to be: {expected_row_count_details[key]}  "
            f"Found: {row_count_details[key]} "
            f"in {row_count_details}",
        ).is_equal_to(expected_row_count_details[key])

    row_count_details_key_count = len(row_count_details)
    expected_row_count_details_key_count = len(expected_row_count_details)
    assert_that(
        row_count_details_key_count,
        "Key count does not match expected. "
        f"Expected number of keys: {expected_row_count_details_key_count}  "
        f"Found: {row_count_details_key_count} "
        f"in {row_count_details}",
    ).is_equal_to(expected_row_count_details_key_count)
