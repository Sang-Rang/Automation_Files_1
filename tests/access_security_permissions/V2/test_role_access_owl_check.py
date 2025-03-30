import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_owl_check import (
    ACCESS_MATRIX_OWL_CHECK,
)
from endpoints.v2.controller_agent import V2_GET_AGENTS
from endpoints.v2.controller_owl_check import (
    V2_GET_OWL_CHECK_Q_BY_AGENT_ID,
    V2_GET_OWL_CHECK_INVENTORY,
    V2_GET_OWL_CHECKLIST,
    V2_GET_AGENT_Q_BY_DATASET_RUN_ID,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessOwlCheck:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Check")
    def test_role_access_get_owl_check_q_by_agent_id(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlcheckqbyagentid"""
        agents = api_utils.get(V2_GET_AGENTS)
        for agent in agents:
            params = {"agentid": agent["agentId"]["id"], "agentuuid": agent["agentId"]["uuid"]}
            security_helper.check_role_permissions(
                api_utils,
                get_auth_headers_multi_user,
                V2_GET_OWL_CHECK_Q_BY_AGENT_ID,
                ACCESS_MATRIX_OWL_CHECK[V2_GET_OWL_CHECK_Q_BY_AGENT_ID],
                payload=params,
            )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Check")
    def test_role_access_get_owl_check_inventory(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlcheckinventory"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECK_INVENTORY,
            ACCESS_MATRIX_OWL_CHECK[V2_GET_OWL_CHECK_INVENTORY],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Check")
    def test_role_access_get_owl_checklist(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlchecklist"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECKLIST,
            ACCESS_MATRIX_OWL_CHECK[V2_GET_OWL_CHECKLIST],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Owl Check")
    def test_role_access_get_agent_q_by_dataset_run_id(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getagentqbydatasetrunid"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_AGENT_Q_BY_DATASET_RUN_ID,
            ACCESS_MATRIX_OWL_CHECK[V2_GET_AGENT_Q_BY_DATASET_RUN_ID],
            payload={"dataset": job["dataset"], "runid": job["runId"]},
        )
