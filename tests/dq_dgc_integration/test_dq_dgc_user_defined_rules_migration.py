import allure
import pytest
from data_test.dq_dgc_integration.data_dgc_user_defined_rule_queries import (
    POSTGRES_SCHEMA_NAME,
    POSTGRES_TABLE_NAME,
)
from data_test.dq_dgc_integration.data_dgc_user_defined_rule_queries import (
    DQ_DGC_USER_DEFINED_RULES_DEFINITIONS,
    DQ_DGC_USER_DEFINED_RULES_EXPECTED_RESULT,
    DATA_CLASS_RULES_EXAMPLE,
    REGEX_RULE_EXAMPLE,
    FREEFORM_RULE_EXAMPLE,
    SIMPLE_RULE_EXAMPLE,
    TEMPLATE_RULE_EXAMPLE,
    QUICK_RULE_EXAMPLE,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from endpoints.dgc_integration.dq.dgc_connection_api import DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS
from payloads.dq_dgc_integration.pl_dq_dgc_user_defined_rules import (
    DS_DEF_DGC_USER_DEFINED_RULES,
    DS_DEF_DGC_USER_DEFINED_RULES_NAME,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DGC_DQ_INTEGRATION_COMMUNITY,
    DGC_SERVICE_TYPE,
    DGC_BASE_URL,
    DGC_AUTH_MODE,
    DGC_BASE_CREDS,
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


@pytest.mark.dq_dgc
class TestDqDgcUserDefinedRules:

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
    def test_dq_dgc_user_defined_rules_migration(self, api_utils, dgc_api_utils):
        """
        Verify user defined rule types and their migration to DIP on a job that is integration
        enabled, ref: DEV-83981.
        """
        # Run a basic job
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DS_DEF_DGC_USER_DEFINED_RULES)
        dataset_run_id = DS_DEF_DGC_USER_DEFINED_RULES["runId"]

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_USER_DEFINED_RULES_NAME,
            DQ_DGC_USER_DEFINED_RULES_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_USER_DEFINED_RULES)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_USER_DEFINED_RULES_NAME,
            job_response["runId"],
            DQ_DGC_USER_DEFINED_RULES_EXPECTED_RESULT,
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_USER_DEFINED_RULES_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_USER_DEFINED_RULES_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_USER_DEFINED_RULES_NAME, dgc_api_utils
        )

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Get a custom rule id
        source_first_rule = dq_dgc_helper.find_source_by_name(
            relations_response, DATA_CLASS_RULES_EXAMPLE
        )
        source_second_rule = dq_dgc_helper.find_source_by_name(
            relations_response, REGEX_RULE_EXAMPLE
        )
        source_third_rule = dq_dgc_helper.find_source_by_name(
            relations_response, FREEFORM_RULE_EXAMPLE
        )
        source_fourth_rule = dq_dgc_helper.find_source_by_name(
            relations_response, SIMPLE_RULE_EXAMPLE
        )
        source_fifth_rule = dq_dgc_helper.find_source_by_name(
            relations_response, TEMPLATE_RULE_EXAMPLE
        )
        source_six_rule = dq_dgc_helper.find_source_by_name(relations_response, QUICK_RULE_EXAMPLE)

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
            expected_passing_fraction=0.0,
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
            expected_passing_fraction=89.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_fifth_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=1.0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_six_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Passing"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Custom Rule"],
        )

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_addition_of_existing_dic_instance(self, api_utils):
        """Verify addition of existing DIC instance integration and enabling it, ref: DEV-83972."""
        pl_dqc_connection_creds = {
            "serviceType": DGC_SERVICE_TYPE,
            "serviceUrl": DGC_BASE_URL,
            "authMode": DGC_AUTH_MODE,
            "username": DGC_BASE_CREDS["username"],
            "password": DGC_BASE_CREDS["password"],
        }
        # Initialize setup of already existing instance
        response = api_utils.post(
            DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS, params=pl_dqc_connection_creds
        )

        existing_dgc_connection_error_output = {
            "statusCode": 400,
            "errorCode": "multipleActiveDgcConnectionError",
            "titleMessage": "Value not allowed",
            "userMessage": "Multiple instances available for the: "
            "'Data Intelligence Cloud' service type.",
            "helpMessage": "Please enter a different service type or disable existing ones.",
        }
        # Validate results
        compare_dicts_are_equal(response, existing_dgc_connection_error_output)
