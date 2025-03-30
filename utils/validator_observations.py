from _operator import itemgetter
from assertpy import assert_that

from endpoints.v2.controller_hoot import (
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
    V2_GET_OBSERVATIONS_BY_TYPE,
)

from utils.helper import BaseHelper

helper = BaseHelper()


def validate_records_findings(api_utils, dataset, run_id, expected_records_findings):
    """
    Verifies records findings.  Expected results are from /v2/getobservationsbytype
    :param api_utils: API Utils
    :param dataset: Dataset name to be validated
    :param run_id: Run ID to be validated
    :param expected_records_findings: The expected records findings for the dataset and runId
    :return:
    """
    get_observations_params = {
        "dataset": dataset,
        "runId": run_id,
        "type": "RECORD_CHANGES",
    }
    issue_type = "RECORD"
    records_findings = api_utils.get(V2_GET_OBSERVATIONS_BY_TYPE, params=get_observations_params)

    validate_observations_findings_count(
        api_utils, dataset, run_id, issue_type, expected_records_findings
    )
    validate_observations_findings_score(
        api_utils, dataset, run_id, issue_type, records_findings
    )
    validate_observations_findings_details(
        run_id, expected_records_findings, records_findings, issue_type
    )


def validate_schema_findings(api_utils, dataset, run_id, expected_schema_findings):
    """
    Verifies schema findings.  Expected results are from /v2/getobservationsbytype.
    :param api_utils: API Utils
    :param dataset: Dataset name to be validated
    :param run_id: Run ID to be validated
    :param expected_schema_findings: The expected schema findings for the dataset and runId
    :return:
    """
    get_observations_params = {
        "dataset": dataset,
        "runId": run_id,
        "type": "SCHEMA_EVOLUTION",
    }
    issue_type = "SCHEMA"
    schema_findings = api_utils.get(V2_GET_OBSERVATIONS_BY_TYPE, params=get_observations_params)

    validate_observations_findings_count(
        api_utils, dataset, run_id, issue_type, expected_schema_findings
    )
    validate_observations_findings_score(
        api_utils, dataset, run_id, issue_type, schema_findings
    )
    validate_observations_findings_details(
        run_id, expected_schema_findings, schema_findings, issue_type
    )


def validate_observations_findings_count(
        api_utils,
        dataset,
        run_id,
        issue_type,
        expected_observations_findings,
):
    """
    Verify the count of observation findings for a dataset and runId
    :param api_utils: API Utils
    :param dataset: The dataset for observations findings count validation
    :param run_id: The runId to be validated
    :param issue_type: The issue type for finding count validation
    :param expected_observations_findings: Expected observations findings for the dataset and runId
    :return:
    """
    expected_observations_findings_count = len(expected_observations_findings)
    dataset_and_runid = {
        "dataset": dataset,
        "runId": run_id,
    }
    issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=dataset_and_runid)
    issue_count_observations_count = issue_count_response[issue_type]

    sleep_interval = 1
    timeout = 10
    issue_count_observations_count = helper.wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count_observations_count,
        expected_observations_findings_count,
        dataset_and_runid,
        sleep_interval,
        timeout,
    )

    assert_that(
        issue_count_observations_count,
        f"Expected {issue_type} count to be: "
        f"{expected_observations_findings_count} for runId {run_id}. "
        f"Actual: {issue_count_observations_count}",
    ).is_equal_to(expected_observations_findings_count)


def validate_observations_findings_score(
        api_utils,
        dataset,
        run_id,
        issue_type,
        observations_findings
):
    """
    Verify the score is properly calculated for the specified observations finding type.
    :param api_utils: API UTILS
    :param dataset: The dataset to validate
    :param run_id: The runId to validate
    :param issue_type: The issue type score to validate
    :param observations_findings: Schema findings from /v2/getobservationsbytype
    :return:
    """
    dataset_scoring = api_utils.get(
        V2_GET_DATASET_SCORING, params={"dataset": dataset, "runId": run_id}
    )
    if issue_type == "SCHEMA":
        issue_score_type = "schemaScore"
        total_score_type = "schemaTotalScore"
    elif issue_type == "RECORD":
        issue_score_type = "recordScore"
        total_score_type = "recordTotalScore"
    else:
        raise ValueError(f"No issue scoring support for issue type {issue_type}.")
    score_per_finding = dataset_scoring[issue_score_type]
    total_score = dataset_scoring[total_score_type]
    finding_count = len(observations_findings)
    expected_score = finding_count * score_per_finding
    assert_that(
        total_score,
        f"Expected {issue_type} score to be: {expected_score}  "
        f"Actual: {total_score}",
    ).is_equal_to(expected_score)


def validate_observations_findings_details(
        expected_run_id,
        expected_findings,
        findings,
        issue_type,
):
    """
    Validate observations findings details.
    :param expected_run_id: The runId expected in observations findings.  Overrides runId in
    expected findings passed in to allow for changing runId values.
    :param expected_findings: Expected findings from /v2/getobservationsbytype.
    :param findings: Findings from /v2/getobservationsbytype.
    :param issue_type: The issue type being validated.
    :return:
    """
    # Only validate keys with data that is predictable
    validation_keys = ["dataset", "runId", "obsType", "obs", "obsScore", "linkId", "obsSubType"]

    expected_findings_sorted = sorted(
        expected_findings, key=itemgetter(*validation_keys)
    )
    findings_sorted = sorted(findings, key=itemgetter(*validation_keys))

    expected_findings_detail_count = len(expected_findings_sorted)
    findings_detail_count = len(findings_sorted)
    assert_that(
        findings_detail_count,
        f"Expected {expected_findings_detail_count} {issue_type} findings.  "
        f"Found {findings_detail_count} {issue_type} findings.",
    ).is_equal_to(expected_findings_detail_count)

    # Validate each relevant key in the sorted lists
    for index, expected_finding in enumerate(expected_findings_sorted, start=0):
        for key in validation_keys:
            if key == "runId":
                assert_that(
                    findings_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_run_id}  "
                    f"Found: {findings_sorted[index][key]} "
                    f"in {findings_sorted[index]}",
                ).is_equal_to(expected_run_id)
            else:
                assert_that(
                    findings_sorted[index][key],
                    f"Expected {key} "
                    f"to be: {expected_finding[key]}  "
                    f"Found: {findings_sorted[index][key]} "
                    f"in {findings_sorted[index]}",
                ).is_equal_to(expected_finding[key])
        assert_that(
            len(findings_sorted[index]),
            "Key count does not match expected. "
            f"Expected number of keys: {len(expected_finding)}  "
            f"Found: {len(findings_sorted[index])} "
            f"in {findings_sorted[index]}",
        ).is_equal_to(len(expected_finding))
