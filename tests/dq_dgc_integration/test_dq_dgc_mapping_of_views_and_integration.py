import copy
import json

import allure
import pytest
from assertpy import assert_that

from data_test.dq_dgc_integration.data_mapping_of_views import (
    MAPPING_OF_SCHEMAS_AFTER_ADDING_VIEWS,
    MAPPING_OF_SCHEMAS_BEFORE_ADDING_VIEWS,
    SAMPLES_VIEW_SCHEMA,
)
from endpoints.dgc_integration.dq.mappings_api import (
    DGC_INTEGRATION_CONNECTION_MAPPING_FOR_CREDENTIAL,
    DGC_INTEGRATION_CONNECTION_MAPPINGS,
    DGC_INTEGRATION_MAPPING_CONNECTION,
)
from payloads.dq_dgc_integration.pl_dq_dgc_mapping_of_views import (
    DS_DEF_DGC_MAPPING_OF_VIEWS,
    DS_DEF_DGC_MAPPING_OF_VIEWS_NAME,
)
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper
from utils.dq_dgc_constants import (
    DGC_DQ_INTEGRATION_COMMUNITY,
    DQ_POSTGRES_CONNECTION_NAME,
    DGC_DATABASE_UUID,
    DQ_BUSINESS_UNIT,
)
from utils.dq_dgc_helper import DqDgcBaseHelper
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal


helper = BaseHelper()
dq_dgc_helper = DqDgcBaseHelper()
dg_dgc_connection_helper = DqDgcConnectionHelper()

POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"


@pytest.mark.dq_dgc
class TestDqDgcMappingOfViews:

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

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    @pytest.mark.flaky(retries=5, delay=5)
    def test_dq_dgc_mapping_of_views_and_integration(self, api_utils, dgc_api_utils):
        """INTEGRATION - Verify Mapping of views, Integration for views and Quality tab,
        ref: DEV-83967"""
        # Get credential ID for the connection
        credential_id = dg_dgc_connection_helper.get_dgc_connections_credentials(api_utils)

        # Get all connection mappings for specified DGC credential ID without schema mappings
        connection_mappings_response = api_utils.get(
            DGC_INTEGRATION_CONNECTION_MAPPING_FOR_CREDENTIAL.format(credentialId=credential_id)
        )
        mapping_id = connection_mappings_response[0]["id"]

        # Get connection mappings
        mapping_params = {"nested": True}
        mappings_response_before = api_utils.get(
            DGC_INTEGRATION_CONNECTION_MAPPINGS.format(connectionId=mapping_id),
            params=mapping_params,
        )

        # Validate mappings before adding mapping of views
        exclude_dynamic_keys = ["id", "credentialId"]
        compare_dicts_are_equal(
            mappings_response_before,
            MAPPING_OF_SCHEMAS_BEFORE_ADDING_VIEWS,
            exclude_dynamic_keys,
            ignore_order=True
        )

        updated_schema_views = copy.deepcopy(SAMPLES_VIEW_SCHEMA)
        updated_schema_views["credentialId"] = credential_id

        # Create mapping connection for views and extract id from response
        pl_schema_mapping_json = json.dumps(updated_schema_views)
        response = api_utils.post(DGC_INTEGRATION_MAPPING_CONNECTION, data=pl_schema_mapping_json)

        # Get connection mappings
        mapping_params = {"nested": True}
        mappings_response_after = api_utils.get(
            DGC_INTEGRATION_CONNECTION_MAPPINGS.format(connectionId=response["id"]),
            params=mapping_params,
        )

        # Validate mappings after adding mapping of views
        exclude_dynamic_keys = ["id", "credentialId"]
        compare_dicts_are_equal(
            mappings_response_after, MAPPING_OF_SCHEMAS_AFTER_ADDING_VIEWS, exclude_dynamic_keys
        )

        # Run a basic job with sales_view_table
        dataset_run_id = DS_DEF_DGC_MAPPING_OF_VIEWS["runId"]
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_MAPPING_OF_VIEWS)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Create business unit and associate the given dataset with it
        dq_dgc_helper.create_business_unit_if_not_exists(api_utils, DQ_BUSINESS_UNIT)
        dq_dgc_helper.add_dataset_to_business_unit(
            api_utils, DQ_BUSINESS_UNIT, DS_DEF_DGC_MAPPING_OF_VIEWS_NAME
        )

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_MAPPING_OF_VIEWS_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_MAPPING_OF_VIEWS_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            "AUTO_DQ_DGC_MAPPING_OF_VIEWS_20241120173534", dgc_api_utils
        )

        # Get Quality Tab details for DQ job
        response = dq_dgc_helper.get_quality_tab_information(dgc_api_utils, asset_id)
        assert_that(
            response["asset"]["type"]["name"],
            f"Invalid asset type name returned, "
            f"expected 'Data Quality Job', but got {response['asset']['type']['name']}",
        ).is_equal_to("Data Quality Job")
        assert_that(
            response["score"],
            f"Invalid quality score returned, " f"expected 100.0, but got {response['score']}",
        ).is_equal_to(100.0)

        # Verify import of business domain as community
        dq_dgc_helper.verify_business_domain_import(dgc_api_utils)

        # Verify import of rule domain
        dq_dgc_helper.verify_imported_rule_domain(
            dgc_api_utils, DS_DEF_DGC_MAPPING_OF_VIEWS_NAME, DQ_BUSINESS_UNIT
        )

        # Verify import of score domain
        dq_dgc_helper.verify_imported_score_domain(
            dgc_api_utils, DS_DEF_DGC_MAPPING_OF_VIEWS_NAME, DQ_BUSINESS_UNIT
        )
