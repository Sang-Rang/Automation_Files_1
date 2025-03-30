import allure
import pytest

from data_test.pullup.data_pullup_sf_shapes_granular_austin_crime_2 import (
    PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES
)

from endpoints.v2.controller_hoot import V2_POST_UPDATE_SHAPE_SETTINGS

from payloads.pullup.pl_pullup_sf_shapes_granular_austin_crime_2 import (
    PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD,
    PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS,
)

from payloads.pullup.pl_pullup_shapes_limit_many_shapes import (
    PULLUP_SHAPES_LIMIT_MANY_SHAPES_DATASET,
    PULLUP_SHAPES_LIMIT_MANY_SHAPES_PAYLOAD,
    PULLUP_SHAPES_LIMIT_MANY_SHAPES_SHAPES_SETTINGS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_shapes import validate_shapes_limit, validate_shapes_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupShapes:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Shapes")
    def test_pullup_shapes_limit_many_shapes(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PULLUP_SHAPES_LIMIT_MANY_SHAPES_SHAPES_SETTINGS,
        )
        job_response = helper.setup_dataset(api_utils, PULLUP_SHAPES_LIMIT_MANY_SHAPES_PAYLOAD)

        validate_shapes_limit(
            api_utils,
            PULLUP_SHAPES_LIMIT_MANY_SHAPES_DATASET,
            job_response["runId"],
        )

    @allure.feature("Pullup")
    @allure.story("Shapes")
    def test_pullup_snowflake_shapes_granular_austin_crime_2(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS
        )
        job_response = helper.setup_dataset(
            api_utils, PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD
        )
        validate_shapes_findings(
            api_utils,
            PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD,
            job_response["runId"],
            PULLUP_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES,
        )
