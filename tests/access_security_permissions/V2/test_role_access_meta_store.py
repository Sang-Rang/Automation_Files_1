import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_meta_store import (
    ACCESS_MATRIX_META_STORE,
)
from endpoints.v2.controller_meta_store import (
    V2_LICENSES,
    V2_GET_MULTI_TENANT_MODE,
    V2_LICENSES_LICENSE_EXPIRATION_COUNTDOWN,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessMetaStore:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Meta Store")
    def test_role_access_licenses(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/licenses"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_LICENSES,
            ACCESS_MATRIX_META_STORE[V2_LICENSES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Meta Store")
    def test_role_access_get_multitenantmode(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getmultitenantmode"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_MULTI_TENANT_MODE,
            ACCESS_MATRIX_META_STORE[V2_GET_MULTI_TENANT_MODE],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Meta Store")
    def test_role_access_licenses_license_expirations_countdown(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/licenses/licenseExpirationCountdown"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_LICENSES_LICENSE_EXPIRATION_COUNTDOWN,
            ACCESS_MATRIX_META_STORE[V2_LICENSES_LICENSE_EXPIRATION_COUNTDOWN],
        )
