import json
from dataclasses import dataclass

import pytest

from endpoints.dgc_integration.dgc.communities_api import DGC_COMMUNITIES
from endpoints.dgc_integration.dq.dgc_connection_api import DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS
from endpoints.dgc_integration.dq.dimensions_api import (
    DGC_INTEGRATIONS_DQ_DIMENSIONS,
    DGC_INTEGRATIONS_DGC_DIMENSIONS,
    DGC_INTEGRATIONS_DQ_DGC_DIMENSIONS_MAPPING,
)
from endpoints.dgc_integration.dq.integration_api import (
    DGC_INTEGRATION_DELETE_DQ_DGC_CONNECTION,
)
from endpoints.dgc_integration.dq.mappings_api import (
    DGC_INTEGRATION_MAPPING,
    DGC_INTEGRATION_MAPPING_CONNECTION_DATABASE,
    DGC_INTEGRATION_MAPPING_SCHEMA,
    DGC_INTEGRATION_MAPPING_TABLE,
    DGC_INTEGRATION_MAPPING_COLUMN,
    DGC_TENANT_MAPPING,
    DGC_UPDATE_MAPPING_TENANT,
)
from payloads.dq_dgc_integration.pl_dq_dgc_dimension_mappings import (
    DQ_DGC_DIMENSIONS_MAPPING_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_constants import DGC_BASE_URL


@dataclass
class DqDgcDatabaseConnectionMappingInfo:
    dq_connection_name: str
    dgc_database_id: str
    dgc_database_schema_name: str
    dgc_database_table_name: str


class DqDgcConnectionHelper:
    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="session")
    def dgc_api_utils(self, dgc_base_url, get_auth_headers_dgc):
        return APIUtils(base_url=dgc_base_url, headers=get_auth_headers_dgc)

    @staticmethod
    def build_dq_dgc_columns_mapping_pl(api_utils, dgc_table_id):
        # Get DGC columns info
        column_mapping_url = DGC_INTEGRATION_MAPPING_COLUMN.format(tableId=dgc_table_id)
        column_mapping_response = api_utils.get(column_mapping_url)

        assert (
            len(column_mapping_response) > 0
        ), f"Couldn't retrieve column mappings from DGC for table id: {dgc_table_id}"

        dq_dgc_columns_mapping = []

        # Assuming DQ/DGC column names are the same
        for column in column_mapping_response:
            column_mapping = {
                "columnId": "",
                "dgcColumn": column["displayName"],
                "dqColumn": column["displayName"],
                "dgcUuid": column["id"],
            }
            dq_dgc_columns_mapping.append(column_mapping)

        return dq_dgc_columns_mapping

    @staticmethod
    def build_dq_dgc_table_mapping_pl(
        api_utils, dgc_schema_name_path, dgc_schema_id, connection_mapping_info
    ):
        # Get DGC table info
        table_mapping_url = DGC_INTEGRATION_MAPPING_TABLE.format(schemaId=dgc_schema_id)
        table_mapping_response = api_utils.get(table_mapping_url)

        assert (
            len(table_mapping_response) > 0
        ), f"Couldn't retrieve table mappings from DGC for schema: {dgc_schema_id}"

        dgc_table_name_path = (
            f"{dgc_schema_name_path}>{connection_mapping_info.dgc_database_table_name}"
        )

        dgc_table_id = ""

        for table in table_mapping_response:
            if table["name"] == dgc_table_name_path:
                dgc_table_id = table["id"]
                break

        columns_mapping = DqDgcConnectionHelper.build_dq_dgc_columns_mapping_pl(
            api_utils, dgc_table_id
        )

        # Assuming DQ/DGC table names are the same
        dq_dgc_table_mapping = {
            "tableId": "",
            "dgcTable": connection_mapping_info.dgc_database_table_name,
            "dqTable": connection_mapping_info.dgc_database_table_name,
            "dgcUuid": dgc_table_id,
            "columnMapping": columns_mapping,
        }

        return dq_dgc_table_mapping

    @staticmethod
    def build_dq_dgc_schema_mapping_pl(api_utils, dgc_database_name_path, connection_mapping_info):
        # Get DGC Schema info
        schema_mapping_url = DGC_INTEGRATION_MAPPING_SCHEMA.format(
            databaseId=connection_mapping_info.dgc_database_id
        )
        schema_mapping_response = api_utils.get(schema_mapping_url)

        assert len(schema_mapping_response) > 0, (
            f"Couldn't retrieve schema mappings from DGC for database id: "
            f"{connection_mapping_info.dgc_database_id}"
        )

        dgc_schema_id = ""
        dgc_schema_name_path = (
            f"{dgc_database_name_path}>{connection_mapping_info.dgc_database_schema_name}"
        )

        for schema in schema_mapping_response:
            if schema["name"] == dgc_schema_name_path:
                dgc_schema_id = schema["id"]
                break

        table_mapping = DqDgcConnectionHelper.build_dq_dgc_table_mapping_pl(
            api_utils, dgc_schema_name_path, dgc_schema_id, connection_mapping_info
        )

        # Assuming DQ/DGC schema names are the same
        dq_dgc_schema_mapping = {
            "schemaId": "",
            "dgcSchema": connection_mapping_info.dgc_database_schema_name,
            "dqSchema": connection_mapping_info.dgc_database_schema_name,
            "dgcUuid": dgc_schema_id,
            "tableMapping": [table_mapping],
        }

        return dq_dgc_schema_mapping

    @staticmethod
    def build_dq_dgc_connection_mapping_pl(api_utils, connection_mapping_info):
        # Get DGC database info
        dgc_database_connection_response = api_utils.get(
            DGC_INTEGRATION_MAPPING_CONNECTION_DATABASE.format(
                databaseId=connection_mapping_info.dgc_database_id
            )
        )
        dgc_connections_response = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)
        dgc_connection_cred_id = dgc_connections_response[0]["id"]

        assert len(dgc_database_connection_response) > 0, (
            f"Couldn't retrieve database connection mapping from DGC for database id: "
            f"{connection_mapping_info.dgc_database_id}"
        )

        dgc_database_name_path = dgc_database_connection_response["name"]

        # Build schema mapping
        dgc_schema_mapping = DqDgcConnectionHelper.build_dq_dgc_schema_mapping_pl(
            api_utils, dgc_database_name_path, connection_mapping_info
        )

        dq_dgc_connection_mapping = {
            "connectionId": "",
            "dqName": connection_mapping_info.dq_connection_name,
            "dgcName": dgc_database_name_path,
            "dgcUuid": connection_mapping_info.dgc_database_id,
            "credentialId": dgc_connection_cred_id,
            "schemaMapping": [dgc_schema_mapping],
        }

        return dq_dgc_connection_mapping

    @staticmethod
    def setup_dgc_credentials(api_utils, pl_dgc_connection_creds):
        response = api_utils.post(
            DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS, params=pl_dgc_connection_creds
        )
        assert (
            response.get("status") == "success"
        ), f"Couldn't setup DGC credentials - {response.get('msg')}"
        assert response.get("cred") is not None, "Credentials shouldn't be empty"

    @staticmethod
    def delete_all_dq_dgc_connections(api_utils):
        dgc_connection_creds = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)

        for connection_credential in dgc_connection_creds:
            credential_id = connection_credential["id"]

            delete_url = DGC_INTEGRATION_DELETE_DQ_DGC_CONNECTION.format(credentialId=credential_id)
            response = api_utils.delete(delete_url, return_json=False)

            assert (
                response.status_code == 204
            ), f"Couldn't delete DQ/DGC connection with id - {credential_id}"

    @staticmethod
    def get_dgc_connections_credentials(api_utils):
        # Get Credential ID
        dgc_connections_response = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)
        credential_id = None

        for connection in dgc_connections_response:
            if connection["serviceUrl"] == DGC_BASE_URL:
                credential_id = connection["id"]

        assert credential_id is not None, "Couldn't find DGC connection credentials"
        return credential_id

    @staticmethod
    def align_tenant_to_dgc_community(api_utils, dgc_api_utils, dgc_community):
        # Get Credential ID
        dgc_connections_response = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)
        credential_id = None

        for connection in dgc_connections_response:
            if connection["serviceUrl"] == DGC_BASE_URL:
                credential_id = connection["id"]

        assert credential_id is not None, "Couldn't find DGC connection credentials"

        # Get DGC community UUID
        community_name_param = {"name": dgc_community}

        dgc_community_id = None
        integration_community_response = dgc_api_utils.get(
            DGC_COMMUNITIES, params=community_name_param
        )

        for community in integration_community_response["results"]:
            if community["name"] == dgc_community:
                dgc_community_id = community["id"]
                break

        assert dgc_community_id is not None, f"Couldn't find {dgc_community} in DGC"

        # Map DGC community
        pl_tenant_community_mapping = {
            "credId": credential_id,
            "resourceType": "Tenant",
            "tableName": "",
            "dgcName": dgc_community,
            "dqName": "",
            "dgcUuid": dgc_community_id,
            "schemaName": "",
            "connectionName": "",
        }

        pl_tenant_community_mapping_json = json.dumps(pl_tenant_community_mapping)

        response = api_utils.post(
            DGC_INTEGRATION_MAPPING, data=pl_tenant_community_mapping_json, return_json=False
        )

        assert response.status_code == 204, f"Couldn't map {dgc_community} on DGC"

    @staticmethod
    def update_tenant_mapping(api_utils, dgc_community):
        """Change tenant to different community."""
        dgc_connections_response = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)
        credential_id = None

        for connection in dgc_connections_response:
            if connection["serviceUrl"] == DGC_BASE_URL:
                credential_id = connection["id"]

        assert credential_id is not None, "Couldn't find DGC connection credentials"

        tenant_mapping = DGC_TENANT_MAPPING.format(credentialId=credential_id)
        response_tenant_id = api_utils.get(tenant_mapping)
        tenant_id = response_tenant_id["id"]

        # Update mapping tenant
        pl_tenant_mapping = {
            "id": tenant_id,
            "credentialId": credential_id,
            "dqName": response_tenant_id["dqName"],
            "dgcName": dgc_community,
            "dgcUuid": response_tenant_id["dgcUuid"],
        }
        pl_tenant_mapping_json = json.dumps(pl_tenant_mapping)
        tenant_id_mapping = DGC_UPDATE_MAPPING_TENANT.format(tenantId=tenant_id)
        response = api_utils.patch(tenant_id_mapping, data=pl_tenant_mapping_json)
        assert response.status_code == 200, f"Couldn't map {dgc_community} on DGC"

    @staticmethod
    def dq_dgc_connection_create_dimension_mapping(api_utils):
        # Get DGC connection info
        dgc_connection_creds_response = api_utils.get(DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS)
        dgc_connection_cred_id = dgc_connection_creds_response[0]["id"]
        assert dgc_connection_cred_id is not None, "No DGC connection is available"

        # Get DQ dimensions
        dq_dimensions_response = api_utils.get(DGC_INTEGRATIONS_DQ_DIMENSIONS)
        assert len(dq_dimensions_response) > 0, "Couldn't retrieve DQ dimensions"

        # Get DGC dimensions
        dgc_dimensions_response = api_utils.get(DGC_INTEGRATIONS_DGC_DIMENSIONS)
        assert len(dgc_dimensions_response) > 0, "Couldn't retrieve DGC dimensions"
        dgc_dimensions_map = {item["name"]: item for item in dgc_dimensions_response}

        # Build DQ/DGC dimensions payload
        pl_dq_dgc_dimensions_mapping = DQ_DGC_DIMENSIONS_MAPPING_PAYLOAD

        for pl_dimensions_mapping in pl_dq_dgc_dimensions_mapping:
            dgc_dimension_name = pl_dimensions_mapping["dgcName"]
            pl_dimensions_mapping["credId"] = dgc_connection_cred_id
            pl_dimensions_mapping["dgcUuid"] = dgc_dimensions_map[dgc_dimension_name]["id"]
            # Create mapping
            pl_dimensions_mapping_json = json.dumps(pl_dimensions_mapping)
            response = api_utils.post(
                DGC_INTEGRATION_MAPPING, data=pl_dimensions_mapping_json, return_json=False
            )

            assert (
                response.status_code == 204
            ), f"Couldn't create DQ/DGC dimensions mapping for {pl_dimensions_mapping}"

        # Verify results
        dq_dgc_dimensions_url = DGC_INTEGRATIONS_DQ_DGC_DIMENSIONS_MAPPING.format(
            credentialId=dgc_connection_cred_id
        )
        dq_dgc_dimensions_response = api_utils.get(dq_dgc_dimensions_url)
        dgc_to_dq_dimensions_payload_map = {
            item["dgcName"]: item for item in DQ_DGC_DIMENSIONS_MAPPING_PAYLOAD
        }

        for dimension_item in dq_dgc_dimensions_response:
            dq_dimensions_name = dimension_item["dqName"]
            dgc_dimensions_name = dimension_item["dgcName"]
            dgc_to_dq_payload_item = dgc_to_dq_dimensions_payload_map[dgc_dimensions_name]

            assert (
                dq_dimensions_name == dgc_to_dq_payload_item["dqName"]
            ), "Expected DQ dimension name does not match actual"
            assert (
                dgc_dimensions_name == dgc_to_dq_payload_item["dgcName"]
            ), "Expected DGC dimension name does not match actual"
