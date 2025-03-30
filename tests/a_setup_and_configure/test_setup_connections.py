import pytest

from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from tests.a_setup_and_configure.data_setup.data_setup_connections import (
    EXPECTED_DATABASES,
    EXPECTED_TABLE_MAPS,
    EXPECTED_NOT_FOUND,
    RUN_CONNECTIONS,
    EXPECTED_REMOTE_FILES,
)
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_connections import ConnectionsHelper

helper = BaseHelper()
connections_helper = ConnectionsHelper()
setup_env_helper = SetupEnvHelper()

# NOTES:
# - GCS:
#   Requires upload of .json file in app, no way to submit that file or contents via our API.
#   Submitting that file generates a password that works on across environments
#   Password may change depending on time or some other factor?

# - KEYTAB:
#   Someone has to place the keytab, password manager scripts at the standard server manually

# SETUP NEW CONNECTION STEPS:
# 1. Add key name for the connection to "RUN_CONNECTIONS" in data_setup_connections
# 2. Add connection data in constants_connections.json with the key from step 1
# 3. Add connection credentials in constants_connections_credentials.json with key from step 1
#       Upload the file so everyone has the new credentials
# 4. Add expected databases to EXPECTED_DATABASES in data_setup_connections with key from step 1
# 5. Add expected tables OR remote files (depending on connection type) with key from step 1
#       in EXPECTED_TABLE_MAPS or EXPECTED_REMOTE_FILES
#       If remote file, ensure 'conntype' is on condition list for "check_remote_files" below


class TestSetupConnections:
    """Setup all the connections in an environment based on json data input"""

    # CONFIGURATION OPTIONS
    # -----------------------------------------------------
    is_cloud = False  # !!!!NOT FULLY SUPPORTED YET!!!! Cloud environment vs RC/Standalone

    set_keytab_secrets = False  # Append new secrets to existing if absent
    overwrite = False  # If the connection already exists, overwrite it or skip?
    continue_on_fail = True  # If a connection fails setup or validation, log & continue?
    add_connections_to_agent = True  # Add non-pushdown connections to an existing agent
    add_connections_to_agent_name = None  # If multiple agents, which agent to use? None = 1st found
    validate_connections = False  # Validate dbs/table data. False for faster execution

    # Testing:
    prefix_conn_name = ""  # Can prefix a connection name with "DONOTUSE_" for example
    delete_connections = False  # Delete option, for local testing/troubleshooting/cleanup purposes

    # -----------------------------------------------------
    # END CONFIGURATION OPTIONS

    # Variables populated at runtime, do not change.
    connection_data = None
    credentials_data = None

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="class")
    def api_utils_xml(self, base_url, get_auth_headers):
        get_auth_headers["X-Requested-With"] = "XMLHttpRequest"
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.mark.skip(reason="Setup connections is a one-time manual execution for new RC envs.")
    def test_setup_connections(self, api_utils, api_utils_xml):
        # Calls used to get data for a connection:
        #   /v2/getconnectionbyalias
        #   /v2/explorer/search
        #   /v2/explorer/tables/search for connections
        #   /v2/getlistremotefilesystem for remote files

        self.connection_data = setup_env_helper.populate_connection_data()
        self.credentials_data = setup_env_helper.populate_credential_data()
        self.connection_data = setup_env_helper.update_connection_credentials_and_agent(
            api_utils, self.connection_data, self.credentials_data, self.prefix_conn_name
        )
        agent_data = setup_env_helper.get_agent_connection(
            api_utils, self.add_connections_to_agent_name
        )

        if self.set_keytab_secrets:
            setup_env_helper.update_keytab_secrets(
                api_utils, self.credentials_data, agent_data, self.is_cloud
            )

        # Use "RUN_CONNECTIONS" list for an easy way to limit run to specific connections
        for connection_parent in RUN_CONNECTIONS:
            # Print out a log of each connection run for validation.
            print(f"Starting connection setup: {connection_parent}")

            # Setup
            connection = self.connection_data[connection_parent]
            alias = connection["Alias"]

            # Check if the connection already exists if it should not be overwritten
            if not self.overwrite:
                existing_check = api_utils.get(
                    V2_GET_CONNECTION_BY_ALIAS, params={"alias": alias}, return_json=False
                )
                if existing_check.status_code == 200:  # Returns 500 if it does not exist.
                    print(f"Connection already exists, skipping: {alias}")
                    continue

            # If the connection already exists, it will be updated.
            conn_added = connections_helper.add_connection(
                api_utils, connection, self.is_cloud, self.continue_on_fail
            )

            if self.validate_connections and conn_added:
                # Confirm a list of databases or files exist within the connection
                connections_helper.check_databases(
                    api_utils, alias, EXPECTED_DATABASES[connection_parent], self.continue_on_fail
                )

                if (
                    connection["conntype"] == "REMOTE_FILE"
                    or connection["conntype"] == "NFS"
                    or connection["conntype"] == "abfs"
                ):
                    connections_helper.check_remote_files(
                        api_utils,
                        alias,
                        "/",
                        EXPECTED_REMOTE_FILES[connection_parent],
                        self.continue_on_fail,
                    )

                    # Verify the connection displays on the explorer panel
                    connections_helper.check_explorer_remote_file_connection(
                        api_utils_xml, alias, False, self.continue_on_fail
                    )
                else:
                    # Confirm a list of tables within a given database exist (validate conn added)
                    connections_helper.check_table_maps(
                        api_utils,
                        alias,
                        EXPECTED_TABLE_MAPS[connection_parent],
                        self.continue_on_fail,
                    )

                    # Verify the connection displays on the explorer panel
                    connections_helper.check_explorer_jdbc_connection(
                        api_utils_xml, alias, self.continue_on_fail
                    )

            # Cleanup the created connection.
            if self.delete_connections and conn_added:
                connections_helper.delete_connection(api_utils, alias)
                connections_helper.check_connection(api_utils, alias, EXPECTED_NOT_FOUND)

        if self.add_connections_to_agent is True and self.delete_connections is False:
            setup_env_helper.update_agent_connections(api_utils, agent_data)
