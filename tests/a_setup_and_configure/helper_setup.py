import json
import pathlib

import pytest
from assertpy import assert_that

from endpoints.v2.controller_agent import (
    V2_GET_AGENTS,
    V2_UPDATE_AGENT_CONNECTION_BY_AGENT_AND_CONNECTION_LIST,
)
from endpoints.v2.controller_connections import V2_GET_CONNECTION_ALIASES_NO_TEMPLATE
from endpoints.v2.controller_email import V2_EMAIL_SERVER, V2_EMAIL_SERVER_STATUS
from endpoints.v3.edge import V3_EDGE_SECRETS, V3_EDGE_NAMESPACE, V3_EDGE_KEYTAB
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_connections import ConnectionsHelper

helper = BaseHelper()
connections_helper = ConnectionsHelper()


class SetupEnvHelper:
    """Helper methods for management and validation of connections and agents"""

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="class")
    def api_utils_xml(self, base_url, get_auth_headers):
        get_auth_headers["X-Requested-With"] = "XMLHttpRequest"
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def populate_connection_data():
        """Populate connection data and credentials data from JSON files"""
        test_data_dir = pathlib.Path(__file__).resolve().parent
        directory = f"{test_data_dir}"
        return connections_helper.read_external_json(directory, "constants_connections")

    @staticmethod
    def populate_credential_data():
        """Populate credential data and credentials data from JSON files"""
        test_data_dir = pathlib.Path(__file__).resolve().parent
        directory = f"{test_data_dir}"
        return connections_helper.read_external_json(directory, "constants_connections_credentials")

    @staticmethod
    def update_connection_credentials_and_agent(
        api_utils, connection_data, credentials_data, prefix_conn_name=""
    ):
        """Update all connection data with username/password/host/prefix"""
        all_agents = api_utils.get(V2_GET_AGENTS)
        assert_that(len(all_agents), "No agents found.").is_greater_than(0)
        agent = all_agents[0]["agentId"]  # Will always use 1st found agent

        for connection in connection_data:
            alias = str(connection)
            connection_data[alias]["Alias"] = prefix_conn_name + connection_data[alias]["Alias"]
            connection_data[alias]["username"] = credentials_data[alias]["username"]
            connection_data[alias]["password"] = credentials_data[alias]["password"]
            connection_data[alias]["agentIds"] = [{"id": agent["id"], "uuid": agent["uuid"]}]

            # S3 connections require additional parameters for user/pass
            if "s3AuthKey" in connection_data[alias]:
                connection_data[alias]["s3AuthKey"] = credentials_data[alias]["username"]
                connection_data[alias]["s3AuthSecret"] = credentials_data[alias]["password"]

            # Some host strings include user/pass
            if "${username}" in connection_data[alias]["Host"]:
                connection_data[alias]["Host"] = connection_data[alias]["Host"].replace(
                    "${username}", credentials_data[alias]["username"]
                )
            if "${password}" in connection_data[alias]["Host"]:
                connection_data[alias]["Host"] = connection_data[alias]["Host"].replace(
                    "${password}", credentials_data[alias]["password"]
                )
        return connection_data

    def fetch_keytab_secrets(self, api_utils_xml, agent_id):
        """Fetch existing keytab secret data"""
        namespace = self.get_namespace(api_utils_xml, agent_id)
        path_v3_keytab = V3_EDGE_KEYTAB.replace("{agentId}", str(agent_id)).replace(
            "{namespace}", namespace
        )
        keytab = api_utils_xml.get(path_v3_keytab)
        data = keytab["data"]
        return data

    def append_keytab_secrets(self, api_utils_xml, agent_id, new_keys):
        """Append new keys to existing keys"""
        existing_keys = self.fetch_keytab_secrets(api_utils_xml, agent_id)
        for key, val in new_keys.items():
            if key not in existing_keys:
                existing_keys[key] = val

        return existing_keys

    @staticmethod
    def get_namespace(api_utils_xml, agent_id):
        """Extract an agent's namespace"""
        resp_namespace = api_utils_xml.get(V3_EDGE_NAMESPACE.replace("{agentId}", str(agent_id)))
        return resp_namespace["metadata"]["namespace"]

    def update_keytab_secrets(self, api_utils_xml, credentials_data, agent_data, is_cloud):
        """Update keytab secrets for an agent"""
        agent_id = agent_data["agentid"]
        namespace = self.get_namespace(api_utils_xml, agent_id)
        creds = credentials_data["keytab_secrets"]

        if is_cloud:
            # Assuming format xxx-xxx-xxx-xxx-!!!-x
            agent_split = agent_data["agentname"].split("-")
            creds["metadata"]["namespace"] = namespace
            creds["metadata"]["name"] = f"owldq-keytab-owldq-{agent_split[4]}"
        else:
            creds["metadata"]["namespace"] = namespace
            creds["metadata"]["name"] = f"dq-keytab-dq-{namespace}"

        creds["data"] = self.append_keytab_secrets(api_utils_xml, agent_id, creds["data"])
        resp_secrets = api_utils_xml.put(
            V3_EDGE_SECRETS.replace("{agentId}", str(agent_id)),
            json=json.dumps(creds),
            return_json=False,
        )
        assert_that(resp_secrets.status_code, "Failed to update keytab secrets").is_equal_to(200)

    @staticmethod
    def get_agent_connection(api_utils, agent_name=None):
        """Add the newly created connections to an agent"""
        all_connections = api_utils.get(V2_GET_CONNECTION_ALIASES_NO_TEMPLATE)
        connection_list = []

        # Make an array of all the connection aliases
        for connection in all_connections:
            # Do not add pushdown connections to agents. If isPushdown absent, default is off.
            if connection["isPushdown"] == 0:
                connection_list.append(connection["aliasname"])

        # Get all agents, error if there are none.
        all_agents = api_utils.get(V2_GET_AGENTS)
        if len(all_agents) < 1:
            raise ValueError("No agents found")

        # Get either the first agent or find the requested agent
        if agent_name is None:
            agent = all_agents[0]
        else:
            agent = [item for item in all_agents if item["agentName"] == agent_name]
            if not agent:
                raise ValueError(f"The given agent was not found. Agents: {all_agents}")
            agent = agent[0]

        return {
            "connectionaliases": connection_list,
            "agentname": agent["agentName"],
            "agentid": agent["agentId"]["id"],
            "agentuuid": agent["agentId"]["uuid"],
        }

    @staticmethod
    def update_agent_connections(api_utils, payload_update_connections):
        # Post the new connection list
        update_connections = api_utils.post(
            V2_UPDATE_AGENT_CONNECTION_BY_AGENT_AND_CONNECTION_LIST,
            params=payload_update_connections,
            return_json=False,
        )
        assert_that(update_connections.status_code, "Update connections failed.").is_equal_to(200)

    def update_alert_config(self, api_utils, include_links):
        credential_key = "smtp_sendinblue"

        # Pull login info
        credentials_data = self.populate_credential_data()
        smtp_username = credentials_data[credential_key]["username"]
        smtp_password = credentials_data[credential_key]["password"]

        pl_alert_setup = {
            "host": "smtp-relay.sendinblue.com",
            "port": 587,
            "email": "",
            "username": smtp_username,
            "password": smtp_password,
            "fromEmail": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
            "fromInfo": "",
            "replyEmail": "no-reply@owl-analytics.com",
            "replyInfo": "",
            "subject": "",
        }

        if include_links:
            pl_alert_setup["includeLinks"] = "on"

        # Update the email server and validate configured
        resp_setup = api_utils.post(V2_EMAIL_SERVER, params=pl_alert_setup)
        assert_that(resp_setup, f"Error in alert email setup: {resp_setup}").contains_key("message")
        assert_that(resp_setup["message"], "Alert email setup failed").is_equal_to("Success")

        resp_status = api_utils.get(V2_EMAIL_SERVER_STATUS)
        assert_that(resp_status, "Error in email server status").contains_key("message")
        assert_that(resp_status["message"], "Error in email server status").is_equal_to(
            "Email Server is Configured."
        )
