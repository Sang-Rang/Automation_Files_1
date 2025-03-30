import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_explorer import V2_GET_REMOTE_HOST
from endpoints.v2.controller_load_opt import V2_UPSERT_LOAD_OPT
from endpoints.v2.controller_hoot import (
    V2_GET_TABLE_STATS,
    V2_GET_SOURCE_COUNT_COMPARISON,
    V2_GET_SOURCE_SCHEMA_COMPARISON,
    V2_GET_SOURCE_VALUE_COMPARISON,
    V2_GET_HOOT,
)
from endpoints.v2.controller_profile import V2_GET_DATASET_SCHEMA
from endpoints.v2.controller_source_opt import V2_POST_UPSERT_SOURCE_OPT, V2_GET_SOURCE_OPT
from endpoints.v3.dataset_def_api import V3_DATASETDEFS
from payloads.pullup.pl_source_scope_operations import (
    SOURCE_DATASET,
    MAPPING_DATASET,
    UPDATED_SOURCE_PAYLOAD,
    DATASET_JDBC_TO_JDBC,
    SELECT_ALL_COLUMNS_PARAMS,
    SOURCE_PAYLOAD_MAPPING_EDITED,
)
from data_test.pullup.data_missing_endpoints_coverage import (
    GET_SCHEMA_RESPONSE_BODY,
    SOURCE_OPT_RESPONSE,
)
from data_test.pullup.data_source_jdbc_to_jdbc import (
    SOURCE_COUNT_EXPECTED,
    SOURCE_SCHEMA_EXPECTED,
    SOURCE_VALUE_EXPECTED,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal


helper = BaseHelper()


@pytest.mark.pullup
class TestSourceScope:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Source")
    def test_source_scope_operations(self, api_utils):
        """SOURCE - Select specific columns in -q and -srcq does it run properly, edit properly."""
        # Setup dataset and verify query before the update.
        helper.setup_dataset(api_utils, SOURCE_DATASET)
        response_before_edit = api_utils.get(V3_DATASETDEFS + "/" + SOURCE_DATASET["dataset"])
        assert_that(response_before_edit["source"]["query"], "Got invalid query value").is_equal_to(
            SOURCE_DATASET["source"]["query"]
        )

        # Update the Source query and verify update was applied after running a job
        api_utils.post(V2_POST_UPSERT_SOURCE_OPT, params=UPDATED_SOURCE_PAYLOAD)
        response_after_edit = api_utils.get(V3_DATASETDEFS + "/" + SOURCE_DATASET["dataset"])
        helper.setup_dataset(api_utils, response_after_edit)
        dataset_defs_after_edit = api_utils.get(V3_DATASETDEFS + "/" + SOURCE_DATASET["dataset"])
        assert_that(
            dataset_defs_after_edit["source"]["query"], "Got invalid query value"
        ).is_equal_to(UPDATED_SOURCE_PAYLOAD["query"])

        # Update a Query to select * from home page and re-run the job
        api_utils.put(V2_UPSERT_LOAD_OPT, params=SELECT_ALL_COLUMNS_PARAMS)
        select_all_response = api_utils.get(V3_DATASETDEFS + "/" + SOURCE_DATASET["dataset"])
        assert_that(select_all_response["load"]["query"], "Got invalid query value").is_equal_to(
            SELECT_ALL_COLUMNS_PARAMS["query"]
        )

        helper.setup_dataset(api_utils, select_all_response)
        select_all_after_run_response = api_utils.get(
            V3_DATASETDEFS + "/" + SOURCE_DATASET["dataset"]
        )
        assert_that(
            select_all_after_run_response["load"]["query"], "Got invalid query value"
        ).is_equal_to(SELECT_ALL_COLUMNS_PARAMS["query"])

        # Validate source number for the selected job.
        payload = {
            "dataset": SOURCE_DATASET["dataset"],
            "runId": SOURCE_DATASET["runId"],
            "sense": 3,
        }
        source_score_response = api_utils.get(V2_GET_TABLE_STATS, params=payload)
        assert_that(
            source_score_response["sourceScore"], "Got an unexpected source score number"
        ).is_equal_to(6)

    @allure.feature("Pullup")
    @allure.story("Source")
    def test_source_mapping_column_names(self, api_utils):
        """SOURCE - Mapping different column names, does the DQ job edit properly."""
        # Setup dataset and verify query before the update.
        response = helper.setup_dataset(api_utils, MAPPING_DATASET)
        # Add coverage for /v2/gethoot endpoint
        hoot_params = {"dataset": response["dataset"], "runId": response["runId"]}
        hoot_response = api_utils.get(V2_GET_HOOT, params=hoot_params)
        assert_that(hoot_response["dataset"], "Dataset name is different").is_equal_to(
            response["dataset"]
        )
        assert_that(hoot_response["score"], "Got unexpected score result").is_equal_to(100)

        response_before_edit = api_utils.get(V3_DATASETDEFS + "/" + MAPPING_DATASET["dataset"])
        source_mapping_expected = {"rating": "releaseyear", "releaseyear": "rating"}
        assert_that(
            response_before_edit["source"]["map"], "Got invalid mapping values"
        ).is_equal_to(source_mapping_expected)
        assert_that(
            response_before_edit["source"]["matches"], "Invalid matching settings"
        ).is_equal_to(False)
        assert_that(
            response_before_edit["source"]["validateSchemaOrder"], "Invalid Schema Order settings"
        ).is_equal_to(False)

        # Validate source number for the selected job.
        payload = {
            "dataset": MAPPING_DATASET["dataset"],
            "runId": MAPPING_DATASET["runId"],
            "sense": 3,
        }
        source_score_response = api_utils.get(V2_GET_TABLE_STATS, params=payload)
        assert_that(
            source_score_response["sourceScore"], "Got an unexpected source score number"
        ).is_equal_to(0)

        # Modify a source settings, enable schema order and validate for matches
        api_utils.put(V2_POST_UPSERT_SOURCE_OPT, params=SOURCE_PAYLOAD_MAPPING_EDITED)
        dataset_defs_after_edit = api_utils.get(V3_DATASETDEFS + "/" + MAPPING_DATASET["dataset"])
        helper.setup_dataset(api_utils, dataset_defs_after_edit)
        dataset_defs_after_run = api_utils.get(V3_DATASETDEFS + "/" + MAPPING_DATASET["dataset"])
        assert_that(
            dataset_defs_after_run["source"]["matches"], "Invalid matching settings"
        ).is_equal_to(True)
        assert_that(
            dataset_defs_after_run["source"]["validateSchemaOrder"], "Invalid Schema Order settings"
        ).is_equal_to(True)
        source_score_response = api_utils.get(V2_GET_TABLE_STATS, params=payload)
        assert_that(
            source_score_response["sourceScore"], "Got an unexpected source score number"
        ).is_equal_to(10)

    @allure.feature("Pullup")
    @allure.story("Source")
    @pytest.mark.flaky(retries=2, delay=5)
    @allure.issue(
        "https://engineering-collibra.atlassian.net/browse/DEV-74255",
        "SOURCE - JDBC to File, invalid cell values findings",
    )
    @pytest.mark.skip(reason="Enable after DEV-74255 is fixed")
    def test_source_jdbc_to_file_operations(self, api_utils):
        """DEV-49008, DEV-49009, SOURCE - JDBC to File Validate Values and columns."""
        # Setup dataset
        setup_response = helper.setup_dataset(api_utils, DATASET_JDBC_TO_JDBC)
        assert_that(setup_response["status"]).is_equal_to("FINISHED")
        response_after_run = api_utils.get(V3_DATASETDEFS + "/" + DATASET_JDBC_TO_JDBC["dataset"])

        payload = {
            "dataset": response_after_run["dataset"],
            "runId": response_after_run["runId"],
        }
        source_count = api_utils.get(V2_GET_SOURCE_COUNT_COMPARISON, params=payload)
        source_schema = api_utils.get(V2_GET_SOURCE_SCHEMA_COMPARISON, params=payload)
        source_value = api_utils.get(V2_GET_SOURCE_VALUE_COMPARISON, params=payload)

        # Sort datasets for accurate comparisons
        source_schema["data"] = sorted(source_schema["data"], key=lambda x: x["targetColNm"])
        source_value["data"] = sorted(source_value["data"], key=lambda x: x["column"])

        SOURCE_SCHEMA_EXPECTED["data"] = sorted(
            SOURCE_SCHEMA_EXPECTED["data"], key=lambda x: x["targetColNm"]
        )
        SOURCE_VALUE_EXPECTED["data"] = sorted(
            SOURCE_VALUE_EXPECTED["data"], key=lambda x: x["column"]
        )

        # Validate Source output
        exclude_dynamic_keys = ["assignmentId", "key"]
        compare_dicts_are_equal(source_count, SOURCE_COUNT_EXPECTED, ["assignmentId"])
        compare_dicts_are_equal(source_schema, SOURCE_SCHEMA_EXPECTED, ["assignmentId"])
        compare_dicts_are_equal(source_value, SOURCE_VALUE_EXPECTED, exclude_dynamic_keys)

        # Add coverage for /v2/getdatasetschema endpoint, not test related.
        dataset_response = api_utils.get(
            V2_GET_DATASET_SCHEMA, params={"dataset": DATASET_JDBC_TO_JDBC["dataset"]}
        )
        compare_dicts_are_equal(dataset_response, GET_SCHEMA_RESPONSE_BODY, ["column"])

        # Add coverage for /v2/source-opt/get endpoint, not test related.
        source_opt_response = api_utils.get(
            V2_GET_SOURCE_OPT, params={"dataset": DATASET_JDBC_TO_JDBC["dataset"]}
        )
        compare_dicts_are_equal(
            source_opt_response,
            SOURCE_OPT_RESPONSE,
            ["validateValuesIgnoreNull", "column", "validateValuesIgnoreNone"],
        )

        # Add coverage for /v2/getremotehost endpoint, not test related.
        expected_host = response_after_run["host"]
        actual_host = api_utils.get(V2_GET_REMOTE_HOST)
        assert_that(str(actual_host[0]), "Got invalid host address").contains(expected_host)
