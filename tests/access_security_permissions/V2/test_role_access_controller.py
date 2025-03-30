import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_controller import (
    ACCESS_MATRIX_CONTROLLER,
)
from endpoints.v2.controller import (
    V2_GET_DATASET_HISTORY_RUN_ID,
    V2_DEPLOYMENT_TYPE,
    V2_GET_COUNT_IN_TRAINING,
    V2_GET_UI_TIMEOUT,
    V2_GET_RECENT_RUNS,
)
from endpoints.v2.controller_dq_inbox import V2_GET_DQ_INBOX
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessController:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_ds_history_run_id(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasethistoryrunid"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_HISTORY_RUN_ID,
            ACCESS_MATRIX_CONTROLLER[V2_GET_DATASET_HISTORY_RUN_ID],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_deployment_type(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/deployment/type"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_DEPLOYMENT_TYPE,
            ACCESS_MATRIX_CONTROLLER[V2_DEPLOYMENT_TYPE],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_get_count_in_training(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcountintraining"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_COUNT_IN_TRAINING,
            ACCESS_MATRIX_CONTROLLER[V2_GET_COUNT_IN_TRAINING],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_get_ui_timeout(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getuitimeout"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_UI_TIMEOUT,
            ACCESS_MATRIX_CONTROLLER[V2_GET_UI_TIMEOUT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_get_recent_runs(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrecentruns"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RECENT_RUNS,
            ACCESS_MATRIX_CONTROLLER[V2_GET_RECENT_RUNS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Controller")
    def test_role_access_get_dq_inbox(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdqinbox"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DQ_INBOX,
            ACCESS_MATRIX_CONTROLLER[V2_GET_DQ_INBOX],
            payload={"limit": 1}
        )
