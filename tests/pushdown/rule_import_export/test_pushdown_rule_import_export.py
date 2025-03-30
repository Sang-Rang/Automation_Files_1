import allure
import pytest
from assertpy import assert_that

from data_test.pushdown.rule_import_export.data_pd_sf_rules_import_export import (
    PD_SF_RULES_IMPORT_EXPORT_RULE_DEFINITIONS,
)
from endpoints.v3.rule_api import V3_RULES_DATASET
from payloads.pushdown.rule_import_export.pl_pd_sf_rules_import_export import (
    PD_SF_RULES_IMPORT_EXPORT_DATASET,
    PD_SF_RULES_IMPORT_EXPORT_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownRuleImportExport:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule import/export")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_export_rules(self, api_utils):
        """Verify exported rules match json used to create rules."""
        helper.run_pushdown_job(
            api_utils, PD_SF_RULES_IMPORT_EXPORT_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_SF_RULES_IMPORT_EXPORT_DATASET,
            PD_SF_RULES_IMPORT_EXPORT_RULE_DEFINITIONS,
        )

        exported_rules = api_utils.get(
            V3_RULES_DATASET.format(dataset=PD_SF_RULES_IMPORT_EXPORT_DATASET)
        )

        rule_count = len(PD_SF_RULES_IMPORT_EXPORT_RULE_DEFINITIONS)
        exported_rule_count = len(exported_rules)

        assert_that(
            exported_rule_count,
            f"Expected {rule_count} rules.  Found {exported_rule_count} rules exported.",
        ).is_equal_to(rule_count)

        for rule in PD_SF_RULES_IMPORT_EXPORT_RULE_DEFINITIONS:
            assert_that(
                exported_rules, f"Expected {rule} to be in exported rule data {exported_rules}."
            ).contains(rule)
