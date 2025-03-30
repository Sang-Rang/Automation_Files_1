from _operator import itemgetter

from assertpy import assert_that

from endpoints.v2.controller_hoot import (
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
    V2_GET_SOURCE_COUNT_COMPARISON,
    V2_GET_SOURCE_SCHEMA_COMPARISON,
    V2_GET_SOURCE_VALUE_COMPARISON,
)
from utils.helper import BaseHelper

helper = BaseHelper()


def validate_source_findings(
    api_utils,
    dataset_defs,
    run_id,
    expected_source_count_comparison,
    expected_source_schema_comparison,
    expected_source_value_comparison=None,
):
    """
    Validate that source findings match expected.  Values are not always enabled for source to
    target analysis so this parameter is optional.
    :param api_utils: APIUtils
    :param dataset_defs: The dataset definition for the dataset being evaluated
    :param run_id: The runId with results to validate
    :param expected_source_count_comparison: Expected source to target count findings.
    Output of /v2/get-source-count-comparison.
    :param expected_source_schema_comparison: Expected source to target schema findings.
    Output of /v2/get-source-schema-comparison.
    :param expected_source_value_comparison: Expected source to target values findings.
    Output of /v2/get-source-value-comparison.
    :return:
    """
    dataset = dataset_defs["dataset"]

    expected_source_finding_count = helper.determine_expected_source_finding_count(
        expected_source_count_comparison,
        expected_source_schema_comparison,
        expected_source_value_comparison,
    )

    validate_source_finding_count(api_utils, dataset, run_id, expected_source_finding_count)
    validate_source_score(api_utils, dataset, run_id)
    validate_source_count_details(api_utils, dataset, run_id, expected_source_count_comparison)
    validate_source_schema_details(api_utils, dataset, run_id, expected_source_schema_comparison)
    if expected_source_value_comparison is not None:
        validate_source_values_details(api_utils, dataset, run_id, expected_source_value_comparison)


def validate_source_finding_count(api_utils, dataset, run_id, expected_source_count):
    """
    Verify the count of source findings displayed on the Source tab of the finding page
    :param api_utils: api_utils
    :param dataset: The dataset to validate
    :param run_id: The runId to validate
    :param expected_source_count: The expected count of the specified finding type
    """
    issue_type = "SOURCE"
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_count_source_count = issue_count_response[issue_type]

    sleep_interval = 1
    timeout = 10
    issue_count_source_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_source_count,
        expected_source_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_source_count,
        f"Expected {issue_type} count to be: {expected_source_count}  "
        f"Actual: {issue_count_source_count}",
    ).is_equal_to(expected_source_count)


def validate_source_score(api_utils, dataset, run_id):
    issue_count_response = api_utils.get(
        V2_GET_ISSUE_COUNTS, params={"dataset": dataset, "runId": run_id}
    )
    issue_type = "SOURCE"
    issue_count_source_count = issue_count_response[issue_type]

    dataset_scoring = api_utils.get(
        V2_GET_DATASET_SCORING, params={"dataset": dataset, "runId": run_id}
    )
    source_total_score = dataset_scoring["validateSrcTotalScore"]

    source_score_per_finding = dataset_scoring["validateSrcScore"]
    expected_source_score = issue_count_source_count * source_score_per_finding
    assert_that(
        source_total_score,
        f"Expected source score to be: {expected_source_score}  Actual: {source_total_score}",
    ).is_equal_to(expected_source_score)


