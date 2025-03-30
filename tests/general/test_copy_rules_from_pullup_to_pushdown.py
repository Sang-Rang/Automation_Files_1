import copy

import allure
import pytest
from assertpy import assert_that

from data_test.general.data_copy_rules_from_athena_pullup_to_pushdown_sales import (
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_bigquery_pullup_to_pushdown_sales import (
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_databricks_pullup_to_pushdown_sales import (
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_redshift_pullup_to_pushdown_sales import (
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_saphana_pullup_to_pushdown_sales import (
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_snowflake_pullup_to_pushdown_sales import (
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_sqlserver_pullup_to_pushdown_sales import (
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from data_test.general.data_copy_rules_from_trino_pullup_to_pushdown_sales import (
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
)
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v3.rule_api import V3_RULES_DATASET, V3_RULES_SOURCE_COPY
from payloads.general.pl_copy_rules_from_athena_pullup_to_pushdown_sales import (
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_bigquery_pullup_to_pushdown_sales import (
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_databricks_pullup_to_pushdown_sales import (
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_redshift_pullup_to_pushdown_sales import (
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_saphana_pullup_to_pushdown_sales import (
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_snowflake_pullup_to_pushdown_sales import (
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_sqlserver_pullup_to_pushdown_sales import (
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from payloads.general.pl_copy_rules_from_trino_pullup_to_pushdown_sales import (
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_PAYLOAD,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_rules import (
    validate_pushdown_rules_archived_break_records,
    validate_rules_findings,
)

helper = BaseHelper()


class TestCopyRulesFromPullupToPushdown:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def setup_validate_pullup(api_utils, dataset_defs, rule_definitions, expected_rule_output):
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils,
            dataset_defs,
        )
        helper.set_rules_on_dataset(
            api_utils,
            dataset_defs["dataset"],
            rule_definitions,
        )

        job_response = helper.setup_dataset(api_utils, dataset_defs)

        validate_rules_findings(
            api_utils,
            dataset_defs["dataset"],
            job_response["runId"],
            expected_rule_output,
        )

    @staticmethod
    def setup_copy_validate_pushdown(
        api_utils,
        pullup_dataset,
        pd_dataset_defs,
        expected_rule_copy_output,
        expected_rule_output,
    ):
        pd_dataset = pd_dataset_defs["dataset"]

        api_utils.delete(V3_RULES_DATASET.format(dataset=pd_dataset), return_json=False)
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, pd_dataset_defs)

        copy_rules_pu_to_pd_output = api_utils.post(
            V3_RULES_SOURCE_COPY.format(source=pullup_dataset), params={"target": pd_dataset}
        )

        copied_rule_count = len(copy_rules_pu_to_pd_output)
        expected_copied_rule_count = len(expected_rule_copy_output)
        assert_that(copied_rule_count).is_equal_to(expected_copied_rule_count)

        for copied_rule in expected_rule_copy_output:
            assert_that(copy_rules_pu_to_pd_output).contains(copied_rule)

        job_response_pd = helper.run_pushdown_job(api_utils, pd_dataset_defs)

        validate_rules_findings(
            api_utils,
            pd_dataset,
            job_response_pd["runId"],
            expected_rule_output,
            skip_exception_msg_check=True,
        )

        return job_response_pd

    @staticmethod
    def pd_rule_archive_breaks_validation(
        api_utils,
        pd_archive_breaks_dataset_defs,
        pd_archive_breaks_runid,
        pd_expected_rule_output,
        pd_archive_breaks_expected_data,
        pd_archive_breaks_expected_query_output,
    ):
        pd_archive_breaks_dataset = pd_archive_breaks_dataset_defs["dataset"]
        pd_archive_breaks_connection = pd_archive_breaks_dataset_defs["pushdown"]["connectionName"]

        pd_archive_breaks_connection_brand = api_utils.get(
            V2_GET_CONNECTION_BY_ALIAS, params={"alias": pd_archive_breaks_connection}
        )["dbBrandName"]

        archived_break_records_run_id = copy.deepcopy(pd_archive_breaks_runid)
        if pd_archive_breaks_connection_brand == "ATHENA":
            archived_break_records_run_id = helper.run_id_to_date_time(pd_archive_breaks_runid)

        validate_rules_findings(
            api_utils,
            pd_archive_breaks_dataset,
            pd_archive_breaks_runid,
            pd_expected_rule_output,
            compare_link_ds_to_nolink_ds=True,
            skip_exception_msg_check=True,
        )

        validate_pushdown_rules_archived_break_records(
            api_utils,
            pd_archive_breaks_connection,
            pd_archive_breaks_dataset,
            archived_break_records_run_id,
            pd_archive_breaks_expected_data,
            pd_archive_breaks_expected_query_output,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_athena_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_bigquery_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_databricks_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_redshift_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_saphana_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_snowflake_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_sqlserver_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("General")
    @allure.story("Copy rules from pull up to pushdown")
    def test_copy_rules_from_trino_pullup_to_pushdown_sales(self, api_utils):
        self.setup_validate_pullup(
            api_utils,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT,
        )

        self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_PAYLOAD,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
        )

        job_response_pd_archive_breaks = self.setup_copy_validate_pushdown(
            api_utils,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_PAYLOAD["dataset"],
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT,
        )

        self.pd_rule_archive_breaks_validation(
            api_utils,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_PAYLOAD,
            job_response_pd_archive_breaks["runId"],
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA,
            COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )
