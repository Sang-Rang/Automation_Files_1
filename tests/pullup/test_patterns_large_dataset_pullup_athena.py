import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_hoot import V2_GET_OBSERVATIONS
from endpoints.v2.controller_pattern_opt import V2_PATTERN_OPT_GET
from payloads.pullup.pl_patterns_on_large_dataset_athena import JOB_PAYLOAD
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import validate_array_dict

helper = BaseHelper()


@pytest.mark.pullup
class TestPatternsLargeDataSet:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Patterns")
    def test_patterns_on_large_datasets_athena(self, api_utils):
        """Test PATTERNS on Large dataset - pull-up source ATHENA."""
        expected_patterns_count = 10
        expected_pattern_opt = [
            {
                "dataset": JOB_PAYLOAD["dataset"],
                "only": False,
                "lookback": 5,
                "key": ["symbol"],
                "dateColumn": None,
                "include": ["high", "low"],
                "exclude": [
                    "exch",
                    "symbol",
                    "trade_date",
                    "open",
                    "close",
                    "volume",
                    "part_date_str",
                ],
                "score": 1,
                "minSupport": 0.000033,
                "confidence": 0.6,
                "limit": 30,
                "query": "",
                "filter": None,
                "timeBin": "DAY",
                "on": False,
                "match": True,
                "lowFreq": False,
                "bucketLimit": 450000,
                "deDupe": True,
            }
        ]

        helper.delete_dataset_pattern_configurations(api_utils, JOB_PAYLOAD["dataset"])
        helper.setup_dataset(api_utils, JOB_PAYLOAD)

        get_patterns_params = {
            "dataset": JOB_PAYLOAD["dataset"],
            "runId": JOB_PAYLOAD["runId"],
        }
        get_patterns_response = api_utils.get(V2_GET_OBSERVATIONS, params=get_patterns_params)

        pattern_count = len(get_patterns_response["data"])

        assert_that(
            expected_patterns_count,
            f"PULLUP - patterns test failed. Expected patterns count: "
            f"{expected_patterns_count} Actual status: "
            f"{pattern_count} Note: Check pattern settings in tenant "
            f"configuration.",
        ).is_equal_to(pattern_count)

        pattern_opt = api_utils.get(V2_PATTERN_OPT_GET, params={"dataset": JOB_PAYLOAD["dataset"]})
        assert_that(pattern_opt, "Unexpected response from pattern opt").contains_key("result")
        validate_array_dict(expected_pattern_opt, pattern_opt["result"], "Pattern Opt")
