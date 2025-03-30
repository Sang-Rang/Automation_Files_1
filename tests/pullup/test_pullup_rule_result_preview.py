import allure
import pytest

from data_test.pullup.data_pullup_rule_result_preview_filter_tolerance_sales import (
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION,
)
from data_test.pullup.data_pullup_rule_result_preview_sales import (
    PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_NATIVE,
    PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
    PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
    PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_NATIVE,
    PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
    PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
)
from payloads.pullup.pl_pullup_rule_result_preview_filter_tolerance_sales import (
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_rule_result_preview_sales import (
    PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
    PULLUP_RULE_RESULT_PREVIEW_SALES_PAYLOAD,
)
from utils.api_utils import APIUtils

from utils.helper import BaseHelper
from utils.validator import validate_rule_result_preview

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupRuleResultPreview:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Rules")
    @allure.story("Pullup rule result preview")
    @pytest.mark.skip(reason="Undo after DEV-110397 is fixed")
    def test_pullup_rule_result_preview_sales(self, api_utils):
        helper.setup_dataset(api_utils, PULLUP_RULE_RESULT_PREVIEW_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF,
            PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF,
        )

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG,
            PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG,
        )

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_NATIVE,
            PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_NATIVE,
        )

    @allure.feature("Rules")
    @allure.story("Pullup rule result preview")
    @pytest.mark.skip(reason="Undo after DEV-122060 is fixed")
    def test_pullup_rule_result_preview_filter_tolerance_sales(self, api_utils):
        helper.setup_dataset(api_utils, PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_PAYLOAD)

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW,
        )

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW,
        )

        validate_rule_result_preview(
            api_utils,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION,
            PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW
        )
