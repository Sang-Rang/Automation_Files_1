import allure
import pytest

# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_athena_finding_page_data_preview_sales import (
    PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_bq_finding_page_data_preview_sales import (
    PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_dbrks_finding_page_data_preview_sales import (
    PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
from data_test.pushdown.finding_page_data_preview.data_pd_mssql_finding_page_data_preview import (
    PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_oracle_finding_page_data_preview_sales import (
    PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_rs_finding_page_data_preview_sales import (
    PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_saph_finding_page_data_preview_sales import (
    PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_sf_finding_page_data_preview_sales import (
    PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.finding_page_data_preview.data_pd_trino_finding_page_data_preview_sales import (
    PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_athena_finding_page_data_preview_sales import (
    PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pushdown.finding_page_data_preview.pl_pd_bq_finding_page_data_preview_sales import (
    PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_dbrks_finding_page_data_preview_sales import (
    PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_mssql_finding_page_data_preview_sales import (
    PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_oracle_finding_page_data_preview_sales import (
    PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pushdown.finding_page_data_preview.pl_pd_rs_finding_page_data_preview_sales import (
    PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pushdown.finding_page_data_preview.pl_pd_saph_finding_page_data_preview_sales import (
    PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_sf_finding_page_data_preview_sales import (
    PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.finding_page_data_preview.pl_pd_trino_finding_page_data_preview_sales import (
    PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_finding_page_data_preview

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownFindingPageDataPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.athena
    def test_pushdown_athena_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Snowflake pushdown dataset"""
        helper.run_pushdown_job(
            api_utils, PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD
        )
        validate_finding_page_data_preview(
            api_utils,
            PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.bigquery
    def test_pushdown_bigquery_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small BigQuery pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.databricks
    def test_pushdown_databricks_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Databricks pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.oracle
    @pytest.mark.skip(reason="Skipped until DEV-116256 is deployed to 2025.05")
    def test_pushdown_oracle_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Oracle pushdown dataset"""
        helper.run_pushdown_job(api_utils,
                                PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.redshift
    def test_pushdown_redshift_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Redshift pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_RS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.saphana
    def test_pushdown_saphana_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small SAP HANA pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_SAPH_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Snowflake pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small SQL Server pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_MSSQL_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Finding Page Data Preview")
    @pytest.mark.trino
    def test_pushdown_trino_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Trino pushdown dataset"""
        helper.run_pushdown_job(api_utils, PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PD_TRINO_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )
