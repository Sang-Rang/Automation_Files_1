import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_rule_definitions import (
    RULE_DEFINITIONS_RULE_DEFINITIONS,
    RULE_DEFINITIONS_RULE_DEFINITIONS_UPDATED,
    RULE_DEFINITIONS_RULE_NAME,
    INITIAL_BUSINESS_DESCRIPTION,
    UPDATED_BUSINESS_DESCRIPTION,
)
from endpoints.v3.rule_api import (
    V3_RULES_DEFINITIONS,
    V3_RULES_DATASET,
    V3_RULES_DATASET_RULENAME,
)
from payloads.pullup.pl_rule_definitions import (
    RULE_DEFINITIONS_PAYLOAD,
    RULE_DEFINITIONS_DATASET,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestRuleDefinitions:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def get_rule_definitions(api_utils):
        return api_utils.get(V3_RULES_DEFINITIONS)

    @allure.feature("Pullup")
    @allure.story("Rule Definitions")
    def test_rule_definitions(self, api_utils):
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, RULE_DEFINITIONS_PAYLOAD)

        api_utils.delete(
            V3_RULES_DATASET.format(dataset=RULE_DEFINITIONS_DATASET), return_json=False
        )

        rule_definition_output = self.get_rule_definitions(api_utils)

        rule_exists = helper.rule_exists_in_rule_definitions(
            rule_definition_output,
            RULE_DEFINITIONS_DATASET,
            RULE_DEFINITIONS_RULE_NAME,
            UPDATED_BUSINESS_DESCRIPTION,
        )

        (
            assert_that(
                rule_exists,
                "Expected: Rule doesn't exist in the rule definition list. Actual: Rule exists.",
            ).is_false()
        )

        helper.set_rules_on_dataset(
            api_utils, RULE_DEFINITIONS_DATASET, RULE_DEFINITIONS_RULE_DEFINITIONS
        )

        rule_definition_output_with_rule = self.get_rule_definitions(api_utils)

        rule_exists = helper.rule_exists_in_rule_definitions(
            rule_definition_output_with_rule,
            RULE_DEFINITIONS_DATASET,
            RULE_DEFINITIONS_RULE_NAME,
            INITIAL_BUSINESS_DESCRIPTION,
        )

        (
            assert_that(
                rule_exists,
                "Expected: Rule exists in the rule definition list. Actual: Rule doesn't exist.",
            ).is_true()
        )

        helper.update_rules_on_dataset(
            api_utils, RULE_DEFINITIONS_DATASET, RULE_DEFINITIONS_RULE_DEFINITIONS_UPDATED
        )

        rule_definition_output_with_updated_rule = self.get_rule_definitions(api_utils)

        rule_exists = helper.rule_exists_in_rule_definitions(
            rule_definition_output_with_updated_rule,
            RULE_DEFINITIONS_DATASET,
            RULE_DEFINITIONS_RULE_NAME,
            UPDATED_BUSINESS_DESCRIPTION,
        )

        (
            assert_that(
                rule_exists,
                "Expected: Rule exists in the rule definition list. Actual: Rule doesn't exist.",
            ).is_true()
        )

        api_utils.delete(
            V3_RULES_DATASET_RULENAME.format(
                dataset=RULE_DEFINITIONS_DATASET,
                rulename=RULE_DEFINITIONS_RULE_NAME,
            ),
            return_json=False,
        )

        rule_definition_output_after_deleting_rule = self.get_rule_definitions(api_utils)

        rule_exists = helper.rule_exists_in_rule_definitions(
            rule_definition_output_after_deleting_rule,
            RULE_DEFINITIONS_DATASET,
            RULE_DEFINITIONS_RULE_NAME,
            UPDATED_BUSINESS_DESCRIPTION,
        )

        (
            assert_that(
                rule_exists,
                "Expected: Rule doesn't exist in the rule definition list. Actual: Rule exists.",
            ).is_false()
        )
