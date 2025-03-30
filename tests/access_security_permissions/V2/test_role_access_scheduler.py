import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_scheduler import (
    ACCESS_MATRIX_SCHEDULER,
)
from endpoints.v2.controller_scheduler import V2_GET_JOB_SCHEDULE, V2_GET_SCHEDULE_RESTRICTION
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessScheduler:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Scheduler")
    def test_role_access_get_job_schedule(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getjobschedule"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_JOB_SCHEDULE,
            ACCESS_MATRIX_SCHEDULER[V2_GET_JOB_SCHEDULE],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Scheduler")
    def test_role_access_get_schedule_restriction(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getschedulerestriction"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SCHEDULE_RESTRICTION,
            ACCESS_MATRIX_SCHEDULER[V2_GET_SCHEDULE_RESTRICTION],
        )
