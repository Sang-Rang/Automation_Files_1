import time

import allure
import pytest
from assertpy import assert_that
from data_test.pullup.data_behavior_settings_persist import (
    DATASET_SETTINGS_PERSIST,
    CONNECTION_SETTINGS_PERSIST,
    QUERY_SETTINGS_PERSIST,
    INDEX_ISMANUAL_SETTINGS_PERSIST,
    INDEX_LENIENT_SETTINGS_PERSIST,
    INDEX_STRICT_SETTINGS_PERSIST,
    INDEX_SUPPRESS_SETTINGS_PERSIST,
    PL_MANUAL_SETTINGS_PERSIST,
    PL_STRICT_SETTINGS_PERSIST,
    PL_LENIENT_SETTINGS_PERSIST,
    PL_SUPPRESS_SETTINGS_PERSIST,
    EXP_SUPPRESS_STATUS,
    EXP_RULES_SETTINGS_PERSIST,
    PL_GENERAL_SETTINGS_PERSIST,
)
from data_test.pullup.data_behavior_operations_drill_in import (
    EXPECTED_DATA,
    EXPECTED_DATA_BROKEN_RULE,
    EXPECTED_DQ_ITEMS_BROKEN_RULE,
)
from endpoints.v2.controller import V2_GET_DATASET_HISTORY_RUN_ID
from endpoints.v2.controller_hoot import (
    V2_BEHAVIOR_DETAILS,
    V2_GET_TABLE_STATS,
    V2_GET_DATASET_SCAN,
)
from endpoints.v2.controller_catalog import V2_GET_DQ_CHECKS_DETAILS
from endpoints.v2.controller_label import (
    V2_SET_BOUNDRY_MANUAL,
    V2_SET_BOUNDRY_SUPPRESS,
    V2_SET_BOUNDRY_TIER,
)

