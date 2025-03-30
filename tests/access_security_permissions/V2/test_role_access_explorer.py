import allure
import pytest
from data_test.access_security_permissions.v2.data_role_access_explorer import (
    ACCESS_MATRIX_EXPLORER,
)
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_explorer import (
    V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS,
    V2_GET_OWL_CHECK_TEMPLATE_BY_DATASET,
    V2_GET_TABLE_INFORMATION,
    V2_DEFAULT_DB_VIEWS,
    V2_GET_TEMP_FILE_DIR,
    V2_GET_UPLOAD_FILE_PATH,
    V2_LIST_TEMP_FILES,
    V2_GET_EXPLORER_SEARCH,
    V2_POST_EXPLORER_TABLE_SEARCH,
    V2_GET_DS_HIST_INITIAL_RUNS_BY_DATASETS,
    V2_GET_REMOTE_RBAC_MODE,
    V2_EXPLORER_DATASET_COVERAGE_SEARCH_JDBC,
    V2_EXPLORER_UNIQUE_DATASET_NAME_JDBC,
    V2_GET_REMOTE_HOST,
    V2_GET_DAYS_WITH_DATA1,
    V2_JOB_ESTIMATOR,
    V2_EVALUATE_CONNECTION,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessExplorer:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_list_data_schema_preview_db_table_by_cols(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getlistdataschemapreviewdbtablebycols"""
        job = security_helper.get_pullup_job(api_utils)
        connection = api_utils.get(
            V2_GET_CONNECTION_BY_ALIAS, params={"alias": job["connectionalias"]}
        )
        params = {
            "table": f"{job['schema']}.{job['table']}",
            "aliasname": job["connectionalias"],
            "hostname": connection["hostname"],
            "drivername": connection["drivername"],
            "cols": "*",
        }
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS,
            ACCESS_MATRIX_EXPLORER[V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS],
            payload=params,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_owl_check_template_by_dataset(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getowlchecktemplatebydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECK_TEMPLATE_BY_DATASET,
            ACCESS_MATRIX_EXPLORER[V2_GET_OWL_CHECK_TEMPLATE_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_table_information(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettableinformation"""
        params = {
            "table": "aclaims_master",
            "aliasname": "APPROVED_ATHENA_PUSHDOWN",
            "schema": "default",
        }
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TABLE_INFORMATION,
            ACCESS_MATRIX_EXPLORER[V2_GET_TABLE_INFORMATION],
            payload=params,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_default_db_views(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/defaultdbviews"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_DEFAULT_DB_VIEWS,
            ACCESS_MATRIX_EXPLORER[V2_DEFAULT_DB_VIEWS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_temp_file_dir(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettempfiledir"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TEMP_FILE_DIR,
            ACCESS_MATRIX_EXPLORER[V2_GET_TEMP_FILE_DIR],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_upload_file_path(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getuploadfilepath"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_UPLOAD_FILE_PATH,
            ACCESS_MATRIX_EXPLORER[V2_GET_UPLOAD_FILE_PATH],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_list_temp_files(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/listtempfiles"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_LIST_TEMP_FILES,
            ACCESS_MATRIX_EXPLORER[V2_LIST_TEMP_FILES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_explorer_search(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/explorer/search"""
        job = security_helper.get_pullup_job(api_utils)
        payload = {
            "alias": job["connectionalias"],
            "showstats": 0,
            "showviews": 0,
            "eagerfetch": False,
        }
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_EXPLORER_SEARCH,
            ACCESS_MATRIX_EXPLORER[V2_GET_EXPLORER_SEARCH],
            payload=payload,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_explorer_tables_search(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/explorer/tables/search"""
        job = security_helper.get_pullup_job(api_utils)
        payload = {
            "alias": job["connectionalias"],
            "schema": job["schema"],
            "tables": "-",
            "showstats": 0,
            "showviews": 0,
            "eagerfetch": False,
        }
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_POST_EXPLORER_TABLE_SEARCH,
            ACCESS_MATRIX_EXPLORER[V2_POST_EXPLORER_TABLE_SEARCH],
            payload=payload,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_ds_hist_initial_runs_by_datasets(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getdshistinitialrunsbydatasets"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DS_HIST_INITIAL_RUNS_BY_DATASETS,
            ACCESS_MATRIX_EXPLORER[V2_GET_DS_HIST_INITIAL_RUNS_BY_DATASETS],
            payload={"datasets[]": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_remote_rbac_mode(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getremoterbacmode"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_REMOTE_RBAC_MODE,
            ACCESS_MATRIX_EXPLORER[V2_GET_REMOTE_RBAC_MODE],
            payload={
                "table": job["table"],
                "aliasname": job["connectionalias"],
                "cols": job["columns"][0],
            },
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_explorer_dataset_coverage_search_jdbc(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/explorer/dataset-coverage/search/jdbc"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_EXPLORER_DATASET_COVERAGE_SEARCH_JDBC,
            ACCESS_MATRIX_EXPLORER[V2_EXPLORER_DATASET_COVERAGE_SEARCH_JDBC],
            payload={
                "table": job["table"],
                "alias": job["connectionalias"],
                "schema": job["schema"],
            },
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_explorer_unique_dataset_name_jdbc(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/explorer/unique-dataset-name/jdbc"""
        job = security_helper.get_pullup_job(api_utils)
        connection = api_utils.get(
            V2_GET_CONNECTION_BY_ALIAS, params={"alias": job["connectionalias"]}
        )
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_EXPLORER_UNIQUE_DATASET_NAME_JDBC,
            ACCESS_MATRIX_EXPLORER[V2_EXPLORER_UNIQUE_DATASET_NAME_JDBC],
            payload={
                "table": job["table"],
                "hostname": connection["hostname"],
                "schema": job["schema"],
            },
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_remote_host(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getremotehost"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_REMOTE_HOST,
            ACCESS_MATRIX_EXPLORER[V2_GET_REMOTE_HOST],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_get_days_with_data1(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdayswithdata1"""
        job = security_helper.get_pullup_job(api_utils)
        payload = {
            "cxn": job["connectionalias"],
            "colNm": job["columns"][0],
            "schemaAndTableNm": f"{job['schema']}.{job['table']}",
            "limit": 1,
        }
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DAYS_WITH_DATA1,
            ACCESS_MATRIX_EXPLORER[V2_GET_DAYS_WITH_DATA1],
            payload=payload,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_job_estimator(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/jobestimator"""
        job = security_helper.get_pullup_job(api_utils)
        connection = api_utils.get(
            V2_GET_CONNECTION_BY_ALIAS, params={"alias": job["connectionalias"]}
        )
        payload = {
            "aliasname": job["connectionalias"],
            "table": job["table"],
            "drivername": connection["drivername"],
            "hostname": connection["hostname"],
            "cols": job["columns"],
            "query": f'{job["query"]} limit 1',
        }
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_JOB_ESTIMATOR,
            ACCESS_MATRIX_EXPLORER[V2_JOB_ESTIMATOR],
            payload=payload,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Explorer")
    def test_role_access_evaluate_connection(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/evaluateconnection"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_EVALUATE_CONNECTION,
            ACCESS_MATRIX_EXPLORER[V2_EVALUATE_CONNECTION],
            payload={"cxn": job["connectionalias"]},
        )
