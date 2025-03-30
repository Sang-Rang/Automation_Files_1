import copy
import allure
import pytest
from endpoints.v2.controller_hoot import V2_POST_UPDATE_SHAPE_SETTINGS
from data_test.pullup.data_shapes_settings_expected import (
    SHAPES_SETTINGS_EXPECTED_SHAPES,
    SHAPES_SETTINGS_UPDATED_RESULTS,
)
from payloads.pullup.pl_shapes_settings_and_configs import SHAPE_SETTINGS_PAYLOAD
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_shapes import validate_shapes_findings

helper = BaseHelper()


@pytest.mark.pullup
class TestShapesSettings:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Shapes")
    @pytest.mark.smoke
    def test_shapes_settings_and_configs(self, api_utils):
        """Test Combination of shapes. Interaction between shape config settings."""
        shape_settings_updated = {
            "dataset": SHAPE_SETTINGS_PAYLOAD["dataset"],
            "dataShapeSensitivity": SHAPE_SETTINGS_PAYLOAD["profile"]["shapeSensitivity"],
            "dataShapeMaxPerCol": SHAPE_SETTINGS_PAYLOAD["profile"]["shapeMaxPerCol"],
            "dataShapeMaxColSize": SHAPE_SETTINGS_PAYLOAD["profile"]["shapeMaxColSize"],
        }
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=shape_settings_updated,
        )
        job_response = helper.setup_dataset(api_utils, SHAPE_SETTINGS_PAYLOAD)

        validate_shapes_findings(
            api_utils,
            SHAPE_SETTINGS_PAYLOAD,
            job_response["runId"],
            SHAPES_SETTINGS_EXPECTED_SHAPES,
        )

        updated_shapes_payload = copy.deepcopy(SHAPE_SETTINGS_PAYLOAD)
        updated_shapes_payload["profile"]["shapeSensitivity"] = 3
        updated_shapes_payload["profile"]["shapeMaxPerCol"] = 5
        updated_shapes_payload["profile"]["shapeMaxColSize"] = 25

        shape_settings_updated = {
            "dataset": updated_shapes_payload["dataset"],
            "dataShapeSensitivity": updated_shapes_payload["profile"]["shapeSensitivity"],
            "dataShapeMaxPerCol": updated_shapes_payload["profile"]["shapeMaxPerCol"],
            "dataShapeMaxColSize": updated_shapes_payload["profile"]["shapeMaxColSize"],
        }
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=shape_settings_updated,
        )

        job_response_updated = helper.setup_dataset(api_utils, updated_shapes_payload)

        validate_shapes_findings(
            api_utils,
            updated_shapes_payload,
            job_response_updated["runId"],
            SHAPES_SETTINGS_UPDATED_RESULTS,
        )
