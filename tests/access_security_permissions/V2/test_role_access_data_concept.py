import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_data_concept import (
    ACCESS_MATRIX_DATA_CONCEPT,
)
from endpoints.v2.controller_data_concept import V2_DATA_CATEGORY
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessDataConcept:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Data Concept")
    def test_role_access_data_category(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/data-category"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_DATA_CATEGORY,
            ACCESS_MATRIX_DATA_CONCEPT[V2_DATA_CATEGORY],
        )
