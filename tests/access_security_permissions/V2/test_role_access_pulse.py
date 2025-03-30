import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_pulse import ACCESS_MATRIX_PULSE
from endpoints.v2.controller_pulse import V2_GET_PULSE_BY_DATASET, V2_GET_PULSE
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessPulse:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Pulse")
    def test_role_access_get_pulse_by_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getpulsebydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PULSE_BY_DATASET,
            ACCESS_MATRIX_PULSE[V2_GET_PULSE_BY_DATASET],
            payload={"dataset": job["dataset"], "runDate": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Pulse")
    def test_role_access_get_pulse(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getpulse"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PULSE,
            ACCESS_MATRIX_PULSE[V2_GET_PULSE],
            payload={"lookback": 1, "runMode": "All", "scheduled": "All", "showFailed": False},
        )
