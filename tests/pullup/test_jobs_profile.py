import time
from datetime import datetime

import allure
import pytest
from assertpy import soft_assertions, assert_that

from data_test.pullup.data__jobs_profile_top_n_appear_athena import EXPECTED_DATA_TOPN
from data_test.pullup.data_jobs_profile_all_params_enabled import (
    EXP_CMD_LINE_ALL_PARAMS,
    EXP_OUTLIER_ALL_PARAMS,
    EXP_OBSERVATIONS_ALL_PARAMS,
    EXP_SHAPES_ALL_PARAMS,
    EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS,
    EXP_RCSRC_ALL_PARAMS,
    EXP_OBS_DETAILS_ALL_PARAMS,
)
from endpoints.v2.controller import V2_GET_LATEST_DATASET_HISTORY
from endpoints.v2.controller_cmd_line import V2_CMD_LINE
from endpoints.v2.controller_hoot import (
    V2_GET_OBSERVATIONS,
    V2_GET_SOURCE_COUNT_COMPARISON,
    V2_GET_RCSRC_BY_DATASET_RUN_ID,
)
from endpoints.v2.controller_hoot import V2_GET_TOP_AND_BOTTOM_SORTED_BY_FIELD
from endpoints.v2.controller_job import (
    V2_GET_JOB_LOG,
    V2_GET_OWL_CHECK_Q,
    V2_GET_PLATFORM_LOGS,
)
from endpoints.v2.controller_profile import V2_GET_PROFILE_DELTA
from endpoints.v2.controller_rule import (
    V2_GET_RULES,
    V2_CREATE_RULE,
    V2_REMOVE_RULE,
)
from endpoints.v3.job_api import V3_JOBS_JOBID_WAITFORCOMPLETION
from endpoints.v3.rule_api import V3_RULES
from payloads.pullup.pl_all_params_enabled import (
    DS_DEFS_ALL_PARAMS,
    PL_DS_RUN_ID_ALL_PARAMS,
    RUN_ID_ALL_PARAMS,
    RUN_ID_FULL_ALL_PARAMS,
)
from payloads.pullup.pl_jobs_profile_payloads import (
    DATA_RULE_DEV48971,
    DATASET_DEFS_DEV48974,
    DATASET_DEFS_LOGS_COMMANDLINE,
    DATASET_DEFS_LOGS_2_3,
    EXPECTED_LOG_DATA,
    EXPECTED_CMD_LINES,
    CONNECTION_DEV48976,
    DATASET_DEV48976,
    QUERY_DEV48976,
    DATASET_DEV48975,
    CORRELATION_DEV48975,
    PROFILE_HISTOGRAM_DEV48975,
    PROFILE_DELTAS_DEV48975,
    CONNECTION_DEV48975,
    QUERY_DEV48975,
    DEV48975_RUN_ID,
)

from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper

from utils.validator import (
    validate_correlation_tab_details,
    validate_profile_tab_details,
    validate_histogram_tab_details,
)