def validate_source_count_details(
    api_utils,
    dataset,
    run_id,
    expected_source_count,
):
    expected_source_count_data = expected_source_count["data"]
    expected_src_count_count = len(expected_source_count)
    expected_src_count_data_count = len(expected_source_count["data"])

    src_count = api_utils.get(
        V2_GET_SOURCE_COUNT_COMPARISON, params={"dataset": dataset, "runId": run_id}
    )
    src_count_data = src_count["data"]
    actual_src_count_count = len(src_count)
    actual_src_count_data_count = len(expected_source_count["data"])

    assert_that(
        expected_src_count_count,
        f"Expected source count findings to have count: {expected_src_count_count}  "
        f"Actual count: {actual_src_count_count}",
    ).is_equal_to(actual_src_count_count)
    assert_that(
        expected_src_count_data_count,
        f"Expected source count findings data to have count: {expected_src_count_data_count}  "
        f"Actual count: {actual_src_count_data_count}",
    ).is_equal_to(actual_src_count_data_count)

    validated_src_count_keys = [
        "targetRowCount",
        "sourceRowCount",
        "targetColCount",
        "sourceColCount",
    ]
    validated_src_count_data_keys = [
        "countType",
        "targetCount",
        "sourceCount",
        "change",
        "percChange",
        "description",
    ]

    expected_src_count_data_dict = {
        expected_src_count_data_output["countType"]: expected_src_count_data_output
        for expected_src_count_data_output in expected_source_count_data
    }
    src_count_data_dict = {
        src_count_data_output["countType"]: src_count_data_output
        for src_count_data_output in src_count_data
    }

    for key in validated_src_count_keys:
        assert_that(
            src_count[key],
            f"Expected {key} "
            f"to be: {expected_source_count[key]} for runId {run_id} "
            f"Found: {src_count[key]} "
            f"in {src_count}",
        ).is_equal_to(expected_source_count[key])
    assert_that(
        len(src_count),
        "Source count key count does not match expected. "
        f"Expected number of keys: {len(expected_source_count)} "
        f"Found: {len(src_count)} for runId {run_id} "
        f"in {src_count}",
    ).is_equal_to(len(expected_source_count))

    for count_type in expected_src_count_data_dict.keys():
        if src_count_data_dict[count_type]:
            for key in validated_src_count_data_keys:
                assert_that(
                    src_count_data_dict[count_type][key],
                    f"Expected {key} to be "
                    f"{expected_src_count_data_dict[count_type][key]} "
                    f"but found {src_count_data_dict[count_type][key]} "
                    f"in {src_count_data_dict[count_type]}",
                ).is_equal_to(expected_src_count_data_dict[count_type][key])
            assert_that(
                len(src_count_data_dict[count_type]),
                f"Source count deta key count does not match expected for countType {count_type}. "
                "Expected number of keys: "
                f"{len(expected_src_count_data_dict[count_type])}  "
                f"Found: {len(src_count_data_dict[count_type])} "
                f"in {src_count_data_dict[count_type]}",
            ).is_equal_to(len(expected_src_count_data_dict[count_type]))
        else:
            raise AssertionError(f"countType {expected_src_count_data_dict[count_type]} not found.")


def validate_source_schema_details(
    api_utils,
    dataset,
    run_id,
    expected_source_schema,
):
    expected_source_schema_data = expected_source_schema["data"]
    expected_src_schema_count = len(expected_source_schema)
    expected_src_schema_data_count = len(expected_source_schema["data"])

    src_schema = api_utils.get(
        V2_GET_SOURCE_SCHEMA_COMPARISON, params={"dataset": dataset, "runId": run_id}
    )
    src_schema_data = src_schema["data"]
    actual_src_schema_count = len(src_schema)
    actual_src_schema_data_count = len(expected_source_schema["data"])

    assert_that(
        expected_src_schema_count,
        f"Expected source schema findings to have count: {expected_src_schema_count}  "
        f"Actual count: {actual_src_schema_count}",
    ).is_equal_to(actual_src_schema_count)
    assert_that(
        expected_src_schema_data_count,
        f"Expected source schema findings data to have count: {expected_src_schema_data_count}  "
        f"Actual count: {actual_src_schema_data_count}",
    ).is_equal_to(actual_src_schema_data_count)

    validated_src_schema_keys = [
        "colOrderPassing",
        "percMatching",
        "percPassing",
        "checkType",
        "checkCase",
        "checkColOrder",
        "targetToSourceMap",
        "colOrderAssignmentId",
        "colOrderTarget",
        "colOrderSource",
    ]
    validated_src_schema_data_keys = [
        "targetColNm",
        "targetColType",
        "targetColOrder",
        "sourceColNm",
        "sourceColType",
        "sourceColOrder",
        "matchLevel",
        "itemLabel",
        "passStatus",
        "description",
        "obsSubType",
        "inferredTargetColNm",
    ]

    expected_src_schema_data_dict = {
        expected_src_schema_data_output["targetColNm"]: expected_src_schema_data_output
        for expected_src_schema_data_output in expected_source_schema_data
    }
    src_schema_data_dict = {
        src_schema_data_output["targetColNm"]: src_schema_data_output
        for src_schema_data_output in src_schema_data
    }

    for key in validated_src_schema_keys:
        assert_that(
            src_schema[key],
            f"Expected {key} "
            f"to be: {expected_source_schema[key]} for runId {run_id} "
            f"Found: {src_schema[key]} "
            f"in {src_schema}",
        ).is_equal_to(expected_source_schema[key])
    assert_that(
        len(src_schema),
        "Source schema key count does not match expected. "
        f"Expected number of keys: {len(expected_source_schema)} "
        f"Found: {len(src_schema)} for runId {run_id} "
        f"in {src_schema}",
    ).is_equal_to(len(expected_source_schema))

    for count_type in expected_src_schema_data_dict.keys():
        if src_schema_data_dict[count_type]:
            for key in validated_src_schema_data_keys:
                assert_that(
                    src_schema_data_dict[count_type][key],
                    f"Expected {key} to be "
                    f"{expected_src_schema_data_dict[count_type][key]} "
                    f"but found {src_schema_data_dict[count_type][key]} "
                    f"in {src_schema_data_dict[count_type]}",
                ).is_equal_to(expected_src_schema_data_dict[count_type][key])
            assert_that(
                len(src_schema_data_dict[count_type]),
                f"Source schema deta key count does not match expected for "
                f"targetColNm {count_type}. Expected number of keys: "
                f"{len(expected_src_schema_data_dict[count_type])}  "
                f"Found: {len(src_schema_data_dict[count_type])} "
                f"in {src_schema_data_dict[count_type]}",
            ).is_equal_to(len(expected_src_schema_data_dict[count_type]))
        else:
            raise AssertionError(
                f"countType {expected_src_schema_data_dict[count_type]} not found."
            )


