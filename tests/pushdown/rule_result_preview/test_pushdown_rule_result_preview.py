import allure
import pytest

from data_test.pushdown.rule_result_preview.data_pd_athena_rule_result_preview_sales import (
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_bq_rule_result_preview_sales import (
    PD_BQ_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_BQ_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_BQ_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_BQ_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_dbrks_rule_result_preview_sales import (
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_mssql_rule_result_preview_sales import (
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_rs_rule_result_preview_sales import (
    PD_RS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_RS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_RS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_RS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_saph_rule_result_preview_sales import (
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)

# pylint: disable-next=line-too-long
from data_test.pushdown.rule_result_preview.data_pd_sf_rule_result_preview_filter_tolerance_sales import (
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION,
)
from data_test.pushdown.rule_result_preview.data_pd_sf_rule_result_preview_sales import (
    PD_SF_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_SF_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_SF_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_SF_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from data_test.pushdown.rule_result_preview.data_pd_trino_rule_result_preview_sales import (
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from payloads.pushdown.rule_result_preview.pl_pd_athena_rule_result_preview_sales import (
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_ATHENA_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_bq_rule_result_preview_sales import (
    PD_BQ_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_BQ_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_dbrks_rule_result_preview_sales import (
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_DBRKS_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_mssql_rule_result_preview_sales import (
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_MSSQL_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_rs_rule_result_preview_sales import (
    PD_RS_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_RS_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_saph_rule_result_preview_sales import (
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_SAPH_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.rule_result_preview.pl_pd_sf_rule_result_preview_filter_tolerance_sales import (
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_sf_rule_result_preview_sales import (
    PD_SF_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_SF_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from payloads.pushdown.rule_result_preview.pl_pd_trino_rule_result_preview_sales import (
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from utils.api_utils import APIUtils

from utils.helper import BaseHelper
from utils.validator import validate_rule_result_preview

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownRuleResultPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.athena
    def test_pushdown_athena_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_ATHENA_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_ATHENA_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_BQ_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_BQ_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.databricks
    def test_pushdown_databricks_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_DBRKS_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_DBRKS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.redshift
    def test_pushdown_redshift_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_RS_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_RS_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_RS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_RS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_RS_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_RS_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_RS_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.saphana
    def test_pushdown_saphana_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_SAPH_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_SAPH_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_SF_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_SF_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_SF_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_SF_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_SF_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_SF_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_SF_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_rule_result_preview_filter_tolerance_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW,
        )

        validate_rule_result_preview(
            api_utils,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW,
        )

        validate_rule_result_preview(
            api_utils,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION,
            PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_MSSQL_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_MSSQL_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown rule result preview")
    @pytest.mark.trino
    def test_pushdown_trino_rule_result_preview_sales(self, api_utils):
        helper.run_pushdown_job(api_utils, PD_TRINO_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )
