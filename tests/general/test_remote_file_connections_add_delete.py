from datetime import datetime

import allure
import pytest
from assertpy import assert_that

from endpoints.v2.controller_connections import V2_ADD_CONNECTION, V2_DELETE_CONNECTION
from utils.api_utils import APIUtils
from utils.helper_connections import ConnectionsHelper

connections_helper = ConnectionsHelper()


class TestRemoteFileConnectionsAddDelete:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        get_auth_headers["X-Requested-With"] = "XMLHttpRequest"
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def add_connection(api_utils, params):
        """Create a new conenction"""
        msg = "Connection saved and valid connection established."
        new_conn = api_utils.post(V2_ADD_CONNECTION, params=params)
        assert_that(new_conn["msg"], "Create connection failed").is_equal_to(msg)

    @staticmethod
    def delete_connection(api_utils, conn_name):
        """Delete a connection"""
        result = api_utils.get(V2_DELETE_CONNECTION, params={"connection": conn_name})
        assert_that(result["msg"], "Delete Connection failed").is_equal_to("Success")

    @allure.feature("Remote Files")
    @allure.story("Connections")
    @pytest.mark.smoke
    def test_remote_file_connection_nfs(self, api_utils):
        """Test Remote File Connection NFS (DEV-48953, DEV-48954)"""
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        new_conn = {
            "conntype": "",
            "Alias": f"AUTO_NFS{now}_DONOTUSE",
            "Host": "/opt/owl/data-packs/",
            "authtype": "nfs",
            "driverprops": "",
            "Port": "3000",
            "username": "",
            "password": "",
            "driver": "remoteFileConnDriver",
            "driverlocation": "remoteFileConndriverlocation",
        }
        expected_files = [
            {"file": "connection-template.csv"},
            {"file": "data-concept.csv"},
            {"file": "semantic-sensitivity.csv"},
            {"file": "rule-repo.csv"},
        ]

        # Add connection
        self.add_connection(api_utils, new_conn)
        connections_helper.check_connection_pwdmgr_sensitive(
            api_utils, new_conn["Alias"], deleted=False
        )

        # Validate availability and data in connection
        connections_helper.check_explorer_remote_file_connection(
            api_utils, new_conn["Alias"], deleted=False
        )
        connections_helper.check_remote_files(api_utils, new_conn["Alias"], "/", expected_files)

        # Delete
        self.delete_connection(api_utils, new_conn["Alias"])

        connections_helper.check_connection_pwdmgr_sensitive(
            api_utils, new_conn["Alias"], deleted=True
        )
        connections_helper.check_explorer_remote_file_connection(
            api_utils, new_conn["Alias"], deleted=True
        )
