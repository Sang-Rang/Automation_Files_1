import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_label import ACCESS_MATRIX_LABEL
from endpoints.v2.controller_label import (
    V2_VIEW_ITEM_LABELS,
    V2_RETRAIN,
    V2_IGNORE_RUN,
    V2_OFF_PEAK_RUN,
    V2_INVALID_RUN,
    V2_REMOVE_DATASET_RUN,
)
from utils.api_utils import APIUtils
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
    def test_role_access_view_item_labels(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/viewitemlabels"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_VIEW_ITEM_LABELS,
            ACCESS_MATRIX_LABEL[V2_VIEW_ITEM_LABELS],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_retrain(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/retrain"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_RETRAIN,
            ACCESS_MATRIX_LABEL[V2_RETRAIN],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_ignore_run(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/ignorerun"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_IGNORE_RUN,
            ACCESS_MATRIX_LABEL[V2_IGNORE_RUN],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_off_peak_run(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/off_peak_run"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_OFF_PEAK_RUN,
            ACCESS_MATRIX_LABEL[V2_OFF_PEAK_RUN],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_invalid_run(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/invalidrun"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_INVALID_RUN,
            ACCESS_MATRIX_LABEL[V2_INVALID_RUN],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Label")
    def test_role_access_remove_dataset_run(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/removedatasetrun"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_REMOVE_DATASET_RUN,
            ACCESS_MATRIX_LABEL[V2_REMOVE_DATASET_RUN],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )
