import allure
import pytest
from assertpy import assert_that
from data_test.pullup.data_rule_discovery import (
    CONN_DC_RULE_REGEX,
    DS_NAME_RUN_RULE_DISCOVERY,
    EXP_PROFILE_DELTAS,
    QUERY_RUN_RULE_DISCOVERY,
    EXP_RUN_DISCOVERY_RULES,
    QUERY_DC_RULE_DATES,
    DS_NAME_RULE_DC_DATES,
    PL_V2_CREATE_RULE_DC_TIMESTAMP,
    RULE_NAME_DC_TIMESTAMP,
    PL_V2_CREATE_RULE_DC_DATE_TYPE_YYYYMMDD,
    RULE_NAME_DC_DATE_TYPE,
    EXP_PROFILE_DELTAS_DATETIME,
    EXP_DC_RULES_DATETIME,
    RUN_ID_FULL,
    RUN_ID,
    QUERY_DC_RULE_COL_NAME,
    CONN_DC_RULE_COL_NAME,
    PL_V2_TESTDATE_PART_NAME_NO_COL,
    PL_V2_TESTDATE_NAME_COL,
    PL_V2_TESTDATE_NONAME_COLTS,
    PL_V2_TESTDATE_NONAME_COLDATE,
    PL_V2_TESTDATE_NAME_NOCOL,
    EXP_COL_TREATMENT_NO_TYPE_RULES,
    EXP_PROFILE_DELTAS_COL_T_NO_TYPE,
    EXP_NO_COL_DATE_TYPE_RULES,
    EXP_PROFILE_DELTAS_NO_COL_DATE_TYPE,
    EXP_NO_COL_TS_TYPE_RULES,
    EXP_PROFILE_DELTAS_NO_COL_TS_TYPE,
    QUERY_DC_RULE_NO_COL_TS_TYPE,
    EXP_PROFILE_DELTAS_COL_TMT_DATE_TYPE,
    EXP_COL_TMT_DATE_TYPE_RULES,
    EXP_COL_PMT_NO_TYPE_RULES,
    EXP_PROFILE_DELTAS_COL_PMT_NO_TYPE,
    DS_NAME_RULE_DC_COL_T_NO_TYPE,
    DS_NAME_RULE_DC_NO_COL_DATE_TYPE,
    DS_NAME_RULE_DC_NO_COL_TS_TYPE,
    DS_NAME_RULE_DC_COL_TMT_DATE_TYPE,
    DS_NAME_RULE_DC_PMT_NO_TYPE,
)
from endpoints.v2.controller_data_concept import V2_DATA_CATEGORY
from endpoints.v2.controller_explorer import V2_RUN_DISCOVERY
from endpoints.v2.controller_rule import (
    V2_INSERT_CUSTOM_RULE,
    V2_DATA_CLASS,
    V2_DELETE_CUSTOM_RULE,
)
from endpoints.v3.job_api import V3_JOBS_JOBID_WAITFORCOMPLETION
from endpoints.v3.rule_api import V3_RULES
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper
from utils.validator import validate_profile_tab_details
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestRuleDiscovery:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def run_discovery(api_utils, ds_name, run_id, data_concept_id):
        """Run discovery on existing job and validate basic data to ensure successfully submitted"""
        discovery = api_utils.post(
            V2_RUN_DISCOVERY,
            {"dataset": ds_name, "runId": run_id, "dataConceptId": data_concept_id},
        )
        assert_that(discovery["msg"]).is_not_none()
        assert_that(discovery["agentQJobUUID"]).is_not_none()
        assert_that(discovery["jobId"]).is_not_none()
        assert_that(discovery["jobUUID"]).is_not_none()
        assert_that(discovery["agentQJobId"]).is_not_none()
        api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=str(discovery["jobId"])))

    @staticmethod
    def create_data_class_if_not_exists(api_utils, payload):
        """Creates a custom rule of data class with the given payload, outputs all data classes"""
        rule_nm = payload["ruleName"]
        rule_str = f"'ruleName': '{rule_nm}'"
        found_data_class = api_utils.get(V2_DATA_CLASS)

        if rule_str not in str(found_data_class):
            custom_rule = api_utils.post(V2_INSERT_CUSTOM_RULE, params=payload)
            assert_that(custom_rule, "Insert custom rule unexpected error").contains_key("message")
            assert_that(custom_rule["message"], "Insert custom rule failed").is_equal_to("Success")
            return api_utils.get(V2_DATA_CLASS)  # Refresh data

        return found_data_class

    @staticmethod
    def create_data_category_add_rules_if_not_exists(api_utils, data_category_name, rule_ids):
        """Creates a data category if not found, adds rules to the new category, outputs ID"""

        # Get all data categories
        resp_get_data_category = api_utils.get(V2_DATA_CATEGORY)
        assert_that(resp_get_data_category, "Get Data Category call failed").contains_key("result")
        found_data_category = resp_get_data_category["result"]
        assert_that(len(found_data_category), "No data categories found").is_greater_than(0)

        # Check if category exists. If previous run failed to delete it will error on creation.
        if data_category_name not in str(found_data_category):
            # With the classes created and the IDs obtained, the data category can now be created
            pl_category = {
                "name": data_category_name,
                "desc": data_category_name,
                "semantics[]": rule_ids,
            }

            data_category = api_utils.post(V2_DATA_CATEGORY, params=pl_category)
            assert_that(data_category["result"]).is_equal_to("success")
            return data_category["id"]

        found_category = next(
            filter(lambda dc: dc["dataConceptNm"] == data_category_name, found_data_category)
        )
        return found_category["dataConceptId"]

    @staticmethod
    def get_rule_repo_ids(api_utils, rule_names):
        """Search for an array of rule names and return their IDs"""
        rule_ids = []
        found_data_class = api_utils.get(V2_DATA_CLASS)

        for rule in found_data_class:
            if rule["ruleName"] in rule_names:
                rule_ids.append(rule["ruleRepoId"])
                if (len(rule_ids)) >= len(rule_names):
                    break

        assert_that(
            len(rule_ids), f"Unable to find rules {str(rule_names)} in {str(found_data_class)}"
        ).is_equal_to(len(rule_names))
        return rule_ids

    @staticmethod
    def cleanup_data_class_and_category(api_utils, category_id, rule_name):
        """Delete given data class and data category"""
        # Note: Category must be deleted first.

        del_cat = api_utils.delete(V2_DATA_CATEGORY, params={"id": category_id}, return_json=False)
        del_class = api_utils.post(
            V2_DELETE_CUSTOM_RULE, params={"customrulename": rule_name}, return_json=False
        )
        assert_that(del_cat.status_code, "Delete data category failed").is_equal_to(200)
        assert_that(del_class.status_code, "Delete data class failed").is_equal_to(200)

    def create_data_class_and_category_and_run_discovery(
        self, api_utils, ds_defs, data_category_name, pl_data_class
    ):
        """Run job, clear rules, create data class and category, run discovery, output IDs"""
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        api_utils.delete(V3_RULES + "/" + ds_defs["dataset"], return_json=False)

        self.create_data_class_if_not_exists(api_utils, pl_data_class)

        rule_id = self.get_rule_repo_ids(api_utils, [pl_data_class["ruleName"]])
        category_id = self.create_data_category_add_rules_if_not_exists(
            api_utils, data_category_name, rule_id
        )

        self.run_discovery(api_utils, ds_defs["dataset"], ds_defs["runId"], category_id)

        return {"ruleId": rule_id, "categoryId": category_id}

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    @allure.issue(
        "https://engineering-collibra.atlassian.net/browse/DEV-88215",
        "Inconsistent data rounding and formatting from the "
        "'v2/getprofiledeltasbyrunid' response.",
    )
    def test_rule_discovery_with_generic_data_category(self, api_utils):
        """Test of Run Rule Discovery results with generic data category"""
        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_REGEX,
            DS_NAME_RUN_RULE_DISCOVERY,
            QUERY_RUN_RULE_DISCOVERY,
            RUN_ID,
        )

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, RUN_ID)
        api_utils.delete(V3_RULES + "/" + DS_NAME_RUN_RULE_DISCOVERY, return_json=False)

        # Run discovery with generic, which will rerun the job
        self.run_discovery(api_utils, DS_NAME_RUN_RULE_DISCOVERY, RUN_ID, "-1")

        # Rules should be created automatically by discovery
        validate_rules_findings(
            api_utils, DS_NAME_RUN_RULE_DISCOVERY, RUN_ID_FULL, EXP_RUN_DISCOVERY_RULES
        )

        # Validate the profile tab on the profile page to ensure dataclass labels and other data
        validate_profile_tab_details(
            api_utils, DS_NAME_RUN_RULE_DISCOVERY, RUN_ID, EXP_PROFILE_DELTAS
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_with_date_and_timestamp_data_category(self, api_utils):
        """Test rule run discovery with date and timestamp data category"""

        # DEV-54743 Defect - When resolved, the expected data will need to be updated.
        #   > EXP_DC_RULES_DATETIME & EXP_PROFILE_DELTAS_DATETIME

        # Note: This test intentionally leaves the data category & timestamp data class
        # These are generic rules with wide applications could be useful in other tests
        # It may be useful to extract into a helper in the future
        auto_data_category = "AUTO_DATE_TIMESTAMP"

        # Setup
        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_REGEX,
            DS_NAME_RULE_DC_DATES,
            QUERY_DC_RULE_DATES,
            RUN_ID,
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        api_utils.delete(V3_RULES + "/" + DS_NAME_RULE_DC_DATES, return_json=False)

        # Create Timestamp & Date (of date type) data class
        self.create_data_class_if_not_exists(api_utils, PL_V2_CREATE_RULE_DC_TIMESTAMP)
        self.create_data_class_if_not_exists(api_utils, PL_V2_CREATE_RULE_DC_DATE_TYPE_YYYYMMDD)

        # Get the rule repo ids of all required data classes
        rule_ids = self.get_rule_repo_ids(
            api_utils, [RULE_NAME_DC_DATE_TYPE, RULE_NAME_DC_TIMESTAMP]
        )

        # Create the data category with the given data classes
        data_concept_id = self.create_data_category_add_rules_if_not_exists(
            api_utils, auto_data_category, rule_ids
        )

        self.run_discovery(api_utils, DS_NAME_RULE_DC_DATES, PROD_RUN_ID, data_concept_id)

        # Rules should be created automatically by discovery
        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_DATES, RUN_ID_FULL, EXP_DC_RULES_DATETIME
        )

        # Validate the profile tab on the profile page to ensure dataclass labels and other data
        validate_profile_tab_details(
            api_utils, DS_NAME_RULE_DC_DATES, RUN_ID, EXP_PROFILE_DELTAS_DATETIME
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_data_class_column_name_treatment_and_no_type(self, api_utils):
        """Test rule discovery on data class of column name 'Treatment' and no type"""
        category_name = "AUTO_DC_COL_TREATMENT_NO_TYPE"

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_COL_NAME,
            DS_NAME_RULE_DC_COL_T_NO_TYPE,
            QUERY_DC_RULE_COL_NAME,
            RUN_ID,
        )

        found_ids = self.create_data_class_and_category_and_run_discovery(
            api_utils, ds_defs, category_name, PL_V2_TESTDATE_NAME_NOCOL
        )
        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_COL_T_NO_TYPE, RUN_ID_FULL, EXP_COL_TREATMENT_NO_TYPE_RULES
        )

        validate_profile_tab_details(
            api_utils, DS_NAME_RULE_DC_COL_T_NO_TYPE, RUN_ID, EXP_PROFILE_DELTAS_COL_T_NO_TYPE
        )

        self.cleanup_data_class_and_category(
            api_utils, found_ids["categoryId"], PL_V2_TESTDATE_NAME_NOCOL["ruleName"]
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_data_class_no_column_name_and_date_type(self, api_utils):
        """Test rule discovery on data class with no column and Date type"""
        category_name = "AUTO_DC_NO_COL_DATE_TYPE"

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_COL_NAME,
            DS_NAME_RULE_DC_NO_COL_DATE_TYPE,
            QUERY_DC_RULE_COL_NAME,
            RUN_ID,
        )

        found_ids = self.create_data_class_and_category_and_run_discovery(
            api_utils, ds_defs, category_name, PL_V2_TESTDATE_NONAME_COLDATE
        )
        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_NO_COL_DATE_TYPE, RUN_ID_FULL, EXP_NO_COL_DATE_TYPE_RULES
        )

        validate_profile_tab_details(
            api_utils, DS_NAME_RULE_DC_NO_COL_DATE_TYPE, RUN_ID, EXP_PROFILE_DELTAS_NO_COL_DATE_TYPE
        )
        self.cleanup_data_class_and_category(
            api_utils, found_ids["categoryId"], PL_V2_TESTDATE_NONAME_COLDATE["ruleName"]
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_data_class_no_column_name_and_timestamp_type(self, api_utils):
        """Test rule discovery on data class with no column and Timestamp type"""
        category_name = "AUTO_DC_NO_COL_TS_TYPE"

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_COL_NAME,
            DS_NAME_RULE_DC_NO_COL_TS_TYPE,
            QUERY_DC_RULE_NO_COL_TS_TYPE,
            RUN_ID,
        )

        found_ids = self.create_data_class_and_category_and_run_discovery(
            api_utils, ds_defs, category_name, PL_V2_TESTDATE_NONAME_COLTS
        )

        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_NO_COL_TS_TYPE, RUN_ID_FULL, EXP_NO_COL_TS_TYPE_RULES
        )

        validate_profile_tab_details(
            api_utils, DS_NAME_RULE_DC_NO_COL_TS_TYPE, RUN_ID, EXP_PROFILE_DELTAS_NO_COL_TS_TYPE
        )

        self.cleanup_data_class_and_category(
            api_utils, found_ids["categoryId"], PL_V2_TESTDATE_NONAME_COLTS["ruleName"]
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_data_class_column_name_treatment_and_date_type(self, api_utils):
        """Test rule discovery on data class of column name 'Treatment' and Date type"""
        category_name = "AUTO_DC_COL_TMT_DATE_TYPE"

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_COL_NAME,
            DS_NAME_RULE_DC_COL_TMT_DATE_TYPE,
            QUERY_DC_RULE_COL_NAME,
            RUN_ID,
        )

        found_ids = self.create_data_class_and_category_and_run_discovery(
            api_utils, ds_defs, category_name, PL_V2_TESTDATE_NAME_COL
        )

        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_COL_TMT_DATE_TYPE, RUN_ID_FULL, EXP_COL_TMT_DATE_TYPE_RULES
        )

        validate_profile_tab_details(
            api_utils,
            DS_NAME_RULE_DC_COL_TMT_DATE_TYPE,
            RUN_ID,
            EXP_PROFILE_DELTAS_COL_TMT_DATE_TYPE,
        )

        self.cleanup_data_class_and_category(
            api_utils, found_ids["categoryId"], PL_V2_TESTDATE_NAME_COL["ruleName"]
        )

    @allure.feature("Pullup")
    @allure.story("Rule Discovery")
    def test_rule_discovery_data_class_column_name_payment_and_no_type(self, api_utils):
        """Test rule discovery on data class of column name 'Payment' and no type"""
        category_name = "AUTO_DC_COL_PMT_NO_TYPE"

        ds_defs = helper.get_minimum_job_payload(
            api_utils,
            CONN_DC_RULE_COL_NAME,
            DS_NAME_RULE_DC_PMT_NO_TYPE,
            QUERY_DC_RULE_COL_NAME,
            RUN_ID,
        )

        found_ids = self.create_data_class_and_category_and_run_discovery(
            api_utils, ds_defs, category_name, PL_V2_TESTDATE_PART_NAME_NO_COL
        )

        validate_rules_findings(
            api_utils, DS_NAME_RULE_DC_PMT_NO_TYPE, RUN_ID_FULL, EXP_COL_PMT_NO_TYPE_RULES
        )

        validate_profile_tab_details(
            api_utils, DS_NAME_RULE_DC_PMT_NO_TYPE, RUN_ID, EXP_PROFILE_DELTAS_COL_PMT_NO_TYPE
        )

        self.cleanup_data_class_and_category(
            api_utils, found_ids["categoryId"], PL_V2_TESTDATE_PART_NAME_NO_COL["ruleName"]
        )