from payloads.pullup.pl_behavior_operations_drill_in import (
    DATASET_DEFS,
    PL_BEH_DETAILS,
    PL_BROKEN,
    TRADE_DATE_START,
)
from payloads.pullup.pl_behavior_suppress_findings import (
    DATASET_DEFS_BEHAVIOR_SUPPRESS,
    RUN_DATE_BEHAVIOR_SUPPRESS,
    PL_GENEREAL_BEHAVIOR_SUPPRESS,
    PL_SUPPRESS_BEHAVIOR_SUPPRESS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestBehaviorOperations:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def helper_validate_dq_checks_details(api_utils):
        resp = api_utils.get(V2_GET_DQ_CHECKS_DETAILS, params=PL_GENERAL_SETTINGS_PERSIST)

        resp_strict = resp[INDEX_STRICT_SETTINGS_PERSIST]["metric"]
        resp_lenient = resp[INDEX_LENIENT_SETTINGS_PERSIST]["metric"]
        resp_suppress = resp[INDEX_SUPPRESS_SETTINGS_PERSIST]["metric"]
        resp_manual = resp[INDEX_ISMANUAL_SETTINGS_PERSIST]["metric"]

        # Strict check
        assert_that(resp_strict["adaptiveTier"], "Pre-Rerun Adaptive Tier").is_equal_to(
            PL_STRICT_SETTINGS_PERSIST["adaptiveTier"]
        )
        assert_that(resp_strict["lbAbs"], "Pre-Rerun lbAbs").is_equal_to(
            PL_STRICT_SETTINGS_PERSIST["lbAbs"]
        )
        assert_that(resp_strict["ubAbs"], "Pre-Rerun ubAbs").is_equal_to(
            PL_STRICT_SETTINGS_PERSIST["ubAbs"]
        )

        # Lenient Check
        assert_that(resp_lenient["adaptiveTier"], "Pre-Rerun Adaptive Tier").is_equal_to(
            PL_LENIENT_SETTINGS_PERSIST["adaptiveTier"]
        )
        assert_that(resp_lenient["lbAbs"], "Pre-Rerun lbAbs").is_equal_to(
            PL_LENIENT_SETTINGS_PERSIST["lbAbs"]
        )
        assert_that(resp_lenient["ubAbs"], "Pre-Rerun ubAbs").is_equal_to(
            PL_LENIENT_SETTINGS_PERSIST["ubAbs"]
        )

        # Suppress
        assert_that(resp_suppress["status"], "Pre-Rerun Suppress Status").is_equal_to(
            EXP_SUPPRESS_STATUS
        )
        assert_that(resp_suppress["lbAbs"], "Pre-Rerun lbAbs").is_equal_to(
            PL_SUPPRESS_SETTINGS_PERSIST["lbAbs"]
        )
        assert_that(resp_suppress["ubAbs"], "Pre-Rerun ubAbs").is_equal_to(
            PL_SUPPRESS_SETTINGS_PERSIST["ubAbs"]
        )

        # Manual
        assert_that(resp_manual["isManual"], "Pre-Rerun is Manual").is_true()

        assert_that(resp_manual["lbAbs"], "Pre-Rerun lbAbs").is_equal_to(
            PL_MANUAL_SETTINGS_PERSIST["lbAbsVal"]
        )
        assert_that(resp_manual["ubAbs"], "Pre-Rerun ubAbs").is_equal_to(
            PL_MANUAL_SETTINGS_PERSIST["ubAbsVal"]
        )

    @allure.feature("Pullup")
    @allure.story("Behavior")
    @pytest.mark.smoke
    def test_behavior_drill_in_and_broken_rule(self, api_utils):
        """Test Behavior - Drill In & Broken Rule"""

        helper.setup_dataset(api_utils, DATASET_DEFS, TRADE_DATE_START)

        max_retries = 30
        wait_time = 3
        attempts = 0
        expected_behavior_details_key = "Row Count__ROW_COUNT"
        # Get behavior detail data
        while attempts < max_retries:
            get_behavior_details = api_utils.get(V2_BEHAVIOR_DETAILS, params=PL_BEH_DETAILS)
            behavior_details_key = get_behavior_details.get("key", None)
            # When we get the correct behavior key we exit the loop
            if behavior_details_key == expected_behavior_details_key:
                break
            time.sleep(wait_time)
            attempts += 1

        # Validate results
        for key, expected_value in EXPECTED_DATA.items():
            assert_that(expected_value, f"Behavior Details -  {key}").is_equal_to(
                get_behavior_details[key]
            )

        # Fetch table stats data and verify.
        # Sub-category stored separately for readability/maintainability.
        data_table_stats = api_utils.get(V2_GET_TABLE_STATS, params=PL_BROKEN)
        data_table_stats_row_count = data_table_stats["dqItems"]["Row Count__ROW_COUNT"]

        for key, expected_value in EXPECTED_DATA_BROKEN_RULE.items():
            assert_that(expected_value, f"Table Stats - {key}").is_equal_to(data_table_stats[key])

        for key, expected_value in EXPECTED_DQ_ITEMS_BROKEN_RULE.items():
            assert_that(expected_value, f"Table Stats dqItems Row Count - {key}").is_equal_to(
                data_table_stats_row_count[key]
            )

    @allure.feature("Pullup")
    @allure.story("Behavior")
    def test_behavior_suppress_finding(self, api_utils):
        """Behavior - Suppress Behavior Finding DEV-48876"""

        # Expected Data for Validation
        exp_behavior_score = 0
        exp_history_score = 100
        exp_history_score_beh = 0
        exp_scan_behavior_score = 0
        exp_scan_score = 100
        exp_score = 100
        exp_source_behavior_score = 30
        exp_source_score = 70

        helper.setup_dataset(
            api_utils,
            DATASET_DEFS_BEHAVIOR_SUPPRESS,
            RUN_DATE_BEHAVIOR_SUPPRESS,
        )

        # Validate score data before the behavior item is suppressed
        # Add re-try logic because initially the behaviorScore is returned as 0
        max_retries = 30
        wait_time = 3
        attempts = 0

        while attempts < max_retries:
            ts_pre = api_utils.get(V2_GET_TABLE_STATS, params=PL_GENEREAL_BEHAVIOR_SUPPRESS)
            behavior_score = ts_pre.get("behaviorScore", None)
            # When we get the correct behavior score we exit the loop
            if behavior_score == exp_source_behavior_score:
                break
            time.sleep(wait_time)
            attempts += 1

        assert_that(ts_pre["behaviorScore"], "Behavior Score Pre-Suppress").is_equal_to(
            exp_source_behavior_score
        )
        assert_that(ts_pre["score"], "Score Pre-Suppress").is_equal_to(exp_source_score)

        # Suppress the behavior
        suppress = api_utils.post(V2_SET_BOUNDRY_SUPPRESS, params=PL_SUPPRESS_BEHAVIOR_SUPPRESS)
        assert_that(suppress["msg"], "Post Boundry Suppress").is_equal_to("Update recorded")

        # Validate data has modified due to suppressed
        ts_post = api_utils.get(V2_GET_TABLE_STATS, params=PL_GENEREAL_BEHAVIOR_SUPPRESS)
        assert_that(ts_post["behaviorScore"], "Behavior Score - Post-Suppress").is_equal_to(
            exp_behavior_score
        )
        assert_that(ts_post["score"], "Score - Post-Suppress").is_equal_to(exp_score)

        # Fetch dataset history and verify score data
        ds_history = api_utils.get(
            V2_GET_DATASET_HISTORY_RUN_ID, params=PL_GENEREAL_BEHAVIOR_SUPPRESS
        )
        assert_that(ds_history["score"], "History - Score").is_equal_to(exp_history_score)
        assert_that(ds_history["scoreBehavior"], "History - Behavior Score").is_equal_to(
            exp_history_score_beh
        )

        # Fetch dataset scan and verify score data
        ds_scan = api_utils.get(V2_GET_DATASET_SCAN, params=PL_GENEREAL_BEHAVIOR_SUPPRESS)
        assert_that(ds_scan["score"], "Data Scan -  Score").is_equal_to(exp_scan_score)
        assert_that(ds_scan["scoreBehavior"], "Data Scan - Behavior Score").is_equal_to(
            exp_scan_behavior_score
        )

    @allure.feature("Pullup")
    @allure.story("Behavior")
    def test_behavior_settings_persist(self, api_utils):
        """Behavior - Validate Settings Persist DEV-48885"""

        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION_SETTINGS_PERSIST,
            DATASET_SETTINGS_PERSIST,
            QUERY_SETTINGS_PERSIST,
        )

        helper.setup_dataset(api_utils, dataset_defs)

        resp_details = api_utils.get(V2_GET_DQ_CHECKS_DETAILS, params=PL_GENERAL_SETTINGS_PERSIST)

        # Sanity check. If existing rules change, index values may change
        assert_that(EXP_RULES_SETTINGS_PERSIST, "Total Rules").is_equal_to(len(resp_details))

        # Update rules to new data
        api_utils.post(V2_SET_BOUNDRY_MANUAL, params=PL_MANUAL_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_TIER, params=PL_STRICT_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_TIER, params=PL_LENIENT_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_SUPPRESS, params=PL_SUPPRESS_SETTINGS_PERSIST)

        # Validate data pre-run
        self.helper_validate_dq_checks_details(api_utils)

        # Rerun Job
        helper.setup_dataset(api_utils, dataset_defs)

        # Validate data post-rerun
        self.helper_validate_dq_checks_details(api_utils)
