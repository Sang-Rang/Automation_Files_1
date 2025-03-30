import allure
import pytest

from data_test.pushdown.dupes.data_pd_bq_dupes_exact_case_employees_dt import (
    PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pushdown.dupes.data_pd_bq_dupes_exact_nocase_employees_dt import (
    PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from payloads.pushdown.dupes.pl_pd_bq_dupes_exact_case_employees_dt import (
    PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_DATASET,
    PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_PAYLOAD,
)
from payloads.pushdown.dupes.pl_pd_bq_dupes_exact_nocase_employees_dt import (
    PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_DATASET,
    PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_dupes import validate_dupes_findings


helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.bigquery
class TestPushdownDupesBigQuery:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Dupes")
    def test_pushdown_bigquery_dupes_exact_case_employees_dt(self, api_utils):
        job_response = helper.run_pushdown_job(
            api_utils, PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_PAYLOAD
        )

        validate_dupes_findings(
            api_utils,
            PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PD_BQ_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Dupes")
    def test_pushdown_bigquery_dupes_exact_nocase_employees_dt(self, api_utils):
        job_response = helper.run_pushdown_job(
            api_utils, PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_PAYLOAD
        )

        validate_dupes_findings(
            api_utils,
            PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PD_BQ_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )
