from datetime import datetime

import allure
import pytest
from assertpy import assert_that, soft_assertions

from endpoints.v2.controller_agent import (
    V2_POST_UPDATE_AGENT,
    V2_GET_AGENT,
    V2_DELETE_AGENT,
    V2_UPDATE_AGENT_CONNECTION_BY_AGENT_AND_CONNECTION_LIST,
    V2_GET_LIST_CONNECTIONS_BY_AGENT,
    V2_GET_LIST_AGENTS,
)
from endpoints.v2.controller_connections import V2_ADD_CONNECTION, V2_DELETE_CONNECTION
from payloads.general.pl_update_agent_settings_data import DATA_AGENT
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_connections import ConnectionsHelper

helper = BaseHelper()
connections_helper = ConnectionsHelper()


class TestAgent:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Admin")
    @allure.story("Agents")
    @pytest.mark.smoke
    def test_create_update_delete_agent(self, api_utils):
        """Create, update, and delete an agent"""
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        agent_name = f"AUTO_AGENT_{now}"
        agent_display_name = f"AUTO_AGENT_DISPLAY_{now}"

        # Create agent and validate
        agent = connections_helper.add_agent(api_utils, agent_name, agent_display_name)
        assert_that(agent["id"], "Creating agent failed, no ID").is_not_empty()
        assert_that(int(agent["id"]), "Creating agent failed, invalid ID").is_greater_than(0)
        assert_that(agent["uuid"], "Creating agent failed, no UUID").is_not_empty()

        pl_agent = {"agentid": agent["id"], "agentuuid": agent["uuid"]}

        # Set test data to newly created agent for later validation
        DATA_AGENT["agentUUID"] = agent["uuid"]
        DATA_AGENT["agentId"] = agent["id"]
        DATA_AGENT["agentName"] = agent_name + "_edit"
        DATA_AGENT["agentDisplayname"] = agent_display_name + "_edit"

        # Update agent. This returns no data or message.
        resp_update_agent = api_utils.post(
            V2_POST_UPDATE_AGENT, params=DATA_AGENT, return_json=False
        )
        assert_that(
            resp_update_agent.status_code, f"Updating agent failed with data {DATA_AGENT}"
        ).is_equal_to(200)

        # Get agent data and validate.
        resp_updated_agent = api_utils.get(V2_GET_AGENT, params=pl_agent)
        for key, value in DATA_AGENT.items():
            if key == "agentId":
                assert_that(str(value), f"Update failed for {key}").is_equal_to(
                    str(resp_updated_agent["agentId"]["id"])
                )
            elif key == "agentUUID":
                assert_that(value, f"Update failed for {key}").is_equal_to(
                    resp_updated_agent["agentId"]["uuid"]
                )
            elif value == "":
                # On an empty field, the response returns either blank or None. It's inconsistent.
                assert_that(resp_updated_agent[key], "Update blank failed").is_false()
            else:
                assert_that(str(value), f"Update failed for {key}").is_equal_to(
                    str(resp_updated_agent[key])
                )

        # Validate get list agents returns the new agent as wel
        resp_list_agents = api_utils.get(V2_GET_LIST_AGENTS)
        assert_that(resp_list_agents, "Did not find agent name").extracting("agentName").contains(
            DATA_AGENT["agentName"]
        )
        assert_that(resp_list_agents, "Did not find agent id and uuid").extracting(
            "agentId"
        ).contains({"id": int(DATA_AGENT["agentId"]), "uuid": f'{DATA_AGENT["agentUUID"]}'})

        # Delete new agent. (There is no delete method, it's a post to a delete API.)
        delete_updated_agent = api_utils.post(V2_DELETE_AGENT, params=pl_agent)
        assert_that(delete_updated_agent["message"], "Delete agent failed").is_equal_to(
            f"Successfully deleted agent: {agent['id']}"
        )

        # Validate agent was deleted correctly.
        # A get call on a nonexistent agent returns a body with nulls.
        resp_delete_agent = api_utils.get(V2_GET_AGENT, params=pl_agent)
        assert_that(resp_delete_agent["agentId"], "Expected no agent Id after delete").is_none()
        assert_that(resp_delete_agent["agentName"], "Expected no agent name after delete").is_none()
        assert_that(
            resp_delete_agent["agentDisplayname"], "Expected no agent display name after delete"
        ).is_none()
        assert_that(
            resp_delete_agent["enabled"], "Expected no enabled value after delete"
        ).is_none()

    @allure.feature("Admin")
    @allure.story("Agents")
    @pytest.mark.smoke
    def test_add_remove_connection_to_agent(self, api_utils):
        """Test Add Remove Connection To Agent (DEV-48870)"""

        # Note: Not testing in depth for creating agents and connections processes
        # Those checks are performed thoroughly in other tests.
        # This test only creates connections and agents to not interfere with the environment

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        agent_name = f"AUTO_AGENT_{now}_DONOTUSE"

        # Any valid connection data can be used here. Not checking connection details.
        pl_new_conn = {
            "conntype": "",
            "Alias": f"AUTO_CONN_NFS_{now}_DONOTUSE",
            "Host": "/opt/owl/data-packs/",
            "authtype": "nfs",
            "driverprops": "",
            "Port": "3000",
            "username": "",
            "password": "",
            "driver": "remoteFileConnDriver",
            "driverlocation": "remoteFileConndriverlocation",
        }

        # Add new connection and agent so the test doesn't break the environment
        agent = connections_helper.add_agent(api_utils, agent_name)
        assert_that(agent["id"], "Creating agent failed, no ID").is_not_empty()
        assert_that(int(agent["id"]), "Creating agent failed, invalid ID").is_greater_than(0)
        assert_that(agent["uuid"], "Creating agent failed, no UUID").is_not_empty()

        resp_new_conn = api_utils.post(V2_ADD_CONNECTION, params=pl_new_conn)
        assert_that(resp_new_conn["msg"], "Add Connection Msg").is_equal_to(
            "Connection saved and valid connection established."
        )

        pl_agent = {
            "agentid": agent["id"],
            "agentuuid": agent["uuid"],
            "agentname": agent["agentName"],
            "connectionaliases": pl_new_conn["Alias"],
        }

        # Add the new connection to the selected agent
        resp_post = api_utils.post(
            V2_UPDATE_AGENT_CONNECTION_BY_AGENT_AND_CONNECTION_LIST,
            params=pl_agent,
            return_json=False,
        )
        assert_that(
            resp_post.status_code,
            f"Assign connection {pl_new_conn['Alias']} to agent {agent['agentName']} failed.",
        ).is_equal_to(200)

        # Validate the connection is now assigned the selected agent
        connection_agent = helper.get_agent_details_for_connection(api_utils, pl_new_conn["Alias"])
        with soft_assertions():
            assert_that(
                str(connection_agent["agentId"]["id"]), "Connection has incorrect agent id"
            ).is_equal_to(str(agent["id"]))
            assert_that(
                connection_agent["agentId"]["uuid"], "Connection has incorrect uuid"
            ).is_equal_to(agent["uuid"])

        # Validate the agent contains the connection
        agent_connections = api_utils.get(
            V2_GET_LIST_CONNECTIONS_BY_AGENT, params={"agentid": pl_agent["agentid"]}
        )
        with soft_assertions():
            assert_that(len(agent_connections), "Invalid number of connections found.").is_equal_to(
                1
            )
            assert_that(
                str(agent_connections[0]["agentId"]["id"]), "Invalid agent id found in agent."
            ).is_equal_to(str(pl_agent["agentid"]))
            assert_that(
                agent_connections[0]["agentId"]["uuid"], "Invalid agent uuid found in agent."
            ).is_equal_to(pl_agent["agentuuid"])
            assert_that(
                agent_connections[0]["connectionAliasname"],
                "Invalid connection name found in agent.",
            ).is_equal_to(pl_new_conn["Alias"])

        # Remove the connection from the selected agent
        # This is done by updating the agent to a new list of connections, which here is none
        pl_agent["connectionaliases"] = ""
        resp_remove = api_utils.post(
            V2_UPDATE_AGENT_CONNECTION_BY_AGENT_AND_CONNECTION_LIST,
            params=pl_agent,
            return_json=False,
        )
        assert_that(
            resp_remove.status_code,
            f"Remove connection {pl_new_conn['Alias']} to agent {agent['agentName']} failed.",
        ).is_equal_to(200)

        # Delete
        res_delete_conn = api_utils.get(
            V2_DELETE_CONNECTION, params={"connection": pl_new_conn["Alias"]}
        )
        assert_that(res_delete_conn["msg"], "Delete Connection failed").is_equal_to("Success")

        res_delete_agent = api_utils.post(V2_DELETE_AGENT, params=pl_agent)
        assert_that(res_delete_agent["message"], "Delete agent failed").is_equal_to(
            f"Successfully deleted agent: {pl_agent['agentid']}"
        )
