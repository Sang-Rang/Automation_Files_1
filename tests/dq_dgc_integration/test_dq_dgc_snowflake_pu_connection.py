import allure
import pytest
from assertpy import assert_that

from payloads.dq_dgc_integration.pl_dq_dgc_snowflake_connection import (
    DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME,
    DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION,
    SNOWFLAKE_SCHEMA_NAME,
    SNOWFLAKE_TABLE_NAME,
    DQ_SNOWFLAKE_PU_CONNECTION_NAME,
    DGC_DATABASE_UUID_SNOWFLAKE_PU,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DQ_BUSINESS_UNIT,
    DGC_DQ_INTEGRATION_COMMUNITY,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper

helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()


@pytest.mark.dq_dgc
class TestDqDgcSnowflakePuConnection:

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
            SNOWFLAKE_SCHEMA_NAME,
            SNOWFLAKE_TABLE_NAME,
            DQ_SNOWFLAKE_PU_CONNECTION_NAME,
            DGC_DATABASE_UUID_SNOWFLAKE_PU,
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
    def test_dq_dgc_snowflake_pu_connection_integration(self, api_utils, dgc_api_utils):
        """INTEGRATION - Verify SNOWFLAKE pullup connection and verify job can
        be successfully be enabled, ref: DEV-88276"""
        dataset_run_id = DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Create business unit and associate the given dataset with it
        dq_dgc_helper.create_business_unit_if_not_exists(api_utils, DQ_BUSINESS_UNIT)
        dq_dgc_helper.add_dataset_to_business_unit(
            api_utils, DQ_BUSINESS_UNIT, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME, dgc_api_utils
        )

        # Get Quality Tab details for DQ job
        response = dq_dgc_helper.get_quality_tab_information(dgc_api_utils, asset_id)
        assert_that(
            response["asset"]["type"]["name"],
            f"Invalid asset type name returned, "
            f"expected 'Data Quality Job', but got {response['asset']['type']['name']}",
        ).is_equal_to("Data Quality Job")
        assert_that(
            response["score"],
            f"Invalid quality score returned, "
            f"expected 100.0, but got {response['score']}",
        ).is_equal_to(100.0)

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(
            dgc_api_utils, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME, DQ_BUSINESS_UNIT
        )

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(
            dgc_api_utils, DS_DEF_DGC_SNOWFLAKE_PU_INTEGRATION_NAME, DQ_BUSINESS_UNIT
        )
