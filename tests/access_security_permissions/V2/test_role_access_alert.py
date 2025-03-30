import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_alert import ACCESS_MATRIX_ALERT
from endpoints.v2.controller_alert import V2_GET_ACTIVE_ALERTS_COUNT
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessAlert:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Alert")
    def test_role_access_get_active_alerts_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getactivealertscount"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ACTIVE_ALERTS_COUNT,
            ACCESS_MATRIX_ALERT[V2_GET_ACTIVE_ALERTS_COUNT],
            payload={"dataset": job["dataset"]},
        )
