import allure
import pytest

from data_test.pullup.data_pullup_schema_sales import PULLUP_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS
from payloads.pullup.pl_pullup_schema_sales import (
    PULLUP_SCHEMA_SALES_DATASET,
    PULLUP_SCHEMA_SALES_MISSING_COLUMN_PAYLOAD,
    PULLUP_SCHEMA_SALES_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_observations import validate_schema_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupSchema:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Schema")
    def test_pullup_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PULLUP_SCHEMA_SALES_PAYLOAD,
            int(PULLUP_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.setup_dataset(
            api_utils, PULLUP_SCHEMA_SALES_MISSING_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PULLUP_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PULLUP_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )
