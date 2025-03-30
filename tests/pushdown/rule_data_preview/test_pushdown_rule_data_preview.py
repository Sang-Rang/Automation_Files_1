import allure
import pytest

from data_test.pushdown.rule_data_preview.data_pd_athena_rule_data_preview_customers import (
    PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_bq_rule_data_preview_customers import (
    PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_dbrks_rule_data_preview_customers import (
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_mssql_rule_data_preview_customers import (
    PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_rs_rule_data_preview_customers import (
    PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_saph_rule_data_preview_customers import (
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_sf_rule_data_preview_customers import (
    PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from data_test.pushdown.rule_data_preview.data_pd_trino_rule_data_preview_customers import (
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
)
from payloads.pushdown.rule_data_preview.pl_pd_athena_rule_data_preview_customers import (
    PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_bq_rule_data_preview_customers import (
    PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_dbrks_rule_data_preview_customers import (
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_mssql_rule_data_preview_customers import (
    PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_rs_rule_data_preview_customers import (
    PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_saph_rule_data_preview_customers import (
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_sf_rule_data_preview_customers import (
    PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from payloads.pushdown.rule_data_preview.pl_pd_trino_rule_data_preview_customers import (
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_rule_data_preview
from utils.validator_rules import validate_rules_findings

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownRuleDataPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def run_rule_data_preview_test(
        api_utils,
        dataset_defs,
        rule_defs,
        rule_name,
        expected_rule_output,
        expected_rule_data_preview,
    ):
        dataset_name = dataset_defs["dataset"]

        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, dataset_defs)
        helper.set_rules_on_dataset(api_utils, dataset_name, rule_defs)

        job_response = helper.run_pushdown_job(api_utils, dataset_defs)

        validate_rules_findings(
            api_utils, dataset_name, job_response["runId"], expected_rule_output
        )

        validate_rule_data_preview(
            api_utils,
            dataset_name,
            job_response["runId"],
            rule_name,
            expected_rule_data_preview,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.athena
    def test_pushdown_athena_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_ATHENA_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.databricks
    def test_pushdown_databricks_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.redshift
    def test_pushdown_redshift_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_RS_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.saphana
    def test_pushdown_saphana_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_SF_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_MSSQL_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rule Data Preview")
    @pytest.mark.trino
    def test_pushdown_trino_rule_data_preview_customers(self, api_utils):
        self.run_rule_data_preview_test(
            api_utils,
            PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD,
            PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS,
            PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT,
            PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW,
        )
