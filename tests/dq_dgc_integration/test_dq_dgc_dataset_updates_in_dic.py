import time
import allure
import pytest
from assertpy import assert_that
from data_test.dq_dgc_integration.data_dgc_dynamic_dataset_update_rules_queries import (
    DQ_DGC_RULES_DEFINITIONS,
    DQ_DGC_RULES_EXPECTED_RESULT,
    POSTGRES_SCHEMA_NAME,
    POSTGRES_TABLE_NAME,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from payloads.dq_dgc_integration.pl_dq_dgc_dataset_updates_in_dic_querie import (
    DS_DEF_DGC_DATASET_UPDATES,
    DS_DEF_DGC_DATASET_UPDATES_NAME,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DGC_DQ_INTEGRATION_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()

dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()


@pytest.mark.dq_dgc
class TestDqDgcDatasetUpdateInDic:

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
            if relations_response["total"] == 46:
                return relations_response

            # Check if timeout has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise AssertionError(
                    f"Timeout reached. "
                    f"Expected total to be 46 but got {relations_response['total']}"
                )

            # Wait before retrying
            time.sleep(interval)

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    @pytest.mark.smoke
    def test_dq_dgc_dataset_update_in_dic(self, api_utils, dgc_api_utils):
        """Verify Dataset updates in DIC when integration is enabled, ref: DEV-83975."""
        # Run a basic job
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DS_DEF_DGC_DATASET_UPDATES)
        dataset_run_id = DS_DEF_DGC_DATASET_UPDATES["runId"]

        # Run dgc integration, no rules added
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_DATASET_UPDATES_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_DATASET_UPDATES_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_DATASET_UPDATES_NAME, dgc_api_utils
        )

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)
        assert_that(
            relations_response["total"],
            f"Unexpected number of rules appear, expected 44, but "
            f"got {relations_response['total']}",
        ).is_equal_to(44)

        # Check a global job score and other parameters before adding rules.
        dq_dgc_helper.get_attributes_details_and_validate_results(
            dgc_api_utils,
            asset_id=asset_id,
            exp_global_score=100.0,
            exp_job_row_filter=102815.0,
            exp_predicate="select * FROM public.nyse",
            exp_last_run_status=["Success"],
        )

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_DATASET_UPDATES_NAME,
            DQ_DGC_RULES_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_DATASET_UPDATES)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_DATASET_UPDATES_NAME,
            job_response["runId"],
            DQ_DGC_RULES_EXPECTED_RESULT,
        )

        relations_response = self.get_updated_relations(dgc_api_utils, assets_params)
        assert_that(
            relations_response["total"],
            f"Unexpected number of rules appear, expected 46, "
            f"but got {relations_response['total']}",
        ).is_equal_to(46)

        # Check a global job score and other parameters after adding rules.
        dq_dgc_helper.get_attributes_details_and_validate_results(
            dgc_api_utils,
            asset_id=asset_id,
            exp_global_score=25.0,
            exp_job_row_filter=102815.0,
            exp_predicate="select * from public.nyse",
            exp_last_run_status=["Failed"],
        )

        # Validate 2 new added rules
        first_rule_name = "open_less_than_10"
        second_rule_name = "simple_rule_example"
        source_first_rule = dq_dgc_helper.find_source_by_name(relations_response, first_rule_name)
        source_second_rule = dq_dgc_helper.find_source_by_name(relations_response, second_rule_name)

        expected_table_row_count = 102815.0
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_first_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=85.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_second_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=38.0,
            expected_rule_type=["Custom Rule"],
        )
