import allure
import pytest

from data_test.dq_dgc_integration.dq_dgc_all_features_on_rule_queries import (
    DQ_DGC_ALL_FEATURES_ON_QUERIES,
    DQ_DGC_ALL_FEATURES_RULE_DEFINITIONS_OUTPUT,
    ADAPTIVE_RULE_EXPECTED_DESCRIPTION,
    DUPLICATE_RULE_EXPECTED_DESCRIPTION,
    OUTLIER_RULE_EXPECTED_DESCRIPTION,
    PATTERN_RULE_EXPECTED_DESCRIPTION,
    RECORD_RULE_EXPECTED_DESCRIPTION,
    SCHEMA_RULE_EXPECTED_DESCRIPTION,
    SHAPE_RULE_EXPECTED_DESCRIPTION,
    SOURCE_RULE_EXPECTED_DESCRIPTION,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from payloads.dq_dgc_integration.pl_dq_dgc_all_features_on import (
    DS_DEF_DGC_ALL_FEATURES_ON,
    DS_DEF_DGC_ALL_FEATURES_ON_NAME,
    DS_DEF_DGC_ALL_FEATURES_SECONDARY,
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
POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"


@pytest.mark.dq_dgc
class TestDqDgcAllFeaturesOn:

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
    @pytest.mark.flaky(retries=2, delay=5)
    def test_dq_dgc_integration_with_all_features_on(self, api_utils, dgc_api_utils):
        # Run a job
        required_back_runs = 5
        helper.backrun_dataset_if_needed(api_utils, DS_DEF_DGC_ALL_FEATURES_ON, required_back_runs)

        helper.setup_dataset(api_utils, DS_DEF_DGC_ALL_FEATURES_ON)

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            DQ_DGC_ALL_FEATURES_ON_QUERIES,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_ALL_FEATURES_SECONDARY)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            job_response["runId"],
            DQ_DGC_ALL_FEATURES_RULE_DEFINITIONS_OUTPUT,
        )

        # Run DGC integration
        dataset_run_id = DS_DEF_DGC_ALL_FEATURES_ON["runId"]
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_ALL_FEATURES_ON_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_ALL_FEATURES_ON_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_ALL_FEATURES_ON_NAME, dgc_api_utils
        )

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Rule names for validation
        source_findings = "Source Finding"
        shape_finding = "Shape Finding"
        schema_finding = "Schema Finding"
        record_finding = "Record Finding"
        pattern_finding = "Pattern Finding"
        outlier_finding = "Outlier Finding"
        duplicate_finding = "Duplicate Finding"
        sqlg_rule_1 = "SQLG_LASTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586"
        sqlg_rule_2 = "SQLG_FIRSTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586"
        custom_rule_1 = "if_costcode_is_SALES_CUSTOM_RULE"
        custom_rule_2 = "SQLF_RULE_POSTMAN_GOLDEN_RUN_1721685131586"
        cost_max_value = "cost:Max Value Range"
        cost_min_value = "cost:Min Value Range"
        sales_state_unique = "salestate:Unique Range"
        rep_unique = "rep:Unique Range"

        # Get a rule id for the specific rule
        source_rule_output = dq_dgc_helper.find_source_by_name(relations_response, source_findings)
        shape_rule_output = dq_dgc_helper.find_source_by_name(relations_response, shape_finding)
        schema_rule_output = dq_dgc_helper.find_source_by_name(relations_response, schema_finding)
        record_rule_output = dq_dgc_helper.find_source_by_name(relations_response, record_finding)
        pattern_rule_output = dq_dgc_helper.find_source_by_name(relations_response, pattern_finding)
        outlier_rule_output = dq_dgc_helper.find_source_by_name(relations_response, outlier_finding)
        duplicate_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, duplicate_finding
        )
        sqlg_1_rule_output = dq_dgc_helper.find_source_by_name(relations_response, sqlg_rule_1)
        sqlg_2_rule_output = dq_dgc_helper.find_source_by_name(relations_response, sqlg_rule_2)
        custom_1_rule_output = dq_dgc_helper.find_source_by_name(relations_response, custom_rule_1)
        custom_2_rule_output = dq_dgc_helper.find_source_by_name(relations_response, custom_rule_2)
        cost_max_value_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, cost_max_value
        )
        cost_min_value_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, cost_min_value
        )
        sales_state_unique_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, sales_state_unique
        )
        rep_unique_rule_output = dq_dgc_helper.find_source_by_name(relations_response, rep_unique)

        # Assert each rule results from the DGC page
        expected_table_row_count = 999
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=69.0,
            expected_rule_type=["Source"],
            expected_rule_description=SOURCE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=shape_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=97.0,
            expected_rule_type=["Shape"],
            expected_rule_description=SHAPE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=schema_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Schema"],
            expected_rule_description=SCHEMA_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=record_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Record"],
            expected_rule_description=RECORD_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=pattern_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Pattern"],
            expected_rule_description=PATTERN_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=outlier_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=97.0,
            expected_rule_type=["Outlier"],
            expected_rule_description=OUTLIER_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=duplicate_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=99.0,
            expected_rule_type=["Duplicate"],
            expected_rule_description=DUPLICATE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=sqlg_1_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=sqlg_2_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=custom_1_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=custom_2_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=0,
            expected_rule_type=["Custom Rule"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=cost_max_value_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=70.0,
            expected_rule_type=["Adaptive Rule"],
            expected_rule_description=ADAPTIVE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=cost_min_value_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=70.0,
            expected_rule_type=["Adaptive Rule"],
            expected_rule_description=ADAPTIVE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=sales_state_unique_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=90.0,
            expected_rule_type=["Adaptive Rule"],
            expected_rule_description=ADAPTIVE_RULE_EXPECTED_DESCRIPTION,
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=rep_unique_rule_output,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=70.0,
            expected_rule_type=["Adaptive Rule"],
            expected_rule_description=ADAPTIVE_RULE_EXPECTED_DESCRIPTION,
        )
