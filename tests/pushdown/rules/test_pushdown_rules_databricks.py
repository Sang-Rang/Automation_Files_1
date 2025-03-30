import allure
import pytest

from data_test.pushdown.rules.data_pd_dbrks_data_types import (
    PD_DBRKS_RULES_DATA_TYPE_DEFINITIONS,
    PD_DBRKS_RULES_DATA_TYPE_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_basic import (
    PD_DBRKS_RULES_BASIC_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULES_BASIC_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_binary_sales import (
    PD_DBRKS_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULES_BINARY_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_nyse import (
    PD_DBRKS_RULES_NYSE_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULES_NYSE_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_sales import (
    PD_DBRKS_RULES_SALES_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULES_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_sales_archive_breaks import (
    PD_DBRKS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_sales_link_id import (
    PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT,
    PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT,
    PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT,
    PD_DBRKS_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT,
    PD_DBRKS_RULES_SALES_LINK_ID_RULE_DEFINITIONS,
    PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT,
    PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT,
)
from data_test.pushdown.rules.data_pd_dbrks_rules_temporal_sales import (
    PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29,
    PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30,
    PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01,
    PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02,
    PD_DBRKS_RULES_TEMPORAL_SALES_RULE_DEFINITIONS,
)
from data_test.pushdown.rules.data_pd_rule_types_with_rundate import (
    PD_RULE_WITH_RUNDATE_DEFINITIONS,
    PD_RULE_WITH_RUNDATE_DEFINITIONS_OUTPUT,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_basic import (
    PD_DBRKS_RULES_BASIC_DATASET,
    PD_DBRKS_RULES_BASIC_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_binary_sales import (
    PD_DBRKS_RULES_BINARY_SALES_DATASET,
    PD_DBRKS_RULES_BINARY_SALES_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_data_types import (
    PD_DBRKS_RULES_DATA_TYPE_PAYLOAD,
    PD_DBRKS_RULES_DATA_TYPE_DATASET,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_nyse import (
    PD_DBRKS_RULES_NYSE_DATASET,
    PD_DBRKS_RULES_NYSE_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_sales import (
    PD_DBRKS_RULES_SALES_DATASET,
    PD_DBRKS_RULES_SALES_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_sales_link_id import (
    PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
    PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_dbrks_rules_temporal_sales import (
    PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
    PD_DBRKS_RULES_TEMPORAL_SALES_PAYLOAD,
)
from payloads.pushdown.rules.pl_pd_rule_types_with_rundate import (
    PD_RULE_TYPES_WITH_RUNDATE_PAYLOAD,
    PD_RULE_TYPES_WITH_RUNDATE_DATASET,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_rules import (
    validate_downloaded_job_rule_breaks,
    validate_downloaded_rule_breaks,
    validate_rules_findings,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.databricks
class TestPushdownRulesDatabricks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_basic(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_DBRKS_RULES_BASIC_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_BASIC_DATASET,
            PD_DBRKS_RULES_BASIC_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_BASIC_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_BASIC_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_BASIC_EXPECTED_RULE_OUTPUT,
            skip_exception_msg_check=True,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_binary_sales(self, api_utils):
        """Binary rules apply when a dataset has no rows and a rule breaks."""
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULES_BINARY_SALES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_BINARY_SALES_DATASET,
            PD_DBRKS_RULES_BINARY_SALES_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_BINARY_SALES_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_BINARY_SALES_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_data_type(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULES_DATA_TYPE_PAYLOAD
        )

        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_DATA_TYPE_DATASET,
            PD_DBRKS_RULES_DATA_TYPE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_DATA_TYPE_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_DATA_TYPE_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_DATA_TYPE_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_nyse(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_DBRKS_RULES_NYSE_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_NYSE_DATASET,
            PD_DBRKS_RULES_NYSE_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_NYSE_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_NYSE_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_NYSE_EXPECTED_RULE_OUTPUT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, PD_DBRKS_RULES_SALES_PAYLOAD)
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_SALES_DATASET,
            PD_DBRKS_RULES_SALES_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_SALES_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_SALES_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_SALES_EXPECTED_RULE_OUTPUT,
        )
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_SALES_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
            compare_link_ds_to_nolink_ds=True,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_sales_link_id(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            PD_DBRKS_RULES_SALES_LINK_ID_RULE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT,
        )
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            PD_DBRKS_RULES_SALES_EXPECTED_RULE_OUTPUT,
            compare_link_ds_to_nolink_ds=True,
        )
        validate_downloaded_rule_breaks(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            job_response["runId"],
            "FF_no_link_column_in_query",
            PD_DBRKS_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT,
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD["runId"],
            "CSV",
            PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT,
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD["runId"],
            "JSON",
            PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT,
        )

        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD["runId"],
            "CSV",
            PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT,
            rule_name="FF_no_link_column_in_query",
        )
        validate_downloaded_job_rule_breaks(
            api_utils,
            PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            PD_DBRKS_RULES_SALES_LINK_ID_PAYLOAD["runId"],
            "JSON",
            PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT,
            rule_name="FF_no_link_column_in_query",
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Rules")
    def test_pushdown_databricks_rules_temporal_sales(self, api_utils):
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_DBRKS_RULES_TEMPORAL_SALES_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
            PD_DBRKS_RULES_TEMPORAL_SALES_RULE_DEFINITIONS,
        )
        helper.run_pushdown_job(api_utils, PD_DBRKS_RULES_TEMPORAL_SALES_PAYLOAD)

        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
            "2022-04-29T00:00:00.000+0000",
            PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29,
        )
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
            "2022-04-30T00:00:00.000+0000",
            PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30,
        )
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
            "2022-05-01T00:00:00.000+0000",
            PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01,
        )
        validate_rules_findings(
            api_utils,
            PD_DBRKS_RULES_TEMPORAL_SALES_DATASET,
            "2022-05-02T00:00:00.000+0000",
            PD_DBRKS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown -  RULES - Freeform, Simple, Template Rules on dataset with rundate")
    def test_pushdown_rules_with_rundate(self, api_utils):
        """RULES - Freeform, Simple, and Template Rules on dataset with rundate {rd}."""
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PD_RULE_TYPES_WITH_RUNDATE_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PD_RULE_TYPES_WITH_RUNDATE_DATASET,
            PD_RULE_WITH_RUNDATE_DEFINITIONS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_RULE_TYPES_WITH_RUNDATE_PAYLOAD)
        validate_rules_findings(
            api_utils,
            PD_RULE_TYPES_WITH_RUNDATE_DATASET,
            job_response["runId"],
            PD_RULE_WITH_RUNDATE_DEFINITIONS_OUTPUT,
        )
