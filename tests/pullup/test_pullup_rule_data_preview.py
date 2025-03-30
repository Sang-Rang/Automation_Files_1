import allure
import pytest

from data_test.pullup.data_pullup_rule_data_preview import (
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from payloads.pullup.pl_pullup_rule_data_preview_customers import (
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from utils.api_utils import APIUtils

from utils.helper import BaseHelper
from utils.validator import validate_rule_data_preview
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupRuleDataPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Rules")
    @allure.story("Pullup rule data preview")
    def test_pullup_rule_data_preview_sales(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
        )

        job_response = helper.setup_dataset(api_utils, PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            job_response["runId"],
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
        )

        validate_rule_data_preview(
            api_utils,
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            job_response["runId"],
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )
