# pylint: disable-msg=broad-exception-caught
import time
import json

import allure
import pytest
from assertpy import assert_that

from data_test.dq_dgc_integration.data_dgc_integration_bu_manual_job import (
    DQ_BREADCRUMBS_BEFORE_UPDATE_WITH_BU,
    DGC_BREADCRUMBS_BEFORE_UPDATE_WITH_BU,
    DQ_BREADCRUMBS_AFTER_UPDATE_WITH_BU,
    DGC_BREADCRUMBS_AFTER_UPDATE_WITH_BU,
)
from data_test.dq_dgc_integration.data_dgc_sheduled_jobs import (
    DQ_DGC_SCHEDULE_RULE_WITH_BU_OUTPUT,
    SCHEDULE_DATA_PAYLOAD_WITH_BU,
    DQ_DGC_SCHEDULE_RULE_DEFINITION_WITH_BU,
)
from endpoints.dgc_integration.dgc.assets_api import DGC_BREADCRUMBS
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from endpoints.dgc_integration.dq.integration_api import (
    DQ_RESET_INTEGRATION,
    DQ_DATASET_INTEGRATION_STATUS,
    PUT_DGC_INTEGRATIONS_STATUS,
)
from endpoints.v2.controller_job import V2_GET_JOB_STATUS_BY_DATASET
from endpoints.v2.controller_scheduler import V2_POST_JOB_SCHEDULE, V2_DELETE_JOBS_SCHEDULE
from endpoints.v3.job_api import V3_JOBS_JOBID_WAITFORCOMPLETION
from payloads.dq_dgc_integration.pl_dq_dgc_shcheduled_run import (
    DS_DEF_DGC_SCHEDULED_JOB_RUN,
    DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DQ_BUSINESS_UNIT,
    DGC_DQ_INTEGRATION_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal, compare_lists_are_equal
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()
POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"
NUM_OF_RULES_ON_PAGE = 44
CONNECTION_NAME = "APPROVED_POSTGRES_UP"
SCHEDULED_JOB = DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME


@pytest.fixture(scope="class", autouse=True)
def manage_schedules(api_utils):
    """Fixture to manage job schedules: cleans up after the test session."""
    yield  # This allows the test to run

    try:
        #  Delete all schedules associated with your dataset.
        delete = api_utils.delete(
            V2_DELETE_JOBS_SCHEDULE, params={"dataset": SCHEDULED_JOB}, return_json=False
        )
        assert_that(delete.status_code, "Delete job schedule fail").is_equal_to(200)
        print("All job schedules for the dataset have been deleted.")

    except Exception as exception:
        print(f"Error during schedule cleanup: {exception}")


@pytest.mark.dq_dgc
class TestDqDgcIntegrationScheduledRun:

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="class")
    def dgc_api_utils(self, dgc_base_url, get_auth_headers_dgc):
        return APIUtils(base_url=dgc_base_url, headers=get_auth_headers_dgc)

    @pytest.fixture(scope="class")
    def setup_dq_dgc_integration(self, api_utils, dgc_api_utils):
        # Delete all DQ/DGC connections
        dg_dgc_connection_helper.delete_all_dq_dgc_connections(api_utils)

        # Setup DGC credentials
        dq_dgc_helper.setup_dgc_credentials(api_utils)

        # Map DQ/DGC connections
        dq_dgc_helper.map_dq_dgc_connections(
            api_utils,
            POSTGRES_SCHEMA_NAME,
            POSTGRES_TABLE_NAME,
            DQ_POSTGRES_CONNECTION_NAME,
            DGC_DATABASE_UUID,
        )

        # Align DGC community
        dg_dgc_connection_helper.align_tenant_to_dgc_community(
            api_utils, dgc_api_utils, DGC_DQ_INTEGRATION_COMMUNITY
        )

        # Map DQ/DGC dimensions
        dg_dgc_connection_helper.dq_dgc_connection_create_dimension_mapping(api_utils)

    @staticmethod
    def get_updated_relations(dgc_api_utils, assets_params):
        # Define the timeout and interval for retries
        timeout = 120  # Maximum time to wait in seconds
        interval = 5  # Time between retries in seconds

        start_time = time.time()

        while True:
            # Fetch the response from the API
            relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

            # Check if the response meets the expected condition
            if relations_response["total"] == NUM_OF_RULES_ON_PAGE:
                return relations_response

            # Check if timeout has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise AssertionError(
                    f"Timeout reached. "
                    f"Expected total to be {NUM_OF_RULES_ON_PAGE} but got "
                    f"{relations_response['total']}"
                )

            # Wait before retrying
            time.sleep(interval)

    @staticmethod
    def get_updated_breadcrumbs(dgc_api_utils, asset_id):
        # Define the timeout and interval for retries
        timeout = 140  # Maximum time to wait in seconds
        interval = 5  # Time between retries in seconds
        len_of_breadcrumbs_path = 4

        start_time = time.time()

        while True:
            # Fetch the response from the API
            asset_url = DGC_BREADCRUMBS.format(assetId=asset_id)
            dgc_breadcrumbs_after_update = dgc_api_utils.get(asset_url)

            # Check if the response meets the expected condition
            if len(dgc_breadcrumbs_after_update) == len_of_breadcrumbs_path:
                return dgc_breadcrumbs_after_update

            # Check if timeout has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise AssertionError(
                    f"Timeout reached. "
                    f"Expected total to be {len_of_breadcrumbs_path} but got "
                    f"{len(dgc_breadcrumbs_after_update)}"
                )

            # Wait before retrying
            time.sleep(interval)

    @staticmethod
    def wait_for_job_id_change(
        api_utils, job_name, run_id, initial_job_id, timeout=180, interval=5
    ):

        end_time = time.time() + timeout

        while time.time() < end_time:
            try:
                job_status = api_utils.get(
                    V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": job_name, "runId": run_id}
                )

                # Check for potential API errors.
                if "jobId" not in job_status or "id" not in job_status["jobId"]:
                    raise ValueError(f"Unexpected API response: {job_status}")

                current_job_id = job_status["jobId"]["id"]

                if current_job_id != initial_job_id:
                    return current_job_id

                time.sleep(interval)

            except Exception as exception:  # Handle potential exceptions during API calls
                print(f"Error during API call: {exception}")
                # For simplicity, we'll just return None after a failed attempt.
                return None

        return None  # Timeout reached

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_enable_disable_reset_integration_with_bu_scheduled(
        self, api_utils, dgc_api_utils
    ):
        """Verify Enable, Reset and Disable integration with Business unit and without business
        unit for Scheduled Run job, ref: DEV-83966"""
        dataset_run_id = DS_DEF_DGC_SCHEDULED_JOB_RUN["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_SCHEDULED_JOB_RUN)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Create business unit and associate the given dataset with it
        dq_dgc_helper.create_business_unit_if_not_exists(api_utils, DQ_BUSINESS_UNIT)
        dq_dgc_helper.add_dataset_to_business_unit(
            api_utils, DQ_BUSINESS_UNIT, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(
            api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
        )
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME, dgc_api_utils
        )

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(
            dgc_api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME, DQ_BUSINESS_UNIT
        )

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(
            dgc_api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME, DQ_BUSINESS_UNIT
        )

        # Check the breadcrumbs on DQ before.
        dq_breadcrumbs = api_utils.get(
            DQ_DATASET_INTEGRATION_STATUS.format(
                dataset=DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
            )
        )
        # Validate results
        exclude_dynamic_keys = ["id", "dgcAssetUrl", "dgcUuid", "resourceDiscriminator"]
        compare_dicts_are_equal(
            dq_breadcrumbs, DQ_BREADCRUMBS_BEFORE_UPDATE_WITH_BU, exclude_dynamic_keys
        )

        # Check the updated breadcrumbs on DIP
        asset_url = DGC_BREADCRUMBS.format(assetId=asset_id)
        dgc_breadcrumbs = dgc_api_utils.get(asset_url)
        compare_lists_are_equal(
            dgc_breadcrumbs, DGC_BREADCRUMBS_BEFORE_UPDATE_WITH_BU, exclude_dynamic_keys
        )

        assets_params = {"targetId": asset_id}
        relations_response = self.get_updated_relations(dgc_api_utils, assets_params)
        assert_that(
            relations_response["total"],
            f"Unexpected number of rules appear, expected {NUM_OF_RULES_ON_PAGE}, but "
            f"got {relations_response['total']}",
        ).is_equal_to(NUM_OF_RULES_ON_PAGE)

        # Change DGC community
        dg_dgc_connection_helper.update_tenant_mapping(api_utils, "JP")

        # Reset Integration for dataset
        api_utils.post(
            DQ_RESET_INTEGRATION.format(dataset=DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME)
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(
            api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
        )
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME, dataset_run_id
        )

        self.get_updated_breadcrumbs(dgc_api_utils, asset_id)

        # Check the updated breadcrumbs on DQ
        dq_breadcrumbs_after_update = api_utils.get(
            DQ_DATASET_INTEGRATION_STATUS.format(
                dataset=DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
            )
        )
        compare_dicts_are_equal(
            dq_breadcrumbs_after_update, DQ_BREADCRUMBS_AFTER_UPDATE_WITH_BU, exclude_dynamic_keys
        )

        # Check the updated breadcrumbs on DIP
        asset_url = DGC_BREADCRUMBS.format(assetId=asset_id)
        dgc_breadcrumbs_after_update = dgc_api_utils.get(asset_url)
        compare_lists_are_equal(
            dgc_breadcrumbs_after_update, DGC_BREADCRUMBS_AFTER_UPDATE_WITH_BU, exclude_dynamic_keys
        )

        # Change Active to false to Disable integration
        req_params = {"dataset": "string", "active": False}
        integration_response = api_utils.put(
            PUT_DGC_INTEGRATIONS_STATUS.format(
                dataset=DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME
            ),
            json=json.dumps(req_params),
        )
        assert_that(
            integration_response["active"],
            f"Job was not disabled, got status:" f"{integration_response['active']}",
        ).is_false()

        # Add a rule, check it shows up on DQ but not on DIP
        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
            DQ_DGC_SCHEDULE_RULE_DEFINITION_WITH_BU,
        )

        # Data setup
        agent_details = helper.get_agent_details_for_connection(api_utils, CONNECTION_NAME)
        scheduled_data = SCHEDULE_DATA_PAYLOAD_WITH_BU

        # Update agent ID and UUID in a payload
        scheduled_data["agentId"] = agent_details["agentId"]["id"]
        scheduled_data["agentUUID"] = agent_details["agentId"]["uuid"]

        add_schedule = api_utils.post(V2_POST_JOB_SCHEDULE, params=scheduled_data)
        assert_that(add_schedule["msg"]).is_equal_to("Success")

        job_id = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET,
            params={
                "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
                "runId": dataset_run_id,
            },
        )["jobId"]["id"]

        new_id = self.wait_for_job_id_change(
            api_utils,
            DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
            run_id=dataset_run_id,
            initial_job_id=job_id,
        )

        # Wait for job to complete
        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=str(new_id)))
        assert_that(job_output["status"], "Job was not finished").is_equal_to("FINISHED")

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
            job_output["runId"],
            DQ_DGC_SCHEDULE_RULE_WITH_BU_OUTPUT,
        )

        # Get relations information (all rules information) after rule added.
        relations_response = self.get_updated_relations(dgc_api_utils, assets_params)
        assert_that(
            relations_response["total"],
            f"Unexpected number of rules appear, expected {NUM_OF_RULES_ON_PAGE}, "
            f"but got {relations_response['total']}",
        ).is_equal_to(NUM_OF_RULES_ON_PAGE)
