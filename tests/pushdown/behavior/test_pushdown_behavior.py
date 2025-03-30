import allure
import pytest

from data_test.pushdown.behavior.data_pd_athena_behavior_row_count_nyse import (
    PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_bq_behavior_row_count_nyse import (
    PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_dbrks_behavior_row_count_nyse import (
    PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_mssql_behavior_row_count_nyse import (
    PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_oracle_behavior_row_count_nyse import (
    PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
    PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
)
from data_test.pushdown.behavior.data_pd_rs_behavior_row_count_nyse import (
    PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_saph_behavior_row_count_nyse import (
    PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_sf_behavior_row_count_nyse import (
    PD_SF_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_SF_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from data_test.pushdown.behavior.data_pd_trino_behavior_row_count_nyse import (
    PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
    PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
)
from payloads.pushdown.behavior.pl_pd_athena_behavior_row_count_nyse import (
    PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_bq_behavior_row_count_nyse import (
    PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_dbrks_behavior_row_count_nyse import (
    PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_mssql_behavior_row_count_nyse import (
    PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_oracle_behavior_row_count_nyse import (
    PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_rs_behavior_row_count_nyse import (
    PD_RS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_RS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_saph_behavior_row_count_nyse import (
    PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_sf_behavior_row_count_nyse import (
    PD_SF_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_SF_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)
from payloads.pushdown.behavior.pl_pd_trino_behavior_row_count_nyse import (
    PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_behaviors import (
    validate_behavior_findings_overview,
    validate_row_count_findings_details,
)

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownBehavior:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.athena
    def test_pushdown_athena_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_ATHENA_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_BQ_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.databricks
    def test_pushdown_databricks_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_DBRKS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.oracle
    @pytest.mark.skip(reason="Skipped until DEV-116256 is deployed to 2025.05")
    def test_pushdown_oracle_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils,
                                               PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_ORACLE_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.redshift
    def test_pushdown_redshift_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_RS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_RS_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_RS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_RS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.saphana
    def test_pushdown_saphana_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_SAPH_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_SF_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_SF_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_SF_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_SF_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_SF_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_SF_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_MSSQL_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Behavior")
    @pytest.mark.trino
    def test_pushdown_trino_behavior_row_count_nyse(self, api_utils):
        required_backrun_count = 5
        helper.backrun_dataset_if_needed(
            api_utils, PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD, required_backrun_count
        )

        job_response = helper.run_pushdown_job(api_utils, PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_PAYLOAD)

        validate_behavior_findings_overview(
            api_utils,
            PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS,
        )
        validate_row_count_findings_details(
            api_utils,
            PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
            job_response["runId"],
            PD_TRINO_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS,
        )
