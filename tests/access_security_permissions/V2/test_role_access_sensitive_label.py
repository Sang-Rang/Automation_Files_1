import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_sensitive_label import (
    ACCESS_MATRIX_SENSITIVE_LABEL,
)
from endpoints.v2.controller_sensitive_label import V2_SENSITIVE_LABEL
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessSensitiveLabel:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Sensitive Label")
    def test_role_access_(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/sensitive-label"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_SENSITIVE_LABEL,
            ACCESS_MATRIX_SENSITIVE_LABEL[V2_SENSITIVE_LABEL],
        )
