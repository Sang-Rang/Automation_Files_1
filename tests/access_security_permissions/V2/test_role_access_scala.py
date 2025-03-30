import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_scala import ACCESS_MATRIX_SCALA
from endpoints.v2.controller_scala import V2_GET_TREND_BY_FIELD
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessScala:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Scala")
    def test_role_access_get_trend_by_field(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettrendbyfield"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TREND_BY_FIELD,
            ACCESS_MATRIX_SCALA[V2_GET_TREND_BY_FIELD],
            payload={"dataset": job["dataset"], "runId": job["runId"], "field": "rc"},
        )
