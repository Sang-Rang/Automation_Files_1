import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_postgres_up import (
    WHERE_DATE,
    DATASET,
    QUERY,
    CONN_NAME,
    ROW_COUNT,
    PL_FILTERGRAM,
    PL_JOB_EST,
    EXP_JOB_EST,
    PL_DAYS_WITH_DATA,
    EXP_DAYS_WITH,
    PL_DS_GEN,
    EXP_DS_SCAN,
    EXP_DS_SCORE,
    PL_DS_STATS,
    EXP_FILTERGRAM,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramPostgresUp:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_postgres_up(self, api_utils):
        """Test analyze, estimate, filtergram approved postgres up"""

        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            connection_name=CONN_NAME,
            dataset_name=DATASET,
            query=QUERY,
            run_id=WHERE_DATE,
        )

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        job_result = helper.setup_dataset(api_utils, dataset_defs, WHERE_DATE)
        aef.validate_job_cmdline(api_utils, job_result)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DATASET, WHERE_DATE)
        aef.row_count(api_utils, PL_DS_STATS, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_GEN, EXP_DS_SCORE)
        aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM)
