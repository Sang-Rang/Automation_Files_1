import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_business_unit import (
    ACCESS_MATRIX_BUSINESS_UNIT_TO_DATASET,
)
from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT
from endpoints.v2.controller_business_unit_to_dataset import (
    V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET,
    V2_BUSINESS_UNIT_TO_DS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessBusinessUnitToDataset:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Business Unit")
    def test_role_access_business_unit_to_ds_get_by_ds(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/business-unit-to-dataset/getbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET,
            ACCESS_MATRIX_BUSINESS_UNIT_TO_DATASET[V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Business Unit")
    def test_role_access_business_unit_to_ds(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/business-unit-to-dataset"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_BUSINESS_UNIT_TO_DS,
            ACCESS_MATRIX_BUSINESS_UNIT_TO_DATASET[V2_BUSINESS_UNIT_TO_DS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Business Unit")
    def test_role_access_business_unit(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/business-unit"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_BUSINESS_UNIT,
            ACCESS_MATRIX_BUSINESS_UNIT_TO_DATASET[V2_BUSINESS_UNIT],
        )
