import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_security import (
    ACCESS_MATRIX_SECURITY,
)
from endpoints.v2.controller_security import (
    V2_GET_CURRENT_USER_OWL_ROLES,
    V2_GET_ACTIVITY_AUDIT,
    V2_GET_LOCAL_DB_ROLES,
    V2_GET_LIST_ROLES_BY_DISTNCT_DATASETS,
    V2_GET_LOCAL_DB_ROLES_WITH_DATASETS_AND_USERS,
    V2_GET_SECURITY_SETTINGS_BY_TYPE,
    V2_GET_SECURITY_SETTINGS_BY_COL_TYPE,
    V2_GET_ALL_DB_USER_DETAILS,
    V2_SQL_EDITOR_ACCESS,
    V2_GLOBAL_RULES_ACCESS,
    V2_USERNAME_ACCESS_BY_DATASET,
    V2_USERNAME_RULES_ACCESS_BY_DATASET,
    V2_GET_DB_USER_LIST_BY_USER,
    V2_GET_PERSONAL_LIST,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY,
    V2_USERNAME,
)
from endpoints.v2.controller_user_profile import V2_GET_USER_PROFILE_BY_USER
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessSecurity:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_current_user_owl_roles(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcurrentuserowlroles"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CURRENT_USER_OWL_ROLES,
            ACCESS_MATRIX_SECURITY[V2_GET_CURRENT_USER_OWL_ROLES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_activity_audit(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getactivityaudit"""
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
            V2_GET_ACTIVITY_AUDIT,
            ACCESS_MATRIX_SECURITY[V2_GET_ACTIVITY_AUDIT],
            payload=params,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_local_db_roles(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getlocalDBRoles"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LOCAL_DB_ROLES,
            ACCESS_MATRIX_SECURITY[V2_GET_LOCAL_DB_ROLES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_list_roles_by_distnct_datasets(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getlistrolesbydistnctdatasets"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIST_ROLES_BY_DISTNCT_DATASETS,
            ACCESS_MATRIX_SECURITY[V2_GET_LIST_ROLES_BY_DISTNCT_DATASETS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_local_db_roles_with_ds_and_users(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getlocalDBRolesWithDatasetsAndUsers"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LOCAL_DB_ROLES_WITH_DATASETS_AND_USERS,
            ACCESS_MATRIX_SECURITY[V2_GET_LOCAL_DB_ROLES_WITH_DATASETS_AND_USERS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_security_settings_by_type(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getsecuritysettingsbytype"""
        db_types = [{"type": "DB"}, {"type": "AD"}, {"type": "SAML"}]
        for db_type in db_types:
            security_helper.check_role_permissions(
                api_utils,
                get_auth_headers_multi_user,
                V2_GET_SECURITY_SETTINGS_BY_TYPE,
                ACCESS_MATRIX_SECURITY[V2_GET_SECURITY_SETTINGS_BY_TYPE],
                payload=db_type,
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_security_settings_by_col_type(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getsecuritysettingsbycoltype"""
        payloads = [{"type": "AD", "col": "ENABLED"}, {"type": "LDAP", "col": "ENABLED"}]
        for params in payloads:
            security_helper.check_role_permissions(
                api_utils,
                get_auth_headers_multi_user,
                V2_GET_SECURITY_SETTINGS_BY_COL_TYPE,
                ACCESS_MATRIX_SECURITY[V2_GET_SECURITY_SETTINGS_BY_COL_TYPE],
                payload=params,
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_all_db_user_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getalldbuserdetails"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ALL_DB_USER_DETAILS,
            ACCESS_MATRIX_SECURITY[V2_GET_ALL_DB_USER_DETAILS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_sql_editor_access(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/sqleditoraccess"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_SQL_EDITOR_ACCESS,
            ACCESS_MATRIX_SECURITY[V2_SQL_EDITOR_ACCESS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_global_rule_access(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/globalrulesaccess"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GLOBAL_RULES_ACCESS,
            ACCESS_MATRIX_SECURITY[V2_GLOBAL_RULES_ACCESS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_username_access_by_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/usernameaccessbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_USERNAME_ACCESS_BY_DATASET,
            ACCESS_MATRIX_SECURITY[V2_USERNAME_ACCESS_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_username_rules_access_by_dataset(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/usernamerulesaccessbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_USERNAME_RULES_ACCESS_BY_DATASET,
            ACCESS_MATRIX_SECURITY[V2_USERNAME_RULES_ACCESS_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_db_user_list_by_user(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdbuserlistbyuser"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DB_USER_LIST_BY_USER,
            ACCESS_MATRIX_SECURITY[V2_GET_DB_USER_LIST_BY_USER],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_get_personal_list(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getpersonalist"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PERSONAL_LIST,
            ACCESS_MATRIX_SECURITY[V2_GET_PERSONAL_LIST],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_update_local_jdbc_user_profile(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/updatelocaljdbcuserprofile"""

        for role in ACCESS_MATRIX_SECURITY[V2_UPDATE_LOCAL_JDBC_USER_PROFILE]:
            user = security_helper.setup_user(get_auth_headers_multi_user, role)
            user_data = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user)
            payload = {
                "firstname": user_data["firstName"],
                "lastname": user_data["lastName"],
                "email": user_data["email"],
            }
            response = api_utils.post(
                V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
                custom_headers=user,
                params=payload,
                return_json=False,
            )
            security_helper.report_results(
                role, V2_UPDATE_LOCAL_JDBC_USER_PROFILE, payload, response
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_update_local_jdbc_user_profile_persona(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/updatelocaljdbcuserprofilePersona"""

        for role in ACCESS_MATRIX_SECURITY[V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA]:
            user = security_helper.setup_user(get_auth_headers_multi_user, role)
            payload = {"username": role["user"], "persona": 1}
            response = api_utils.post(
                V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA,
                custom_headers=user,
                params=payload,
                return_json=False,
            )
            security_helper.report_results(
                role, V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA, payload, response
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_update_local_jdbc_user_profile_story(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/updatelocaljdbcuserprofileStory"""

        for role in ACCESS_MATRIX_SECURITY[V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY]:
            user = security_helper.setup_user(get_auth_headers_multi_user, role)
            payload = {
                "username": role["user"],
                "title": "TempTestTitle",
                "description": "TempTestDesc",
            }
            response = api_utils.post(
                V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY,
                custom_headers=user,
                params=payload,
                return_json=False,
            )
            security_helper.report_results(
                role, V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY, payload, response
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Security")
    def test_role_access_username(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/username"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_USERNAME,
            ACCESS_MATRIX_SECURITY[V2_USERNAME],
        )
