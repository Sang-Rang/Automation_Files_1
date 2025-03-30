import json
import time

import allure
import pytest
from assertpy import assert_that

from endpoints.dgc_integration.dq.mappings_api import (
    DGC_INTEGRATIONS_MAPPING_SCHEMA,
    DGC_INTEGRATION_GET_AUTO_MAPPING_JOB,
    DGC_INTEGRATION_CANCEL_MAPPING_SCHEMA,
    DGC_INTEGRATION_MAPPING_SCHEMA_BATCH,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DGC_DQ_INTEGRATION_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper

helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()
POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"

MAPPED_DGC_DATABASE_ID = "d4ae34d5-171c-402b-b4df-51cb0cb030c7"
MAPPED_DGC_SCHEMA_ID = "b462ffbf-f0ec-4492-bc5d-76fda7de0bea"
MAPPED_CONNECTION_NAME = "APPROVED_POSTGRES_UP"


@pytest.mark.dq_dgc
class TestDqDgcAutoMapConnections:

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="class")
    def dgc_api_utils(self, dgc_base_url, get_auth_headers_dgc):
        return APIUtils(base_url=dgc_base_url, headers=get_auth_headers_dgc)

    @pytest.fixture(scope="class")
    def setup_dq_dgc_integration(self, api_utils, dgc_api_utils):
        # Delete all DQ/DGC connections
        dg_dgc_connection_helper.delete_all_dq_dgc_connections(api_utils)

        # Setup DGC credentials
        dq_dgc_helper.setup_dgc_credentials(api_utils)

        # Map DQ/DGC connections
        dq_dgc_helper.map_dq_dgc_connections(
            api_utils,
            POSTGRES_SCHEMA_NAME,
            POSTGRES_TABLE_NAME,
            DQ_POSTGRES_CONNECTION_NAME,
            DGC_DATABASE_UUID,
        )

        # Align DGC community
        dg_dgc_connection_helper.align_tenant_to_dgc_community(
            api_utils, dgc_api_utils, DGC_DQ_INTEGRATION_COMMUNITY
        )

        # Map DQ/DGC dimensions
        dg_dgc_connection_helper.dq_dgc_connection_create_dimension_mapping(api_utils)

    @staticmethod
    def get_updated_status_of_mapped_job(api_utils, job_id, mapped_tables=None, total_tables=None):
        # Retrieves schema auto-mapping job by id
        timeout = 240  # Maximum time to wait in seconds
        interval = 5  # Time between retries in seconds

        start_time = time.time()

        while True:
            # Fetch the response from the API
            asset_url = DGC_INTEGRATION_GET_AUTO_MAPPING_JOB.format(jobId=job_id)
            auto_mapping_job_response = api_utils.get(asset_url)

            # Check if the response meets the expected condition
            if auto_mapping_job_response["status"] == "FINISHED":
                assert (
                    auto_mapping_job_response["mappedTables"] == mapped_tables
                ), "Invalid number of mapped tables returned"
                assert (
                    auto_mapping_job_response["totalTables"] == total_tables
                ), "Invalid number of total tables returned"
                assert auto_mapping_job_response["exception"] is None, "Exception is returned"
                return auto_mapping_job_response["status"]

            # Check if timeout has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise AssertionError(
                    f"Timeout reached. "
                    f"Expected status to be FINISHED but got "
                    f"{auto_mapping_job_response['status']}"
                )

            # Wait before retrying
            time.sleep(interval)

    @staticmethod
    def submit_single_mapping_job(api_utils, job_schema):
        pl_schema_mapping_json = json.dumps(job_schema)

        response = api_utils.post(DGC_INTEGRATIONS_MAPPING_SCHEMA, data=pl_schema_mapping_json)
        return response

    @staticmethod
    def get_id_by_schema_name(api_response, schema_name):
        for item in api_response:
            if item["schemaName"] == schema_name:
                return item["id"]
        return None

    @staticmethod
    def submit_multiple_mapping_job(api_utils, job_schema):
        pl_schema_mapping_json = json.dumps(job_schema)

        response = api_utils.post(DGC_INTEGRATION_MAPPING_SCHEMA_BATCH, data=pl_schema_mapping_json)
        return response

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_auto_map_connections_single_job(self, api_utils):
        """Auto-map connections, mapping status and cancel mapping."""
        credential_id = dg_dgc_connection_helper.get_dgc_connections_credentials(api_utils)

        auto_mapping_single_connections = {
            "dgcCredentialId": credential_id,
            "connectionName": MAPPED_CONNECTION_NAME,
            "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
            "schemaName": "berka",
            "dgcSchemaId": MAPPED_DGC_SCHEMA_ID,
        }

        # Create a single auto mapping job and check status
        response = self.submit_single_mapping_job(api_utils, auto_mapping_single_connections)
        assert_that(
            response["status"],
            f"Invalid job status returned, " f"expected QUEUED, but got {response['status']}",
        ).is_equal_to("QUEUED")

        job_id = response["id"]

        # Get the schema-mapping jobs total count
        req_params = {"dgcCredentialId": credential_id}
        get_mapping_count = api_utils.get(DGC_INTEGRATIONS_MAPPING_SCHEMA, params=req_params)

        assert_that(
            get_mapping_count["total"],
            f"Invalid number of mapped jobs returned, "
            f"expected 1 job, but got {get_mapping_count['total']}",
        ).is_equal_to(1)

        # Verify the job is Finished and correct number of tables mapped
        self.get_updated_status_of_mapped_job(api_utils, job_id, mapped_tables=6, total_tables=9)

        # Submit a new job and cancel right after, check status
        second_job_response = self.submit_single_mapping_job(
            api_utils, auto_mapping_single_connections
        )
        assert_that(
            second_job_response["status"],
            f"Invalid job status returned, "
            f"expected QUEUED, but got {second_job_response['status']}",
        ).is_equal_to("QUEUED")

        # Cancel mapping job
        asset_url = DGC_INTEGRATION_CANCEL_MAPPING_SCHEMA.format(jobId=second_job_response["id"])
        cancel_mapping_job_response = api_utils.post(asset_url)
        assert cancel_mapping_job_response.status_code == 204, (
            f"Invalid status code returned for canceling job mapping, expected 204, but got: "
            f"{cancel_mapping_job_response.status_code}"
        )

        # Check the status after canceling a mapping
        asset_url = DGC_INTEGRATION_GET_AUTO_MAPPING_JOB.format(jobId=second_job_response["id"])
        second_mapping_job_response = api_utils.get(asset_url)
        assert_that(
            second_mapping_job_response["status"],
            f"Invalid job status returned, "
            f"expected TERMINATED, but got {second_mapping_job_response['status']}",
        ).is_equal_to("TERMINATED")

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_auto_map_connections_multiple_jobs(self, api_utils):
        credential_id = dg_dgc_connection_helper.get_dgc_connections_credentials(api_utils)
        auto_mapping_multiple_connections = [
            {
                "dgcCredentialId": credential_id,
                "connectionName": MAPPED_CONNECTION_NAME,
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "public",
                "dgcSchemaId": "09f2d6bf-0caf-408c-872b-ffbf7972810d",
            },
            {
                "dgcCredentialId": credential_id,
                "connectionName": MAPPED_CONNECTION_NAME,
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "berka",
                "dgcSchemaId": MAPPED_DGC_SCHEMA_ID,
            },
            {
                "dgcCredentialId": credential_id,
                "connectionName": MAPPED_CONNECTION_NAME,
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "owl_test",
                "dgcSchemaId": "018d7811-b050-77cb-886e-4e0457502179",
            },
            {
                "dgcCredentialId": credential_id,
                "connectionName": MAPPED_CONNECTION_NAME,
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "samples",
                "dgcSchemaId": "018ce8b4-b9d2-7bec-91ab-a390d3dc4031",
            },
        ]

        response = self.submit_multiple_mapping_job(api_utils, auto_mapping_multiple_connections)

        assert_that(
            response[0]["status"],
            f"Invalid job status returned, " f"expected QUEUED, but got {response[0]['status']}",
        ).is_equal_to("QUEUED")
        assert_that(
            response[1]["status"],
            f"Invalid job status returned, " f"expected QUEUED, but got {response[1]['status']}",
        ).is_equal_to("QUEUED")
        assert_that(
            response[2]["status"],
            f"Invalid job status returned, " f"expected QUEUED, but got {response[2]['status']}",
        ).is_equal_to("QUEUED")
        assert_that(
            response[3]["status"],
            f"Invalid job status returned, " f"expected QUEUED, but got {response[3]['status']}",
        ).is_equal_to("QUEUED")

        public_schema_id = self.get_id_by_schema_name(response, "public")
        berka_schema_id = self.get_id_by_schema_name(response, "berka")
        owl_test_schema_id = self.get_id_by_schema_name(response, "owl_test")
        samples_schema_id = self.get_id_by_schema_name(response, "samples")

        # Verify job is Finished and correct number of tables mapped
        self.get_updated_status_of_mapped_job(
            api_utils, samples_schema_id, mapped_tables=13, total_tables=15
        )
        self.get_updated_status_of_mapped_job(
            api_utils, berka_schema_id, mapped_tables=6, total_tables=9
        )
        self.get_updated_status_of_mapped_job(
            api_utils, public_schema_id, mapped_tables=296, total_tables=372
        )
        self.get_updated_status_of_mapped_job(
            api_utils, owl_test_schema_id, mapped_tables=46, total_tables=58
        )

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_auto_map_connections_single_and_multiple_job_invalid_data(self, api_utils):
        """Auto-map connections, with invalid data inputs, single and multiple jobs."""
        credential_id = dg_dgc_connection_helper.get_dgc_connections_credentials(api_utils)

        auto_mapping_single_connections_invalid = {
            "dgcCredentialId": credential_id,
            "connectionName": "APPROVED_POSTGRES_UP_Invalid",
            "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
            "schemaName": "berka",
            "dgcSchemaId": MAPPED_DGC_SCHEMA_ID,
        }
        response = self.submit_single_mapping_job(
            api_utils, auto_mapping_single_connections_invalid
        )
        assert_that(
            response["statusCode"],
            f"Invalid job status code, " f"expected 404, but got {response['statusCode']}",
        ).is_equal_to(404)
        assert_that(
            response["userMessage"],
            "Invalid user message returned",
        ).is_equal_to(
            "'Connection' with provided identifier: 'APPROVED_POSTGRES_UP_Invalid' does not exist."
        )

        # For the batch request it would "Silently ignores invalid mapping jobs requests",
        # so even if all jobs are invalid it will return empty list and 201
        auto_mapping_multiple_connections_invalid = [
            {
                "dgcCredentialId": credential_id,
                "connectionName": "APPROVED_POSTGRES_UP_Invalid",
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "public",
                "dgcSchemaId": "09f2d6bf-0caf-408c-872b-ffbf79728101",
            },
            {
                "dgcCredentialId": credential_id,
                "connectionName": "APPROVED_POSTGRES_UP_Invalid",
                "dgcDatabaseId": MAPPED_DGC_DATABASE_ID,
                "schemaName": "berka",
                "dgcSchemaId": MAPPED_DGC_SCHEMA_ID,
            },
        ]

        pl_schema_mapping_json = json.dumps(auto_mapping_multiple_connections_invalid)

        response_secondary_job = api_utils.post(
            DGC_INTEGRATION_MAPPING_SCHEMA_BATCH, data=pl_schema_mapping_json, return_json=False
        )
        assert_that(
            response_secondary_job.status_code,
            f"Invalid job status code, "
            f"expected 201, but got {response_secondary_job.status_code}",
        ).is_equal_to(201)

        response_secondary_job = self.submit_multiple_mapping_job(
            api_utils, auto_mapping_multiple_connections_invalid
        )
        assert_that(
            response_secondary_job,
            f"Invalid job status response, "
            f"expected empty list[], but got {response_secondary_job}",
        ).is_equal_to([])
