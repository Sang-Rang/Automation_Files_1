import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_audit_trail import (
    ACCESS_MATRIX_AUDIT_TRAIL,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper
from endpoints.v2.controller_audit_trail import (
    V2_GET_DATASETS_AUDIT_TRAIL_ITEMS,
    V2_GET_AUDIT_TRAIL_ITEMS,
)

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessAuditTrail:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Audit Trail")
    def test_role_access_get_ds_audit_trail_items(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-datasets-audit-trail-items"""
        params = {
            "draw": 1,
            "start": 0,
            "length": 10,
            "order[0][column]": 0,
            "order[0][dir]": "desc",
            "search[value]": "",
        }
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASETS_AUDIT_TRAIL_ITEMS,
            ACCESS_MATRIX_AUDIT_TRAIL[V2_GET_DATASETS_AUDIT_TRAIL_ITEMS],
            payload=params,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Audit Trail")
    def test_role_access_get_audit_trail_items(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getaudittrailitems"""
        params = {
            "draw": 1,
            "start": 0,
            "length": 10,
            "order[0][column]": 0,
            "order[0][dir]": "asc",
            "search[value]": "",
        }
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_AUDIT_TRAIL_ITEMS,
            ACCESS_MATRIX_AUDIT_TRAIL[V2_GET_AUDIT_TRAIL_ITEMS],
            payload=params,
        )
