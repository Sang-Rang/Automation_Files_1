import allure
import pytest

from data_test.pushdown.dq_dataset_metatags.pd_dataset_metatags import (
    PARAMS_PUSHDOWN_DQ_DATASET_WITH_METATAGS,
)
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_alerts import AlertsHelper

helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pushdown
class TestPushdownDatasetMetatags:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown_Dataset_Metatags")
    @pytest.mark.parametrize(
        "test_data",
        PARAMS_PUSHDOWN_DQ_DATASET_WITH_METATAGS,
        ids=lambda val: f"{val['connection']}",
    )
    def test_pushdown_dataset_metatags(self, api_utils, test_data):
        # This test validates that the metatags are stored and
        # added correctly to dataset definitions
        # when creating and executing a job using the /v3/datasetdefs API.
        dataset_definition = helper.get_pd_job_payload_sales(
            test_data["connection_name"],
            test_data["dataset"],
            test_data["include_columns"],
            test_data["source_query"],
        )
        helper.run_pushdown_job_v3(api_utils, dataset_definition)
        validator.validate_dataset_metatags(
            api_utils, dataset_definition["dataset"], dataset_definition["metaTags"]
        )
