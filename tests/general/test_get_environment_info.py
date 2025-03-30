import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_health import (
    V2_GET_VERSION,
    V2_GET_ENVIRONMENT,
    V2_GET_ENVIRONMENT_DETAILS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.logger import Logger

helper = BaseHelper()
LOGGER = Logger.get_instance()


class TestEnvInfo:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Admin")
    @allure.story("Environment")
    @pytest.mark.smoke
    def test_get_app_details_info(self, api_utils):
        """Get a system environment information."""
        get_version = api_utils.get(V2_GET_VERSION)
        get_environment = api_utils.get(V2_GET_ENVIRONMENT)
        get_environment_details = api_utils.get(V2_GET_ENVIRONMENT_DETAILS)
        LOGGER.log_info("******************************************")
        LOGGER.log_info(f"Environment details: {get_environment_details}")
        LOGGER.log_info("******************************************")
        assert_that(get_environment_details["version"]).is_equal_to(get_version["version"])
        assert_that(get_environment_details["env"]).is_equal_to(get_environment["env"])
