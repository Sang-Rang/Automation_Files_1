import allure
import pytest

from data_test.pullup.data_pullup_records_nyse import (
    PULLUP_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
)
from payloads.pullup.pl_pullup_records_nyse import (
    PULLUP_RECORDS_NYSE_DATASET,
    PULLUP_RECORDS_NYSE_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_observations import validate_records_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupRecords:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Record")
    def test_pullup_records_nyse(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_RECORDS_NYSE_PAYLOAD)

        validate_records_findings(
            api_utils,
            PULLUP_RECORDS_NYSE_DATASET,
            job_response["runId"],
            PULLUP_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
        )
