import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_health import ACCESS_MATRIX_HEALTH
from endpoints.v2.controller_health import (
    V2_GET_ENVIRONMENT_DETAILS,
    V2_GET_LIST_OF_FILES,
    V2_CHECK_FILES_V_MAP,
    V2_GET_CUSTOMER_NAME,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessHealth:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Health")
    def test_role_access_get_env_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getEnvDetails"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ENVIRONMENT_DETAILS,
            ACCESS_MATRIX_HEALTH[V2_GET_ENVIRONMENT_DETAILS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Health")
    def test_role_access_get_list_of_files(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getlistoffiles"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIST_OF_FILES,
            ACCESS_MATRIX_HEALTH[V2_GET_LIST_OF_FILES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Health")
    def test_role_access_check_files_vmap(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/checkfilesvmap"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_CHECK_FILES_V_MAP,
            ACCESS_MATRIX_HEALTH[V2_CHECK_FILES_V_MAP],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Health")
    def test_role_access_get_customer_name(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcustomername"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CUSTOMER_NAME,
            ACCESS_MATRIX_HEALTH[V2_GET_CUSTOMER_NAME],
        )
