from datetime import datetime

import allure
import pytest
from assertpy import assert_that

from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT
from endpoints.v2.controller_business_unit_to_dataset import (
    V2_BUSINESS_UNIT_TO_DS_BULK_UPDATE,
    V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET,
    V2_BUSINESS_UNIT_TO_DS,
)
from endpoints.v2.controller_catalog import (
    V2_DELETE_DATASET_LIST,
    V2_GET_DATA_ASSETS_WITH_FILTERS,
    V2_UPDATE_CATALOG_DATA_CATEGORY,
    V2_GET_CATALOG_BY_DATASET,
    V2_UPDATE_SCHEMA_COL_METADATA,
    V2_CATALOG_COLUMN_BULK_UPDATE_DATA_CLASS,
    V2_CATALOG_COLUMN_BULK_UPDATE_RULES,
    V2_CATALOG_COLUMN_BULK_UPDATE_SENSITIVE_LABEL,
    V2_GET_COLUMN_ASSETS_ARR_FOR_SERVER_SIDE_WITH_MULTIFILTERS,
)
from endpoints.v2.controller_data_concept import V2_DATA_CATEGORY_BULK_UPDATE, V2_DATA_CATEGORY
from endpoints.v2.controller_catalog import V2_GET_CATALOG_AND_CONN_SRC_NAME_BY_DATASET
from endpoints.v2.controller_dataset import V2_RENAME_DATASET
from endpoints.v2.controller_hoot import V2_GET_TABLE_STATS
from endpoints.v2.controller_rule import V2_GET_RULE_REPO_WITH_METADATA_LABEL, V2_DATA_CLASS
from endpoints.v2.controller_sensitive_label import V2_SENSITIVE_LABEL
from endpoints.v3.rule_api import V3_RULES
from payloads.pullup.pl_catalog_datasets import (
    DATASET_RENAME,
    PL_FILTER_DS,
    PL_FILTER_COL,
    PL_FILTER_SOURCE_COUNTS,
    DS_BULK_1,
    DS_BULK_2,
    CONNECTION,
    QUERY,
    PL_FILTER_BULK_DELETE1,
    PL_FILTER_BULK_DELETE2,
    PL_UPDATE_METADATA,
    PL_FILTER_MULTI,
    FIELD2_DC_SL,
    FIELD1_DC_SL,
    PL_DC_SL,
    PL_DC_SEARCH,
)
from data_test.analyze_estimate_filtergram_file_types.data_aef_oracle_up import (
    C_NAME_CON_ORACLE,
    DS_CON_ORACLE,
    QUERY_CON_ORACLE,
    WHERE_DATE_CON_ORACLE,
)
from data_test.pullup.data_missing_endpoints_coverage import (
    SNOWFLAKE_CATALOG_OUTPUT,
    ORACLE_CATALOG_OUTPUT,
    S3_CATALOG_OUTPUT,
)
from data_test.analyze_estimate_filtergram_file_types.data_aef_s3 import DS_DEFS
from data_test.analyze_estimate_filtergram_file_types.data_aef_snowflake_up import (
    DS_DEFS_FULL_PROFILE,
    WHERE_DATE,
)
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal

helper = BaseHelper()


