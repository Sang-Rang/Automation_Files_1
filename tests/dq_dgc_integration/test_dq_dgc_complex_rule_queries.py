import allure
import pytest
from data_test.dq_dgc_integration.data_complex_rule_queries import (
    DQ_DGC_COMPLEX_RULE_DEFINITIONS,
    DQ_DGC_COMPLEX_RULE_DEFINITIONS_OUTPUT,
    DERIVED_RULE_NAME,
    ALIAS_RULE_NAME,
    INNERJOIN_RULE_NAME,
    LOOKUP_RULE_NAME,
)
from data_test.dq_dgc_integration.dq_dgc_complex_rule_governs_expexted_output import (
    DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_1,
    DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_2,
    DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_3,
    DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_4,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from payloads.dq_dgc_integration.pl_dq_dgc_complex_rule_querie import (
    DS_DEF_DGC_COMPLEX_RULE_NAME,
    DS_DEF_DGC_COMPLEX_RULE,
    DS_DEF_DGC_COMPLEX_RULE_SECONDARY,
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
from utils.validator import compare_dicts_are_equal
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()

dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()
POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"


@pytest.mark.dq_dgc
class TestDqDgcComplexRulesIntegration:

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
    def test_dq_dgc_complex_rule_queries_integration(self, api_utils, dgc_api_utils):
        # Run a job
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, DS_DEF_DGC_COMPLEX_RULE_SECONDARY
        )
        dataset_run_id = DS_DEF_DGC_COMPLEX_RULE["runId"]
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DS_DEF_DGC_COMPLEX_RULE)

        required_backruns = 2
        helper.backrun_dataset_if_needed(api_utils, DS_DEF_DGC_COMPLEX_RULE, required_backruns)

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_COMPLEX_RULE_NAME,
            DQ_DGC_COMPLEX_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_COMPLEX_RULE)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_COMPLEX_RULE_NAME,
            job_response["runId"],
            DQ_DGC_COMPLEX_RULE_DEFINITIONS_OUTPUT,
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_COMPLEX_RULE_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_COMPLEX_RULE_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(DS_DEF_DGC_COMPLEX_RULE_NAME, dgc_api_utils)

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Get a custom rule id
        source_first_rule = dq_dgc_helper.find_source_by_name(relations_response, DERIVED_RULE_NAME)
        source_second_rule = dq_dgc_helper.find_source_by_name(relations_response, ALIAS_RULE_NAME)
        source_third_rule = dq_dgc_helper.find_source_by_name(
            relations_response, INNERJOIN_RULE_NAME
        )
        source_fourth_rule = dq_dgc_helper.find_source_by_name(relations_response, LOOKUP_RULE_NAME)

        expected_table_row_count = 102815.0
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_first_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_second_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_third_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_fourth_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Custom Rule"],
        )

        # Get governs Column information and validate results
        # Rule "derivedrule_symbol_open_close_br" details
        exclude_dynamic_keys = ["id", "createdOn", "lastModifiedOn", "resourceDiscriminator"]
        rule_1_governs_response = dq_dgc_helper.get_data_governs_column_details(
            dgc_api_utils, source_first_rule["id"]
        )
        compare_dicts_are_equal(
            rule_1_governs_response, DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_1, exclude_dynamic_keys
        )

        # Rule "ff_alias_br" details
        rule_2_governs_response = dq_dgc_helper.get_data_governs_column_details(
            dgc_api_utils, source_second_rule["id"]
        )
        compare_dicts_are_equal(
            rule_2_governs_response, DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_2, exclude_dynamic_keys
        )

        # Rule "Innerjoin" details
        rule_3_governs_response = dq_dgc_helper.get_data_governs_column_details(
            dgc_api_utils, source_third_rule["id"]
        )
        compare_dicts_are_equal(
            rule_3_governs_response, DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_3, exclude_dynamic_keys
        )

        # Rule "lookuprule" details
        rule_4_governs_response = dq_dgc_helper.get_data_governs_column_details(
            dgc_api_utils, source_fourth_rule["id"]
        )
        compare_dicts_are_equal(
            rule_4_governs_response, DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_4, exclude_dynamic_keys
        )
