import allure
import pytest

from data_test.pushdown.shapes.data_pd_sf_shapes_granular_austin_crime import (
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_EXPECTED_SHAPES,
)
from data_test.pushdown.shapes.data_pd_sf_shapes_granular_austin_crime_2 import (
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES,
)

from endpoints.v2.controller_hoot import V2_POST_UPDATE_SHAPE_SETTINGS

from payloads.pushdown.shapes.pl_pd_sf_shapes_granular_austin_crime import (
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_PAYLOAD,
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_SHAPES_SETTINGS,
)
from payloads.pushdown.shapes.pl_pd_sf_shapes_granular_austin_crime_2 import (
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD,
    PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS,
)
from payloads.pushdown.shapes.pl_pd_sf_shapes_limit_many_shapes import (
    PD_SF_SHAPES_LIMIT_MANY_SHAPES_DATASET,
    PD_SF_SHAPES_LIMIT_MANY_SHAPES_PAYLOAD,
    PD_SF_SHAPES_LIMIT_MANY_SHAPES_SHAPES_SETTINGS,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_shapes import (
    validate_shapes_findings,
    validate_shapes_limit,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.snowflake
class TestPushdownShapesSnowflake:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Shapes")
    def test_pushdown_snowflake_shapes_granular_austin_crime(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_SHAPES_SETTINGS,
        )
        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_PAYLOAD
        )

        validate_shapes_findings(
            api_utils,
            PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_PAYLOAD,
            job_response["runId"],
            PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_EXPECTED_SHAPES,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Shapes")
    def test_pushdown_snowflake_shapes_granular_austin_crime_2(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS,
        )
        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD
        )

        validate_shapes_findings(
            api_utils,
            PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD,
            job_response["runId"],
            PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Shapes")
    def test_pushdown_snowflake_shapes_limit_many_shapes(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PD_SF_SHAPES_LIMIT_MANY_SHAPES_SHAPES_SETTINGS,
        )
        job_response = helper.run_pushdown_job(api_utils, PD_SF_SHAPES_LIMIT_MANY_SHAPES_PAYLOAD)

        validate_shapes_limit(
            api_utils,
            PD_SF_SHAPES_LIMIT_MANY_SHAPES_DATASET,
            job_response["runId"],
        )
