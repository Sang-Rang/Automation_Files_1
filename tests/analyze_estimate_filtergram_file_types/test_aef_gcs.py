import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_gcs import (
    WHERE_DATE,
    ROW_COUNT,
    PL_DAYS_WITH_DATA,
    PL_DS_GEN,
    PL_DS_STATS,
    PL_READ_REMOTE_FILE,
    EXP_READ_REMOTE_FILE,
    EXP_DS_SCAN,
    EXP_DS_SCORE,
    EXP_DAYS_WITH,
    DS_DEFS,
    PL_DS_STATS_GCS_PQ,
    ROW_COUNT_GCS_PQ,
    EXP_DS_SCORE_GCS_PQ,
    PL_DS_RUN_ID_GCS_PQ,
    EXP_DS_SCAN_GCS_PQ,
    DS_DEFS_GCS_PQ,
    DS_DEFS_GCS_JSON,
    PL_DS_STATS_GCS_JSON,
    ROW_COUNT_GCS_JSON,
    EXP_DS_SCAN_GCS_JSON,
    PL_DS_RUN_ID_GCS_JSON,
    EXP_DS_SCORE_GCS_JSON,
    # PL_JOB_EST,
    # PL_FILTERGRAM,
    # EXP_JOB_EST,
    # EXP_FILTERGRAM,
    # EXP_FILTERGRAM,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramGcs:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    @pytest.mark.xfail(run=True, reason="Passes when run during the day, fails on nightly runs")
    def test_analyze_estimate_filtergram_gcs_up_csv(self, api_utils):
        """Test analyze, estimate, filtergram approved GCS remote file"""

        aef.read_remote_file(api_utils, PL_READ_REMOTE_FILE, EXP_READ_REMOTE_FILE)
        aef.analyze_file(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)

        # Bug DEV-60712. Uncomment & run when fixed, no data changes needed. Uncomment imports
        # aef.job_estimator_file(api_utils, PL_JOB_EST, EXP_JOB_EST)

        job_result = helper.setup_dataset(api_utils, DS_DEFS, WHERE_DATE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_DEFS["dataset"], WHERE_DATE)
        aef.row_count(api_utils, PL_DS_STATS, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_GEN, EXP_DS_SCORE)

        # Bug DEV-60127. Uncomment & run when fixed, expected data needs updating. Uncomment imports
        # aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM) # failing DEV-60127

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_gcs_up_json(self, api_utils):
        """Test Create job with GCS JSON remote file"""

        job_result = helper.setup_dataset(api_utils, DS_DEFS_GCS_JSON)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Validate some basic data on the job
        aef.row_count(api_utils, PL_DS_STATS_GCS_JSON, ROW_COUNT_GCS_JSON)
        aef.dataset_scan(api_utils, PL_DS_STATS_GCS_JSON, EXP_DS_SCAN_GCS_JSON)
        aef.scoring(api_utils, PL_DS_RUN_ID_GCS_JSON, EXP_DS_SCORE_GCS_JSON)

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_gcs_up_parquet(self, api_utils):
        """Test Create job with GCS Parquet remote file"""

        job_result = helper.setup_dataset(api_utils, DS_DEFS_GCS_PQ)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")

        # Validate some basic data on the job
        aef.row_count(api_utils, PL_DS_STATS_GCS_PQ, ROW_COUNT_GCS_PQ)
        aef.dataset_scan(api_utils, PL_DS_STATS_GCS_PQ, EXP_DS_SCAN_GCS_PQ)
        aef.scoring(api_utils, PL_DS_RUN_ID_GCS_PQ, EXP_DS_SCORE_GCS_PQ)
