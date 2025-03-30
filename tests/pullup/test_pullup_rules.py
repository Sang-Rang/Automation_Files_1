import json
import time

import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_create_apply_template import (
    PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
    QUERY_TEMPLATE,
    CONNECTION_TEMPLATE,
    PL_VALIDATE_TEMPLATE,
    EX_RESPONSE_TEMPLATE,
    INPUTS_TEMPLATE,
    PL_CREATE_CUSTOM_TEMPLATE,
    PL_ADD_RULE_TEMPLATE,
    PL_ADD_RULE_BREAK_TEMPLATE,
    PL_DELETE_CUSTOM_TEMPLATE,
    PL_GENERAL,
    EX_CREATE_RULE,
    EX_CREATE_RULE2,
    PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_EXPECTED_RULE_OUTPUT,
    RUN_ID_FULL_TEMPLATE,
)
from data_test.pullup.data_export_rules import (
    CONNECTION_EXPORT_RULE_DETAILS,
    DATASET_EXPORT_RULE_DETAILS,
    QUERY_EXPORT_RULE_DETAILS,
    EXP_EXPORT_RULE_DETAILS,
    PL_EXPORT_RULE_DETAILS,
    PL_GEN_EXPORT_RULE_DETAILS,
    RUN_ID_EXPORT_RULE_DETAILS,
)
from data_test.pullup.data_pullup_20_rules_on_large_dataset import (
    PULLUP_TWENTY_RULES_ON_LARGE_DATASET_EXPECTED_RULE_OUTPUT,
    PULLUP_TWENTY_RULES_ON_LARGE_DATASET_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_complex_rule_freeform import (
    PULLUP_COMPLEX_RULE_FREEFORM_EXPECTED_RULE_OUTPUT,
    PULLUP_COMPLEX_RULE_FREEFORM_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_historical_rule import (
    PULLUP_HISTORICAL_RULE_EXPECTED_RULE_OUTPUT,
    PULLUP_HISTORICAL_RULE_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_multipath_editing import (
    RULES_ALL_PATHS_QUERY,
    RULES_ALL_PATHS_CONN,
    RULES_ALL_PATHS_DS,
    RULES_ALL_PATHS_V3_SIMPLE1,
    RULES_ALL_PATHS_V3_FREEFORM1,
    RULES_ALL_PATHS_V2_QUICK_RULE,
    RULES_ALL_PATHS_V2_RULE,
    EXPECTED_RULE_OUT1,
    RULES_ALL_PATHS_RUN_ID_FULL,
    RULES_ALL_PATHS_V3_FREEFORM2,
    EXPECTED_RULE_OUT2,
    RULES_ALL_PATHS_V2_QUICK_RULE2,
)
from data_test.pullup.data_pullup_rule_sql_types import (
    PULLUP_RULES_SQL_TYPES_DATASET,
    PULLUP_RULES_SQL_TYPES_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_SQL_TYPES_RULE_DEFINITIONS,
    CONNECTION_SQL_TYPE,
    QUERY_SQL_TYPE,
    FULL_RUN_ID_SQL_TYPE,
    FULL_RUN_ID_SQL_TYPE_PWDMGR,
    PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_DATASET,
    PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_RULE_DEFINITIONS,
    PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_PAYLOAD,
)
from data_test.pullup.data_pullup_rules_addlib_join import (
    PULLUP_RULES_ADDLIB_JOIN_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_ADDLIB_JOIN_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_binary_sales import (
    PULLUP_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_BINARY_SALES_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_data_class_regex import (
    PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
    PL_V2_CREATE_RULE_DC_REGEX,
    PL_V2_CREATE_RULE_DC_NO_REGEX,
    PL_V2_ASSIGN_RULE_REGEX,
    PL_V2_ASSIGN_RULE_NO_REGEX,
    RULE_SAVED_MSG,
    PULLUP_RULES_DATA_CLASS_REGEX_EXPECTED_RULE_OUTPUT,
    QUERY_DC_RULE_REGEX,
    CONN_DC_RULE_REGEX,
    PROD_RUN_ID_FULL,
)
from data_test.pullup.data_pullup_rules_filter_tolerance_sales import (
    PULLUP_RULES_FILTER_TOLERANCE_SALES_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_FILTER_TOLERANCE_SALES_FF_FILTER_AND_TOLERANCE_EXPECTED_RULE_DATA_PREVIEW,
    PULLUP_RULES_FILTER_TOLERANCE_SALES_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_link_id_breaks import (
    PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_LINK_ID_BREAKS_RULE_DEFINITIONS,
    PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS,
    PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS_V2,
)
from data_test.pullup.data_pullup_rules_s3_to_jdbc import (
    PULLUP_RULES_S3_TO_JDBC_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_S3_TO_JDBC_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_sales import (
    PULLUP_RULES_SALES_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_SALES_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_sales_link_id import (
    PULLUP_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_SALES_LINK_ID_FF_ALL_COLUMNS_EXPECTED_CSV_OUTPUT,
    PULLUP_RULES_SALES_LINK_ID_RULE_DEFINITIONS,
    PULLUP_RULES_SALES_LINK_ID_SIMPLE_LINK_COLUMN_EXPECTED_CSV_OUTPUT,
    PULLUP_RULES_SALES_LINK_ID_SIMPLE_NO_LINK_COLUMN_EXPECTED_CSV_OUTPUT,
    PULLUP_RULES_SALES_LINK_ID_STAT_RULE_EXPECTED_CSV_OUTPUT,
)
from data_test.pullup.data_pullup_rules_secondary_dataset import (
    PULLUP_RULES_SECONDARY_DATASET_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_SECONDARY_DATASET_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_temporal_sales import (
    PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29,
    PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30,
    PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01,
    PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02,
    PULLUP_RULES_TEMPORAL_SALES_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_rules_two_jdbc_s3 import (
    PULLUP_RULES_TWO_JDBC_S3_EXPECTED_RULE_OUTPUT,
    PULLUP_RULES_TWO_JDBC_S3_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_stat_rule import (
    PULLUP_STAT_RULE_EXPECTED_RULE_OUTPUT,
    PULLUP_STAT_RULE_RULE_DEFINITIONS,
)
from data_test.pullup.data_pullup_test_all_rule_types import (
    PULLUP_TEST_ALL_RULE_TYPES_EXPECTED_RULE_OUTPUT,
    PULLUP_TEST_ALL_RULE_TYPES_RULE_DEFINITIONS,
)
from endpoints.v2.controller import V2_GET_LATEST_DATASET_HISTORY
from endpoints.v2.controller_rule import (
    V2_CREATE_RULE,
    V2_CREATE_RULE2,
    V2_GET_ACTIVE_RULES_COUNT,
    V2_GET_RULES,
    V2_VALIDATE_SYNTAX,
    V2_VALIDATE_SPARK_REGEX,
    V2_CREATE_CUSTOM_RULE,
    V2_TEMPLATE_RULES,
    V2_DELETE_CUSTOM_RULE,
    V2_GET_RULE_OUTPUT2,
    V2_GET_RULE_WITH_DETAILS,
    V2_INSERT_CUSTOM_RULE,
)
from endpoints.v3.rule_api import V3_RULES, V3_RULES_COPY
from payloads.pullup.pl_pullup_20_rules_on_large_dataset import (
    PULLUP_TWENTY_RULES_ON_LARGE_DATASET_PAYLOAD,
)
from payloads.pullup.pl_pullup_complex_rule_freeform import (
    PULLUP_COMPLEX_RULE_FREEFORM_PAYLOAD,
    PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_PAYLOAD,
    PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
)
from payloads.pullup.pl_pullup_historical_rule import (
    PULLUP_HISTORICAL_RULE_DATASET,
    PULLUP_HISTORICAL_RULE_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_addlib_join import (
    PULLUP_RULES_ADDLIB_JOIN_PAYLOAD,
    PULLUP_RULES_ADDLIB_JOIN_DATASET,
)
from payloads.pullup.pl_pullup_rules_addlib_join1 import (
    PULLUP_RULES_ADDLIB_JOIN1_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_binary_sales import (
    PULLUP_RULES_BINARY_SALES_DATASET,
    PULLUP_RULES_BINARY_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_filter_tolerance_sales import (
    PULLUP_RULES_FILTER_TOLERANCE_SALES_DATASET,
    PULLUP_RULES_FILTER_TOLERANCE_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_link_id_breaks import (
    PULLUP_RULES_LINK_ID_BREAKS_PAYLOAD,
    PULLUP_RULES_LINK_ID_BREAKS_DATASET,
)
from payloads.pullup.pl_pullup_rules_s3_to_jdbc import (
    PULLUP_RULES_S3_TO_JDBC_PAYLOAD,
    PULLUP_RULES_S3_TO_JDBC_DATASET,
)
from payloads.pullup.pl_pullup_rules_sales import (
    PULLUP_RULES_SALES_DATASET,
    PULLUP_RULES_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_sales_link_id import (
    PULLUP_RULES_SALES_LINK_ID_DATASET,
    PULLUP_RULES_SALES_LINK_ID_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_secondary_dataset import (
    PULLUP_RULES_SECONDARY_DATASET_PAYLOAD,
    PULLUP_RULES_SECONDARY_DATASET_DATASET,
)
from payloads.pullup.pl_pullup_rules_secondary_dataset_1 import (
    PULLUP_RULES_SECONDARY_DATASET1_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_temporal_sales import (
    PULLUP_RULES_TEMPORAL_SALES_DATASET,
    PULLUP_RULES_TEMPORAL_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_rules_two_jdbc_s3 import (
    PULLUP_RULES_TWO_JDBC_S3_PAYLOAD,
    PULLUP_RULES_TWO_JDBC_S3_DATASET,
)
from payloads.pullup.pl_pullup_stat_rule import (
    PULLUP_STAT_RULE_PAYLOAD,
    PULLUP_STAT_RULE_DATASET,
)
from payloads.pullup.pl_pullup_test_all_rule_types import (
    PULLUP_TEST_ALL_RULE_TYPES_PAYLOAD,
)
from payloads.pullup.pl_rules_copy import (
    DS_DEFS_COPY_TARGET_NAME,
    PL_RULES_SOURCE_COPY,
    DS_DEFS_COPY_SOURCE_NAME,
    PL_RULES_COPY,
    DS_DEFS_COPY_TARGET_RUN_ID,
    DS_DEFS_COPY_SOURCE,
    DS_DEFS_COPY_TARGET,
    PL_RULES,
)
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper
from utils.validator import validate_rule_data_preview
from utils.validator_rules import (
    validate_rule_breaks,
    validate_rule_breaks_v2,
    validate_rules_findings,
    validate_downloaded_rule_breaks,
)

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupRules:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_20_rules_on_large_dataset(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_TWENTY_RULES_ON_LARGE_DATASET_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_TWENTY_RULES_ON_LARGE_DATASET_PAYLOAD["dataset"],
            PULLUP_TWENTY_RULES_ON_LARGE_DATASET_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_TWENTY_RULES_ON_LARGE_DATASET_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_TWENTY_RULES_ON_LARGE_DATASET_PAYLOAD["dataset"],
            job_response["runId"],
            PULLUP_TWENTY_RULES_ON_LARGE_DATASET_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    @pytest.mark.smoke
    def test_pullup_test_all_rule_types(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_TEST_ALL_RULE_TYPES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_TEST_ALL_RULE_TYPES_PAYLOAD["dataset"],
            PULLUP_TEST_ALL_RULE_TYPES_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_TEST_ALL_RULE_TYPES_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_TEST_ALL_RULE_TYPES_PAYLOAD["dataset"],
            job_response["runId"],
            PULLUP_TEST_ALL_RULE_TYPES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_multipath_editing(self, api_utils):
        ds_defs = helper.get_minimum_job_payload(
            api_utils, RULES_ALL_PATHS_CONN, RULES_ALL_PATHS_DS, RULES_ALL_PATHS_QUERY
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)

        # Delete existing rules and create V3 rules
        helper.set_rules_on_dataset(
            api_utils,
            RULES_ALL_PATHS_DS,
            [RULES_ALL_PATHS_V3_SIMPLE1, RULES_ALL_PATHS_V3_FREEFORM1],
        )

        # Create rule
        v2_rule = api_utils.post(V2_CREATE_RULE, params=RULES_ALL_PATHS_V2_RULE, return_json=False)
        assert_that(v2_rule.status_code, "V2 Create Rule").is_equal_to(200)

        # Create quick rule
        v2_quick_rule = api_utils.post(
            V2_CREATE_RULE2, params=RULES_ALL_PATHS_V2_QUICK_RULE, return_json=False
        )
        assert_that(v2_quick_rule.status_code, "V2 Quick Rule").is_equal_to(200)

        helper.setup_dataset(api_utils, ds_defs)

        # Validate findings
        validate_rules_findings(
            api_utils, ds_defs["dataset"], RULES_ALL_PATHS_RUN_ID_FULL, EXPECTED_RULE_OUT1
        )

        # Edit existing rules and rerun
        v2_update = api_utils.post(
            V2_CREATE_RULE2, params=RULES_ALL_PATHS_V2_QUICK_RULE2, return_json=False
        )
        assert_that(v2_update.status_code, "V2 Create Rule to Update").is_equal_to(200)

        v3_update = api_utils.post(
            V3_RULES, data=json.dumps(RULES_ALL_PATHS_V3_FREEFORM2), return_json=False
        )
        assert_that(v3_update.status_code, "V3 Rule Update").is_equal_to(200)

        helper.setup_dataset(api_utils, ds_defs)

        # Validate findings
        validate_rules_findings(
            api_utils, ds_defs["dataset"], RULES_ALL_PATHS_RUN_ID_FULL, EXPECTED_RULE_OUT2
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_complex_rule_freeform(self, api_utils):
        # This test requires a secondary dataset
        # Ensure it exists prior to running the test
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_PAYLOAD
        )

        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_COMPLEX_RULE_FREEFORM_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
            PULLUP_COMPLEX_RULE_FREEFORM_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_COMPLEX_RULE_FREEFORM_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
            job_response["runId"],
            PULLUP_COMPLEX_RULE_FREEFORM_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_s3_to_jdbc(self, api_utils):
        # This test requires a secondary dataset
        # Ensure it exists prior to running the test
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_TWO_JDBC_S3_PAYLOAD)

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_S3_TO_JDBC_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_S3_TO_JDBC_DATASET,
            PULLUP_RULES_S3_TO_JDBC_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_S3_TO_JDBC_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_S3_TO_JDBC_DATASET,
            job_response["runId"],
            PULLUP_RULES_S3_TO_JDBC_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_two_jdbc_s3(self, api_utils):
        # This test requires a secondary dataset
        # Ensure it exists prior to running the test
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_S3_TO_JDBC_PAYLOAD)

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_TWO_JDBC_S3_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_TWO_JDBC_S3_DATASET,
            PULLUP_RULES_TWO_JDBC_S3_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_TWO_JDBC_S3_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_TWO_JDBC_S3_DATASET,
            job_response["runId"],
            PULLUP_RULES_TWO_JDBC_S3_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_stat_rule(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_STAT_RULE_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_STAT_RULE_DATASET,
            PULLUP_STAT_RULE_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_STAT_RULE_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_STAT_RULE_DATASET,
            job_response["runId"],
            PULLUP_STAT_RULE_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_link_id_breaks(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_LINK_ID_BREAKS_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            PULLUP_RULES_LINK_ID_BREAKS_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_LINK_ID_BREAKS_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            job_response["runId"],
            PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_RULE_OUTPUT,
        )
        validate_rule_breaks(
            api_utils,
            PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            job_response["runId"],
            PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS,
        )

        validate_rule_breaks_v2(
            api_utils,
            PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            job_response["runId"],
            PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS_V2,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_secondary_dataset(self, api_utils):
        # This test requires a secondary dataset
        # Ensure it exists prior to running the test
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_SECONDARY_DATASET1_PAYLOAD
        )

        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_SECONDARY_DATASET_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_SECONDARY_DATASET_DATASET,
            PULLUP_RULES_SECONDARY_DATASET_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_SECONDARY_DATASET_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_SECONDARY_DATASET_DATASET,
            job_response["runId"],
            PULLUP_RULES_SECONDARY_DATASET_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_addlib_join(self, api_utils):
        # This test requires a secondary dataset
        # Ensure it exists prior to running the test
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_ADDLIB_JOIN1_PAYLOAD
        )

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_ADDLIB_JOIN_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_ADDLIB_JOIN_DATASET,
            PULLUP_RULES_ADDLIB_JOIN_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_ADDLIB_JOIN_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_ADDLIB_JOIN_DATASET,
            job_response["runId"],
            PULLUP_RULES_ADDLIB_JOIN_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_sql_types(self, api_utils):
        """Rule SQL Types DEV-48989"""

        # Note: Data-driven test, review during consolidation DEV-57741
        pullup_rules_sql_types_dataset_defs = helper.get_minimum_job_payload(
            api_utils, CONNECTION_SQL_TYPE, PULLUP_RULES_SQL_TYPES_DATASET, QUERY_SQL_TYPE
        )
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, pullup_rules_sql_types_dataset_defs
        )

        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_SQL_TYPES_DATASET,
            PULLUP_RULES_SQL_TYPES_RULE_DEFINITIONS,
        )

        helper.setup_dataset(api_utils, pullup_rules_sql_types_dataset_defs)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_SQL_TYPES_DATASET,
            FULL_RUN_ID_SQL_TYPE,
            PULLUP_RULES_SQL_TYPES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    @pytest.mark.flaky(retries=2, delay=5)
    def test_pullup_create_apply_template_rule(self, api_utils):
        """Rules - Create and Apply Template DEV-48988"""

        # Run job and check regex
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION_TEMPLATE,
            PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
            QUERY_TEMPLATE,
        )
        spark = api_utils.post(V2_VALIDATE_SPARK_REGEX, params=PL_VALIDATE_TEMPLATE)

        # Validate regex condition and breaks data passed with given data
        assert_that(spark["condition"], "Validate Spark Regex Condition").is_equal_to(
            EX_RESPONSE_TEMPLATE["condition"]
        )
        breaks = spark["breaks"][f"[{INPUTS_TEMPLATE}]"]
        assert_that(breaks, "Regex Breaks").contains(EX_RESPONSE_TEMPLATE["breaks"])

        # Create custom template rule
        custom = api_utils.post(V2_CREATE_CUSTOM_RULE, data=json.dumps(PL_CREATE_CUSTOM_TEMPLATE))
        assert_that(custom["message"], "Create Custom Rule").is_equal_to("Success")

        # Create the dataset, then add rules to job
        helper.setup_dataset(api_utils, dataset_defs)

        add_rule1 = api_utils.post(V3_RULES, data=json.dumps(PL_ADD_RULE_TEMPLATE))
        for key, expected_value in EX_CREATE_RULE.items():
            assert_that(expected_value, f"Create Rule 1 - Key {key}").is_equal_to(add_rule1[key])
        add_rule2 = api_utils.post(V3_RULES, data=json.dumps(PL_ADD_RULE_BREAK_TEMPLATE))
        for key, expected_value in EX_CREATE_RULE2.items():
            assert_that(expected_value, f"Create Rule 2 - Key {key}").is_equal_to(add_rule2[key])

        helper.setup_dataset(api_utils, dataset_defs)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
            RUN_ID_FULL_TEMPLATE,
            PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_EXPECTED_RULE_OUTPUT,
        )

        # Delete custom template rule and validate deleted
        api_utils.post(
            V2_DELETE_CUSTOM_RULE,
            params=PL_DELETE_CUSTOM_TEMPLATE,
            return_json=False,
        )

        call_get_template_rules_deleted = api_utils.get(V2_TEMPLATE_RULES, params=PL_GENERAL)
        assert_that(
            call_get_template_rules_deleted, "Deleted rule should not exist"
        ).does_not_contain(PL_DELETE_CUSTOM_TEMPLATE["customrulename"])

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_validate_syntax_rules(self, api_utils):
        """Test validate syntax of rules"""

        # NOTES:
        # This does not automate the generation of the Excel file
        # Test verifies the API provides accurate data to excel download.
        # Excel does output all the given data. There are over 50 columns.
        data_rules = [
            {
                "dataset": PL_GEN_EXPORT_RULE_DETAILS["dataset"],
                "type": "NATIVE",
                "runId": PROD_RUN_ID,
                "value": 'select * from NYSE where NYSE."CLOSE" = 25.300',
            },
            {
                "dataset": PL_GEN_EXPORT_RULE_DETAILS["dataset"],
                "type": "SQLF",
                "runId": PROD_RUN_ID,
                "value": f"select * from @{PL_GEN_EXPORT_RULE_DETAILS['dataset']} A "
                "where A.ADJ_RATE_CHANGE > 1",
            },
            {
                "dataset": PL_GEN_EXPORT_RULE_DETAILS["dataset"],
                "type": "SQLG",
                "runId": PROD_RUN_ID,
                "value": "AUTO_LN_RATE > 0",
            },
        ]

        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION_EXPORT_RULE_DETAILS,
            DATASET_EXPORT_RULE_DETAILS,
            QUERY_EXPORT_RULE_DETAILS,
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dataset_defs)
        latest_run_id = api_utils.get(
            V2_GET_LATEST_DATASET_HISTORY, params={"dataset": PL_GEN_EXPORT_RULE_DETAILS["dataset"]}
        )["runId"]

        # Validate Rule Syntax the rules
        for rule in data_rules:
            rule["runId"] = latest_run_id

            syntax = api_utils.get(V2_VALIDATE_SYNTAX, params=rule)
            assert_that(
                syntax["message"],
                f"Syntax check failed. Found: {syntax['message']} with rule data: {rule}",
            ).is_equal_to("success")

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_validate_schema_export_rules(self, api_utils):
        """Test validate schema export of rules"""
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION_EXPORT_RULE_DETAILS,
            DATASET_EXPORT_RULE_DETAILS,
            QUERY_EXPORT_RULE_DETAILS,
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dataset_defs)

        # Create the rules
        helper.set_rules_on_dataset(
            api_utils, PL_GEN_EXPORT_RULE_DETAILS["dataset"], PL_EXPORT_RULE_DETAILS, True
        )

        count_active_rules = api_utils.get(
            V2_GET_ACTIVE_RULES_COUNT, params=PL_GEN_EXPORT_RULE_DETAILS
        )
        assert_that(count_active_rules["count"], "Active Rules Count").is_equal_to(
            len(PL_EXPORT_RULE_DETAILS)
        )

        # Re-Run the Job
        helper.setup_dataset(api_utils, dataset_defs)

        # Get rule data from job
        rule_output = api_utils.get(V2_GET_RULE_OUTPUT2, PL_GEN_EXPORT_RULE_DETAILS)["data"]

        # Sanity Check. Data rule validation covered in other test.
        assert_that(len(rule_output), "Rule Output Quantity").is_equal_to(
            len(PL_EXPORT_RULE_DETAILS)
        )

        # Get the rule with details data (This is very large.)
        resp_details = api_utils.get(V2_GET_RULE_WITH_DETAILS, params=PL_GEN_EXPORT_RULE_DETAILS)

        # Sort the lists for ensured accurate comparison
        found_details_all = sorted(resp_details, key=lambda x: x["main"]["ruleNm"])
        expected_details_all = sorted(EXP_EXPORT_RULE_DETAILS, key=lambda x: x["main"]["ruleNm"])

        # Every object contains 2 sub-objects: main and details
        # The details sub-object contains its own array of objects.
        #
        # Example:
        #  returned_data = [
        #   {
        #       "main": { "dataset": DATASET },
        #       "detail": [
        #               { "MORTGAGE_AMT": "0" },
        #               { "MORTGAGE_AMT": "0" },
        #             ]
        #   },]

        for index1, expected_details in enumerate(expected_details_all):
            # The top most object, which is an array of sub-objects
            exp_obj_main = expected_details["main"]
            exp_obj_detail = expected_details["detail"]

            found_main = found_details_all[index1]["main"]
            found_detail = found_details_all[index1]["detail"]

            found_main["assignmentId"] = {}  # Assignment IDs vary between runs, ignore.
            exp_obj_main["runId"] = RUN_ID_EXPORT_RULE_DETAILS  # Set the run ID to current

            # MAIN - Loop through "main" sub-object
            for key_main, expected_main_value in exp_obj_main.items():
                assert_that(
                    expected_main_value,
                    f"Expected: {expected_main_value} but found: "
                    f"{found_main[key_main]} in data {found_main}",
                ).is_equal_to(found_main[key_main])

            # DETAIL - Some expected values contain no data
            if len(exp_obj_detail) > 0:
                # Loop through the array of 'detail' objects
                for index2, expected_detail_items in enumerate(exp_obj_detail):
                    # Validate that the keys in the expected data exist within the found data.
                    # Actual results may vary and some values can be null.
                    for key_detail in expected_detail_items.items():
                        assert_that(found_detail[index2], "Key not found.").contains(key_detail[0])
            else:
                assert_that(len(found_detail)).is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_historical_rule(self, api_utils):
        """Test rules that reference past runs"""
        required_backruns = 4
        helper.backrun_dataset_if_needed(
            api_utils, PULLUP_HISTORICAL_RULE_PAYLOAD, required_backruns
        )

        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_HISTORICAL_RULE_DATASET,
            PULLUP_HISTORICAL_RULE_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_HISTORICAL_RULE_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_HISTORICAL_RULE_DATASET,
            job_response["runId"],
            PULLUP_HISTORICAL_RULE_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_temporal_sales(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_TEMPORAL_SALES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_TEMPORAL_SALES_DATASET,
            PULLUP_RULES_TEMPORAL_SALES_RULE_DEFINITIONS,
        )
        helper.setup_dataset(api_utils, PULLUP_RULES_TEMPORAL_SALES_PAYLOAD)
        time.sleep(10)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_TEMPORAL_SALES_DATASET,
            "2022-04-29T00:00:00.000+0000",
            PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29,
        )
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_TEMPORAL_SALES_DATASET,
            "2022-04-30T00:00:00.000+0000",
            PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30,
        )
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_TEMPORAL_SALES_DATASET,
            "2022-05-01T00:00:00.000+0000",
            PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01,
        )
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_TEMPORAL_SALES_DATASET,
            "2022-05-02T00:00:00.000+0000",
            PULLUP_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_rules_copy(self, api_utils):
        # Create the source & target datasets if needed
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, DS_DEFS_COPY_SOURCE, DS_DEFS_COPY_TARGET_RUN_ID
        )
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, DS_DEFS_COPY_TARGET, DS_DEFS_COPY_TARGET_RUN_ID
        )

        # Delete any rules on the target and validate zero
        api_utils.delete(V3_RULES + "/" + DS_DEFS_COPY_TARGET_NAME, return_json=False)
        rules_target = api_utils.get(V2_GET_RULES, params={"dataset": DS_DEFS_COPY_TARGET_NAME})
        assert_that(len(rules_target), "Target DS - Rules not deleted").is_equal_to(0)

        # Delete, set, and confirm the rules on the source dataset
        helper.set_rules_on_dataset(api_utils, DS_DEFS_COPY_SOURCE_NAME, PL_RULES)
        found_rules = api_utils.get(
            V3_RULES + "/" + DS_DEFS_COPY_SOURCE_NAME, params={"dataset": DS_DEFS_COPY_SOURCE_NAME}
        )
        assert_that(len(found_rules), "Source: Set Rules expected count").is_equal_to(12)

        # Copy a single rule from the source to the target dataset and validate 1 copied
        post_copy = api_utils.post(V3_RULES_COPY, json=PL_RULES_COPY, return_json=False)
        assert_that(post_copy.status_code, "Post Copy Status").is_equal_to(200)
        found_rules_copy = api_utils.get(
            V3_RULES + "/" + DS_DEFS_COPY_TARGET_NAME, params={"dataset": DS_DEFS_COPY_TARGET_NAME}
        )
        assert_that(len(found_rules_copy), "Target: Set 1 Rule expected count").is_equal_to(1)

        # Delete any rules on the target and validate zero again
        api_utils.delete(V3_RULES + "/" + DS_DEFS_COPY_TARGET_NAME, return_json=False)
        rules_target2 = api_utils.get(V2_GET_RULES, params={"dataset": DS_DEFS_COPY_TARGET_NAME})
        assert_that(len(rules_target2), "Target DS - Rules not deleted").is_equal_to(0)

        # Copy all rules from the source to the target dataset and validate all copied
        post_copy_all = api_utils.post(
            V3_RULES + "/" + DS_DEFS_COPY_SOURCE_NAME + "/copy",
            params=PL_RULES_SOURCE_COPY,
            return_json=False,
        )
        assert_that(post_copy_all.status_code, "Post Copy All Status").is_equal_to(200)
        found_rules_copy_all = api_utils.get(
            V3_RULES + "/" + DS_DEFS_COPY_TARGET_NAME, params={"dataset": DS_DEFS_COPY_TARGET_NAME}
        )
        assert_that(len(found_rules_copy_all), "Target: Set All Rules expected count").is_equal_to(
            12
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    @pytest.mark.flaky(retries=2, delay=5)
    def test_rules_regex(self, api_utils):
        """Test rules with and without regex"""
        # Notes: React uses v2 to create data class rules

        # Delete data class rules from previous runs
        api_utils.post(
            V2_DELETE_CUSTOM_RULE, params={"customrulename": PL_V2_CREATE_RULE_DC_REGEX["ruleName"]}
        )
        api_utils.post(
            V2_DELETE_CUSTOM_RULE,
            params={"customrulename": PL_V2_CREATE_RULE_DC_NO_REGEX["ruleName"]},
        )

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_REGEX,
            PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
            QUERY_DC_RULE_REGEX,
        )

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        api_utils.delete(V3_RULES + "/" + PULLUP_RULES_DATA_CLASS_REGEX_DATASET, return_json=False)

        # Create
        rule_regex = api_utils.post(V2_INSERT_CUSTOM_RULE, params=PL_V2_CREATE_RULE_DC_REGEX)
        rule_no_regex = api_utils.post(V2_INSERT_CUSTOM_RULE, params=PL_V2_CREATE_RULE_DC_NO_REGEX)
        assert_that(rule_regex["message"]).is_equal_to("Success")
        assert_that(rule_no_regex["message"]).is_equal_to("Success")

        # Assign
        assign_regex = api_utils.post(V2_CREATE_RULE, params=PL_V2_ASSIGN_RULE_REGEX)
        assign_no_regex = api_utils.post(V2_CREATE_RULE, params=PL_V2_ASSIGN_RULE_NO_REGEX)
        assert_that(assign_regex["message"]).is_equal_to(RULE_SAVED_MSG)
        assert_that(assign_no_regex["message"]).is_equal_to(RULE_SAVED_MSG)

        helper.setup_dataset(api_utils, ds_defs)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
            PROD_RUN_ID_FULL,
            PULLUP_RULES_DATA_CLASS_REGEX_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_rules_pwdmgr_all_rule_types(self, api_utils):
        """Test a connection that uses password management with all sql rule types"""
        # Defect coverage for DEV-53052

        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_DATASET,
            PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_RULE_DEFINITIONS,
        )

        helper.setup_dataset(api_utils, PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_DATASET,
            FULL_RUN_ID_SQL_TYPE_PWDMGR,
            PULLUP_RULES_PWDMGR_ALL_RULE_TYPES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_binary_sales(self, api_utils):
        """Binary rules apply when a dataset has no rows but a rule breaks."""
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_BINARY_SALES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_BINARY_SALES_DATASET,
            PULLUP_RULES_BINARY_SALES_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_BINARY_SALES_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_BINARY_SALES_DATASET,
            job_response["runId"],
            PULLUP_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_filter_tolerance_sales(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_FILTER_TOLERANCE_SALES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_FILTER_TOLERANCE_SALES_DATASET,
            PULLUP_RULES_FILTER_TOLERANCE_SALES_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_FILTER_TOLERANCE_SALES_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_FILTER_TOLERANCE_SALES_DATASET,
            job_response["runId"],
            PULLUP_RULES_FILTER_TOLERANCE_SALES_EXPECTED_RULE_OUTPUT,
        )
        validate_rule_data_preview(
            api_utils,
            PULLUP_RULES_FILTER_TOLERANCE_SALES_DATASET,
            job_response["runId"],
            "FF_filter_and_tolerance",
            PULLUP_RULES_FILTER_TOLERANCE_SALES_FF_FILTER_AND_TOLERANCE_EXPECTED_RULE_DATA_PREVIEW
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_sales(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PULLUP_RULES_SALES_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_SALES_DATASET,
            PULLUP_RULES_SALES_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_SALES_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_SALES_DATASET,
            job_response["runId"],
            PULLUP_RULES_SALES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pullup")
    @allure.story("Rules")
    def test_pullup_rules_sales_link_id(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULES_SALES_LINK_ID_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            PULLUP_RULES_SALES_LINK_ID_RULE_DEFINITIONS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_RULES_SALES_LINK_ID_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            PULLUP_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT,
        )
        validate_rules_findings(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            PULLUP_RULES_SALES_EXPECTED_RULE_OUTPUT,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_downloaded_rule_breaks(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            "ff_all_columns",
            PULLUP_RULES_SALES_LINK_ID_FF_ALL_COLUMNS_EXPECTED_CSV_OUTPUT,
        )

        # Per DEV-104222:
        # Download not supported for pull up free form rules without link column in select clause

        validate_downloaded_rule_breaks(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            "Simple_link_column",
            PULLUP_RULES_SALES_LINK_ID_SIMPLE_LINK_COLUMN_EXPECTED_CSV_OUTPUT,
        )

        validate_downloaded_rule_breaks(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            "Simple_no_link_column",
            PULLUP_RULES_SALES_LINK_ID_SIMPLE_NO_LINK_COLUMN_EXPECTED_CSV_OUTPUT,
        )

        validate_downloaded_rule_breaks(
            api_utils,
            PULLUP_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            "stat_rule",
            PULLUP_RULES_SALES_LINK_ID_STAT_RULE_EXPECTED_CSV_OUTPUT,
        )
