import allure
import pytest

from data_test.pushdown.records.data_pd_sf_records_nyse import (
    PD_SF_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
)
from data_test.pushdown.records.data_pd_sf_records_union_lookback_nyse import (
    PD_SF_RECORDS_NYSE_UNION_LOOKBACK_EXPECTED_RECORDS_FINDINGS,
)
from payloads.pushdown.records.pl_pd_sf_records_nyse import (
    PD_SF_RECORDS_NYSE_DATASET,
    PD_SF_RECORDS_NYSE_PAYLOAD,
)
from payloads.pushdown.records.pl_pd_sf_records_union_lookback_nyse import (
    PD_SF_RECORDS_NYSE_UNION_LOOKBACK_DATASET,
    PD_SF_RECORDS_NYSE_UNION_LOOKBACK_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_observations import validate_records_findings

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.snowflake
class TestPushdownRecordsSnowflake:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Records")
    def test_pushdown_snowflake_records_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(api_utils, PD_SF_RECORDS_NYSE_DATASET)
        job_response = helper.run_pushdown_job(api_utils, PD_SF_RECORDS_NYSE_PAYLOAD)

        validate_records_findings(
            api_utils,
            PD_SF_RECORDS_NYSE_DATASET,
            job_response["runId"],
            PD_SF_RECORDS_NYSE_EXPECTED_RECORDS_FINDINGS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Records")
    def test_pushdown_snowflake_records_union_lookback_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_RECORDS_NYSE_UNION_LOOKBACK_PAYLOAD
        )

        helper.delete_dataset_if_exists(
            api_utils, PD_SF_RECORDS_NYSE_UNION_LOOKBACK_DATASET
        )

        lookback_run_id_values = [
            "2017-12-12",
            # "2017-12-17", Uncomment when DEV-114756 and DEV-114757 are addressed
        ]
        helper.create_dataset_runs_for_run_id_values(
            api_utils,
            PD_SF_RECORDS_NYSE_UNION_LOOKBACK_PAYLOAD,
            lookback_run_id_values,
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_RECORDS_NYSE_UNION_LOOKBACK_PAYLOAD
        )

        validate_records_findings(
            api_utils,
            PD_SF_RECORDS_NYSE_UNION_LOOKBACK_DATASET,
            job_response["runId"],
            PD_SF_RECORDS_NYSE_UNION_LOOKBACK_EXPECTED_RECORDS_FINDINGS,
        )
