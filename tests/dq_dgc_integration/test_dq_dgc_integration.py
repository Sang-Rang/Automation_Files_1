import allure
import pytest
from assertpy import assert_that
from payloads.dq_dgc_integration.pl_nyse_basic_pullup_job import get_dynamic_nyse_dataset_def
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DQ_BUSINESS_UNIT,
    DGC_UNASSIGNED_DQ_JOB_COMMUNITY,
    DGC_DQ_INTEGRATION_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper

helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()
POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"


@pytest.mark.dq_dgc
class TestDqDgcIntegration:

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

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_integration_with_assigned_business_unit(self, api_utils, dgc_api_utils):
        nyse_dataset_def = get_dynamic_nyse_dataset_def()
        dataset_name = nyse_dataset_def["dataset"]
        dataset_run_id = nyse_dataset_def["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, nyse_dataset_def)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Create business unit and associate the given dataset with it
        dq_dgc_helper.create_business_unit_if_not_exists(api_utils, DQ_BUSINESS_UNIT)
        dq_dgc_helper.add_dataset_to_business_unit(api_utils, DQ_BUSINESS_UNIT, dataset_name)

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, dataset_name)
        dq_dgc_helper.submit_dgc_job_and_check_status(api_utils, dataset_name, dataset_run_id)

        # Verify counts of imported assets
        # TODO enable with DGC 2024.03
        # self.verify_imported_assets_count(api_utils, dataset_name, dgc_api_utils,
        #                                 integration_response)

        # Verify import of DQ Job
        dq_dgc_helper.verify_dq_job_import(dataset_name, dgc_api_utils)

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(dgc_api_utils, dataset_name, DQ_BUSINESS_UNIT)

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(dgc_api_utils, dataset_name, DQ_BUSINESS_UNIT)

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_integration_with_unassigned_business_unit(self, api_utils, dgc_api_utils):
        nyse_dataset_def = get_dynamic_nyse_dataset_def()
        dataset_name = nyse_dataset_def["dataset"]
        dataset_run_id = nyse_dataset_def["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, nyse_dataset_def)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, dataset_name)
        dq_dgc_helper.submit_dgc_job_and_check_status(api_utils, dataset_name, dataset_run_id)

        # Verify counts of imported assets
        # TODO enable with DGC 2024.03
        # self.verify_imported_assets_count(api_utils, dataset_name,
        #                                  dgc_api_utils, integration_response)

        # Verify import of DQ Job
        dq_dgc_helper.verify_dq_job_import(dataset_name, dgc_api_utils)

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(
            dgc_api_utils, dataset_name, DGC_UNASSIGNED_DQ_JOB_COMMUNITY
        )

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(
            dgc_api_utils, dataset_name, DGC_UNASSIGNED_DQ_JOB_COMMUNITY
        )
