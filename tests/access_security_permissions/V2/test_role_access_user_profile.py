import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_user_profile import (
    ACCESS_MATRIX_USER_PROFILE,
)
from endpoints.v2.controller_user_profile import (
    V2_GET_USER_PROFILES_USER_LIST,
    V2_GET_USER_PROFILE_BY_USER,
    V2_GET_LIST_DATASETS_BY_ROLE,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessUserProfile:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - User Profile")
    def test_role_access_get_user_profiles_user_list(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getuserprofilesuserlist"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_USER_PROFILES_USER_LIST,
            ACCESS_MATRIX_USER_PROFILE[V2_GET_USER_PROFILES_USER_LIST],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - User Profile")
    def test_role_access_get_user_profiles_by_user(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getuserprofilebyuser"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_USER_PROFILE_BY_USER,
            ACCESS_MATRIX_USER_PROFILE[V2_GET_USER_PROFILE_BY_USER],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - User Profile")
    def test_role_access_get_list_datasets_by_role(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getlistdatasetsbyrole"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIST_DATASETS_BY_ROLE,
            ACCESS_MATRIX_USER_PROFILE[V2_GET_LIST_DATASETS_BY_ROLE],
        )
