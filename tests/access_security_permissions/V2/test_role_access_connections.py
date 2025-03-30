import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_connections import (
    ACCESS_MATRIX_CONNECTIONS,
    ALL_DATABASE_BRANDS,
)
from endpoints.v2.controller_connections import (
    V2_GET_CONNECTION_ALIASES_NO_TEMPLATE,
    V2_GET_CONNECTIONS_COUNT,
    V2_GET_CONNECTIONS_BY_DB_BRAND,
    V2_GET_TEMPLATES,
    V2_GET_CONNECTIONS_WITH_ROLES2,
    V2_CONNECTIONS_GET_BY_DATASET,
    V2_GET_JDBC_CONNECTIONS_SENSITIVE,
    V2_GET_REMOTE_FILE_CONNECTIONS_SENSITIVE,
    V2_GET_ARCHIVE_CONNECTIONS,
    V2_GET_CONNECTION_ALIASES,
    V2_CHECK_CORE_SPECIFIC_DRIVER,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessConnections:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_connections_get_by_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/connections/get-by-dataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_CONNECTIONS_GET_BY_DATASET,
            ACCESS_MATRIX_CONNECTIONS[V2_CONNECTIONS_GET_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_connection_aliases_no_template(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getconnectionaliasesnotemplate"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CONNECTION_ALIASES_NO_TEMPLATE,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_CONNECTION_ALIASES_NO_TEMPLATE],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_connections_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getConnectionsCount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CONNECTIONS_COUNT,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_CONNECTIONS_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_connections_by_db_brand(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getconnectionsByDbBrand"""
        for database in ALL_DATABASE_BRANDS:
            security_helper.check_role_permissions(
                api_utils,
                get_auth_headers_multi_user,
                V2_GET_CONNECTIONS_BY_DB_BRAND,
                ACCESS_MATRIX_CONNECTIONS[V2_GET_CONNECTIONS_BY_DB_BRAND],
                payload={"dbBrandName": database},
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_templates(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettemplates"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TEMPLATES,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_TEMPLATES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_connections_with_roles2(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getconnectionswithroles2"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CONNECTIONS_WITH_ROLES2,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_CONNECTIONS_WITH_ROLES2],
            "xmlhttp",
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_jdbc_connections_sensitive(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getjdbcconnectionssensitive"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_JDBC_CONNECTIONS_SENSITIVE,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_JDBC_CONNECTIONS_SENSITIVE],
            "xmlhttp",
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_remote_file_connections_sensitive(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getremotefileconnectionssensitive"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_REMOTE_FILE_CONNECTIONS_SENSITIVE,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_REMOTE_FILE_CONNECTIONS_SENSITIVE],
            "xmlhttp",
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_archive_connections(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getarchiveconnections"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ARCHIVE_CONNECTIONS,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_ARCHIVE_CONNECTIONS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_get_connection_aliases(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getconnectionaliases"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CONNECTION_ALIASES,
            ACCESS_MATRIX_CONNECTIONS[V2_GET_CONNECTION_ALIASES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Connections")
    def test_role_access_check_core_specific_driver(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/checkCoreSpecificDriver"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_CHECK_CORE_SPECIFIC_DRIVER,
            ACCESS_MATRIX_CONNECTIONS[V2_CHECK_CORE_SPECIFIC_DRIVER],
            payload={"aliasname": job["connectionalias"]},
        )
