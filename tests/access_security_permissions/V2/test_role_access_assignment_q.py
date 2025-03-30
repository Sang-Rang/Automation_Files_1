import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_assignment_q import (
    ACCESS_MATRIX_ASSIGNMENT_Q,
)
from endpoints.v2.controller_assignment_q import V2_FIND_ALL_PAGING_DATATABLES
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessAssignmentQ:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Assignment Q")
    def test_role_access_assignment_q_find_all_paging_datatables(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/assignment-q/find-all-paging-datatables"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_FIND_ALL_PAGING_DATATABLES,
            ACCESS_MATRIX_ASSIGNMENT_Q[V2_FIND_ALL_PAGING_DATATABLES],
            payload={
                "draw": 0,
                "start": 0,
                "length": 1,
            },
        )
