import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_owl_options import (
    ACCESS_MATRIX_OWL_OPTIONS,
)
from endpoints.v2.controller_owl_options import (
    V2_OWL_OPTIONS_GET,
    V2_OWL_OPTIONS_DISTINCT_USERNAMES,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessOwlOptions:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Options")
    def test_role_access_owl_options_get(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/owl-options/get"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_OWL_OPTIONS_GET,
            ACCESS_MATRIX_OWL_OPTIONS[V2_OWL_OPTIONS_GET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Options")
    def test_role_access_owl_options_distinct_usernames(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/owl-options/distinctUserNames"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_OWL_OPTIONS_DISTINCT_USERNAMES,
            ACCESS_MATRIX_OWL_OPTIONS[V2_OWL_OPTIONS_DISTINCT_USERNAMES],
        )
