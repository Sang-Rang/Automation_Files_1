import allure
import pytest

from payloads.pullup.pl_pullup_dataset_metatags import PL_PULLUP_DATASET_WITH_METATAGS
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_alerts import AlertsHelper

helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pullup
class TestPullupMetatags:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Pullup_Dataset_Metatags")
    def test_pullup_dataset_metatags(self, api_utils):
        # This test validates that the metatags are
        # stored and added correctly to dataset definitions
        # when creating and executing a job using the /v3/datasetdefs API.
        dataset_definition = PL_PULLUP_DATASET_WITH_METATAGS
        helper.setup_dataset(api_utils, PL_PULLUP_DATASET_WITH_METATAGS)
        validator.validate_dataset_metatags(
            api_utils, dataset_definition["dataset"], dataset_definition["metaTags"]
        )
