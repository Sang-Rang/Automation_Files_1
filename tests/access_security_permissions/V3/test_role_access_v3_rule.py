import allure
import pytest
from data_test.access_security_permissions.v3.data_role_access_v3_rule import ACCESS_MATRIX_V3_RULE
from endpoints.v3.job_api import GET_V3_JOBS
from endpoints.v3.rule_api import V3_RULES, V3_RULES_BREAKS
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
    def test_role_access_v3_get_rules(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v3/rules"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V3_RULES,
            ACCESS_MATRIX_V3_RULE[V3_RULES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Rule")
    def test_role_access_v3_rule_breaks(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v3/rules/breaks"""
        jobs = api_utils.get(GET_V3_JOBS, {"limit": 1})
        job_id = jobs[0]["jobId"]
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V3_RULES_BREAKS,
            ACCESS_MATRIX_V3_RULE[V3_RULES_BREAKS],
            payload={"jobId": job_id},
        )
