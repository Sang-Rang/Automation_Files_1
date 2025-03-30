import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_web_log import ACCESS_MATRIX_WEB_LOG
from endpoints.v2.controller_web_log import V2_GET_LIMITED_WEB_LOGS, V2_GET_ALL_WEB_LOGS
from utils.api_utils import APIUtils
from utils.constants import BASE_CREDS
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessLabel:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_get_limited_web_logs(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getLimitedWebLogs"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIMITED_WEB_LOGS,
            ACCESS_MATRIX_WEB_LOG[V2_GET_LIMITED_WEB_LOGS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_get_all_web_logs(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getallweblogs"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ALL_WEB_LOGS,
            ACCESS_MATRIX_WEB_LOG[V2_GET_ALL_WEB_LOGS],
            payload={"userName": BASE_CREDS["username"], "activity": "EXPLORER"},
        )
