import allure
import pytest

from data_test.pullup.data_pullup_athena_data_preview_sales import (
    PULLUP_ATHENA_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
from data_test.pullup.data_pullup_bq_finding_page_data_preview_sales import (
    PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
from data_test.pullup.data_pullup_dbrks_finding_page_data_preview_sales import (
    PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
from data_test.pullup.data_pullup_oracle_finding_page_data_preview_sales_data import (
    PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_EXPECTED_DATA,
)
from data_test.pullup.data_pullup_sf_finding_page_data_preview_sales import (
    PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
)
from payloads.pullup.pl_pullup_athena_data_preview_sales import (
    PULLUP_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pullup.pl_pullup_bq_findings_page_data_preview_sales_profile_pl import (
    PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pullup.pl_pullup_dbrks_finding_page_data_preview_sales import (
    PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from payloads.pullup.pl_pullup_oracle_finding_page_data_preview_sales_data import (
    PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_PAYLOAD,
)
from payloads.pullup.pl_pullup_sf_finding_page_data_preview_sales import (
    PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_finding_page_data_preview

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupDataPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Pullup - Finding Page Data Preview")
    def test_pullup_athena_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Athena pullup dataset"""
        helper.setup_dataset(
            api_utils, PULLUP_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD
        )
        validate_finding_page_data_preview(
            api_utils,
            PULLUP_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PULLUP_ATHENA_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PULLUP_ATHENA_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pullup")
    @allure.story("Pullup - Finding Page Data Preview")
    def test_pullup_bigquery_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small BigQuery pullup dataset"""
        helper.setup_dataset(api_utils, PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PULLUP_BQ_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pullup")
    @allure.story("Pullup - Finding Page Data Preview")
    def test_pullup_databricks_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Databricks pullup dataset"""
        helper.setup_dataset(
            api_utils, PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD
        )
        validate_finding_page_data_preview(
            api_utils,
            PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PULLUP_DBRKS_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )

    @allure.feature("Pullup")
    @allure.story("Pullup - Finding Page Data Preview")
    def test_pullup_oracle_dataset_preview_sales_rep(self, api_utils):
        """Verify data preview on finding page using Oracle pullup dataset"""
        helper.setup_dataset(api_utils, PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_PAYLOAD["dataset"],
            PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_PAYLOAD["runId"],
            PULLUP_ORACLE_FINDING_PAGE_DATA_PREVIEW_SALES_REP_EXPECTED_DATA,
        )

    @allure.feature("Pullup")
    @allure.story("Pullup - Finding Page Data Preview")
    def test_pullup_snowflake_dataset_preview_sales_profile(self, api_utils):
        """Verify data preview on finding page using a small Snowflake pullup dataset"""
        helper.setup_dataset(api_utils, PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD)
        validate_finding_page_data_preview(
            api_utils,
            PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["dataset"],
            PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_PAYLOAD["runId"],
            PULLUP_SF_FINDING_PAGE_DATA_PREVIEW_SALES_PROFILE_EXPECTED_DATA,
        )
