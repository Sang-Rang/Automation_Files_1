import pytest
from assertpy import assert_that

from endpoints.v2.controller_admin import V2_GET_APP_CONFIG, V2_ADD_APP_CONFIG
from tests.a_setup_and_configure.test_setup_connections import setup_env_helper
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_connections import ConnectionsHelper

helper = BaseHelper()
connections_helper = ConnectionsHelper()


class TestSetupAlerts:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.mark.skip(reason="Setup alerts is a one-time manual execution for new RC envs.")
    def test_setup_smtp(self, api_utils):
        """Setup the alerts smtp server to send alert emails"""

        # Configuration
        include_links = True
        setup_env_helper.update_alert_config(api_utils, include_links)

        # Update Host Name in app config if blank, required for alert email links
        get_app_config = api_utils.get(V2_GET_APP_CONFIG)
        host_name = next((col for col in get_app_config if col["colNm"] == "HOST_NAME"), None)
        if host_name["colValue"] == "":
            pl_app_config = {"columnname": "HOST_NAME", "columnvalue": api_utils.base_url}
            resp_config = api_utils.post(V2_ADD_APP_CONFIG, params=pl_app_config, return_json=False)
            assert_that(resp_config.status_code, "Updating host config failed").is_equal_to(200)
