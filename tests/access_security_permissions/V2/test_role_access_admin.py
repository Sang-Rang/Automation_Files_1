import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_admin import ACCESS_MATRIX_ADMIN
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper
from endpoints.v2.controller_admin import (
    V2_GET_ADMIN_CONFIG,
    V2_GET_TOTAL_BYTES,
    V2_GET_APP_CONFIG,
    V2_GET_CLI_OPTIONS,
)

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessAdmin:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Admin")
    def test_role_access_get_admin_config(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getadminconfig"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ADMIN_CONFIG,
            ACCESS_MATRIX_ADMIN[V2_GET_ADMIN_CONFIG],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Admin")
    def test_role_access_get_total_bytes(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettotalbytes"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TOTAL_BYTES,
            ACCESS_MATRIX_ADMIN[V2_GET_TOTAL_BYTES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Admin")
    def test_role_access_get_app_config(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getappconfig"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_APP_CONFIG,
            ACCESS_MATRIX_ADMIN[V2_GET_APP_CONFIG],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Admin")
    def test_role_access_get_cli_options(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getclioptions"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CLI_OPTIONS,
            ACCESS_MATRIX_ADMIN[V2_GET_CLI_OPTIONS],
        )