def validate_source_values_details(
    api_utils,
    dataset,
    run_id,
    expected_source_values,
):
    source_values = api_utils.get(
        V2_GET_SOURCE_VALUE_COMPARISON, params={"dataset": dataset, "runId": run_id}
    )

    expected_source_values_data = expected_source_values["data"]
    source_values_data = source_values["data"]
    expected_source_values_count = len(expected_source_values)
    actual_source_values_count = len(source_values)
    expected_source_values_data_count = len(expected_source_values_data)
    actual_source_values_data_count = len(source_values_data)
    assert_that(
        expected_source_values_count,
        f"Expected source values findings to have count: {expected_source_values_count}  "
        f"Actual count: {actual_source_values_count}",
    ).is_equal_to(actual_source_values_count)
    assert_that(
        expected_source_values_data_count,
        f"Expected source values findings data to have count: {expected_source_values_data_count}  "
        f"Actual count: {actual_source_values_data_count}",
    ).is_equal_to(actual_source_values_data_count)

    validated_source_values_keys = [
        "checkValues",
        "validateValuesTrim",
        "validateValuesShowMissingKeys",
        "countRowMismatch",
        "countRowTotal",
        "percRowMatch",
        "countColumnShift",
        "colIssueCountMap",
    ]
    validated_source_values_data_keys = [
        "obsSubType",
        "system",
        "column",
        "passStatus",
        "count",
    ]

    expected_source_values_data_sorted = sorted(
        expected_source_values_data,
        key=itemgetter(*validated_source_values_data_keys),
    )
    source_values_data_sorted = sorted(
        source_values_data,
        key=itemgetter(*validated_source_values_data_keys),
    )

    for index, expected_source_value_data_finding in enumerate(
        expected_source_values_data_sorted, start=0
    ):
        for key in validated_source_values_data_keys:
            assert_that(
                source_values_data_sorted[index][key],
                f"Expected source value data {key} "
                f"to be: {expected_source_value_data_finding[key]} for runId {run_id} "
                f"Found: {source_values_data_sorted[index][key]} "
                f"in {source_values_data_sorted[index]}",
            ).is_equal_to(expected_source_value_data_finding[key])
        assert_that(
            len(source_values_data_sorted[index]),
            "Source value data key count does not match expected. "
            f"Expected number of keys: {len(expected_source_value_data_finding)} "
            f"Found: {len(source_values_data_sorted[index])} for runId {run_id} "
            f"in {source_values_data_sorted[index]}",
        ).is_equal_to(len(expected_source_value_data_finding))

    for key in validated_source_values_keys:
        assert_that(
            source_values[key],
            f"Expected {key} "
            f"to be: {expected_source_values[key]} "
            f"but found: {source_values[key]} "
            f"for source values in runId {run_id} "
            f"in {source_values}",
        ).is_equal_to(expected_source_values[key])
    assert_that(
        len(source_values),
        "Key count does not match expected. "
        f"Expected number of keys: {len(expected_source_values)} "
        f"Found: {len(source_values)} "
        f"for source values in runId {run_id} "
        f"in {source_values}",
    ).is_equal_to(len(expected_source_values))
