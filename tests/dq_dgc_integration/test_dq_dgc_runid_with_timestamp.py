import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_dataset import V2_RENAME_DATASET
from endpoints.v3.dataset_def_api import V3_DATASETDEFS_DATASET
from payloads.dq_dgc_integration.pl_dq_dgc_integration_for_run_id_with_timestamp import (
    DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP,
    DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_NAME,
    POSTGRES_SCHEMA_NAME,
    POSTGRES_TABLE_NAME,
    DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY_NAME,
    DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DQ_BUSINESS_UNIT,
    DGC_DQ_INTEGRATION_COMMUNITY,
    DGC_UNASSIGNED_DQ_JOB_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper

helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()


@pytest.mark.dq_dgc
class TestDqDgcRunIdWithTimestamp:

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
    def run_integration_and_check_business_unit(
        api_utils, dgc_api_utils, dataset_name, dataset_run_id, business_unit
    ):
        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, dataset_name)
        dq_dgc_helper.submit_dgc_job_and_check_status(api_utils, dataset_name, dataset_run_id)

        # Verify import of DQ Job
        dq_dgc_helper.verify_dq_job_import(dataset_name, dgc_api_utils)

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(dgc_api_utils, dataset_name, business_unit)

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(dgc_api_utils, dataset_name, business_unit)

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_integration_for_run_id_with_timestamp_with_bu(self, api_utils, dgc_api_utils):
        """Verify integration for runID with timestamp and for renamed dataset, ref: DEV-95106."""
        dataset_run_id = DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Create business unit and associate the given dataset with it
        dq_dgc_helper.create_business_unit_if_not_exists(api_utils, DQ_BUSINESS_UNIT)
        dq_dgc_helper.add_dataset_to_business_unit(
            api_utils, DQ_BUSINESS_UNIT, DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_NAME
        )

        self.run_integration_and_check_business_unit(
            api_utils,
            dgc_api_utils,
            DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_NAME,
            dataset_run_id,
            DQ_BUSINESS_UNIT,
        )

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_integration_for_run_id_with_timestamp_no_bu_renamed(
        self, api_utils, dgc_api_utils
    ):
        # Check integration without business unit
        dataset_run_id = DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY["runId"]
        job_result = helper.setup_dataset(
            api_utils, DS_DEF_DGC_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY
        )
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        self.run_integration_and_check_business_unit(
            api_utils,
            dgc_api_utils,
            DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY_NAME,
            dataset_run_id,
            DGC_UNASSIGNED_DQ_JOB_COMMUNITY,
        )

        # Rename a DS and verify updated name updated in Integration
        ds_name_edit = f"{DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY_NAME}_edited"
        pl_patch = {
            "sourceDataset": DS_DEF_INTEGRATION_RUNID_WITH_TIMESTAMP_SECONDARY_NAME,
            "targetDataset": ds_name_edit,
        }
        response_rename = api_utils.patch(V2_RENAME_DATASET, params=pl_patch, return_json=False)
        assert_that(response_rename.status_code, "Rename call failed").is_equal_to(200)

        # Re-run the job, make sure new name was updated in DIP
        dataset_defs = api_utils.get(V3_DATASETDEFS_DATASET.format(dataset=ds_name_edit))
        helper.setup_dataset(api_utils, dataset_defs)

        # Verify updated information on import of DQ Job
        dq_dgc_helper.verify_dq_job_import(ds_name_edit, dgc_api_utils)
