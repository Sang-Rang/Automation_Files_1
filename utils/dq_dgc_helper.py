import json
import time
from dataclasses import dataclass

import pytest
from assertpy import assert_that

from endpoints.dgc_integration.dgc.assets_api import DGC_ASSETS
from endpoints.dgc_integration.dgc.attributes_api import DGC_ATTRIBUTES
from endpoints.dgc_integration.dgc.communities_api import DGC_COMMUNITIES
from endpoints.dgc_integration.dgc.domain_api import DGC_DOMAIN
from endpoints.dgc_integration.dgc.dq_service_api import DGC_DQ_SERVICE_HEALTH_CHECK
from endpoints.dgc_integration.dgc.quality_api import DGC_QUALITY
from endpoints.dgc_integration.dgc.relations_api import DGC_RELATIONS
from endpoints.dgc_integration.dq.integration_api import (
    DGC_INTEGRATIONS_INTEGRATION_JSON,
    PUT_DGC_INTEGRATIONS_STATUS,
    DGC_SUBMIT_INTEGRATIONS_JOB,
    DGC_GET_INTEGRATION_JOB_BY_ID,
)
from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT, V2_BUSINESS_UNIT_BY_NAME
from endpoints.v2.controller_business_unit_to_dataset import V2_BUSINESS_UNIT_TO_DS
from endpoints.dgc_integration.dq.dgc_connection_api import DGC_INTEGRATIONS_CONNECTIONS_MAPPING
from utils.api_utils import APIUtils
from utils.dq_dgc_connection_helper import DqDgcConnectionHelper, DqDgcDatabaseConnectionMappingInfo
from utils.dq_dgc_constants import (
    DGC_SERVICE_TYPE,
    DGC_BASE_URL,
    DGC_BASE_CREDS,
    DGC_AUTH_MODE,
    DQ_BUSINESS_UNIT,
)

dg_dgc_connection_helper = DqDgcConnectionHelper()


@dataclass
class ResourceTypeCount:
    domain_count: int = 0
    asset_count: int = 0


