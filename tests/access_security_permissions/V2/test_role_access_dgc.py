import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_dgc import ACCESS_MATRIX_DGC
from endpoints.dgc_integration.dq.dgc_connection_api import DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS
from endpoints.dgc_integration.dq.integration_api import DGC_INTEGRATIONS_STATUS
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessDgc:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - DGC")
    def test_role_access_dgc_integrations_conns_creds(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /dgc/integrations/connections/credentials"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS,
            ACCESS_MATRIX_DGC[DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - DGC")
    def test_role_access_dgc_integration_status(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /dgc/integrations/status"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            DGC_INTEGRATIONS_STATUS + "/" + job["dataset"],
            ACCESS_MATRIX_DGC[DGC_INTEGRATIONS_STATUS],
        )
