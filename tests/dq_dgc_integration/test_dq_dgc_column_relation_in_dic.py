import allure
import pytest

from data_test.dq_dgc_integration.data_dgc_column_relation_rule_queries import (
    DQ_DGC_COLUMN_RELATION_RULE_DEFINITIONS,
    DQ_DGC_COLUMN_RELATION_RULE_OUTPUT,
)
from data_test.dq_dgc_integration.data_dgc_governs_column_relation_in_dip import (
    OUTLIERS_GOVERNS_COLUMN_OUTPUT,
    CUSTOM_RULE_GOVERNS_COLUMN_OUTPUT,
    PATTERNS_RULE_GOVERNS_COLUMN_OUTPUT,
    SOURCE_RULE_GOVERNS_COLUMN_OUTPUT,
    RECORD_RULE_GOVERNS_COLUMN_OUTPUT,
    SCHEMA_RULE_GOVERNS_COLUMN_OUTPUT,
    DUPES_RULE_GOVERNS_COLUMN_OUTPUT,
    SHAPES_RULE_GOVERNS_COLUMN_OUTPUT,
    SALES_REP_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT,
    SALE_STATE_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT,
    REPRESENTS_TABLE_OUTPUT,
)
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from payloads.dq_dgc_integration.pl_dq_dgc_all_features_on import DS_DEF_DGC_ALL_FEATURES_ON
from payloads.dq_dgc_integration.pl_dq_dgc_column_relation_in_dic import (
    DS_DEF_DGC_COLUMN_RELATION_IN_DIC,
    DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
    DS_DEF_DGC_COLUMN_RELATIONS_SECONDARY,
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
POSTGRES_TABLE_NAME = "sales_data_002"


@pytest.mark.dq_dgc
class TestDqDgColumnRelationInDic:

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
    def test_dq_dgc_column_relation_in_dic(self, api_utils, dgc_api_utils):
        """Column relation in DIC for adaptive rules, custom rule, Outliers, Dupes, Shapes,
        Patterns, Source, Schema, Record changes rules and Table relation for DQ job,
        ref: DEV-83969.
        """
        # Run a job
        required_back_runs = 5
        helper.backrun_dataset_if_needed(
            api_utils, DS_DEF_DGC_COLUMN_RELATION_IN_DIC, required_back_runs
        )

        helper.setup_dataset(api_utils, DS_DEF_DGC_COLUMN_RELATION_IN_DIC)

        helper.set_rules_on_dataset(
            api_utils,
            DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
            DQ_DGC_COLUMN_RELATION_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, DS_DEF_DGC_COLUMN_RELATIONS_SECONDARY)

        validate_rules_findings(
            api_utils,
            DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
            job_response["runId"],
            DQ_DGC_COLUMN_RELATION_RULE_OUTPUT,
        )

        # Run DGC integration
        dataset_run_id = DS_DEF_DGC_ALL_FEATURES_ON["runId"]
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_COLUMN_RELATION_JOB_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_COLUMN_RELATION_JOB_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_COLUMN_RELATION_JOB_NAME, dgc_api_utils
        )

        # Verify represents table is showing for DQ job asset in DIP.
        exclude_dynamic_keys = ["id", "createdOn", "createdBy", "lastModifiedOn"]
        represents_table_relation_id = "00000000-0000-0000-0000-090000010026"
        relation_params = {"relationTypeId": represents_table_relation_id, "sourceId": asset_id}
        represents_table_response = dgc_api_utils.get(DGC_RELATIONS, params=relation_params)
        compare_dicts_are_equal(
            represents_table_response, REPRESENTS_TABLE_OUTPUT, exclude_dynamic_keys
        )

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Rule names for validation
        outlier_finding = "Outlier Finding"
        source_findings = "Source Finding"
        shape_finding = "Shape Finding"
        schema_finding = "Schema Finding"
        record_finding = "Record Finding"
        pattern_finding = "Pattern Finding"
        duplicate_finding = "Duplicate Finding"
        custom_sales_rep_rule = "sales_rep_rule"
        sales_rep_adaptive = "sales_rep:Empty Range"
        sale_state_adaptive = "sale_state:Null Range"

        # Get a rule id for the specific rule
        source_rule_output = dq_dgc_helper.find_source_by_name(relations_response, source_findings)
        shape_rule_output = dq_dgc_helper.find_source_by_name(relations_response, shape_finding)
        schema_rule_output = dq_dgc_helper.find_source_by_name(relations_response, schema_finding)
        record_rule_output = dq_dgc_helper.find_source_by_name(relations_response, record_finding)
        pattern_rule_output = dq_dgc_helper.find_source_by_name(relations_response, pattern_finding)
        outlier_rule_output = dq_dgc_helper.find_source_by_name(relations_response, outlier_finding)

        # Get relations column response for different rules
        custom_sales_rep_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, custom_sales_rep_rule
        )
        duplicate_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, duplicate_finding
        )

        sales_rep_adaptive_rule_output = dq_dgc_helper.find_source_by_name(
            relations_response, sales_rep_adaptive
        )
        sale_state_adaptive_output = dq_dgc_helper.find_source_by_name(
            relations_response, sale_state_adaptive
        )

        outlier_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, outlier_rule_output
        )
        compare_dicts_are_equal(
            outlier_governs, OUTLIERS_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        custom_sales_rep_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, custom_sales_rep_rule_output
        )
        compare_dicts_are_equal(
            custom_sales_rep_rule_governs, CUSTOM_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        pattern_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, pattern_rule_output
        )
        compare_dicts_are_equal(
            pattern_rule_governs, PATTERNS_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        source_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, source_rule_output
        )
        compare_dicts_are_equal(
            source_rule_governs, SOURCE_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        record_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, record_rule_output
        )
        compare_dicts_are_equal(
            record_rule_governs, RECORD_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        schema_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, schema_rule_output
        )
        compare_dicts_are_equal(
            schema_rule_governs, SCHEMA_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        dupes_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, duplicate_rule_output
        )
        compare_dicts_are_equal(
            dupes_rule_governs, DUPES_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        shapes_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, shape_rule_output
        )
        compare_dicts_are_equal(
            shapes_rule_governs, SHAPES_RULE_GOVERNS_COLUMN_OUTPUT, exclude_dynamic_keys
        )

        sales_rep_adaptive_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, sales_rep_adaptive_rule_output
        )
        compare_dicts_are_equal(
            sales_rep_adaptive_rule_governs,
            SALES_REP_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT,
            exclude_dynamic_keys,
        )

        sale_state_adaptive_rule_governs = dq_dgc_helper.get_governs_column_info_for_rule_id(
            dgc_api_utils, sale_state_adaptive_output
        )
        compare_dicts_are_equal(
            sale_state_adaptive_rule_governs,
            SALE_STATE_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT,
            exclude_dynamic_keys,
        )
