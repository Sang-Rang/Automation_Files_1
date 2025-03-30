import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_profile import ACCESS_MATRIX_PROFILE
from endpoints.v2.controller_profile import (
    V2_GET_RUN_IDS_BY_DATASET_DESC,
    V2_GET_PROFILE_DELTA,
    V2_GET_DATASET_SCHEMA,
    V2_GET_DATASET_SCHEMA_AND_STATS,
    V2_GET_DATA_HISTOGRAM,
    V2_GET_DATASET_CORR,
    V2_GET_FILTERGRAM,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessProfile:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_run_ids_by_ds_desc(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrunidsbydatasetdesc"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RUN_IDS_BY_DATASET_DESC,
            ACCESS_MATRIX_PROFILE[V2_GET_RUN_IDS_BY_DATASET_DESC],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_profile_deltas_by_run_id(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getprofiledeltasbyrunid"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PROFILE_DELTA,
            ACCESS_MATRIX_PROFILE[V2_GET_PROFILE_DELTA],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_dataset_schema(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetschema"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_SCHEMA,
            ACCESS_MATRIX_PROFILE[V2_GET_DATASET_SCHEMA],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_dataset_schema_and_stats(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetschemaandstats"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_SCHEMA_AND_STATS,
            ACCESS_MATRIX_PROFILE[V2_GET_DATASET_SCHEMA_AND_STATS],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_data_histogram(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatahistogram"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATA_HISTOGRAM,
            ACCESS_MATRIX_PROFILE[V2_GET_DATA_HISTOGRAM],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_dataset_corr(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetcorr"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_CORR,
            ACCESS_MATRIX_PROFILE[V2_GET_DATASET_CORR],
            payload={"dataset": job["dataset"], "runid": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Profile")
    def test_role_access_get_filtergram(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/filtergram"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_FILTERGRAM,
            ACCESS_MATRIX_PROFILE[V2_GET_FILTERGRAM],
            payload={
                "dataset": job["dataset"],
                "runid": job["runId"],
                "column": job["columns"][0],
                "limit": 1,
            },
        )
