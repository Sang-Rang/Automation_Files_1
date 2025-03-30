import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_s3 import (
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
    DS_DEFS, PL_READ_REMOTE_FILE_PIPE, EXP_READ_REMOTE_FILE_PIPE, PL_DS_STATS_PIPE, PL_DS_RID_PIPE,
    DS_DEFS_PIPE, PL_READ_REMOTE_FILE_JSON, EXP_READ_REMOTE_FILE_JSON, PL_DS_STATS_JSON,
    PL_DS_RID_JSON, DS_DEFS_JSON, EXP_DS_SCORE_JSON, EXP_DAYS_WITH_PQT, PL_DAYS_WITH_DATA_PQT,
    EXP_READ_REMOTE_FILE_PQT, PL_READ_REMOTE_FILE_PQT, DS_DEFS_PQT, PL_DS_STATS_PQT, PL_DS_RID_PQT,
    WHERE_DATE_PQT, EXP_DS_SCORE_PQT,
    # PL_JOB_EST,
    # PL_FILTERGRAM,
    # EXP_JOB_EST,
    # EXP_FILTERGRAM,
    # EXP_FILTERGRAM,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramS3:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    @pytest.mark.xfail(run=True, reason="Known issue, connection goes down often")
    def test_analyze_estimate_filtergram_s3_up_csv(self, api_utils):
        """Test analyze, estimate, filtergram approved s3 csv remote file"""

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
    @pytest.mark.xfail(run=True, reason="Known issue, connection goes down often")
    def test_analyze_estimate_filtergram_s3_up_pipe(self, api_utils):
        """Test analyze, estimate, filtergram approved s3 csv remote file with pipe delimiter"""

        aef.read_remote_file(api_utils, PL_READ_REMOTE_FILE_PIPE, EXP_READ_REMOTE_FILE_PIPE)
        # NOTE: No date data for analyze

        # Bug DEV-60712. Uncomment & run when fixed, no data changes needed. Uncomment imports
        # aef.job_estimator_file(api_utils, PL_JOB_EST, EXP_JOB_EST)

        job_result = helper.setup_dataset(api_utils, DS_DEFS_PIPE)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_DEFS_PIPE["dataset"], PROD_RUN_ID)
        aef.row_count(api_utils, PL_DS_STATS_PIPE, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS_PIPE, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_RID_PIPE, EXP_DS_SCORE)

        # Bug DEV-60127. Uncomment & run when fixed, expected data needs updating. Uncomment imports
        # aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM) # failing DEV-60127

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    @pytest.mark.xfail(run=True, reason="Known issue, connection goes down often")
    def test_analyze_estimate_filtergram_s3_up_json(self, api_utils):
        """Test analyze, estimate, filtergram approved s3 json remote file"""

        aef.read_remote_file(api_utils, PL_READ_REMOTE_FILE_JSON, EXP_READ_REMOTE_FILE_JSON)
        # NOTE: No date data for analyze

        # Bug DEV-60712. Uncomment & run when fixed, no data changes needed. Uncomment imports
        # aef.job_estimator_file(api_utils, PL_JOB_EST, EXP_JOB_EST)

        job_result = helper.setup_dataset(api_utils, DS_DEFS_JSON)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_DEFS_JSON["dataset"], PROD_RUN_ID)
        aef.row_count(api_utils, PL_DS_STATS_JSON, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS_JSON, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_RID_JSON, EXP_DS_SCORE_JSON)

        # Bug DEV-60127. Uncomment & run when fixed, expected data needs updating. Uncomment imports
        # aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM) # failing DEV-60127

    @allure.feature("Remote Files")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    @pytest.mark.xfail(run=True, reason="Known issue, connection goes down often")
    def test_analyze_estimate_filtergram_s3_up_pqt(self, api_utils):
        """Test analyze, estimate, filtergram approved s3 parquet remote file"""

        aef.read_remote_file(api_utils, PL_READ_REMOTE_FILE_PQT, EXP_READ_REMOTE_FILE_PQT)
        aef.analyze_file(api_utils, PL_DAYS_WITH_DATA_PQT, EXP_DAYS_WITH_PQT)

        # Bug DEV-60712. Uncomment & run when fixed, no data changes needed. Uncomment imports
        # aef.job_estimator_file(api_utils, PL_JOB_EST, EXP_JOB_EST)

        job_result = helper.setup_dataset(api_utils, DS_DEFS_PQT, WHERE_DATE_PQT)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_DEFS_PQT["dataset"], WHERE_DATE_PQT)
        aef.row_count(api_utils, PL_DS_STATS_PQT, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS_PQT, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_RID_PQT, EXP_DS_SCORE_PQT)

        # Bug DEV-60127. Uncomment & run when fixed, expected data needs updating. Uncomment imports
        # aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM) # failing DEV-60127
