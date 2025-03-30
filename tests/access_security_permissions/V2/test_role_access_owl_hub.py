import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_owl_hub import ACCESS_MATRIX_OWL_HUB
from endpoints.v2.controller_owl_hub import V2_GET_CLEAN_DB_DEFAULTS
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessOwlHub:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Hub")
    def test_role_access_get_clean_db_defaults(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcleandbdefaults"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CLEAN_DB_DEFAULTS,
            ACCESS_MATRIX_OWL_HUB[V2_GET_CLEAN_DB_DEFAULTS],
        )
