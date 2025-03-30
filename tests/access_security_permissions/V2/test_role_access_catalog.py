from datetime import datetime

import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_catalog import ACCESS_MATRIX_CATALOG
from endpoints.v2.controller_catalog import (
    V2_GET_DATA_ASSET,
    V2_GET_CATALOG_BY_DATASET,
    V2_UPDATE_CATALOG_OBJ,
    V2_DELETE_DATASET_LIST,
    V2_GET_CATALOG_RECENT_RUNS,
    V2_GET_CATALOG_FREQUENT_RUNS,
    V2_SEARCH_DETAILS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessCatalog:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    def test_role_access_get_data_asset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdataasset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATA_ASSET,
            ACCESS_MATRIX_CATALOG[V2_GET_DATA_ASSET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    def test_role_access_get_catalog_by_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcatalogbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CATALOG_BY_DATASET,
            ACCESS_MATRIX_CATALOG[V2_GET_CATALOG_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    @pytest.mark.skip(reason="Until we update the tests to handle dataset security enabled")
    def test_role_access_update_catalog_obj(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/updatecatalogobj"""
        job = security_helper.get_pullup_job(api_utils)
        catalog = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": job["dataset"]})

        # Host & Table Name are swapped in the GET vs PUT calls.
        data = {
            "alias": catalog["dataset"],
            "dataset": catalog["alias"],
            "dbNm": catalog["dbNm"],
            "host": catalog["tableNm"],
            "source": catalog["source"],
            "t1": f'TAG{datetime.now().strftime("%Y%m%d%H%M%S")}',
            "t2": None,
            "t3": None,
            "t4": None,
            "tableNm": catalog["host"],
        }
        security_helper.check_role_permissions_put_data(
            api_utils,
            get_auth_headers_multi_user,
            V2_UPDATE_CATALOG_OBJ,
            ACCESS_MATRIX_CATALOG[V2_UPDATE_CATALOG_OBJ],
            payload=data,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    @pytest.mark.skip(reason="Bug DEV-98025, fix version - N/A")
    @allure.issue(
        "https://engineering-collibra.atlassian.net/browse/DEV-98025",
        "Delete dataset endpoint /v2/deletedatasetlist returns code 400 instead of 403 "
        "for restricted user roles",
    )
    def test_role_access_delete_dataset_list(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/deletedatasetlist"""
        # Bug coverage: DEV-24664

        connection_name = "APPROVED_POSTGRES_UP"
        query = "select * from public.aclaims_master limit 1"
        ds_nm = "ROLE_ACCESS_JOB_TO_DELETE"
        payload = {"datasets": ds_nm}

        for role in ACCESS_MATRIX_CATALOG[V2_DELETE_DATASET_LIST]:
            dsdef = helper.get_minimum_job_payload(api_utils, connection_name, ds_nm, query=query)
            helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dsdef)

            user = security_helper.setup_user(get_auth_headers_multi_user, role)
            response = api_utils.post(
                V2_DELETE_DATASET_LIST, custom_headers=user, params=payload, return_json=False
            )
            security_helper.report_results(role, V2_DELETE_DATASET_LIST, payload, response)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    def test_role_access_get_catalog_recent_runs(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcatalogrecentruns"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CATALOG_RECENT_RUNS,
            ACCESS_MATRIX_CATALOG[V2_GET_CATALOG_RECENT_RUNS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    def test_role_access_get_catalog_frequent_runs(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcatalogfrequentruns"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_CATALOG_FREQUENT_RUNS,
            ACCESS_MATRIX_CATALOG[V2_GET_CATALOG_FREQUENT_RUNS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Catalog")
    def test_role_access_search_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/searchdetails"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_SEARCH_DETAILS,
            ACCESS_MATRIX_CATALOG[V2_SEARCH_DETAILS],
            payload={"term": "AUTO"},
        )
