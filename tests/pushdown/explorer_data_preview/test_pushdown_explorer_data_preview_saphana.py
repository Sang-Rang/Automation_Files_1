import allure
import pytest

from data_test.pushdown.explorer_data_preview.data_pd_saph_explorer_data_preview_sales import (
    PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_CONNECTION,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_EXPECTED_DATA,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_LIMIT,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_QUERY,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.explorer_data_preview.data_pd_saph_explorer_data_preview_special_characters import (
    PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_CONNECTION,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_EXPECTED_DATA,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_LIMIT,
    PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_QUERY,
)
from data_test.pushdown.explorer_data_preview.data_pd_saph_explorer_schema_preview_sales import (
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_COLUMNS,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_CONNECTION,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_EXPECTED,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_TABLE,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.explorer_data_preview.data_pd_saph_explorer_schema_preview_special_characters import (
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_COLUMNS,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_CONNECTION,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_EXPECTED,
    PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_TABLE,
)

from utils.api_utils import APIUtils
from utils.validator import (
    validate_explorer_data_preview_schema,
    validate_explorer_data_preview_sql,
)


@pytest.mark.pushdown
@pytest.mark.saphana
class TestPushdownExplorerDataPreviewSAPHANA:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_saphana_explorer_data_preview_sales(self, api_utils):
        """Verify data returned from SQL in explorer data preview for SAP HANA pushdown
        using a small table"""
        validate_explorer_data_preview_sql(
            api_utils,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_CONNECTION,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_QUERY,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_LIMIT,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SALES_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_saphana_explorer_data_preview_special_characters(self, api_utils):
        """Verify data returned from SQL in explorer data preview for SAP HANA pushdown
        using a table that has special characters in its name."""
        validate_explorer_data_preview_sql(
            api_utils,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_CONNECTION,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_QUERY,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_LIMIT,
            PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_EXPECTED_DATA,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_saphana_explorer_schema_preview_sales(self, api_utils):
        """Verify schema preview on explorer for SAP HANA pushdown using a small table"""
        validate_explorer_data_preview_schema(
            api_utils,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_CONNECTION,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_TABLE,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_COLUMNS,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SALES_EXPECTED,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Explorer data preview")
    def test_pushdown_saphana_explorer_schema_preview_special_characters(self, api_utils):
        """Verify schema preview on explorer for SAP HANA pushdown using a table that has special
        characters in its name."""
        validate_explorer_data_preview_schema(
            api_utils,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_CONNECTION,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_TABLE,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_COLUMNS,
            PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_EXPECTED,
        )
