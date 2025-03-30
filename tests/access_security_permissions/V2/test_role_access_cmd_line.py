import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_cmd_line import (
    ACCESS_MATRIX_CMD_LINE,
)
from endpoints.v2.controller_cmd_line import V2_OPTIONS_CMD_LINE, V2_CMD_LINE_VALIDATE
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessCmdLine:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Cmd Line")
    def test_role_access_options_2_cmd_line(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/options2CmdLine"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_OPTIONS_CMD_LINE,
            ACCESS_MATRIX_CMD_LINE[V2_OPTIONS_CMD_LINE],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Cmd Line")
    def test_role_access_cmd_line_validate(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/cmdline/validate"""
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_CMD_LINE_VALIDATE,
            ACCESS_MATRIX_CMD_LINE[V2_CMD_LINE_VALIDATE],
            payload={"cmdLine": '-numexecutors 1'},  # Invalid data returns a 200 with req params
        )
