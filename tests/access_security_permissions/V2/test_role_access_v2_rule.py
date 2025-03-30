import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_rule import ACCESS_MATRIX_RULE
from endpoints.v2.controller_rule import (
    V2_DATA_CLASS,
    V2_GET_ACTIVE_RULES_COUNT,
    V2_TEMPLATE_RULES,
    V2_GET_RULES,
    V2_GET_RULE_OUTPUT2,
    V2_GET_RULE_HISTORY,
    V2_GET_RULE_HISTORY_AUDIT,
    V2_GET_MOST_RECENT_OWL_CHECK_HISTORY,
    V2_GET_RULE_REPO,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessRule:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_data_class(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/data-class"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_DATA_CLASS,
            ACCESS_MATRIX_RULE[V2_DATA_CLASS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_get_active_rules_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getactiverulescount"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ACTIVE_RULES_COUNT,
            ACCESS_MATRIX_RULE[V2_GET_ACTIVE_RULES_COUNT],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_template_rules(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/templateRules"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_TEMPLATE_RULES,
            ACCESS_MATRIX_RULE[V2_TEMPLATE_RULES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_rules(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrules"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULES,
            ACCESS_MATRIX_RULE[V2_GET_RULES],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_rule_output2(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getruleoutput2"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_OUTPUT2,
            ACCESS_MATRIX_RULE[V2_GET_RULE_OUTPUT2],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_rule_history_audit(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrulehistoryaudit"""
        job = security_helper.get_pullup_job(api_utils)
        rule = security_helper.add_v3_rule_if_none(api_utils, job["dataset"])
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_HISTORY_AUDIT,
            ACCESS_MATRIX_RULE[V2_GET_RULE_HISTORY_AUDIT],
            payload={"dataset": job["dataset"], "rulename": rule["rule_name"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_rule_history(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrulehistory"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_HISTORY,
            ACCESS_MATRIX_RULE[V2_GET_RULE_HISTORY],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_most_recent_owl_check_history(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getmostrecentowlcheckhistory"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_MOST_RECENT_OWL_CHECK_HISTORY,
            ACCESS_MATRIX_RULE[V2_GET_MOST_RECENT_OWL_CHECK_HISTORY],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v2_get_rule_repo(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrulerepo"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_REPO,
            ACCESS_MATRIX_RULE[V2_GET_RULE_REPO],
        )
