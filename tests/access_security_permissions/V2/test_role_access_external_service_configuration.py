import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_ext_service_configuration import (
    ACCESS_MATRIX_EXT_SERVICE_CONFIG,
)
from endpoints.v2.controller_external_service_configuration import (
    V2_EXTERNAL_SERVICE_CONFIGURATION_SERVICE_TYPES,
    V2_EXTERNAL_SERVICE_CONFIGURATION_FIND_ALL,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessExternalServiceConfiguration:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Ext Service Configuration")
    def test_role_access_ext_service_config_service_types(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/external-service-configuration/service-types"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_EXTERNAL_SERVICE_CONFIGURATION_SERVICE_TYPES,
            ACCESS_MATRIX_EXT_SERVICE_CONFIG[V2_EXTERNAL_SERVICE_CONFIGURATION_SERVICE_TYPES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Ext Service Configuration")
    def test_role_access_ext_service_config_find_all(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/external-service-configuration/findAll"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_EXTERNAL_SERVICE_CONFIGURATION_FIND_ALL,
            ACCESS_MATRIX_EXT_SERVICE_CONFIG[V2_EXTERNAL_SERVICE_CONFIGURATION_FIND_ALL],
            payload="xmlhttp",
        )
