# pylint: disable=anomalous-backslash-in-string
import json
import pathlib
import re
import pytest
from assertpy import assert_that

from endpoints.v2.controller_agent import V2_CREATE_AGENT
from endpoints.v2.controller_connections import (
    V2_GET_LIST_REMOTE_FILE_SYSTEM,
    V2_GET_REMOTE_FILE_CONNECTIONS_SENSITIVE,
    V2_GET_CONNECTIONS_PWDMGR_SENSITIVE,
    V2_GET_CONNECTION_BY_ALIAS,
    V2_DELETE_CONNECTION,
    V2_ADD_CONNECTION,
    V2_GET_JDBC_CONNECTIONS_SENSITIVE,
)
from endpoints.v2.controller_explorer import V2_GET_EXPLORER_SEARCH, V2_POST_EXPLORER_TABLE_SEARCH
from utils.api_utils import APIUtils


class ConnectionsHelper:
    """Helper methods for management and validation of connections and agents"""

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def add_agent(api_utils, agent_name, agent_display_name=""):
        """Create an agent and parse out its id and uuid"""

        # Default it to match the agent name if none provided
        agent_display_name = agent_display_name or agent_name

        # Creating the agent returns a string with the new id and uuid.
        # This pattern extracts those values using regular expressions
        # [id=  and  uuid=
        regex_id = r"(?<=\[id=)(.*?)(?=\,)"
        regex_uuid = r"(?<=uuid=)(.*?)(?=\])"

        # Call accepts only a name, no option to input data.
        resp_create_agent = api_utils.post(V2_CREATE_AGENT, params={"agentname": agent_name})

        # Extract the newly created Agent ID and Agent UUID with regex pattern.
        found_id = re.search(regex_id, resp_create_agent["msg"]).group(1)
        found_uuid = re.search(regex_uuid, resp_create_agent["msg"]).group(1)

        return {
            "id": found_id,
            "uuid": found_uuid,
            "agentName": agent_name,
            "agentDisplayName": agent_display_name,
        }

    @staticmethod
    def check_connection_pwdmgr_sensitive(api_utils, conn_name, deleted=False):
        """Confirm the connections page reflects the new connection"""
        connections = api_utils.get(V2_GET_CONNECTIONS_PWDMGR_SENSITIVE)
        found_conn = list(filter(lambda conn: conn["aliasname"] == conn_name, connections))
        if deleted:
            assert_that(len(found_conn), f"Found deleted connection {conn_name}").is_equal_to(0)
            return None

        assert_that(len(found_conn), f"No connection found for {conn_name}").is_equal_to(1)
        return found_conn[0]

    @staticmethod
    def check_explorer_remote_file_connection(
        api_utils, conn_name, deleted=False, continue_on_fail=False
    ):
        """Confirm the explorer tree reflects this new connection"""
        connections = api_utils.get(V2_GET_REMOTE_FILE_CONNECTIONS_SENSITIVE)
        found_conn = list(filter(lambda conn: conn["aliasname"] == conn_name, connections))
        if deleted:
            assert_that(len(found_conn), f"Found deleted connection {conn_name}").is_equal_to(0)
            return None

        if continue_on_fail and len(found_conn) < 1:
            print(f"No connection found for {conn_name} in remote file explorer")
            return None

        assert_that(len(found_conn), f"No connection found for {conn_name}").is_equal_to(1)
        return found_conn[0]

    @staticmethod
    def check_explorer_jdbc_connection(api_utils, conn_name, continue_on_fail=False):
        """Confirm the explorer tree reflects this new connection"""
        connections = api_utils.get(V2_GET_JDBC_CONNECTIONS_SENSITIVE)
        found_conn = list(filter(lambda conn: conn["aliasname"] == conn_name, connections))

        if continue_on_fail:
            if len(found_conn) != 1:
                print(f"No connection found for {conn_name}")
                return None
            return found_conn[0]

        assert_that(len(found_conn), f"No connection found for {conn_name}").is_equal_to(1)
        return found_conn[0]

    @staticmethod
    def check_remote_files(api_utils, conn_name, path, expected_data, continue_on_fail=False):
        """Check the contents of a remote file connection"""
        resp_found_files = api_utils.get(
            V2_GET_LIST_REMOTE_FILE_SYSTEM,
            {"connectionalias": conn_name, "path": path},
            return_json=False,
        )

        if continue_on_fail and resp_found_files.status_code != 200:
            print(f"Unable to check remote file for {conn_name}, resp: {resp_found_files}")
            return

        found_files = resp_found_files.json()
        # Validates every item in the expected list exists
        # But allows for more options than given list, in case new data is added later.
        # Key in dict check for remote file connections that have both directories (dir) and files
        for expected in expected_data:
            for key, val in expected.items():
                found = any(key in d and d[key] == val for d in found_files)
                assert_that(found, f"Not found: {key} of {val} in {found_files}").is_equal_to(True)

    @staticmethod
    def add_connection(api_utils, params, is_cloud, continue_on_fail=False):
        """Create a new conenction"""
        msg = "Connection saved and valid connection established."
        msg_key = "message"

        if params["isPushdown"] == 1 and is_cloud:
            print("Pushdown is not supported on cloud environments.")
            return False

        # Saved code for working on CLOUD env updates, work in progress. Add agentId param
        # params["agentId"] = agent_data["agentid"]
        # params["agentUUID"] = agent_data["agentuuid"]
        # params["agentIds"] = [{
        #   "id": agent_data["agentid"],
        #   "uuid": agent_data["agentuuid"]
        # }]

        new_conn = api_utils.post(V2_ADD_CONNECTION, params=params, return_json=False)
        new_conn_json = new_conn.json()

        if "msg" in new_conn_json:  # If there is an error, sometimes it's a different key
            msg_key = "msg"

        if continue_on_fail and (new_conn.status_code != 200 or new_conn_json[msg_key] != msg):
            print(f"Add connection failed for: {params['Alias']} from: {new_conn_json[msg_key]}")
            return False

        assert_that(new_conn_json[msg_key], "Create connection failed").is_equal_to(msg)
        return True

    @staticmethod
    def delete_connection(api_utils, conn_name):
        """Delete a connection"""
        result = api_utils.get(V2_DELETE_CONNECTION, params={"connection": conn_name})
        assert_that(result["msg"], "Delete Connection failed").is_equal_to("Success")

    @staticmethod
    def check_connection(api_utils, conn_name, expected_data):
        """Check the detailed info of the connection"""
        found_conn = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": conn_name})
        for key, value in expected_data.items():
            assert_that(value, f"Check Connection: Unexpected value for {key}").is_equal_to(
                found_conn[key]
            )

    @staticmethod
    def check_databases(api_utils, conn_name, expected_data, continue_on_fail=False):
        """Check the databases that are available in the connection"""
        # Note: This will only validate the given connections exist, it will ignore others.
        resp_dbs = api_utils.get(
            V2_GET_EXPLORER_SEARCH, params={"alias": conn_name}, return_json=False
        )

        # Sometimes the new connection needs a moment before it's available. Retry.
        if resp_dbs.status_code != 200:
            resp_dbs = api_utils.get(
                V2_GET_EXPLORER_SEARCH, params={"alias": conn_name}, return_json=False
            )

        if continue_on_fail and resp_dbs.status_code != 200:
            print(
                f"Failed Database Check for {conn_name}. "
                f"Status: {resp_dbs.status_code} Text: {resp_dbs.text}"
            )
            return

        assert_that(
            resp_dbs.status_code,
            f"Database Check failed for {conn_name}. Text: {resp_dbs.text}",
        ).is_equal_to(200)

        dbs = resp_dbs.json()
        assert_that(len(dbs), "No databases found").is_greater_than(0)

        for expected_item in expected_data:
            found = any(found_item["database"] == expected_item["database"] for found_item in dbs)
            if continue_on_fail and found is False:
                print(f"{expected_item['database']} was not found in {dbs}")
            else:
                assert_that(found, f"{expected_item['database']} was not found in {dbs}").is_true()

    @staticmethod
    def check_table_maps(api_utils, conn_name, expected_data, continue_on_fail=False):
        """Check the tables that are available in the connection"""
        # Note: This will only validate the given maps exist, it will ignore others.
        for schema in expected_data:
            pl_table_map = {"alias": conn_name, "schema": schema, "tables": "-"}

            resp_tables = api_utils.post(
                V2_POST_EXPLORER_TABLE_SEARCH, params=pl_table_map, return_json=False
            )

            # Sometimes the new connection needs a moment before it's available. Retry.
            if resp_tables.status_code != 200:
                resp_tables = api_utils.post(
                    V2_POST_EXPLORER_TABLE_SEARCH, params=pl_table_map, return_json=False
                )

            if resp_tables.status_code != 200 and continue_on_fail:
                print(
                    f"Failed Table Maps Check. Status: {resp_tables.status_code}."
                    f" Text: {resp_tables.text}"
                )
                return  # Exit to continue running the other connections

            assert_that(
                resp_tables.status_code, "Failed to get explorer table search data"
            ).is_equal_to(200)

            tables = resp_tables.json()
            assert_that(len(tables), "No table maps found").is_greater_than(0)
            found_tables = tables["tableMaps"]

            for expected_item in expected_data[schema]:
                is_found = any(
                    found_item["table"] == expected_item["table"] for found_item in found_tables
                )
                if continue_on_fail and is_found is False:
                    print(f"{expected_item['table']} was not found in {found_tables}")
                else:
                    assert_that(
                        is_found, f"{expected_item['table']} was not found in {found_tables}"
                    ).is_true()

    @staticmethod
    def is_environment_cloud(api_utils):
        """Extract the Base URL from the cloud jenkins file"""
        # Note: Is there a better way to get this info?
        test_data_dir = pathlib.Path(__file__).resolve().parent.parent
        file = pathlib.Path(f"{test_data_dir}/Jenkinsfile.cloud")
        with open(file, "r", encoding="UTF-8") as file_open:
            text = file_open.read()

        base_url_start_string = "string(name: 'BASE_URL', defaultValue: '"
        base_url_end_string = ".com"
        start_char_pos = text.find(base_url_start_string) + len(base_url_start_string)
        end_char_pos = text.find(base_url_end_string)

        found_url = text[start_char_pos:end_char_pos]

        if api_utils.base_url == found_url:
            return True
        return False

    @staticmethod
    def read_external_json(directory, file_name):
        file = pathlib.Path(f"{directory}/data_setup/{file_name}.json")
        with open(file, "r", encoding="UTF-8") as file_open:
            data = json.load(file_open)
        return data
