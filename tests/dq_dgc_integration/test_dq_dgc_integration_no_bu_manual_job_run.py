import time
import json
import allure
import pytest
from assertpy import assert_that

from data_test.dq_dgc_integration.data_dgc_integration_bu_manual_job import (
    DQ_DGC_FREEFORM_RULE_OUTPUT,
    DQ_DGC_FREEFORM_RULE_DEFINITION,
    DQ_BREADCRUMBS_BEFORE_UPDATE,
    DGC_BREADCRUMBS_BEFORE_UPDATE,
    DQ_BREADCRUMBS_AFTER_UPDATE,
    DGC_BREADCRUMBS_AFTER_UPDATE,
)
from endpoints.dgc_integration.dgc.assets_api import DGC_BREADCRUMBS
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from endpoints.dgc_integration.dq.integration_api import (
    DQ_RESET_INTEGRATION,
    DQ_DATASET_INTEGRATION_STATUS,
    PUT_DGC_INTEGRATIONS_STATUS,
)
from payloads.dq_dgc_integration.pl_dq_dgc_manual_job_run import (
    DS_DEF_DGC_MANUAL_JOB_RUN,
    DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DGC_UNASSIGNED_DQ_JOB_COMMUNITY,
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


@pytest.mark.dq_dgc
class TestDqDgcIntegrationNoBusinessUnit:

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

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_enable_disable_reset_integration_without_bu(self, api_utils, dgc_api_utils):
        """Verify Enable, Reset and Disable integration with Business unit and without business
        unit for Manual Run job, ref: DEV-83978"""
        dataset_run_id = DS_DEF_DGC_MANUAL_JOB_RUN["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_MANUAL_JOB_RUN)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME, dgc_api_utils
        )

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(
            dgc_api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME, DGC_UNASSIGNED_DQ_JOB_COMMUNITY
        )

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(
            dgc_api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME, DGC_UNASSIGNED_DQ_JOB_COMMUNITY
        )

        # Check the breadcrumbs on DQ before.
        dq_breadcrumbs = api_utils.get(
            DQ_DATASET_INTEGRATION_STATUS.format(dataset=DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME)
        )
        # Validate results
        exclude_dynamic_keys = ["id", "dgcAssetUrl", "dgcUuid", "resourceDiscriminator"]
        compare_dicts_are_equal(dq_breadcrumbs, DQ_BREADCRUMBS_BEFORE_UPDATE, exclude_dynamic_keys)

        # Check breadcrumbs on DIP before
        asset_url = DGC_BREADCRUMBS.format(assetId=asset_id)
        dgc_breadcrumbs = dgc_api_utils.get(asset_url)
        compare_lists_are_equal(
            dgc_breadcrumbs, DGC_BREADCRUMBS_BEFORE_UPDATE, exclude_dynamic_keys
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
        api_utils.post(DQ_RESET_INTEGRATION.format(dataset=DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME))

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME, dataset_run_id
        )

        # Check the updated breadcrumbs on DQ
        dq_breadcrumbs_after_update = api_utils.get(
            DQ_DATASET_INTEGRATION_STATUS.format(dataset=DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME)
        )
        compare_dicts_are_equal(
            dq_breadcrumbs_after_update, DQ_BREADCRUMBS_AFTER_UPDATE, exclude_dynamic_keys
        )

        # Check the updated breadcrumbs on DIP
        self.get_updated_breadcrumbs(dgc_api_utils, asset_id)
        asset_url = DGC_BREADCRUMBS.format(assetId=asset_id)
        dgc_breadcrumbs_after_update = dgc_api_utils.get(asset_url)
        compare_lists_are_equal(
            dgc_breadcrumbs_after_update, DGC_BREADCRUMBS_AFTER_UPDATE, exclude_dynamic_keys
        )

        # Change Active to false to Disable integration
        req_params = {"dataset": "string", "active": False}
        integration_response = api_utils.put(
            PUT_DGC_INTEGRATIONS_STATUS.format(dataset=DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME),
            json=json.dumps(req_params),
        )
        assert_that(
            integration_response["active"],
            f"Job was not disabled, got status:" f"{integration_response['active']}",
        ).is_false()

        # Add a rule, check it shows up on DQ but not on DIP
        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
            DQ_DGC_FREEFORM_RULE_DEFINITION,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_MANUAL_JOB_RUN)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
            job_response["runId"],
            DQ_DGC_FREEFORM_RULE_OUTPUT,
        )

        # Get relations information (all rules information) after rule added.
        relations_response = self.get_updated_relations(dgc_api_utils, assets_params)
        assert_that(
            relations_response["total"],
            f"Unexpected number of rules appear, expected {NUM_OF_RULES_ON_PAGE}, "
            f"but got {relations_response['total']}",
        ).is_equal_to(NUM_OF_RULES_ON_PAGE)
