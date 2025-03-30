import allure
import pytest
from assertpy import assert_that
from data_test.dq_dgc_integration.data_quality_tab_overview_rule_queries import (
    DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_QUERIES,
    DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_EXPECTED_RESULT,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from payloads.dq_dgc_integration.pl_dq_dgc_quality_tab_overivew_for_dataset import (
    DS_DEF_DGC_QUALITY_TAB_OVERVIEW_FOR_DATASET,
    DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
    POSTGRES_SCHEMA_NAME,
    POSTGRES_TABLE_NAME,
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
class TestDqDgcQualityTabOverview:

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
    def test_dq_dgc_quality_tab_overview_and_details_for_dataset(self, api_utils, dgc_api_utils):
        """
        Verify Quality tab Overview section for dataset, rule in Banyan, ref: DEV-83985
        Verify Quality tab Details section for dataset, rule in Banyan, ref: DEV-83986
        """
        # Backrun a WF to see if updates score got to DIP
        required_back_runs = 2
        helper.backrun_dataset_if_needed(
            api_utils, DS_DEF_DGC_QUALITY_TAB_OVERVIEW_FOR_DATASET, required_back_runs
        )

        helper.setup_dataset(api_utils, DS_DEF_DGC_QUALITY_TAB_OVERVIEW_FOR_DATASET)

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
            DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_QUERIES,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_QUALITY_TAB_OVERVIEW_FOR_DATASET)

        validate_rules_findings(
            api_utils,
            DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
            job_response["runId"],
            DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_EXPECTED_RESULT,
        )

        # Run DGC integration
        dataset_run_id = DS_DEF_DGC_QUALITY_TAB_OVERVIEW_FOR_DATASET["runId"]
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME, dgc_api_utils
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
            f"expected 53.0, but got {response['score']}",
        ).is_equal_to(53.0)

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)
        custom_1_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, "sales_rep_rule08"
        )

        # Assert each rule results from the DGC page
        expected_table_row_count = 4999
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=custom_1_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=53.0,
            expected_rule_type=["Custom Rule"],
        )

        # Get Quality Tab details for DQ rule
        rule_id = custom_1_rule_output["id"]
        response = dq_dgc_helper.get_quality_tab_information(dgc_api_utils, rule_id)
        print(response)
        assert_that(
            response["asset"]["type"]["name"],
            f"Invalid asset type name returned, "
            f"expected 'Data Quality Rule', but got {response['asset']['type']['name']}",
        ).is_equal_to("Data Quality Rule")
        assert_that(
            response["score"],
            f"Invalid quality score returned, "
            f"expected 53.0, but got {response['score']}",
        ).is_equal_to(53.0)
