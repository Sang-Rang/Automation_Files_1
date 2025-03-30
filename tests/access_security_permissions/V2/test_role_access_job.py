import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_job import ACCESS_MATRIX_JOB
from endpoints.v2.controller_job import (
    V2_GET_IS_PUSHDOWN,
    V2_GET_JOB_STATUS_BY_DATASET,
    V2_JOB_CHART_SERIES,
    V2_GET_OWL_CHECK_Q,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessJob:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Job")
    def test_role_access_get_is_pushdown(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-is-pushdown"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_IS_PUSHDOWN,
            ACCESS_MATRIX_JOB[V2_GET_IS_PUSHDOWN],
            payload={"datasetName": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Job")
    def test_role_access_get_job_status_by_ds(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getjobstatusbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_JOB_STATUS_BY_DATASET,
            ACCESS_MATRIX_JOB[V2_GET_JOB_STATUS_BY_DATASET],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Job")
    def test_role_access_job_chart_series(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/job-chart-series"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_JOB_CHART_SERIES,
            ACCESS_MATRIX_JOB[V2_JOB_CHART_SERIES],
            payload={"timeBin": "day"},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Job")
    def test_role_access_get_owl_check_q(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlcheckq"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECK_Q,
            ACCESS_MATRIX_JOB[V2_GET_OWL_CHECK_Q],
            payload={"limit": 1},
        )
