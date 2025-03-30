import allure
import pytest

from data_test.analyze_estimate_filtergram_file_types.data_aef_saphana_pd import (
    AEF_SAPH_PD_SPECIAL_CHARS_CONNECTION,
    AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
    AEF_SAPH_PD_SPECIAL_CHARS_DAYS_WITH_DATA_PARAMS,
    AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA,
    AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA_ROW_FILTER_SALE_STATE,
    AEF_SAPH_PD_SPECIAL_CHARS_ROW_FILTER_SALE_STATE_PARAMS,
    AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
    AEF_SAPH_PD_SPECIAL_CHARS_QUERY,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pushdown
@pytest.mark.saphana
class TestAnalyzeEstimateFiltergramSaphanaPd:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Connections - Analyze, Estimate, Filtergram")
    def test_analyze_estimate_filtergram_approved_saphana_pd_special_characters(self, api_utils):
        """Test analyze & estimate approved saphana pd with special characters in table name"""
        helper.get_minimum_job_payload(
            api_utils,
            connection_name=AEF_SAPH_PD_SPECIAL_CHARS_CONNECTION,
            dataset_name=AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
            query=AEF_SAPH_PD_SPECIAL_CHARS_QUERY,
            run_id=AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
        )

        aef.analyze(
            api_utils,
            AEF_SAPH_PD_SPECIAL_CHARS_DAYS_WITH_DATA_PARAMS,
            AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA,
        )
        aef.analyze(
            api_utils,
            AEF_SAPH_PD_SPECIAL_CHARS_ROW_FILTER_SALE_STATE_PARAMS,
            AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA_ROW_FILTER_SALE_STATE,
        )
        # Job does not run due to special characters in table name.
        # job_result = helper.run_pushdown_job(api_utils, dataset_defs)
        # assert_that(job_result["status"], "Job was not finished").is_equal_to("FINISHED")
        #
        # validate_job_timezone(
        #     api_utils,
        #     AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
        #     AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
        # )
        # aef.row_count(
        #     api_utils,
        #     {
        #         "dataset": AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
        #         "runId": AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
        #         "sense": 3,
        #     },
        #     AEF_SAPH_PD_SPECIAL_CHARS_ROW_COUNT,
        # )
        # aef.dataset_scan(
        #     api_utils,
        #     {
        #         "dataset": AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
        #         "runId": AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
        #     },
        #     AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DS_SCAN,
        # )
        # aef.scoring(
        #     api_utils,
        #     {
        #         "dataset": AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
        #         "runId": AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE,
        #     },
        #     AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_SCORE
        # )
        # aef.filtergram(
        #     api_utils,
        #     AEF_SAPH_PD_SPECIAL_CHARS_FILTERGRAM_PARAMS,
        #     AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_FILTERGRAM_OUTPUT,
        # )
