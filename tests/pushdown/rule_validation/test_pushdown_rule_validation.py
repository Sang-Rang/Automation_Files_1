import allure
import pytest

from data_test.pushdown.rule_validation.data_pd_athena_rule_validation_sales import (
    PD_ATHENA_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rule_validation.data_pd_saph_rule_validation_sales import (
    PD_SAPH_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_athena_rules_basic import (
    PD_ATHENA_RULES_BASIC_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_athena_rules_nyse import PD_ATHENA_RULES_NYSE_RULE_DEFINITIONS
from data_test.pushdown.rule_validation.data_pd_bq_rule_validation_sales import (
    PD_BQ_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
    PD_BQ_RULE_VALIDATION_SALES_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rules.data_pd_bq_rules_basic import (
    PD_BQ_RULES_BASIC_RULE_DEFINITIONS,
    PD_BQ_RULES_BASIC_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rules.data_pd_bq_rules_nyse import (
    PD_BQ_RULES_NYSE_RULE_DEFINITIONS,
    PD_BQ_RULES_NYSE_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rule_validation.data_pd_dbrks_rule_validation_sales import (
    PD_DBRKS_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_basic import PD_DBRKS_RULES_BASIC_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_dbrks_rules_nyse import PD_DBRKS_RULES_NYSE_RULE_DEFINITIONS
from data_test.pushdown.rule_validation.data_pd_rs_rule_validation_sales import (
    PD_RS_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_rs_rules_basic import PD_RS_RULES_BASIC_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_rs_rules_nyse import PD_RS_RULES_NYSE_RULE_DEFINITIONS
from data_test.pushdown.rule_validation.data_pd_sf_rule_validation_sales import (
    PD_SF_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_saph_rules_basic import PD_SAPH_RULES_BASIC_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_saph_rules_nyse import PD_SAPH_RULES_NYSE_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_sf_rules_basic import PD_SF_RULES_BASIC_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_sf_rules_filter_tolerance_sales import (
    PD_SF_RULES_FILTER_TOLERANCE_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_sf_rules_nyse import PD_SF_RULES_NYSE_RULE_DEFINITIONS
from data_test.pushdown.rule_validation.data_pd_trino_rule_validation_sales import (
    PD_TRINO_RULE_VALIDATION_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_trino_rules_basic import PD_TRINO_RULES_BASIC_RULE_DEFINITIONS
from data_test.pushdown.rules.data_pd_trino_rules_nyse import PD_TRINO_RULES_NYSE_RULE_DEFINITIONS
from payloads.pushdown.rule_validation.pl_pd_athena_rule_validation_sales import (
    PD_ATHENA_RULE_VALIDATION_SALES_PAYLOAD,
    PD_ATHENA_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rule_validation.pl_pd_saph_rule_validation_sales import (
    PD_SAPH_RULE_VALIDATION_SALES_PAYLOAD,
    PD_SAPH_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_athena_rules_basic import PD_ATHENA_RULES_BASIC_PAYLOAD
from payloads.pushdown.rules.pl_pd_athena_rules_nyse import PD_ATHENA_RULES_NYSE_PAYLOAD
from payloads.pushdown.rule_validation.pl_pd_bq_rule_validation_sales import (
    PD_BQ_RULE_VALIDATION_SALES_PAYLOAD,
    PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_bq_rules_basic import PD_BQ_RULES_BASIC_PAYLOAD
from payloads.pushdown.rules.pl_pd_bq_rules_nyse import PD_BQ_RULES_NYSE_PAYLOAD
from payloads.pushdown.rules.pl_pd_dbrks_rules_basic import PD_DBRKS_RULES_BASIC_PAYLOAD
from payloads.pushdown.rule_validation.pl_pd_dbrks_rule_validation_sales import (
    PD_DBRKS_RULE_VALIDATION_SALES_PAYLOAD,
    PD_DBRKS_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_nyse import PD_DBRKS_RULES_NYSE_PAYLOAD
from payloads.pushdown.rule_validation.pl_pd_rs_rule_validation_sales import (
    PD_RS_RULE_VALIDATION_SALES_PAYLOAD,
    PD_RS_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_rs_rules_basic import PD_RS_RULES_BASIC_PAYLOAD
from payloads.pushdown.rules.pl_pd_rs_rules_nyse import PD_RS_RULES_NYSE_PAYLOAD
from payloads.pushdown.rules.pl_pd_saph_rules_basic import PD_SAPH_RULES_BASIC_PAYLOAD
from payloads.pushdown.rules.pl_pd_saph_rules_nyse import PD_SAPH_RULES_NYSE_PAYLOAD
from payloads.pushdown.rules.pl_pd_sf_rules_basic import PD_SF_RULES_BASIC_PAYLOAD
from payloads.pushdown.rule_validation.pl_pd_sf_rule_validation_sales import (
    PD_SF_RULE_VALIDATION_SALES_PAYLOAD,
    PD_SF_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_sf_rules_filter_tolerance_sales import (
    PD_SF_RULES_FILTER_TOLERANCE_SALES_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_sf_rules_nyse import PD_SF_RULES_NYSE_PAYLOAD
from payloads.pushdown.rule_validation.pl_pd_trino_rule_validation_sales import (
    PD_TRINO_RULE_VALIDATION_SALES_PAYLOAD,
    PD_TRINO_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_trino_rules_basic import PD_TRINO_RULES_BASIC_PAYLOAD
from payloads.pushdown.rules.pl_pd_trino_rules_nyse import PD_TRINO_RULES_NYSE_PAYLOAD

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_rules import validate_pushdown_rule_validation

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownRuleValidation:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.athena
    def test_pushdown_athena_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_ATHENA_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_ATHENA_RULES_BASIC_PAYLOAD

        for rule in PD_ATHENA_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                     api_utils,
                     dataset_defs,
                     rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.athena
    def test_pushdown_athena_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_ATHENA_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_ATHENA_RULES_NYSE_PAYLOAD

        for rule in PD_ATHENA_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.athena
    def test_pushdown_athena_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_ATHENA_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_ATHENA_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_ATHENA_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_ATHENA_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_BQ_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_BQ_RULES_BASIC_PAYLOAD

        for rule in PD_BQ_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                rule_name = rule["ruleNm"]
                for output in PD_BQ_RULES_BASIC_EXPECTED_RULE_OUTPUT["data"]:
                    if output["ruleNm"] == rule["ruleNm"]:
                        expected_rule_output = output
                        break
                else:
                    raise ValueError(f"No expected output found for rule {rule_name}")
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                    expected_rule_output=expected_rule_output,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_BQ_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_BQ_RULES_NYSE_PAYLOAD

        for rule in PD_BQ_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                rule_name = rule["ruleNm"]
                for output in PD_BQ_RULES_NYSE_EXPECTED_RULE_OUTPUT["data"]:
                    if output["ruleNm"] == rule["ruleNm"]:
                        expected_rule_output = output
                        break
                else:
                    raise ValueError(f"No expected output found for rule {rule_name}")
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                    expected_rule_output=expected_rule_output,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.bigquery
    @pytest.mark.skip(reason="Enable when DEV-86067 is resolved")
    def test_pushdown_bigquery_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_BQ_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_BQ_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_BQ_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                rule_name = rule["ruleNm"]
                for output in PD_BQ_RULE_VALIDATION_SALES_EXPECTED_RULE_OUTPUT["data"]:
                    if output["ruleNm"] == rule["ruleNm"]:
                        expected_rule_output = output
                        break
                else:
                    raise ValueError(f"No expected output found for rule {rule_name}")
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                    expected_rule_output=expected_rule_output,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.databricks
    def test_pushdown_databricks_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_DBRKS_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_DBRKS_RULES_BASIC_PAYLOAD

        for rule in PD_DBRKS_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.databricks
    def test_pushdown_databricks_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_DBRKS_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_DBRKS_RULES_NYSE_PAYLOAD

        for rule in PD_DBRKS_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.databricks
    def test_pushdown_databricks_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_DBRKS_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_DBRKS_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.redshift
    def test_pushdown_redshift_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_RS_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_RS_RULES_BASIC_PAYLOAD

        for rule in PD_RS_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.redshift
    def test_pushdown_redshift_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_RS_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_RS_RULES_NYSE_PAYLOAD

        for rule in PD_RS_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.redshift
    def test_pushdown_redshift_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_RS_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_RS_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_RS_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_RS_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.saphana
    def test_pushdown_saphana_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_SAPH_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_SAPH_RULES_BASIC_PAYLOAD

        for rule in PD_SAPH_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.saphana
    def test_pushdown_saphana_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_SAPH_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_SAPH_RULES_NYSE_PAYLOAD

        for rule in PD_SAPH_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.saphana
    def test_pushdown_saphana_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_SAPH_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_SAPH_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_SAPH_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_SAPH_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_SF_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_SF_RULES_BASIC_PAYLOAD

        for rule in PD_SF_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_SF_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_SF_RULES_NYSE_PAYLOAD

        for rule in PD_SF_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_SF_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_SF_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_SF_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_SF_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_validation_filter_tolerance_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_SF_RULES_FILTER_TOLERANCE_SALES_PAYLOAD
        )
        dataset_defs = PD_SF_RULES_FILTER_TOLERANCE_SALES_PAYLOAD

        for rule in PD_SF_RULES_FILTER_TOLERANCE_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.trino
    def test_pushdown_trino_rule_validation_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_TRINO_RULES_BASIC_PAYLOAD)
        dataset_defs = PD_TRINO_RULES_BASIC_PAYLOAD

        for rule in PD_TRINO_RULES_BASIC_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.trino
    def test_pushdown_trino_rule_validation_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_TRINO_RULES_NYSE_PAYLOAD)
        dataset_defs = PD_TRINO_RULES_NYSE_PAYLOAD

        for rule in PD_TRINO_RULES_NYSE_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Validation")
    @pytest.mark.trino
    def test_pushdown_trino_rule_validation_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_TRINO_RULE_VALIDATION_SALES_PAYLOAD
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_TRINO_RULE_VALIDATION_SALES_SECONDARY_DATASET_PAYLOAD
        )
        dataset_defs = PD_TRINO_RULE_VALIDATION_SALES_PAYLOAD

        for rule in PD_TRINO_RULE_VALIDATION_SALES_RULE_DEFINITIONS:
            if (
                rule["ruleType"] in ["SQLF", "SQLG"]
                and "EXCEPTION" not in str(rule["ruleNm"]).upper()
            ):
                rule_definition = rule
                validate_pushdown_rule_validation(
                    api_utils,
                    dataset_defs,
                    rule_definition,
                )
