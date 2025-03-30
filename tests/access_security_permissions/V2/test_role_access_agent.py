import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_agents import ACCESS_MATRIX_AGENTS

from endpoints.v2.controller_agent import (
    V2_GET_AGENTS,
    V2_GET_LIST_CONNECTIONS_BY_AGENT,
    V2_GET_LIST_AGENTS_DETAILS_BY_CONNECTION_ALIAS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessAgent:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Agent")
    def test_role_access_get_agents(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getagents"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_AGENTS,
            ACCESS_MATRIX_AGENTS[V2_GET_AGENTS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Agent")
    def test_role_access_get_list_connections_by_agent(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getlistconnectionsbyagent"""
        agents = api_utils.get(V2_GET_AGENTS)
        for agent in agents:
            params = {"agentid": agent["agentId"]["id"], "agentuuid": agent["agentId"]["uuid"]}

            security_helper.check_role_permissions(
                api_utils,
                get_auth_headers_multi_user,
                V2_GET_LIST_CONNECTIONS_BY_AGENT,
                ACCESS_MATRIX_AGENTS[V2_GET_LIST_CONNECTIONS_BY_AGENT],
                payload=params,
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Agent")
    def test_role_access_get_list_agents_details_by_conn_alias(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getlistagentsdetailsbyconnectionalias"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_LIST_AGENTS_DETAILS_BY_CONNECTION_ALIAS,
            ACCESS_MATRIX_AGENTS[V2_GET_LIST_AGENTS_DETAILS_BY_CONNECTION_ALIAS],
            payload={"connectionalias": job["connectionalias"]},
        )
