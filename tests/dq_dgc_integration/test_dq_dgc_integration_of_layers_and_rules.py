import time
import allure
import pytest
from assertpy import assert_that

from endpoints.dgc_integration.dgc.quality_api import DGC_QUALITY
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from endpoints.dgc_integration.dq.layers_api import DQ_DGC_LAYERS_INTEGRATION
from payloads.dq_dgc_integration.pl_dq_dgc_layers_and_rules_mapping import (
    POSTGRES_SCHEMA_NAME,
    POSTGRES_TABLE_NAME,
    DS_DEF_DGC_LAYERS_RULES_INTEGRATION,
    DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
    DS_DEF_DGC_LAYERS_RULES_INTEGRATION_BASIC,
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


@pytest.mark.dq_dgc
class TestDqDgcLayersRulesMapping:

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
    def get_layer_id(layers, target_layer):
        for layer in layers:
            if layer["layer"] == target_layer:
                return layer["id"]
        return None  # Return None if the target_layer is not found

    @staticmethod
    def set_layers_status(api_utils, asset_id, is_active):
        layer_params = {"id": asset_id, "active": is_active}
        layers_status_response = api_utils.patch(
            DQ_DGC_LAYERS_INTEGRATION, json=layer_params, return_json=False
        )
        assert_that(
            layers_status_response.status_code,
            f"Layer creation failed, expected code 204, but got {layers_status_response}",
        ).is_equal_to(204)
        return layers_status_response

    @staticmethod
    def get_updated_quality_information(dgc_api_utils, asset_id):
        # Define the timeout and interval for retries
        timeout = 120  # Maximum time to wait in seconds
        interval = 5  # Time between retries in seconds

        start_time = time.time()

        while True:
            # Fetch the response from the API
            attributes_params = {"assetId": asset_id}
            quality_tab_response = dgc_api_utils.get(DGC_QUALITY, params=attributes_params)

            # Check if the response meets the expected condition
            if quality_tab_response["score"] == 37:
                return quality_tab_response

            # Check if timeout has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise AssertionError(
                    f"Timeout reached. "
                    f"Expected score to be 37 but got {quality_tab_response['total']}"
                )

            # Wait before retrying
            time.sleep(interval)

    @staticmethod
    def assert_layer_active(layers_mapping, layer_name, expected_status):
        for layer in layers_mapping:
            if layer["layer"] == layer_name:
                assert layer["active"] == expected_status, (
                    f"Assertion failed: Layer {layer_name} expected status to be "
                    f"{expected_status}, but found {layer['active']}"
                )
                return
        raise ValueError(f"Layer '{layer_name}' not found in the mapping.")

    @allure.feature("DQ DGC Integration")
    @allure.story("Basic DGC integration")
    @pytest.mark.usefixtures("setup_dq_dgc_integration")
    def test_dq_dgc_layers_and_rules_mapping_integration(self, api_utils, dgc_api_utils):
        """INTEGRATION - Verify Layers/Rules in mapping, ref: DEV-97564."""
        dataset_run_id = DS_DEF_DGC_LAYERS_RULES_INTEGRATION_BASIC["runId"]

        # Run a job
        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_LAYERS_RULES_INTEGRATION_BASIC)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Run dgc integration
        dq_dgc_helper.run_dgc_integration(api_utils, DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME)
        dq_dgc_helper.submit_dgc_job_and_check_status(
            api_utils, DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME, dataset_run_id
        )

        # Verify import of DQ Job
        asset_id = dq_dgc_helper.verify_dq_job_import(
            DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME, dgc_api_utils
        )

        # Get Quality Tab details for DQ job with 0 findings
        response = dq_dgc_helper.get_quality_tab_information(dgc_api_utils, asset_id)
        assert_that(
            response["score"],
            f"Invalid quality score returned, "
            f"expected 100.0, but got {response['score']}",
        ).is_equal_to(100.0)

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Get a custom rule id, and check rules result before layers update
        source_outlier_rule = dq_dgc_helper.find_source_by_name(
            relations_response, "Outlier Finding"
        )
        source_shape_rule = dq_dgc_helper.find_source_by_name(relations_response, "Shape Finding")
        source_dupes_rule = dq_dgc_helper.find_source_by_name(
            relations_response, "Duplicate Finding"
        )

        expected_table_row_count = 102815.0
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_outlier_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Suppressed"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Outlier"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_shape_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Suppressed"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Shape"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_dupes_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Suppressed"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Duplicate"],
        )

        # Get current layers details
        layers_response = api_utils.get(DQ_DGC_LAYERS_INTEGRATION)
        self.assert_layer_active(layers_response, "DUPES", True)
        self.assert_layer_active(layers_response, "DUPES_BREAKS", False)
        self.assert_layer_active(layers_response, "OUTLIERS", True)
        self.assert_layer_active(layers_response, "OUTLIERS_BREAKS", False)
        self.assert_layer_active(layers_response, "SHAPES", True)
        self.assert_layer_active(layers_response, "SHAPES_BREAKS", False)

        # Get layer ID by name
        outliers_id = self.get_layer_id(layers_response, "OUTLIERS")
        dupes_id = self.get_layer_id(layers_response, "DUPES")
        dupes_breaks_id = self.get_layer_id(layers_response, "DUPES_BREAKS")
        shapes_id = self.get_layer_id(layers_response, "SHAPES")

        # Update default layers
        self.set_layers_status(api_utils, outliers_id, "False")
        self.set_layers_status(api_utils, dupes_id, "True")
        self.set_layers_status(api_utils, dupes_breaks_id, "True")
        self.set_layers_status(api_utils, shapes_id, "False")

        # Verify updated layers response
        updated_layers_response = api_utils.get(DQ_DGC_LAYERS_INTEGRATION)
        self.assert_layer_active(updated_layers_response, "DUPES", True)
        self.assert_layer_active(updated_layers_response, "DUPES_BREAKS", True)
        self.assert_layer_active(updated_layers_response, "OUTLIERS", False)
        self.assert_layer_active(updated_layers_response, "OUTLIERS_BREAKS", False)
        self.assert_layer_active(updated_layers_response, "SHAPES", False)
        self.assert_layer_active(updated_layers_response, "SHAPES_BREAKS", False)

        job_result = helper.setup_dataset(api_utils, DS_DEF_DGC_LAYERS_RULES_INTEGRATION)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Get Quality Tab details for DQ job with outliers, dupes, and shapes findings
        response = self.get_updated_quality_information(dgc_api_utils, asset_id)
        assert_that(
            response["score"],
            f"Invalid quality score returned, "
            f"expected 37.0, but got {response['score']}",
        ).is_equal_to(37.0)

        # Get relations information (all rules information)
        assets_params = {"targetId": asset_id}
        relations_response = dgc_api_utils.get(DGC_RELATIONS, params=assets_params)

        # Check rules result after the second run
        source_outlier_rule = dq_dgc_helper.find_source_by_name(
            relations_response, "Outlier Finding"
        )
        source_shape_rule = dq_dgc_helper.find_source_by_name(relations_response, "Shape Finding")
        source_dupes_rule = dq_dgc_helper.find_source_by_name(
            relations_response, "Duplicate Finding"
        )

        expected_table_row_count = 102815.0
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_outlier_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Suppressed"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Outlier"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_shape_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Suppressed"],
            expected_passing_fraction=100.0,
            expected_rule_type=["Shape"],
        )
        dq_dgc_helper.get_rule_details_for_selected_rule_and_validate_results(
            dgc_api_utils,
            rule_id=source_dupes_rule,
            expected_loaded_rows=expected_table_row_count,
            expected_rule_status=["Breaking"],
            expected_passing_fraction=70.0,
            expected_rule_type=["Duplicate"],
        )
