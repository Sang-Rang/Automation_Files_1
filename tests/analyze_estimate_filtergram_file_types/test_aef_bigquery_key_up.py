import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_bigquery_key_up import (
    WHERE_DATE,
    ROW_COUNT,
    PL_JOB_EST,
    EXP_JOB_EST,
    PL_DAYS_WITH_DATA,
    EXP_DAYS_WITH,
    PL_DS_RUN_ID,
    EXP_DS_SCAN,
    EXP_DS_SCORE,
    PL_DS_STATS,
    DS_DEFS_FULL_PROFILE,
    DATASET_NAME_NO_PROFILE,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramBigqueryKeyUp:
    # NOTES: All data used here the same base DS & updates the profile parameter and DS name

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_bigquery_key_up_no_profile(self, api_utils):
        """Test analyze & estimate approved bigquery_key up with Profile = No Pushdown"""

        # Copy the payload objects and update the dataset name and profile parameter
        ds_defs = aef.rename_dataset_defs(DS_DEFS_FULL_PROFILE, DATASET_NAME_NO_PROFILE)
        pl_ds_run_id = PL_DS_RUN_ID.copy()
        pl_ds_stats = PL_DS_STATS.copy()
        pl_ds_stats["dataset"] = DATASET_NAME_NO_PROFILE
        pl_ds_run_id["dataset"] = DATASET_NAME_NO_PROFILE

        # When the parameter "Profile Pushdown" is set to "No Pushdown", it is omitted.
        del ds_defs["profile"]["profilePushDown"]

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        job_result = helper.setup_dataset(api_utils, ds_defs, WHERE_DATE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DATASET_NAME_NO_PROFILE, WHERE_DATE)
        aef.row_count(api_utils, pl_ds_stats, ROW_COUNT)
        aef.dataset_scan(api_utils, pl_ds_stats, EXP_DS_SCAN)
        aef.scoring(api_utils, pl_ds_run_id, EXP_DS_SCORE)