class DqDgcBaseHelper:
    DQ_RULE = "DQ Rule-"
    DQ_SCORE = "DQ Score-"

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="session")
    def dgc_api_utils(self, dgc_base_url, get_auth_headers_dgc):
        return APIUtils(base_url=dgc_base_url, headers=get_auth_headers_dgc)

    @staticmethod
    def create_business_unit_if_not_exists(api_utils, business_unit):
        params = {"name": business_unit}

        response = api_utils.get(V2_BUSINESS_UNIT_BY_NAME, params=params)

        if response.get("result", {}).get("name") == business_unit:
            return

        create_response = api_utils.post(V2_BUSINESS_UNIT, params=params)
        assert "result" in create_response, "Failed to create business unit"

    @staticmethod
    def add_dataset_to_business_unit(api_utils, business_unit_name, dataset):
        search_by_name_param = {"name": business_unit_name}

        search_response = api_utils.get(V2_BUSINESS_UNIT_BY_NAME, params=search_by_name_param)

        business_unit_id = search_response.get("result", {}).get("id")
        if not business_unit_id:
            raise ValueError(f"Business unit {business_unit_name} not found")

        create_params = {"business_unit_id": business_unit_id, "dataset": dataset}

        create_response = api_utils.post(V2_BUSINESS_UNIT_TO_DS, params=create_params)
        assert "result" in create_response, "Failed to add dataset to business unit"

    @staticmethod
    def get_resource_type_counts(api_utils, dgc_api_utils, dataset):
        params = {"dataset": dataset}
        resource_type_counts = ResourceTypeCount()

        is_dq_service_enabled = DqDgcBaseHelper.is_dq_service_enabled_on_dgc(dgc_api_utils)
        resources = None

        dgc_json = api_utils.get(DGC_INTEGRATIONS_INTEGRATION_JSON, params=params)
        if is_dq_service_enabled:
            resources = dgc_json.get("KnowledgeGraph", [])
        else:
            resources = dgc_json

        for resource in resources:
            if resource.get("resourceType") == "Domain":
                resource_type_counts.domain_count += 1
            elif resource.get("resourceType") == "Asset":
                resource_type_counts.asset_count += 1

        return resource_type_counts

    @staticmethod
    def get_asset_count_from_summary(summary_response):
        asset_added_count = 0

        for resource_type in summary_response.get("resourceTypes", []):
            if resource_type.get("resourceType") == "ASSET":
                asset_added_count = resource_type.get("counters", {}).get("added", 0)
                break

        return asset_added_count

    @staticmethod
    def is_dq_service_enabled_on_dgc(dgc_api_utils):
        response = dgc_api_utils.get(DGC_DQ_SERVICE_HEALTH_CHECK, return_json=False)
        is_enabled = response.text == "Healthy"
        return is_enabled

    @staticmethod
    def setup_dgc_credentials(api_utils):
        pl_dqc_connection_creds = {
            "serviceType": DGC_SERVICE_TYPE,
            "serviceUrl": DGC_BASE_URL,
            "authMode": DGC_AUTH_MODE,
            "username": DGC_BASE_CREDS["username"],
            "password": DGC_BASE_CREDS["password"],
        }
        dg_dgc_connection_helper.setup_dgc_credentials(api_utils, pl_dqc_connection_creds)

    def map_dq_dgc_connections(
        self, api_utils, database_schema_name, database_table_name, connection_name, connection_id
    ):
        # Build connection mapping payload
        connection_mappings_json_payload = self.build_connection_mapping_json_payload(
            api_utils, connection_name, connection_id, database_schema_name, database_table_name
        )

        # Map connections
        connection_mapping_response = api_utils.post(
            DGC_INTEGRATIONS_CONNECTIONS_MAPPING,
            data=connection_mappings_json_payload,
            return_json=False,
        )

        assert_that(
            connection_mapping_response.status_code, "Couldn't map DQ/DGC database connections"
        ).is_equal_to(201)

    @staticmethod
    def build_connection_mapping_json_payload(
        api_utils, connection_name, connection_id, database_schema_name, database_table_name
    ):
        dq_dgc_connection_mapping_info = DqDgcDatabaseConnectionMappingInfo(
            dq_connection_name=connection_name,
            dgc_database_id=connection_id,
            dgc_database_schema_name=database_schema_name,
            dgc_database_table_name=database_table_name,
        )

        connection_mappings = dg_dgc_connection_helper.build_dq_dgc_connection_mapping_pl(
            api_utils, dq_dgc_connection_mapping_info
        )

        return json.dumps(connection_mappings)

    @staticmethod
    def run_dgc_integration(api_utils, dataset_name):
        req_params = {"dataset": "string", "active": True}
        integration_response = api_utils.put(
            PUT_DGC_INTEGRATIONS_STATUS.format(dataset=dataset_name), json=json.dumps(req_params)
        )
        return integration_response

    @staticmethod
    def submit_dgc_job_and_check_status(
        api_utils, dataset_name, dataset_run_id, check_intervals=5, timeout=240
    ):
        # Submit a job
        integration_params = {"dataset": dataset_name, "runId": dataset_run_id}
        run_integration_response = api_utils.post(
            DGC_SUBMIT_INTEGRATIONS_JOB, json=integration_params, return_json=True
        )
        integration_job_id = run_integration_response["integrationJobId"]

        # Wait until job returns status FINISHED
        start_time = time.time()
        while True:
            try:
                response = api_utils.get(
                    DGC_GET_INTEGRATION_JOB_BY_ID.format(id=integration_job_id), return_json=True
                )

                if response["dqIntegrationJobStatus"] == "FINISHED":
                    return response
            except ValueError as exception:
                print(f"Response processing failed {exception}")

            if time.time() - start_time > timeout:
                raise TimeoutError(
                    "The status did not change to 'FINISH' withing the specified timeout."
                )

            time.sleep(check_intervals)

    def verify_imported_assets_count(
        self, api_utils, dataset_name, dgc_api_utils, integration_response
    ):
        exported_asset_counts = self.get_resource_type_counts(
            api_utils, dgc_api_utils, dataset_name
        ).asset_count

        imported_assets_count = self.get_asset_count_from_summary(integration_response)

        assert_that(
            exported_asset_counts, "Exported assets should be greater than 0"
        ).is_greater_than(0)

        assert_that(
            imported_assets_count, "Imported assets should be greater than 0"
        ).is_greater_than(0)

        assert_that(
            exported_asset_counts, "Imported / Exported asset counts do not match"
        ).is_equal_to(imported_assets_count)

    @staticmethod
    def verify_dq_job_import(dataset_name, dgc_api_utils, delay=5, timeout=120):
        assets_params = {"name": dataset_name}
        start_time = time.time()  # Record the start time
        while True:
            assets_response = dgc_api_utils.get(DGC_ASSETS, params=assets_params)
            # Check if the response contains results and the expected asset is available
            results = assets_response.get("results", [])
            if results:
                asset = results[0]
                assert_that(assets_response.get("total", 0), "No assets found").is_equal_to(1)
                assert_that(asset["domain"]["name"], "Asset domain is not 'DQ Job'").is_equal_to(
                    "DQ Job"
                )
                assert_that(
                    asset["type"]["name"], "Asset type is not 'Data Quality Job'"
                ).is_equal_to("Data Quality Job")
                return asset["id"]
            # Check if the timeout has been reached
            if time.time() - start_time > timeout:
                raise ValueError(f"Asset '{dataset_name}' not found within {timeout} seconds")
            # If asset is not found, wait for the specified delay before retrying
            time.sleep(delay)

    @staticmethod
    def verify_business_domain_import(dgc_api_utils):
        community_param = {"name": DQ_BUSINESS_UNIT}

        community_response = dgc_api_utils.get(DGC_COMMUNITIES, params=community_param)
        community = community_response["results"][0]

        assert_that(
            community_response.get("total", 0), "Business unit was not imported"
        ).is_equal_to(1)

        assert_that(
            community["parent"]["name"],
            f"{DQ_BUSINESS_UNIT} is not part of DQ Integration Community",
        ).is_equal_to("DQ_INTEGRATION_COMMUNITY")

    def verify_imported_rule_domain(self, dgc_api_utils, dataset_name, business_unit):
        rule_domain_param = {"name": f"{self.DQ_RULE}{dataset_name}"}

        rule_domain_response = dgc_api_utils.get(DGC_DOMAIN, params=rule_domain_param)
        rules = rule_domain_response["results"][0]

        (
            assert_that(
                rule_domain_response.get("total", 0), "No rule domain was found"
            ).is_equal_to(1)
        )

        (
            assert_that(
                rules["type"]["name"], "Rule domain should be of Rulebook type"
            ).is_equal_to("Rulebook")
        )

        assert_that(
            rules["community"]["name"], f"Rule domain is not part of {business_unit} business unit"
        ).is_equal_to(business_unit)

    def verify_imported_score_domain(self, dgc_api_utils, dataset_name, business_unit):
        score_domain_param = {"name": f"{self.DQ_SCORE}{dataset_name}"}

        score_domain_response = dgc_api_utils.get(DGC_DOMAIN, params=score_domain_param)

        scores = score_domain_response["results"][0]

        assert_that(score_domain_response.get("total", 0), "No score domain was found").is_equal_to(
            1
        )

        assert_that(scores["type"]["name"], "Score domain should be of Rulebook type").is_equal_to(
            "Rulebook"
        )

        assert_that(
            scores["community"]["name"],
            f"Score domain is not part of {business_unit} business unit",
        ).is_equal_to(business_unit)

    @staticmethod
    def find_source_by_name(json_data, name):
        results = json_data.get("results", [])
        for obj in results:
            if obj.get("source", {}).get("name") == name:
                return obj["source"]
        return None

    @staticmethod
    def find_value_by_type_name(json_data, type_name):
        results = json_data.get("results", [])
        for obj in results:
            if obj.get("type", {}).get("name") == type_name:
                return obj.get("value")
        return None

    # pylint: disable-msg=too-many-arguments
    def get_rule_details_for_selected_rule_and_validate_results(
        self,
        dgc_api_utils,
        rule_id,
        expected_loaded_rows,
        expected_rule_status,
        expected_passing_fraction,
        expected_rule_type,
        expected_rule_description=None,
    ):
        # Get rule details for the specified rule id
        asset = rule_id["id"]
        attributes_params = {"assetId": asset}
        attributes_response = dgc_api_utils.get(DGC_ATTRIBUTES, params=attributes_params)

        # Get the rule status information
        loaded_rows = self.find_value_by_type_name(attributes_response, "Loaded Rows")
        assert_that(loaded_rows, f"Loaded rows number is different, got {loaded_rows}").is_equal_to(
            expected_loaded_rows
        )

        rule_status = self.find_value_by_type_name(attributes_response, "Rule Status")
        assert_that(rule_status, "Unexpected rule status").is_equal_to(expected_rule_status)

        passing_fraction = self.find_value_by_type_name(attributes_response, "Passing Fraction")
        assert_that(passing_fraction, "Unexpected passing fraction").is_equal_to(
            expected_passing_fraction
        )

        rule_type = self.find_value_by_type_name(attributes_response, "Rule Type")
        assert_that(rule_type, "Unexpected rule type").is_equal_to(expected_rule_type)

        if expected_rule_description is not None:
            rule_description = self.find_value_by_type_name(attributes_response, "Description")
            assert_that(rule_description, "Unexpected rule description").is_equal_to(
                expected_rule_description
            )

    @staticmethod
    def get_data_governs_column_details(dgc_api_utils, rule_id):
        params = {"relationTypeId": "00000000-0000-0000-0000-090000010022", "sourceId": rule_id}
        governs_response = dgc_api_utils.get(DGC_RELATIONS, params=params)

        return governs_response

    def get_attributes_details_and_validate_results(
        self,
        dgc_api_utils,
        asset_id,
        exp_global_score,
        exp_job_row_filter,
        exp_predicate,
        exp_last_run_status,
        exp_last_job_run=None,
        exp_description=None,
    ):
        """Get the results from job Overview page in DGC."""
        # Get rule details for the specified rule id
        # asset = asset_id["id"]
        attributes_params = {"assetId": asset_id}
        attributes_response = dgc_api_utils.get(DGC_ATTRIBUTES, params=attributes_params)

        # Validate Overview tab information for asset
        global_score = self.find_value_by_type_name(attributes_response, "Global Score")
        assert_that(
            global_score, f"Global score number is different, got {global_score}"
        ).is_equal_to(exp_global_score)

        job_row_filter = self.find_value_by_type_name(attributes_response, "Job Row Filter")
        assert_that(
            job_row_filter, f"Job Row Filter number is different, got {job_row_filter}"
        ).is_equal_to(exp_job_row_filter)

        predicate_out = self.find_value_by_type_name(attributes_response, "Predicate")
        assert_that(
            predicate_out, f"Predicate number is different, got {predicate_out}"
        ).is_equal_to(exp_predicate)

        last_run_status = self.find_value_by_type_name(attributes_response, "Last Run Status")
        assert_that(
            last_run_status, f"Last Run Status is different, got {last_run_status}"
        ).is_equal_to(exp_last_run_status)

        if exp_last_job_run is not None:
            last_job_run = self.find_value_by_type_name(attributes_response, "Last Job Run")
            assert_that(
                last_job_run, f"Last Job Run Status is different, got {last_job_run}"
            ).is_equal_to(exp_last_job_run)

        if exp_description is not None:
            description = self.find_value_by_type_name(attributes_response, "Description")
            assert_that(description, "Unexpected asset description").is_equal_to(exp_description)

    @staticmethod
    def get_quality_tab_information(dgc_api_utils, asset_id):
        """Get a quality tab info for specified asset_id."""
        attributes_params = {"assetId": asset_id}
        quality_tab_response = dgc_api_utils.get(DGC_QUALITY, params=attributes_params)
        return quality_tab_response

    @staticmethod
    def get_governs_column_info_for_rule_id(dgc_api_utils, rule_id):
        """Get relations information for governs Columns of the specified rule_id."""
        governs_column_relation_id = "00000000-0000-0000-0000-090000010022"
        asset = rule_id["id"]

        relation_params = {"relationTypeId": governs_column_relation_id, "sourceId": asset}
        governs_response = dgc_api_utils.get(DGC_RELATIONS, params=relation_params)
        return governs_response
