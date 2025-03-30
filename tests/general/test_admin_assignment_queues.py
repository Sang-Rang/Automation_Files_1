import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_external_service_configuration import (
    V2_EXTERNAL_SERVICE_CONFIGURATION_TEST_CONNECTION,
    V2_EXTERNAL_SERVICE_CONFIGURATION_UPSERT,
)
from utils.api_utils import APIUtils


class TestAdminAssignmentQueues:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Admin")
    @allure.story("Assignment Queues")
    @pytest.mark.smoke
    @pytest.mark.skip(reason="Requires secure access to Service Now credentials")
    def test_admin_assignment_queues_service_now_setup(self, api_utils):
        """Admin - Assignment Queues - ServiceNow assignment setup DEV-48880"""

        conn_data = {
            "userName": "admin",
            "url": "https://dev68247.service-now.com",
            "proxyServerUrl": "",
            "defaultFields": None,
            "clientId": None,
            "id": 1,
            "defaultServiceType": "SERVICE_NOW",
            "defaultAuthenticationType": "BASIC",
            "password": "",
            "authenticationMode": "BASIC",
            "type": "SERVICE_NOW",
        }

        expected_data = {
            "id": conn_data["id"],
            "type": conn_data["defaultServiceType"],
            "authenticationMode": conn_data["authenticationMode"],
            "proxyServerUrl": conn_data["proxyServerUrl"],
            "url": conn_data["url"],
            "userName": conn_data["userName"],
            "password": "*****",
            "clientId": conn_data["clientId"],
            "clientSecret": None,
            "defaultFields": conn_data["defaultFields"],
        }

        testconn_response = api_utils.post(
            V2_EXTERNAL_SERVICE_CONFIGURATION_TEST_CONNECTION, json=conn_data
        )
        for key, value in expected_data.items():
            assert_that(value).is_equal_to(testconn_response["result"][key])

        saveresponse = api_utils.post(V2_EXTERNAL_SERVICE_CONFIGURATION_UPSERT, json=conn_data)
        for key, value in expected_data.items():
            assert_that(value).is_equal_to(saveresponse["result"][key])
