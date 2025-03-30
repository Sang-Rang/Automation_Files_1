import allure
import pytest

from data_test.pushdown.records.data_pd_trino_records_nyse import (
    PD_TRINO_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
)
from payloads.pushdown.records.pl_pd_trino_records_nyse import (
    PD_TRINO_RECORDS_NYSE_DATASET,
    PD_TRINO_RECORDS_NYSE_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_observations import validate_records_findings

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.trino
class TestPushdownRecordsTrino:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Records")
    def test_pushdown_trino_records_nyse(self, api_utils):
        job_response = helper.run_pushdown_job(api_utils, PD_TRINO_RECORDS_NYSE_PAYLOAD)

        validate_records_findings(
            api_utils,
            PD_TRINO_RECORDS_NYSE_DATASET,
            job_response["runId"],
            PD_TRINO_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
        )
