import allure
import pytest

from data_test.pushdown.ai_rule_generation.data_pd_sf_ai_rule_generation import (
    PD_SF_AI_RULE_SALES_AI_PROMPT_PAYLOAD,
    PD_SF_AI_RULE_SALES_RULE_DEFINITION,
)
from payloads.pushdown.ai_rule_generation.pl_pd_sf_ai_rule_generation import (
    PD_SF_AI_RULE_SALES_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_rules import validate_pushdown_rule_validation

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushDownAIRuleCreation:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - AI Rule Generation")
    @pytest.mark.snowflake
    def test_pushdown_ai_rule_generation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_SF_AI_RULE_SALES_PAYLOAD)
        ai_rule = helper.generate_ai_rule(
            api_utils, PD_SF_AI_RULE_SALES_AI_PROMPT_PAYLOAD, PD_SF_AI_RULE_SALES_RULE_DEFINITION
        )
        validate_pushdown_rule_validation(
            api_utils,
            PD_SF_AI_RULE_SALES_PAYLOAD,
            ai_rule,
        )
