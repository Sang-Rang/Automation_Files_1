import allure
import pytest

from data_test.pullup.data_pullup_behavior_row_count_nyse import (
    PULLUP_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PULLUP_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from payloads.pullup.pl_pullup_behavior_row_count_nyse import (
    PULLUP_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PULLUP_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_behaviors import (
    validate_behavior_findings_overview,
    validate_row_count_findings_details,
)

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupBehavior:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Behavior")
    def test_pullup_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PULLUP_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.setup_dataset(api_utils, PULLUP_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PULLUP_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PULLUP_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PULLUP_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PULLUP_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )
