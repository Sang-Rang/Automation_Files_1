import allure
import pytest

from data_test.pushdown.schema.data_pd_athena_schema_sales import (
    PD_ATHENA_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_bq_schema_sales import (
    PD_BQ_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_dbrks_schema_sales import (
    PD_DBRKS_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_mssql_schema_sales import (
    PD_MSSQL_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_rs_schema_sales import (
    PD_RS_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_saph_schema_sales import (
    PD_SAPH_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_sf_schema_sales import (
    PD_SF_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from data_test.pushdown.schema.data_pd_trino_schema_sales import (
    PD_TRINO_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
)
from payloads.pushdown.schema.pl_pd_athena_schema_sales import (
    PD_ATHENA_SCHEMA_SALES_DATASET,
    PD_ATHENA_SCHEMA_SALES_PAYLOAD,
    PD_ATHENA_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_bq_schema_sales import (
    PD_BQ_SCHEMA_SALES_DATASET,
    PD_BQ_SCHEMA_SALES_PAYLOAD,
    PD_BQ_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_dbrks_schema_sales import (
    PD_DBRKS_SCHEMA_SALES_DATASET,
    PD_DBRKS_SCHEMA_SALES_PAYLOAD,
    PD_DBRKS_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_mssql_schema_sales import (
    PD_MSSQL_SCHEMA_SALES_DATASET,
    PD_MSSQL_SCHEMA_SALES_PAYLOAD,
    PD_MSSQL_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_rs_schema_sales import (
    PD_RS_SCHEMA_SALES_DATASET,
    PD_RS_SCHEMA_SALES_PAYLOAD,
    PD_RS_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_saph_schema_sales import (
    PD_SAPH_SCHEMA_SALES_DATASET,
    PD_SAPH_SCHEMA_SALES_PAYLOAD,
    PD_SAPH_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_sf_schema_sales import (
    PD_SF_SCHEMA_SALES_DATASET,
    PD_SF_SCHEMA_SALES_PAYLOAD,
    PD_SF_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from payloads.pushdown.schema.pl_pd_trino_schema_sales import (
    PD_TRINO_SCHEMA_SALES_DATASET,
    PD_TRINO_SCHEMA_SALES_PAYLOAD,
    PD_TRINO_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_observations import validate_schema_findings

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownSchema:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.athena
    def test_pushdown_athena_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_ATHENA_SCHEMA_SALES_PAYLOAD,
            int(PD_ATHENA_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_ATHENA_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PD_ATHENA_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_ATHENA_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_BQ_SCHEMA_SALES_PAYLOAD,
            int(PD_BQ_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(api_utils, PD_BQ_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD)

        validate_schema_findings(
            api_utils,
            PD_BQ_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_BQ_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.databricks
    def test_pushdown_databricks_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_DBRKS_SCHEMA_SALES_PAYLOAD,
            int(PD_DBRKS_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_DBRKS_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PD_DBRKS_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_DBRKS_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.redshift
    def test_pushdown_redshift_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_RS_SCHEMA_SALES_PAYLOAD,
            int(PD_RS_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(api_utils, PD_RS_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD)

        validate_schema_findings(
            api_utils,
            PD_RS_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_RS_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.saphana
    def test_pushdown_saphana_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_SAPH_SCHEMA_SALES_PAYLOAD,
            int(PD_SAPH_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SAPH_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PD_SAPH_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_SAPH_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_SF_SCHEMA_SALES_PAYLOAD,
            int(PD_SF_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(api_utils, PD_SF_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD)

        validate_schema_findings(
            api_utils,
            PD_SF_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_SF_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_MSSQL_SCHEMA_SALES_PAYLOAD,
            int(PD_MSSQL_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_MSSQL_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PD_MSSQL_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_MSSQL_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Schema")
    @pytest.mark.trino
    def test_pushdown_trino_schema_sales(self, api_utils):
        helper.backrun_dataset_if_needed(
            api_utils,
            PD_TRINO_SCHEMA_SALES_PAYLOAD,
            int(PD_TRINO_SCHEMA_SALES_PAYLOAD["profile"]["behaviorMinSupport"]),
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_SCHEMA_SALES_REMOVED_COLUMN_PAYLOAD
        )

        validate_schema_findings(
            api_utils,
            PD_TRINO_SCHEMA_SALES_DATASET,
            job_response["runId"],
            PD_TRINO_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS,
        )
