import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_oracle_up import (
    DS_CON_ORACLE,
    C_NAME_CON_ORACLE,
    QUERY_CON_ORACLE,
    WHERE_DATE_CON_ORACLE,
    PL_GENERAL_CON_ORACLE,
    PL_TABLE_STATS_CON_ORACLE,
    PL_FG_CON_ORACLE,
    PL_DAYS_WITH_DATA_CON_ORACLE,
    EX_FG_CON_ORACLE,
    EX_JOB_CON_ORACLE,
    EX_DAYS_WITH_CON_ORACLE,
    EX_DS_SCAN_CON_ORACLE,
    EX_DS_SCORING_CON_ORACLE,
    ROW_COUNT_CON_ORACLE,
    PL_JOB_EST_CON_ORACLE_NO_LIMIT,
    PL_JOB_EST_CON_ORACLE_LIMIT,
    EX_ESTIMATE_CON_ORACLE,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_job_timezone

helper = BaseHelper()


@pytest.mark.pullup_aef
class TestAnalyzeEstimateFiltergramOracleUp:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_oracle_up(self, api_utils):
        """Connections: Oracle - Analyze, Estimate, Filtergram DEV-48907, DEV-52141"""

        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            C_NAME_CON_ORACLE,
            DS_CON_ORACLE,
            QUERY_CON_ORACLE,
            WHERE_DATE_CON_ORACLE,
        )

        aef = AnalyzeEstimateFiltergram()
        aef.analyze(api_utils, PL_DAYS_WITH_DATA_CON_ORACLE, EX_DAYS_WITH_CON_ORACLE)
        aef.job_estimator(api_utils, PL_JOB_EST_CON_ORACLE_LIMIT, EX_JOB_CON_ORACLE)
        aef.job_estimator(api_utils, PL_JOB_EST_CON_ORACLE_NO_LIMIT, EX_ESTIMATE_CON_ORACLE)
        job_result = helper.setup_dataset(api_utils, dataset_defs, WHERE_DATE_CON_ORACLE)
        aef.validate_job_cmdline(api_utils, job_result)
        assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        validate_job_timezone(api_utils, DS_CON_ORACLE, WHERE_DATE_CON_ORACLE)
        aef.row_count(api_utils, PL_TABLE_STATS_CON_ORACLE, ROW_COUNT_CON_ORACLE)
        aef.dataset_scan(api_utils, PL_GENERAL_CON_ORACLE, EX_DS_SCAN_CON_ORACLE)
        aef.scoring(api_utils, PL_GENERAL_CON_ORACLE, EX_DS_SCORING_CON_ORACLE)
        aef.filtergram(api_utils, PL_FG_CON_ORACLE, EX_FG_CON_ORACLE)
