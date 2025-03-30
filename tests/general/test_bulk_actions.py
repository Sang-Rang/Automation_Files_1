import allure
import pytest

from data_test.general.data_bulk_actions import (
    DATA_BULK_ACTIONS_ERROR_MESSAGE,
    DATA_BULK_ACTIONS_INVALID_DATASET_ERROR_MESSAGE,
    DATA_BULK_ACTIONS_VALID_DATASET_MESSAGE,
)

from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator
from utils.helper_alerts import AlertsHelper
from utils.api_utils import APIUtils
from utils.helper import BaseHelper


helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pullup
class TestBulkActions:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("General")
    @allure.story("Bulk Actions")
    def test_bulk_actions_manage_host(self, api_utils):
        dataset_name = "AUTO_TEST_BULK_ACTIONS_HOST"
        job_payload = helper.get_pu_job_payload_sales(dataset_name)
        helper.setup_dataset(api_utils, job_payload)
        parameters_without_host = {"datasets": dataset_name}
        validator.validate_bulk_actions_manage_hosts(
            api_utils, parameters_without_host, DATA_BULK_ACTIONS_ERROR_MESSAGE
        )
        parameters_without_datasets = {"host": "validation"}
        validator.validate_bulk_actions_manage_hosts(
            api_utils, parameters_without_datasets, DATA_BULK_ACTIONS_ERROR_MESSAGE
        )
        invalid_parameters = {"host": "ABC", "datasets": "ABC"}
        validator.validate_bulk_actions_manage_hosts(
            api_utils, invalid_parameters, DATA_BULK_ACTIONS_INVALID_DATASET_ERROR_MESSAGE
        )
        valid_parameters = {"host": "validation", "datasets": dataset_name}
        validator.validate_bulk_actions_manage_hosts(
            api_utils, valid_parameters, DATA_BULK_ACTIONS_VALID_DATASET_MESSAGE
        )
