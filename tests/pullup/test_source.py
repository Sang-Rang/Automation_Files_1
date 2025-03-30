import allure
import pytest
from assertpy import soft_assertions, assert_that

from data_test.pullup.data_source_no_keys_run_display_correctly_edit import (
    INCLUDE_NO_KEYS_RUN_DISPLAY_EDIT,
    EXCLUDE_NO_KEYS_RUN_DISPLAY_EDIT,
)
from payloads.pullup.pl_jdbc_to_s3_to_oracle_tojdbc import (
    DEFS_MULTI_SOURCE_JDBCJDBC,
    DEFS_MULTI_SOURCE_JDBCS3,
    DEFS_MULTI_SOURCE_S3ORACLE,
    DEFS_MULTI_SOURCE_S3JDBC,
)
from payloads.pullup.pl_no_keys_run_display_correctly_edit import (
    PL_DS_DEFS_NO_KEYS,
    PL_DS_DEFS_NO_KEYS_EDIT,
)
from payloads.pullup.pl_source_downtrain_and_persist_properly import (
    DS_DEF_DOWNTRAIN_PERSIST,
)
from payloads.pullup.pl_source_turn_off_validate_values import (
    DS_DEF_SOUCE_OFF_VALIDATE_VALUES,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.logger import Logger
from endpoints.v2.controller_hoot import (
    V2_GET_SOURCE_VALUE_COMPARISON,
    V2_GET_ISSUE_COUNTS,
    V2_GET_SOURCE_SCHEMA,
)
from endpoints.v2.controller_assignment_q import V2_ASSIGNMENT_Q_INVALIDATE
from endpoints.v2.controller_label import V2_RETRAIN, V2_VIEW_ITEM_LABELS
from endpoints.v3.dataset_def_api import V3_DATASETDEFS


helper = BaseHelper()
LOGGER = Logger.get_instance()


@pytest.mark.pullup
class TestSource:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Source")
    def test_source_no_keys_run_display_correctly_edit(self, api_utils):
        """SOURCE-No keys, does it run, display correctly, edit."""
        source_count = 30
        nokey_count = 0
        nokeys_count_edit = 0
        dupe_count = 1

        get_source_values_params = {
            "dataset": PL_DS_DEFS_NO_KEYS["dataset"],
            "runId": f"{PL_DS_DEFS_NO_KEYS['runId']}T00:00:00.000+0000",
        }
        get_source_values_edited_dataset_params = {
            "dataset": PL_DS_DEFS_NO_KEYS_EDIT["dataset"],
            "runId": f"{PL_DS_DEFS_NO_KEYS_EDIT['runId']}T00:00:00.000+0000",
        }

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PL_DS_DEFS_NO_KEYS)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, PL_DS_DEFS_NO_KEYS_EDIT)
        initial_dataset_data = helper.run_source_job(api_utils, PL_DS_DEFS_NO_KEYS)

        source_data = api_utils.get(V2_GET_SOURCE_VALUE_COMPARISON, params=get_source_values_params)

        # Validating all keys are blank and source
        for source_value in source_data["data"]:
            if source_value["key"] == [""]:
                nokey_count = nokey_count + 1

        assert_that(initial_dataset_data["source"], "Source issue count #1").is_equal_to(
            source_count
        )
        assert_that(nokey_count, "No key count #1").is_equal_to(len(source_data["data"]))

        # Turn off dupe and re-run
        PL_DS_DEFS_NO_KEYS_EDIT["dupe"]["on"] = False
        ds_nokeys_edit = helper.run_source_job(api_utils, PL_DS_DEFS_NO_KEYS_EDIT)
        ds_defs_after_edit = api_utils.get(
            V3_DATASETDEFS + "/" + get_source_values_edited_dataset_params["dataset"]
        )

        # Validate no dupes, then turn back on and re-run job
        assert_that(ds_nokeys_edit["dupe"], "Expected no dupes prior to edit").is_equal_to(0)
        ds_defs_after_edit["dupe"]["dataset"] = PL_DS_DEFS_NO_KEYS["dataset"]
        ds_defs_after_edit["dupe"]["on"] = True
        ds_defs_after_edit["dupe"]["include"] = INCLUDE_NO_KEYS_RUN_DISPLAY_EDIT
        ds_defs_after_edit["dupe"]["exclude"] = EXCLUDE_NO_KEYS_RUN_DISPLAY_EDIT

        edited_dataset_data = api_utils.post(
            V3_DATASETDEFS, json=ds_defs_after_edit, return_json=False
        )
        assert_that(
            edited_dataset_data.status_code, "Dataset definitions update failed"
        ).is_equal_to(200)

        ds_nokeys_edit_run = helper.run_source_job(api_utils, ds_defs_after_edit)

        source_data_edited = api_utils.get(
            V2_GET_SOURCE_VALUE_COMPARISON, params=get_source_values_edited_dataset_params
        )

        for source_value_edit in source_data_edited["data"]:
            if source_value_edit["key"] == [""]:
                nokeys_count_edit = nokeys_count_edit + 1

        assert_that(ds_nokeys_edit_run["source"], "Source issue count #2").is_equal_to(source_count)
        assert_that(nokeys_count_edit, "No key count #2").is_equal_to(
            len(source_data_edited["data"])
        )
        assert_that(ds_nokeys_edit_run["dupe"], "Duplicate count").is_equal_to(dupe_count)

    @allure.feature("Pullup")
    @allure.story("Source")
    def test_source_turn_off_validate_values(self, api_utils):
        """Test SOURCE - Turn off validate values."""
        source_count = 3
        pl_general = {
            "dataset": DS_DEF_SOUCE_OFF_VALIDATE_VALUES["dataset"],
            "runId": DS_DEF_SOUCE_OFF_VALIDATE_VALUES["runId"],
        }

        helper.setup_dataset(api_utils, DS_DEF_SOUCE_OFF_VALIDATE_VALUES)

        resp_issue_count = api_utils.get(V2_GET_ISSUE_COUNTS, params=pl_general)

        resp_source_value = api_utils.get(V2_GET_SOURCE_VALUE_COMPARISON, params=pl_general)

        with soft_assertions():
            assert_that(
                source_count,
                f"Expected source count is {source_count}, "
                f"Actual count is {resp_issue_count['SOURCE']}",
            ).is_equal_to(resp_issue_count["SOURCE"])
            assert_that(
                resp_source_value["checkValues"],
                "Expected checkValues to be: False",
            ).is_false()
            assert_that(
                len(resp_source_value["data"]),
                f"Expected 0 SOURCE findings from value comparison. "
                f"Found {len(resp_source_value['data'])}",
            ).is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Source")
    def test_source_downtrain_and_persist_properly(self, api_utils):
        """SOURCE - Does it downtrain properly, persist properly after re-run,
        retrain properly and score properly."""

        # Run job and fetch history, issues, and schema data
        helper.setup_dataset(api_utils, DS_DEF_DOWNTRAIN_PERSIST)
        resp_ds_history_issues = helper.get_dataset_history_issues(
            api_utils, DS_DEF_DOWNTRAIN_PERSIST["dataset"]
        )

        pl_general = {
            "dataset": DS_DEF_DOWNTRAIN_PERSIST["dataset"],
            "runId": resp_ds_history_issues["runId"],
        }

        resp_schema = api_utils.get(V2_GET_SOURCE_SCHEMA, params=pl_general)
        assert_that(len(resp_schema), "No source schema found").is_greater_than(0)

        # Invalidate data and retrain
        uuid = resp_schema[0]["assignmentId"]["uuid"]
        pl_uuid = {"uuid": uuid, "annotation": "invalid"}

        resp_invalidate = api_utils.post(V2_ASSIGNMENT_Q_INVALIDATE, json=pl_uuid)
        assert_that(resp_invalidate["result"]).is_true()
        resp_retrain = api_utils.post(V2_RETRAIN, params=pl_general, return_json=False)
        assert_that(resp_retrain.status_code).is_equal_to(200)

        # Refresh data pre-run and validate
        resp_labels = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)

        assert_that(str(resp_labels["data"]), "UUID not found in item labels").contains(uuid)

        resp_ds_history_issues_prerun = helper.get_dataset_history_issues(
            api_utils, pl_general["dataset"]
        )

        with soft_assertions():
            assert_that(
                resp_ds_history_issues_prerun["score"], "Pre-rerun Invalidate Score"
            ).is_equal_to(resp_ds_history_issues["score"] + 1)

            assert_that(
                resp_ds_history_issues_prerun["scoreSource"], "Pre-rerun Invalidate Source Score"
            ).is_equal_to(resp_ds_history_issues["scoreSource"] - 1)

            assert_that(
                resp_ds_history_issues_prerun["source"], "Pre-rerun Invalidate Source"
            ).is_equal_to(resp_ds_history_issues["source"] - 1)

        # Rerun job after invalidate/retrain and validate data
        resp_source = helper.run_source_job(api_utils, DS_DEF_DOWNTRAIN_PERSIST)

        resp_labels_rerun = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)
        assert_that(str(resp_labels_rerun["data"]), "Post-rerun UUID not found in labels").contains(
            uuid
        )

        with soft_assertions():
            assert_that(resp_source["score"], "Post-rerun, Invalidate Score").is_equal_to(
                resp_ds_history_issues_prerun["score"]
            )

            assert_that(
                resp_source["scoreSource"], "Post-rerun, Invalidate Source Score"
            ).is_equal_to(resp_ds_history_issues_prerun["scoreSource"])

            assert_that(resp_source["source"], "Post-rerun, Source").is_equal_to(
                resp_ds_history_issues_prerun["source"]
            )

    @allure.feature("Pullup")
    @allure.story("Source")
    @pytest.mark.skip(reason="Enable after DEV-71866 is fixed")
    @allure.issue(
        "https://engineering-collibra.atlassian.net/browse/DEV-71866",
        "Source: Not matching column data type returned as passing result.",
    )
    def test_jdbc_to_jdbc_jdbc_to_s3_s3_to_oracle_s3_to_jdbc(self, api_utils):
        """Test SOURCE - JDBC TO JDBC, JDBC TO S3, S3 TO ORACLE, S3 TO JDBC."""
        exp_jdbc_jdbc = 12
        exp_source_jdbcs3 = 10
        exp_source_s3oracle = 32
        exp_source_s3jdbc = 35

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DEFS_MULTI_SOURCE_JDBCJDBC)
        data = helper.get_dataset_history_issues(api_utils, DEFS_MULTI_SOURCE_JDBCJDBC["dataset"])
        assert_that(exp_jdbc_jdbc, "DEFS_MULTI_SOURCE_JDBCJDBC").is_equal_to(data["source"])

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DEFS_MULTI_SOURCE_JDBCS3)
        data = helper.get_dataset_history_issues(api_utils, DEFS_MULTI_SOURCE_JDBCS3["dataset"])
        assert_that(exp_source_jdbcs3, "DEFS_MULTI_SOURCE_JDBCS3").is_equal_to(data["source"])

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DEFS_MULTI_SOURCE_S3ORACLE)
        data = helper.get_dataset_history_issues(api_utils, DEFS_MULTI_SOURCE_S3ORACLE["dataset"])
        assert_that(exp_source_s3oracle, "DEFS_MULTI_SOURCE_S3ORACLE").is_equal_to(data["source"])

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, DEFS_MULTI_SOURCE_S3JDBC)
        data = helper.get_dataset_history_issues(api_utils, DEFS_MULTI_SOURCE_S3JDBC["dataset"])
        assert_that(exp_source_s3jdbc, "DEFS_MULTI_SOURCE_S3JDBC1").is_equal_to(data["source"])
