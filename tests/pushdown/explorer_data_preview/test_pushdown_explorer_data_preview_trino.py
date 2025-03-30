import allure
import pytest

from data_test.pushdown.explorer_data_preview.data_pd_trino_explorer_data_preview_sales import (
    PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_CONNECTION,
    PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_EXPECTED_DATA,
    PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_LIMIT,
    PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_QUERY,
)
from data_test.pushdown.explorer_data_preview.data_pd_trino_explorer_schema_preview_sales import (
    PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_COLUMNS,
    PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_CONNECTION,
    PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_EXPECTED,
    PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_TABLE,
)

from utils.api_utils import APIUtils
from utils.validator import (
    validate_explorer_data_preview_schema,
    validate_explorer_data_preview_sql,
)


@pytest.mark.pushdown
@pytest.mark.trino
class TestPushdownExplorerDataPreviewTrino:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_trino_explorer_data_preview_sales(self, api_utils):
        """Verify data returned from SQL in explorer data preview for Trino pushdown
        using a small table"""
        validate_explorer_data_preview_sql(
            api_utils,
            PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_CONNECTION,
            PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_QUERY,
            PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_LIMIT,
            PD_TRINO_EXPLORER_DATA_PREVIEW_SALES_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_trino_explorer_schema_preview_sales(self, api_utils):
        """Verify schema preview on explorer for Trino pushdown using a small table"""
        validate_explorer_data_preview_schema(
            api_utils,
            PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_CONNECTION,
            PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_TABLE,
            PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_COLUMNS,
            PD_TRINO_EXPLORER_SCHEMA_PREVIEW_SALES_EXPECTED,
        )
