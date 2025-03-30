import allure
import pytest

from data_test.pushdown.rules.data_pd_rs_rules_sales import (
    PD_RS_RULES_SALES_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rules.data_pd_rs_rules_sales_archive_breaks import (
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT,
)
from payloads.pushdown.rules.pl_pd_rs_rules_sales_archive_breaks import (
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_CONNECTION,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_pushdown_archived_breaks import (
    validate_pushdown_archived_break_records_single_rule_query_results,
)
from utils.validator_rules import (
    validate_rules_findings,
    validate_pushdown_rules_archived_break_records,
    validate_downloaded_rule_breaks,
    validate_downloaded_job_rule_breaks,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.redshift
class TestPushdownRulesRedshiftArchiveBreaks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules - Archive Break Records")
    def test_pushdown_redshift_rules_sales_archive_breaks(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )
        validate_rules_findings(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_RS_RULES_SALES_EXPECTED_RULE_OUTPUT,
            compare_link_ds_to_nolink_ds=True,
        )
        validate_pushdown_rules_archived_break_records(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_CONNECTION,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )
        validate_downloaded_rule_breaks(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            "FF_no_link_column_in_query",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT,
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD["runId"],
            "CSV",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT,
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD["runId"],
            "JSON",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT,
        )

        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD["runId"],
            "CSV",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT,
            rule_name="FF_no_link_column_in_query",
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD["runId"],
            "JSON",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT,
            rule_name="FF_no_link_column_in_query",
        )
        validate_pushdown_archived_break_records_single_rule_query_results(
            api_utils,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD["runId"],
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_CONNECTION,
            "FF_no_link_column_in_query",
            PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT,
        )