@pytest.mark.pullup
class TestCatalogDatasets:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def delete_all_business_units_on_dataset(api_utils, ds_name):
        """Delete any existing business units found on a dataset"""
        found_business_units = api_utils.get(
            V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET, params={"dataset": ds_name}
        )

        # If none, returns an empty "result" object
        if len(found_business_units["result"]) > 0:
            for item in found_business_units["result"]:
                api_utils.delete(V2_BUSINESS_UNIT_TO_DS, params={"id": item["id"]})

            recheck_business_units = api_utils.get(
                V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET, params={"dataset": ds_name}
            )
            assert_that(
                len(recheck_business_units["result"]), "Failed to delete all business units"
            ).is_equal_to(0)

    @staticmethod
    def get_or_create_buisness_unit(api_utils):
        """Get any business unit, or create a business unit if none are found"""
        get_all_business_units = api_utils.get(V2_BUSINESS_UNIT)
        pl_bu = {"name": "Auto_Business_Unit", "subId": ""}

        if len(get_all_business_units["result"]) > 0:
            bu_id = get_all_business_units["result"][0]["id"]
        else:
            # Create business unit
            new_bu = api_utils.post(V2_BUSINESS_UNIT, params=pl_bu, return_json=False)
            assert_that(new_bu.status_code, "Creating new business unit failed").is_equal_to(200)

            # Get the newly created BU
            get_new_bu = api_utils.get(V2_BUSINESS_UNIT + "/", return_json=False)
            assert_that(get_new_bu.status_code, "Getting business unit failed").is_equal_to(200)

            bu_id = get_new_bu.json()["result"][0]["id"]

        # Sanity check the business unit found and valid
        assert_that(bu_id, "Business unit was not set correctly.").is_greater_than(0)

        return bu_id

    @staticmethod
    def find_fields_in_column_assets_filter(api_utils, payload, field1, field2):
        """Search and return two fields from the column assets after multifilter call"""
        found_field_1 = -1
        found_field_2 = -1

        # Grab all the column data
        resp_search = api_utils.get(
            V2_GET_COLUMN_ASSETS_ARR_FOR_SERVER_SIDE_WITH_MULTIFILTERS, params=payload
        )
        asset_list = resp_search["dataAssetList"]
        assert_that(len(asset_list), f"No assets found in search {PL_DC_SEARCH}").is_greater_than(0)

        # Search for the updated fields and corresponding data
        for item in asset_list:
            if item["fieldNm"] == field1:
                found_field_1 = item
            elif item["fieldNm"] == field2:
                found_field_2 = item
            if found_field_1 != -1 and found_field_2 != -1:
                break

        # Validate the fields were found (sanity)
        assert_that(
            found_field_1, f"Field {FIELD1_DC_SL} not found in {asset_list} for {payload}"
        ).is_not_equal_to(-1)
        assert_that(
            found_field_2, f"Field {FIELD2_DC_SL} not found in {asset_list} for {payload}"
        ).is_not_equal_to(-1)
        return [found_field_1, found_field_2]

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    @pytest.mark.smoke
    def test_dataset_mgr_rename_filter_delete_dataset(self, api_utils):
        """Test Dataset Manager - Rename, Filter, Delete Dataset"""
        ds_name_edit = f"{DATASET_RENAME}_edited"
        pl_patch = {"sourceDataset": DATASET_RENAME, "targetDataset": ds_name_edit}

        # Create the dataset
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DATASET_RENAME, QUERY)
        helper.setup_dataset(api_utils, ds_defs, PROD_RUN_ID)
        ds_stats = api_utils.get(
            V2_GET_TABLE_STATS, params={"dataset": DATASET_RENAME, "runId": PROD_RUN_ID, "sense": 3}
        )
        assert_that(ds_stats["rows"], "Issue with job, no rows found").is_greater_than(0)
        assert_that(ds_stats["score"], "Score").is_greater_than(98)

        # Get the dataset via filter
        filter_ds = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_DS)
        filter_ds_asset = filter_ds["dataAssetList"][0]
        assert_that(filter_ds_asset, "No data found with dataset filter, search #1").is_not_empty()

        # Filter for a column and dataset
        filter_col = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_COL)
        assert_that(filter_col["recordsFiltered"], f"Column filter: {PL_FILTER_COL}").is_equal_to(1)

        # Filter with additional options
        filter_source_counts = api_utils.get(
            V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_SOURCE_COUNTS
        )
        assert_that(
            filter_source_counts["recordsFiltered"],
            f"Filter source counts with {PL_FILTER_SOURCE_COUNTS}",
        ).is_equal_to(1)

        # Update the data table name
        resp_rename = api_utils.patch(V2_RENAME_DATASET, params=pl_patch, return_json=False)
        assert_that(resp_rename.status_code, "Rename call failed").is_equal_to(200)

        # Get the column data via search query again
        filter_ds2 = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_DS)
        assert_that(filter_ds2, "No data found with dataset filter, search #2").is_not_empty()
        filter_ds2_asset = filter_ds2["dataAssetList"][0]

        # Validate the dataset name has been updated
        assert_that(filter_ds2_asset["dataset"], "Rename failed").is_equal_to(ds_name_edit)

        # Delete the dataset
        api_utils.post(V2_DELETE_DATASET_LIST, params={"datasets": ds_name_edit})

        # Search to confirm deleted
        filter_deleted = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_DS)
        assert_that(len(filter_deleted["dataAssetList"]), "Delete DS failed.").is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_bulk_action_delete(self, api_utils):
        """Test - Dataset Manager Bulk Action Delete"""
        # Create two jobs.
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        ds1_name = f"AUTO_BULK_DELETE1_{now}"
        ds2_name = f"AUTO_BULK_DELETE2_{now}"

        ds_defs1 = helper.get_minimum_job_payload(api_utils, CONNECTION, ds1_name, QUERY)
        ds_defs2 = helper.get_minimum_job_payload(api_utils, CONNECTION, ds2_name, QUERY)

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs1, PROD_RUN_ID)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs2, PROD_RUN_ID)

        # Bulk delete both jobs
        api_utils.post(V2_DELETE_DATASET_LIST, params={"datasets": [ds1_name, ds2_name]})

        # Search to confirm deleted
        search1 = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_BULK_DELETE1)
        search2 = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_FILTER_BULK_DELETE2)
        assert_that(len(search1["dataAssetList"]), "Bulk Delete Dataset #1 failed").is_equal_to(0)
        assert_that(len(search2["dataAssetList"]), "Bulk Delete Dataset #2 failed").is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_bulk_actions_update_business_units(self, api_utils):
        """Test Dataset Manager - Bulk Actions Update Business Units"""
        bu_id = str(self.get_or_create_buisness_unit(api_utils))

        # Create payload for updating business units on datasets
        pl_update_bu = {"business_unit_id": bu_id, "datasets": [DS_BULK_1, DS_BULK_2]}

        # Create two jobs
        ds_defs1 = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_1, QUERY)
        ds_defs2 = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_2, QUERY)

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs1, PROD_RUN_ID)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs2, PROD_RUN_ID)

        # If the dataset already existed, remove any business units from the dataset
        self.delete_all_business_units_on_dataset(api_utils, DS_BULK_1)
        self.delete_all_business_units_on_dataset(api_utils, DS_BULK_2)

        # Update Business Units on jobs
        add_bu = api_utils.post(
            V2_BUSINESS_UNIT_TO_DS_BULK_UPDATE, params=pl_update_bu, return_json=False
        )
        assert_that(add_bu.status_code, "Failed to update business units").is_equal_to(200)

        # Get to confirm business unit was updated
        found_bu_job1 = api_utils.get(
            V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET, params={"dataset": DS_BULK_1}
        )
        found_bu_job2 = api_utils.get(
            V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET, params={"dataset": DS_BULK_2}
        )

        bu_id_job1 = str(found_bu_job1["result"][0]["businessUnitId"])
        bu_id_job2 = str(found_bu_job2["result"][0]["businessUnitId"])

        assert_that(bu_id_job1, "Business unit on dataset #1 failed to update").is_equal_to(bu_id)
        assert_that(bu_id_job2, "Business unit on dataset #2 failed to update").is_equal_to(bu_id)

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_single_action_update_business_units(self, api_utils):
        """Test Dataset Manager - Update Single Business Unit on Dataset"""

        bu_id = str(self.get_or_create_buisness_unit(api_utils))
        pl_update_bu = {"business_unit_id": bu_id, "dataset": DS_BULK_1}

        # Run job if necessary, otherwise cleanup existing business units
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_1, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)
        self.delete_all_business_units_on_dataset(api_utils, DS_BULK_1)

        # Update Business Units on job
        add_bu = api_utils.post(V2_BUSINESS_UNIT_TO_DS, params=pl_update_bu, return_json=False)
        assert_that(add_bu.status_code, "Failed to update single business unit").is_equal_to(200)

        # Get to confirm business unit was updated
        found_bu = api_utils.get(
            V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET, params={"dataset": DS_BULK_1}
        )
        assert_that(len(found_bu["result"]), "Business unit failed to update").is_equal_to(1)

        found_bu_id = str(found_bu["result"][0]["businessUnitId"])
        assert_that(found_bu_id, "Business unit had incorrect ID").is_equal_to(bu_id)

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_bulk_actions_update_dataset_categories(self, api_utils):
        """Test Dataset Manager - Bulk Update Dataset Categories"""
        # Note: DQ comes with 'out of the box' categories which are negative IDs.

        # Create two jobs
        ds_defs1 = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_1, QUERY)
        ds_defs2 = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_2, QUERY)

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs1, PROD_RUN_ID)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs2, PROD_RUN_ID)

        # Get any data category
        resp_data_categories = api_utils.get(V2_DATA_CATEGORY)
        data_categories = resp_data_categories["result"][0]

        # A dataset can only have 1 category. Remove any that exist by updating to nothing.
        api_utils.post(V2_UPDATE_CATALOG_DATA_CATEGORY, {"dataset": DS_BULK_1, "conceptId": None})
        api_utils.post(V2_UPDATE_CATALOG_DATA_CATEGORY, {"dataset": DS_BULK_2, "conceptId": None})
        ds1_catalog_setup = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_1})
        ds2_catalog_setup = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_2})
        assert_that(ds1_catalog_setup["dataConceptId"], "DS1-Remove business unit failed").is_none()
        assert_that(ds2_catalog_setup["dataConceptId"], "DS2-Remove business unit failed").is_none()

        pl_bulk_update = {
            "datasets": [DS_BULK_1, DS_BULK_2],
            "id": data_categories["dataConceptId"],
        }

        expected_resp_bulk_update = {
            "id": data_categories["dataConceptId"],
            "result": [DS_BULK_1, DS_BULK_2],
        }

        # Bulk update both jobs to the given category
        resp_bulk_update = api_utils.post(V2_DATA_CATEGORY_BULK_UPDATE, params=pl_bulk_update)
        assert_that(resp_bulk_update, "Failed to bulk update data category").is_equal_to(
            expected_resp_bulk_update
        )

        # Validate changes
        ds1_catalog = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_1})
        ds2_catalog = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_2})
        assert_that(ds1_catalog["dataConceptId"], "DS1-Invalid data category ID").is_equal_to(
            data_categories["dataConceptId"]
        )
        assert_that(ds2_catalog["dataConceptId"], "DS2-Invalid data category ID").is_equal_to(
            data_categories["dataConceptId"]
        )

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_single_action_update_dataset_category(self, api_utils):
        """Test Dataset Manager - Update Single Dataset Category"""
        # Note: DQ comes with 'out of the box' categories which are negative IDs.

        # Create a job if needed.
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_1, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        # Get any data category
        resp_data_categories = api_utils.get(V2_DATA_CATEGORY)

        # Even in a new environment, there should be many out of the box data categories.
        # Validate a known minimum exist, but not exact as more could be added in the future.
        assert_that(
            len(resp_data_categories["result"]),
            "Expected at least 10 options in data categories out of the box.",
        ).is_greater_than(10)

        # Get any data category to use
        data_category = resp_data_categories["result"][0]

        # A dataset can only have 1 data category. Remove any that exist by updating to nothing.
        api_utils.post(V2_UPDATE_CATALOG_DATA_CATEGORY, {"dataset": DS_BULK_1, "conceptId": None})
        ds_catalog_setup = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_1})
        assert_that(ds_catalog_setup["dataConceptId"], "Failed to remove data category").is_none()

        pl_update_dc = {"dataset": DS_BULK_1, "conceptId": data_category["dataConceptId"]}

        # Update job to the given data category
        resp_bulk_update = api_utils.post(V2_UPDATE_CATALOG_DATA_CATEGORY, params=pl_update_dc)
        assert_that(resp_bulk_update["msg"], "Update data category failed").is_equal_to("success")

        # Validate changes
        ds_catalog = api_utils.get(V2_GET_CATALOG_BY_DATASET, {"dataset": DS_BULK_1})
        assert_that(ds_catalog["dataConceptId"], "Invalid data category id").is_equal_to(
            data_category["dataConceptId"]
        )

    @allure.feature("Pullup")
    @allure.story("Catalog - Dataset Manager")
    def test_dataset_mgr_filter_options(self, api_utils):
        """Test Dataset Manager - Filter For All Predictable Options"""
        # Note: Sensitive Labels & Data Classes come out of box, so will exist in fresh environment

        # Create a job
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_1, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        # Add dataclass and sensitive labels
        resp_metadata = api_utils.post(
            V2_UPDATE_SCHEMA_COL_METADATA, PL_UPDATE_METADATA, return_json=False
        )
        assert_that(resp_metadata.status_code, "Update metadata failed").is_equal_to(200)

        # Add Business Unit
        self.delete_all_business_units_on_dataset(api_utils, DS_BULK_1)
        bu_id = str(self.get_or_create_buisness_unit(api_utils))
        pl_update_bu = {"business_unit_id": bu_id, "dataset": DS_BULK_1}
        PL_FILTER_MULTI["filterBusinessUnits"] = bu_id
        add_bu = api_utils.post(V2_BUSINESS_UNIT_TO_DS, params=pl_update_bu, return_json=False)
        assert_that(add_bu.status_code, "Failed to update single business unit").is_equal_to(200)

        # Add Data Category
        resp_data_categories = api_utils.get(V2_DATA_CATEGORY)
        data_category = resp_data_categories["result"][0]
        pl_update_dc = {"dataset": DS_BULK_1, "conceptId": data_category["dataConceptId"]}
        PL_FILTER_MULTI["filterDataConcepts"] = data_category["dataConceptId"]
        resp_bulk_update = api_utils.post(V2_UPDATE_CATALOG_DATA_CATEGORY, params=pl_update_dc)
        assert_that(resp_bulk_update["msg"], "Update data category failed").is_equal_to("success")

        # Run filter and validate
        filtered_data = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, PL_FILTER_MULTI)
        assert_that(
            filtered_data["recordsTotal"], f"Filter query returned no data: {PL_FILTER_MULTI}"
        ).is_greater_than(0)
        assert_that(
            filtered_data["dataAssetList"], "Expected dataset missing in filter results"
        ).extracting("dataset").contains(DS_BULK_1)

    @allure.feature("Pullup")
    @allure.story("Catalog - Column Manager")
    def test_column_mgr_bulk_update_data_class(self, api_utils):
        """Test Column Manager - Bulk Update Data Class"""

        # Notes:
        #   Data Classes come out of the box and will exist in fresh environments
        #   Data Classes are unique. A dataset can only have 1.
        #   Data class cannot be removed, so the class must be changed twice to validate it changes
        #       The 2nd option is running a unique job, but this is faster.

        # Get all data classes and grab the first two.
        data_class = api_utils.get(V2_DATA_CLASS)
        assert_that(len(data_class), "No data classes found").is_greater_than(0)

        data_class_1 = {"name": data_class[0]["ruleName"], "id": data_class[0]["ruleRepoId"]}
        data_class_2 = {"name": data_class[1]["ruleName"], "id": data_class[1]["ruleRepoId"]}

        # Run a job if needed
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_2, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        # Apply the data class via bulk update to two columns twice,
        # to ensure it can be changed on repeat runs
        for data_class in [data_class_1, data_class_2]:
            # Update the data class on the columns
            PL_DC_SL["idToUpdate"] = data_class["id"]
            resp_bulk_update = api_utils.post(
                V2_CATALOG_COLUMN_BULK_UPDATE_DATA_CLASS, json=PL_DC_SL, return_json=False
            )
            assert_that(
                resp_bulk_update.status_code, f"Data class bulk update failed with {PL_DC_SL}"
            ).is_equal_to(200)

            # Find the fields within the filters
            found_fields = self.find_fields_in_column_assets_filter(
                api_utils, PL_DC_SEARCH, FIELD1_DC_SL, FIELD2_DC_SL
            )

            # Validate the data is correct
            assert_that(
                found_fields[0]["colSemantic"], f"Data class name incorrect for {data_class}"
            ).is_equal_to(data_class["name"])
            assert_that(
                found_fields[1]["colSemantic"], f"Data class name incorrect for {data_class}"
            ).is_equal_to(data_class["name"])

    @allure.feature("Pullup")
    @allure.story("Catalog - Column Manager")
    def test_column_mgr_bulk_update_sensitive_label(self, api_utils):
        """Test Column Manager = Bulk Update Sensitive Label"""

        # Notes:
        #   Sensitive Labels come out of the box and will exist in fresh environments
        #   Labels are unique. A dataset can only have 1.
        #   Labels cannot be removed, so the data must be changed twice to validate it changes
        #       The other option is running a unique job, but this is faster.

        # Get all data classes and grab the first two.
        s_labels = api_utils.get(V2_SENSITIVE_LABEL)
        assert_that(len(s_labels), "No sensitive labels found").is_greater_than(0)

        s_label_1 = {
            "name": s_labels["result"][0]["sensitiveLabelName"],
            "id": s_labels["result"][0]["sensitiveLabelId"],
        }
        s_label_2 = {
            "name": s_labels["result"][1]["sensitiveLabelName"],
            "id": s_labels["result"][1]["sensitiveLabelId"],
        }

        # Run a job if needed
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_2, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        # Apply the data class via bulk update to two columns twice,
        # to ensure it can be changed on repeat runs
        for s_label in [s_label_1, s_label_2]:
            # Update the data class on the columns
            PL_DC_SL["idToUpdate"] = s_label["id"]
            resp_bulk_update = api_utils.post(
                V2_CATALOG_COLUMN_BULK_UPDATE_SENSITIVE_LABEL, json=PL_DC_SL, return_json=False
            )
            assert_that(
                resp_bulk_update.status_code, f"Data class bulk update failed with {PL_DC_SL}"
            ).is_equal_to(200)

            # Find the fields within the filters
            found_fields = self.find_fields_in_column_assets_filter(
                api_utils, PL_DC_SEARCH, FIELD1_DC_SL, FIELD2_DC_SL
            )

            # Validate the data is correct
            assert_that(
                found_fields[0]["sensitiveLabelName"], f"Data class name incorrect for {s_label}"
            ).is_equal_to(s_label["name"])
            assert_that(
                found_fields[1]["sensitiveLabelName"], f"Data class name incorrect for {s_label}"
            ).is_equal_to(s_label["name"])

    @allure.feature("Pullup")
    @allure.story("Catalog - Column Manager")
    def test_column_mgr_bulk_update_rules(self, api_utils):
        """Test Column Manager - Bulk Update Rules"""
        # Note: Rules come out of the box and will exist in fresh environments

        # Run a job if needed
        ds_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DS_BULK_2, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs, PROD_RUN_ID)

        # Cleanup existing
        cleanup_rules = api_utils.delete(V3_RULES + "/" + DS_BULK_2, return_json=False)
        assert_that(cleanup_rules.status_code, "Failed to delete rules").is_equal_to(200)

        # Get all data classes and grab the first two.
        all_rules = api_utils.get(V2_GET_RULE_REPO_WITH_METADATA_LABEL)
        assert_that(len(all_rules), "No sensitive labels found").is_greater_than(0)

        pl_rule = {"name": all_rules[0]["ruleName"], "id": all_rules[0]["ruleRepoId"]}

        # Update the data class on the columns
        PL_DC_SL["idsToUpdate"] = [pl_rule["id"]]
        resp_bulk_update = api_utils.post(
            V2_CATALOG_COLUMN_BULK_UPDATE_RULES, json=PL_DC_SL, return_json=False
        )
        assert_that(
            resp_bulk_update.status_code, f"Data class bulk update failed with {PL_DC_SL}"
        ).is_equal_to(200)

        # Validate the data is correct
        found_rules = api_utils.get(V3_RULES + "/" + DS_BULK_2)
        found_rules_sorted = sorted(found_rules, key=lambda x: x["ruleNm"])

        assert_that(
            len(found_rules), f"Unexpected number of rules found. Found: {found_rules_sorted}"
        ).is_equal_to(2)
        assert_that(
            found_rules_sorted[0]["ruleRepo"], f"Unexpected rule name for {FIELD2_DC_SL}"
        ).is_equal_to(pl_rule["name"])
        assert_that(
            found_rules_sorted[0]["columnName"], f"Unexpected column name for {FIELD2_DC_SL}"
        ).is_equal_to(FIELD2_DC_SL)
        assert_that(
            found_rules_sorted[0]["isActive"], f"Expected rule to be active for {FIELD2_DC_SL}"
        ).is_equal_to(1)

        assert_that(
            found_rules_sorted[1]["ruleRepo"], f"Unexpected rule name for {FIELD1_DC_SL}"
        ).is_equal_to(pl_rule["name"])
        assert_that(
            found_rules_sorted[1]["columnName"], f"Unexpected column name for {FIELD1_DC_SL}"
        ).is_equal_to(FIELD1_DC_SL)
        assert_that(
            found_rules_sorted[1]["isActive"], f"Expected rule to be active for {FIELD1_DC_SL}"
        ).is_equal_to(1)

    @allure.feature("Pullup")
    @allure.story("Get catalog and source name")
    def test_get_catalog_and_source_name_snowflake(self, api_utils):
        # Add coverage for /v2/getcatalogandconnsrcnamebydataset for Snowflake
        response = helper.setup_dataset(api_utils, DS_DEFS_FULL_PROFILE, WHERE_DATE)
        catalog_response = api_utils.get(
            V2_GET_CATALOG_AND_CONN_SRC_NAME_BY_DATASET, params={"dataset": response["dataset"]}
        )
        compare_dicts_are_equal(catalog_response, SNOWFLAKE_CATALOG_OUTPUT, ["runs", "updtTs"])

    @allure.feature("Pullup")
    @allure.story("Get catalog and source name")
    def test_get_catalog_and_source_name_oracle(self, api_utils):
        # Add coverage for /v2/getcatalogandconnsrcnamebydataset for Oracle
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            C_NAME_CON_ORACLE,
            DS_CON_ORACLE + "_1",
            QUERY_CON_ORACLE,
            WHERE_DATE_CON_ORACLE,
        )
        response = helper.setup_dataset(api_utils, dataset_defs, WHERE_DATE_CON_ORACLE)
        catalog_response = api_utils.get(
            V2_GET_CATALOG_AND_CONN_SRC_NAME_BY_DATASET, params={"dataset": response["dataset"]}
        )
        compare_dicts_are_equal(catalog_response, ORACLE_CATALOG_OUTPUT, ["runs", "updtTs"])

    @allure.feature("Pullup")
    @allure.story("Get catalog and source name")
    def test_get_catalog_and_source_name_s3(self, api_utils):
        # Add coverage for /v2/getcatalogandconnsrcnamebydataset for S3
        response = helper.setup_dataset(api_utils, DS_DEFS, "2017-12-20")
        catalog_response = api_utils.get(
            V2_GET_CATALOG_AND_CONN_SRC_NAME_BY_DATASET, params={"dataset": response["dataset"]}
        )
        compare_dicts_are_equal(catalog_response, S3_CATALOG_OUTPUT, ["runs", "updtTs"])
