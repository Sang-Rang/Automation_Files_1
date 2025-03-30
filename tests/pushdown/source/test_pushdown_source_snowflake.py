import allure
import pytest

from data_test.pushdown.source.data_pd_sf_source_key_time_nyse import (
    PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_COUNT,
    PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA,
    PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_VALUES,
)
from data_test.pushdown.source.data_pd_sf_source_nokey_time_nyse import (
    PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_COUNT,
    PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA,
    PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_VALUES,
)
from payloads.pushdown.source.pl_pd_sf_source_key_time_nyse import (
    PD_SF_SOURCE_KEY_TIME_NYSE_PAYLOAD,
)
from payloads.pushdown.source.pl_pd_sf_source_nokey_time_nyse import (
    PD_SF_SOURCE_NOKEY_TIME_NYSE_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_source import validate_source_findings

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.snowflake
class TestPushdownSourceSnowflake:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Source")
    def test_pushdown_snowflake_source_key_time_nyse(self, api_utils):
        job_response = helper.run_pushdown_job(api_utils, PD_SF_SOURCE_KEY_TIME_NYSE_PAYLOAD)

        validate_source_findings(
            api_utils,
            PD_SF_SOURCE_KEY_TIME_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_COUNT,
            PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA,
            PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_VALUES,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Source")
    def test_pushdown_snowflake_source_nokey_time_nyse(self, api_utils):
        job_response = helper.run_pushdown_job(api_utils, PD_SF_SOURCE_NOKEY_TIME_NYSE_PAYLOAD)

        validate_source_findings(
            api_utils,
            PD_SF_SOURCE_NOKEY_TIME_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_COUNT,
            PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA,
            PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_VALUES,
        )
