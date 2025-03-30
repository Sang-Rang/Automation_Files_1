import random
import string
import allure
import pytest
from assertpy import assert_that
from data_test.access_security_permissions.v2.data_role_access_dataset import ACCESS_MATRIX_DATASET
from endpoints.v2.controller_dataset import V2_RENAME_DATASET
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessDataset:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Dataset")
    def test_role_access_rename_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/renamedataset"""
        job = security_helper.get_pullup_job(api_utils)
        ds_nm = "ROLE_ACCESS_JOB_TO_RENAME"
        ds_nm_rename = "ROLE_ACCESS_JOB_RENAMED"
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        ds_nm_rename += random_suffix
        params_rename = {"sourceDataset": ds_nm, "targetDataset": ds_nm_rename}
        params_reset = {"sourceDataset": ds_nm_rename, "targetDataset": ds_nm}

        dsdef = helper.get_minimum_job_payload(
            api_utils, job["connectionalias"], ds_nm, query=job["query"]
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dsdef)

        for role in ACCESS_MATRIX_DATASET[V2_RENAME_DATASET]:
            user = security_helper.setup_user(get_auth_headers_multi_user, role)
            rename = api_utils.patch(
                V2_RENAME_DATASET, custom_headers=user, params=params_rename, return_json=False
            )
            security_helper.report_results(role, V2_RENAME_DATASET, params_rename, rename)

            if rename.status_code == 200:
                reset = api_utils.patch(V2_RENAME_DATASET, params=params_reset, return_json=False)
                assert_that(reset.status_code, "Reset of rename dataset failed").is_equal_to(200)
