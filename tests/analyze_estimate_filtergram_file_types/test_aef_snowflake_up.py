import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_snowflake_up import (
    WHERE_DATE,
    QUERY,
    CONN_NAME,
    ROW_COUNT,
    PL_JOB_EST,
    EXP_JOB_EST,
    PL_DAYS_WITH_DATA,
    EXP_DAYS_WITH,
    PL_DS_GEN,
    EXP_DS_SCAN,
    EXP_DS_SCORE,
    PL_DS_STATS,
    DS_DEFS_FULL_PROFILE,
    DS_DEFS_COUNT_PROFILE,
    DATASET_NAME_COUNT_PROFILE,
    DATASET_NAME_NO_PROFILE,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramSnowflakeUp:
    # NOTES:
    # - All data in this file uses the same base DS & updates the profile parameter and DS name
    # - Per JP, Filtergram is not a feature in snowflake connection.

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_snowflake_up_no_profile(self, api_utils):
        """Test analyze & estimate approved snowflake up with Profile = No Pushdown."""

        # Note: When the parameter "Profile Pushdown" is set to "No Pushdown", it is omitted.
        # None is the default, so the test can use a minimum payload here instead of a full dataset.
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            connection_name=CONN_NAME,
            dataset_name=DATASET_NAME_NO_PROFILE,
            query=QUERY,
            run_id=WHERE_DATE,
        )

        # Copy the payload objects and update the dataset name
        pl_ds_run_id = PL_DS_GEN.copy()
        pl_ds_stats = PL_DS_STATS.copy()
        pl_ds_stats["dataset"] = DATASET_NAME_NO_PROFILE
        pl_ds_run_id["dataset"] = DATASET_NAME_NO_PROFILE

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        job_result = helper.setup_dataset(api_utils, dataset_defs, WHERE_DATE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DATASET_NAME_NO_PROFILE, WHERE_DATE)
        aef.row_count(api_utils, pl_ds_stats, ROW_COUNT)
        aef.dataset_scan(api_utils, pl_ds_stats, EXP_DS_SCAN)
        aef.scoring(api_utils, pl_ds_run_id, EXP_DS_SCORE)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    @pytest.mark.smoke
    def test_analyze_estimate_filtergram_approved_snowflake_up_full_profile(self, api_utils):
        """Test analyze & estimate approved snowflake up with Profile Pushdown = Full Profile.
        # DEV-52156"""

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        job_result = helper.setup_dataset(api_utils, DS_DEFS_FULL_PROFILE, WHERE_DATE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_DEFS_FULL_PROFILE["dataset"], WHERE_DATE)
        aef.row_count(api_utils, PL_DS_STATS, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_GEN, EXP_DS_SCORE)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_snowflake_up_count_profile(self, api_utils):
        """Test analyze & estimate approved snowflake up with Profile Pushdown = Count. DEV-52156"""

        # Copy the payload objects and update the dataset name and profile parameter
        pl_ds_run_id = PL_DS_GEN.copy()
        pl_ds_stats = PL_DS_STATS.copy()
        pl_ds_stats["dataset"] = DATASET_NAME_COUNT_PROFILE
        pl_ds_run_id["dataset"] = DATASET_NAME_COUNT_PROFILE

        ds_defs = aef.rename_dataset_defs(DS_DEFS_FULL_PROFILE, DATASET_NAME_COUNT_PROFILE)
        ds_defs["profile"]["profilePushDown"] = DS_DEFS_COUNT_PROFILE

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        job_result = helper.setup_dataset(api_utils, ds_defs, WHERE_DATE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DATASET_NAME_COUNT_PROFILE, WHERE_DATE)
        aef.row_count(api_utils, pl_ds_stats, ROW_COUNT)
        aef.dataset_scan(api_utils, pl_ds_stats, EXP_DS_SCAN)
        aef.scoring(api_utils, pl_ds_run_id, EXP_DS_SCORE)
