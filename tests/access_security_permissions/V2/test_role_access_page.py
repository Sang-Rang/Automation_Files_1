import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_page import ACCESS_MATRIX_PAGE
from endpoints.v2.controller_page import V2_GET_PAGES, V2_ADD_PAGE, V2_DELETE_PAGE
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessPage:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Page")
    def test_role_access_get_pages(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getpages"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PAGES,
            ACCESS_MATRIX_PAGE[V2_GET_PAGES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Page")
    def test_role_access_add_delete_pages(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/addpage & /v2/deletepage"""
        pl_add_page = {"pageNm": "AUTO_PAGE"}
        pl_del_page = {"page": "AUTO_PAGE"}

        for role in ACCESS_MATRIX_PAGE[V2_ADD_PAGE]:
            user = security_helper.setup_user(get_auth_headers_multi_user, role)

            # Delete scorecard page as precondition
            response = api_utils.delete(
                V2_DELETE_PAGE, custom_headers=user, params=pl_del_page, return_json=False
            )
            security_helper.report_results(role, V2_DELETE_PAGE, pl_del_page, response)

            # Add scorecard page
            response = api_utils.post(
                V2_ADD_PAGE, custom_headers=user, params=pl_add_page, return_json=False
            )
            security_helper.report_results(role, V2_ADD_PAGE, pl_add_page, response)

            # Delete scorecard page
            response = api_utils.delete(
                V2_DELETE_PAGE, custom_headers=user, params=pl_del_page, return_json=False
            )
            security_helper.report_results(role, V2_DELETE_PAGE, pl_del_page, response)
