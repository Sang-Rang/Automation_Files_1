import allure
import pytest
from assertpy import assert_that

from endpoints.v2.controller_explorer import V2_POST_UPDATE_LIVY_SESSION_CONFIG

from utils.api_utils import APIUtils


class TestAAALivyReset:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Admin")
    @allure.story("Livy Reset")
    @pytest.mark.smoke
    def test_aaa_reset_livy(self, api_utils):
        """Verify that resetting Livy returns a success status code.  This test can be used to
        reset Livy and is named so that it will run before most other tests when parallel
        runs are kicked off in the pipeline."""
        livy_reset_response = api_utils.post(V2_POST_UPDATE_LIVY_SESSION_CONFIG, return_json=False)

        assert_that(livy_reset_response.status_code == 200)