from utils.validator_shapes import validate_shapes_findings
from utils.validator_outliers import validate_outliers_findings
from utils.validator_dupes import validate_dupes_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestJobsProfile:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def assert_dataset_setup(job_completion_response):
        job_status = job_completion_response["status"]
        assert_that(
            "FINISHED",
            f"Job failed to finish. Status found: {job_status}",
        ).is_equal_to(job_status)

    @allure.feature("Jobs")
    @allure.story("Profile")
    def test_jobs_profile_validation_athena(self, api_utils):
        """Test Jobs - Profile - Stats Appear (Athena) DEV-48975"""
        ds_defs = helper.get_minimum_job_payload(
            api_utils, CONNECTION_DEV48975, DATASET_DEV48975, QUERY_DEV48975, DEV48975_RUN_ID
        )
        helper.setup_dataset(api_utils, ds_defs, DEV48975_RUN_ID)
        validate_profile_tab_details(
            api_utils, DATASET_DEV48975, DEV48975_RUN_ID, PROFILE_DELTAS_DEV48975
        )
        validate_histogram_tab_details(
            api_utils, DATASET_DEV48975, DEV48975_RUN_ID, PROFILE_HISTOGRAM_DEV48975
        )
        validate_correlation_tab_details(
            api_utils, DATASET_DEV48975, DEV48975_RUN_ID, CORRELATION_DEV48975
        )

    @allure.feature("Jobs")
    @allure.story("Profile")
    @pytest.mark.cloud
    def test_jobs_profile_precision_and_decimal_appear(self, api_utils):
        """Test Jobs - Profile - Precision and Decimals Appear (Postgres)."""
        expected_min_precision = 1
        expected_max_precision = 7

        job_completion_response = helper.setup_dataset(
            api_utils, DATASET_DEFS_DEV48974, PROD_RUN_ID
        )
        self.assert_dataset_setup(job_completion_response)
        run_id = job_completion_response["runId"]

        # Get the STATS data for claimant age row
        get_response_stats = api_utils.get(
            V2_GET_PROFILE_DELTA
            + "?dataset="
            + DATASET_DEFS_DEV48974["dataset"]
            + "&runId="
            + run_id
        )
        desired_dict = next(
            (
                item
                for item in get_response_stats
                if item.get("datasetField", {}).get("fieldNm") == "low"
            ),
            None,
        )
        column_volume = desired_dict["datasetField"]

        # Confirm STATS related to the Precision column based on DECIMAL d/type
        assert_that(
            column_volume["minPrecision"],
            f"Expected {str(expected_min_precision)},"
            f"but found {str(column_volume['minPrecision'])}",
        ).is_equal_to(expected_min_precision)
        assert_that(
            column_volume["maxPrecision"],
            f"Expected {str(expected_max_precision)},"
            f"but found {str(column_volume['maxPrecision'])}",
        ).is_equal_to(expected_max_precision)

    @allure.feature("Jobs")
    @allure.story("Profile")
    def test_jobs_log_and_command_line_postgres(self, api_utils):
        """Test Jobs - Log & Command Line (Postgres)."""
        # Data expected to appear in the command line.
        # Broken up to ignore values that are potentially variable or unordered

        job_completion_response = helper.setup_dataset(
            api_utils, DATASET_DEFS_LOGS_COMMANDLINE, PROD_RUN_ID
        )
        job_id = job_completion_response["jobId"]
        job_id_str = "{'jobId': {'id': " + str(job_id)
        found_log_data = api_utils.get(f"{V2_GET_JOB_LOG}?jobId={job_id}")

        # Flags set for validation
        exp_log_data = {tuple(check.items()): False for check in EXPECTED_LOG_DATA}
        exp_cmd_lines = {check: False for check in tuple(EXPECTED_CMD_LINES)}

        # Arbitrary number for sanity check, logs has multiple pages of data.
        assert_that(
            len(found_log_data),
            f"Inadequate number of results, expected minimum of 5. Found: {len(found_log_data)}",
        ).is_greater_than(5)

        # Sanity check
        assert_that(
            int(found_log_data[0]["logId"]), f"Invalid Log ID. Found: {found_log_data[0]['logId']}"
        ).is_greater_than(0)
        assert_that(
            int(found_log_data[0]["jobId"]["id"]),
            f"Invalid Job ID. Found: {found_log_data[0]['jobId']['id']}",
        ).is_greater_than(0)

        # Loop through all expected items in job log, set to true if found,
        # then validate all findings are true
        for check, found in exp_log_data.items():
            for log_item in found_log_data:
                if not found and all(item in log_item.items() for item in dict(check).items()):
                    exp_log_data[check] = True

        for key, value in exp_log_data.items():
            assert_that(
                value, f"Job Logs - {dict(key)} not found in data: {found_log_data}"
            ).is_true()

        job_data = api_utils.get(V2_GET_OWL_CHECK_Q, params={"jobStatus": "", "limit": 50})
        assert_that(job_data, "No job data found").is_not_empty()
        assert_that(str(job_data), f"Job {job_id} not found.").contains(job_id_str)

        # Find the job in the jobs list.
        for found_job_data in job_data["data"]:
            if found_job_data["jobId"]["id"] == job_id:
                found_job = found_job_data
                break
        else:
            raise AssertionError(f"Job ID not found {job_id} in {job_data['data']}")

        # Loop through all items in the expected list, set them to true if found,
        # then validate all items are true
        for key in exp_cmd_lines.items():
            if key[0] in str(found_job["cmdLine"]):
                exp_cmd_lines[key[0]] = True

        for key, value in exp_cmd_lines.items():
            assert_that(value, f"{key} not found in {found_job['cmdLine']}").is_equal_to(True)

    @allure.feature("Jobs")
    @allure.story("Profile")
    @pytest.mark.flaky(retries=3, delay=5)
    def test_jobs_stage_2_and_3_logs_postgres(self, api_utils):
        """Test Jobs - Stage 2 & 3 Logs (Postgres)."""
        # Setup
        today = datetime.utcnow().strftime("%y/%m/%d")

        # API Calls
        api_get_owl_check = f"{V2_GET_OWL_CHECK_Q}?jobStatus=&limit=100"
        api_logs = f"{V2_GET_PLATFORM_LOGS}?agentjobid="

        # Get IDs
        job_completion_response = helper.setup_dataset(
            api_utils, DATASET_DEFS_LOGS_2_3, PROD_RUN_ID
        )
        self.assert_dataset_setup(job_completion_response)
        job_id = job_completion_response["jobId"]
        agent_job_id = job_completion_response["agentJobId"]

        # # Create full stage log api calls
        api_stage2log = f"{api_logs}{agent_job_id}&type=submit"
        api_stage3log = f"{api_logs}{agent_job_id}&type=driver"

        # Wait for job to complete
        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=job_id))
        assert "FINISHED" == job_output["status"], (
            "Job failed to finish. Status found: " + job_output["status"]
        )

        # Get all job data
        get_response_owl = api_utils.get(api_get_owl_check, return_json=False)
        assert (
            get_response_owl.status_code == 200
        ), f"The getowlcheck call failed. Found: {get_response_owl}"
        job_data = get_response_owl.json()["data"]

        def get_logs(url, stream=False):
            log = ""
            for _ in range(10):
                if log == "":
                    response = api_utils.get(url, stream=stream, return_json=False)
                    assert response.status_code == 200, f"Failed to get logs from {url}: {response}"
                    log = response.text
                    if log == "":
                        time.sleep(1)
                else:
                    break
            else:
                raise AssertionError(f"Error: Found no log data at {url}")
            return log

        # Data validation checks
        stage2_log_check_line1 = "INFO LoggingPodStatusWatcherImpl: Application status for spark"
        stage2_log_check_line2 = "termination reason: Completed"
        stage3_log_check_line1 = "INFO OwlCheck$: Deployment mode: STANDARD"
        stage3_log_check_line2 = "OwlCheckQ JobId: Identifier[id="
        stage3_log_check_line3 = "Owlcheck exiting with status: 0 (FINISHED)"
        stage3_log_check_line4 = "Job Status Captured"

        # Find the job in the jobs list.
        for job_d in job_data:
            if job_d["jobId"]["id"] == job_id:
                break
        else:
            raise AssertionError(f"Did not find {str(job_id)} in jobs list.")

        def validate_stage2_logs(stage2_log):
            assert today in stage2_log, f"Did not find [{today}] in stage 2 log: {stage2_log}"
            assert (
                "ERROR" not in stage2_log
            ), f"Found an unexpected error in stage 2 log: {stage2_log}"
            assert stage2_log_check_line1 in stage2_log, (
                f"Did not find [{stage2_log_check_line1}] in " f"stage 2 log: {stage2_log}"
            )
            assert stage2_log_check_line2 in stage2_log, (
                f"Did not find [{stage2_log_check_line2}] in " f"stage 2 log: {stage2_log}"
            )

        def validate_stage3_logs(stage3_log, job_id):
            assert today in stage3_log, f"Did not find [{today}] in stage 3 log: {stage3_log}"
            assert job_d["cmdLine"] in stage3_log, (
                f"Did not find cmdline. Expected: [{job_d['cmdLine']}] "
                f"in stage 3 log: {stage3_log}"
            )
            assert stage3_log_check_line1 in stage3_log, (
                f"Did not find [{stage3_log_check_line1}] " f"in stage 3 log: {stage3_log}"
            )
            assert stage3_log_check_line2 + str(job_id) in stage3_log, (
                f"Did not find [{stage3_log_check_line2 + str(job_id)}] "
                f"in stage 3 log: {stage3_log}"
            )
            assert stage3_log_check_line3 in stage3_log, (
                f"Did not find [{stage3_log_check_line3}] " f"in stage 3 log: {stage3_log}"
            )
            assert stage3_log_check_line4 in stage3_log, (
                f"Did not find [{stage3_log_check_line4}] " f"in stage 3 log: {stage3_log}"
            )

        # Get and validate stage 2 logs
        stage2_log = get_logs(api_stage2log)
        validate_stage2_logs(stage2_log)

        # Get and validate stage 3 logs
        stage3_log = get_logs(api_stage3log, stream=True)
        validate_stage3_logs(stage3_log, job_id)

        # Validate errors in stage 3 log
        if "ERROR OwlCheckQDao: Attempted reuse of agent job id: Identifier" in stage3_log:
            count_errors = stage3_log.count("ERROR")
            assert count_errors <= 1, (
                f"Unexpected errors were found in the stage 3 log. " f"Found: {stage3_log}"
            )
        else:
            assert "ERROR" not in stage3_log, (
                f"Unexpected errors were found in the stage 3 log. " f"Found: {stage3_log}"
            )

    @allure.feature("Jobs")
    @allure.story("Profile")
    def test_jobs_profile_top_n_appear_add_rule_athena(self, api_utils):
        """Test Jobs - Profile - TopN Appear & Add Rule"""
        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION_DEV48976,
            DATASET_DEV48976,
            QUERY_DEV48976,
        )
        exp_func = "TOPN"
        rule_msg = "Rule Saved"
        pl_general = {
            "dataset": ds_defs["dataset"],
            "runId": ds_defs["runId"],
        }
        exp_fields = {
            "dataset": "dataset",
            "ruletype": "ruleType",
            "primarycolumn": "columnName",
            "rulenm": "ruleNm",
            "where": "ruleValue",
            "points": "points",
            "perc": "perc",
            "previewlimit": "previewLimit",
            "runTimeLimit": "runTimeLimit",
        }

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        latest_dataset_run_id = api_utils.get(
            V2_GET_LATEST_DATASET_HISTORY, params={"dataset": ds_defs["dataset"]}
        )["runId"]
        pl_field_name = {
            "dataset": pl_general["dataset"],
            "runId": latest_dataset_run_id,
            "fieldnm": "cm_claimant_age",
        }

        # Fetch TopN data
        get_response_top_n = api_utils.get(
            V2_GET_TOP_AND_BOTTOM_SORTED_BY_FIELD, params=pl_field_name
        )

        for i, exp in enumerate(EXPECTED_DATA_TOPN):
            row = get_response_top_n[i]
            with soft_assertions():
                assert_that(row["fieldNm"], "Field Name").is_equal_to(pl_field_name["fieldnm"])
                assert_that(row["fieldFunc"], "Field Function").is_equal_to(exp_func)

                assert_that(row["fieldValue"], "Field Value").is_equal_to(exp["fieldValue"])
                assert_that(row["uniqueCnt"], "Unique Count").is_equal_to(exp["uniqueCnt"])

        api_utils.delete(V3_RULES + "/" + ds_defs["dataset"], return_json=False)

        # Post the dataset and verify rule is saved
        r_post_rule = api_utils.post(V2_CREATE_RULE, params=DATA_RULE_DEV48971)
        assert_that(r_post_rule["message"], "Create Rule").is_equal_to(rule_msg)

        # Get all rules for the dataset
        r_get_rule = api_utils.get(V2_GET_RULES, params=pl_general)

        # Confirm only 1 rule exists (the one just created)
        assert_that(len(r_get_rule), "Rule Count").is_equal_to(1)
        response_rule_data = r_get_rule[0]

        # Perform assertions for each field
        for expected_field, response_field in exp_fields.items():
            expected_value = DATA_RULE_DEV48971[expected_field]
            response_value = response_rule_data[response_field]
            assert_that(expected_value, f"Field {expected_field}").is_equal_to(response_value)

        # Confirm the rule is active
        assert_that(response_rule_data["active"], "Rule Active").is_true()
        assert_that(response_rule_data["isActive"], "Rule IsActive").is_equal_to(1)

        # Delete the rule
        post_response_delete = api_utils.post(
            V2_REMOVE_RULE, params=DATA_RULE_DEV48971, return_json=False
        )
        assert_that(post_response_delete.status_code, "Delete Call").is_equal_to(200)

        # Get all rules for the dataset
        get_response_rule_delete = api_utils.get(V2_GET_RULES, params=pl_general)

        # Confirm no rule exists
        assert_that(len(get_response_rule_delete), "Rule Delete").is_equal_to(0)

    @allure.feature("Jobs")
    @allure.story("Profile")
    @pytest.mark.skip(reason="DEV-61462")
    def test_jobs_all_parameters_enabled(self, api_utils):
        """Test Jobs - All Parameters Enabled DEV-48929"""

        # Run job
        helper.delete_dataset_outlier_configurations(api_utils, DS_DEFS_ALL_PARAMS["dataset"])
        helper.setup_dataset(api_utils, DS_DEFS_ALL_PARAMS)

        # Validate command line contents
        resp_cmd = api_utils.get(V2_CMD_LINE, params=PL_DS_RUN_ID_ALL_PARAMS)
        result_cmd = resp_cmd["result"]
        for expected in EXP_CMD_LINE_ALL_PARAMS:
            assert_that(result_cmd, "CMD Line").contains(expected)

        # Observations (includes records & patterns)
        resp_observations = api_utils.get(V2_GET_OBSERVATIONS, PL_DS_RUN_ID_ALL_PARAMS)
        found_observations = resp_observations["data"]
        assert_that(len(found_observations), "Found no observations").is_greater_than(0)
        for i, expected in enumerate(EXP_OBSERVATIONS_ALL_PARAMS):
            for key, expected_value in expected.items():
                assert_that(str(expected_value), f"Observations - {key} on item #{i}").is_equal_to(
                    str(found_observations[i][key])
                )
        # Source
        resp_source = api_utils.get(V2_GET_SOURCE_COUNT_COMPARISON, params=PL_DS_RUN_ID_ALL_PARAMS)
        found_source_data = resp_source["data"]
        assert_that(len(found_source_data), "No souce count data found").is_greater_than(0)

        assert_that(resp_source["targetRowCount"], "Source - Target Row Count").is_equal_to(
            EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS["targetRowCount"]
        )
        assert_that(resp_source["sourceRowCount"], "Source - Source Row Count").is_equal_to(
            EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS["sourceRowCount"]
        )
        assert_that(resp_source["targetColCount"], "Source - Target Col Count").is_equal_to(
            EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS["targetColCount"]
        )
        assert_that(resp_source["sourceColCount"], "Source - Source Col Count").is_equal_to(
            EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS["sourceColCount"]
        )

        for i, expected in enumerate(EXP_SOURCE_COUNT_COMPARISON_ALL_PARAMS["data"]):
            for key, expected_value in expected.items():
                assert_that(
                    str(expected_value), f"Source Count Comparison - {key} on item #{i}"
                ).is_equal_to(str(found_source_data[i][key]))

        # Source By RunId
        resp_rcsrc = api_utils.get(V2_GET_RCSRC_BY_DATASET_RUN_ID, params=PL_DS_RUN_ID_ALL_PARAMS)
        assert_that(len(resp_rcsrc), "No RCSRC results found").is_greater_than(0)
        for i, expected in enumerate(EXP_RCSRC_ALL_PARAMS):
            for key, expected_value in expected.items():
                assert_that(str(expected_value), f"RCSRC - {key} on item #{i}").is_equal_to(
                    str(resp_rcsrc[i][key])
                )

        validate_dupes_findings(
            api_utils, DS_DEFS_ALL_PARAMS["dataset"], RUN_ID_ALL_PARAMS, EXP_OBS_DETAILS_ALL_PARAMS
        )
        validate_outliers_findings(
            api_utils, DS_DEFS_ALL_PARAMS, RUN_ID_FULL_ALL_PARAMS, EXP_OUTLIER_ALL_PARAMS
        )
        validate_shapes_findings(
            api_utils, DS_DEFS_ALL_PARAMS, RUN_ID_FULL_ALL_PARAMS, EXP_SHAPES_ALL_PARAMS
        )
