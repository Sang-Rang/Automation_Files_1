import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_dbrks_pd import (
    ROW_COUNT,
    PL_DAYS_WITH_DATA,
    EXP_DAYS_WITH,
    PL_DS_RUN_ID,
    EXP_DS_SCAN,
    EXP_DS_SCORE,
    PL_DS_STATS,
    DSDEFS,
    # EXP_FILTERGRAM, # Will need when defect resolved
    # PL_FILTERGRAM,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pushdown
@pytest.mark.databricks
class TestAnalyzeEstimateFiltergramDbrksPd:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_dbrks_pd(self, api_utils):
        """Run a basic DQ job on pushdown databricks"""

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        job_result = helper.run_pushdown_job(api_utils, DSDEFS)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DSDEFS["dataset"], DSDEFS["runId"])
        aef.row_count(api_utils, PL_DS_STATS, ROW_COUNT)
        aef.dataset_scan(api_utils, PL_DS_STATS, EXP_DS_SCAN)
        aef.scoring(api_utils, PL_DS_RUN_ID, EXP_DS_SCORE)

        # Defect for filtergram DEV-60127. Expected data will need updating.
        # aef.filtergram(api_utils, PL_FILTERGRAM, EXP_FILTERGRAM)
