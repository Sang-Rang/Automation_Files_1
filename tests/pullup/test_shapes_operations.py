import allure
import pytest
from assertpy import assert_that, soft_assertions

from endpoints.v2.controller_assignment_q import V2_INVALIDATE_ASSIGNMENT
from endpoints.v2.controller_hoot import V2_GET_DATA_SHAPES
from endpoints.v2.controller_label import (
    V2_RETRAIN,
    V2_VIEW_ITEM_LABELS,
)
from payloads.pullup.pl_shapes_operations import DS_DEF_SHAPE_OP
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestShapesOperations:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Shapes")
    @pytest.mark.smoke
    def test_shapes_operations(self, api_utils):
        """
        Test SHAPES - Does it downtrain properly, persist properly after
        re-run, retrain properly and score properly
        """
        pl_general = {
            "dataset": DS_DEF_SHAPE_OP["dataset"],
            "runId": DS_DEF_SHAPE_OP["runId"],
        }

        helper.setup_dataset(api_utils, DS_DEF_SHAPE_OP)
        resp_ds_history_issues = helper.get_dataset_history_issues(api_utils, pl_general["dataset"])

        resp_shapes = api_utils.get(V2_GET_DATA_SHAPES, params=pl_general)
        uuid = resp_shapes["data"][0]["assignmentId"]["uuid"]
        assert_that(len(resp_shapes["data"]), "No shapes data found").is_greater_than(0)

        pl_invalid = {"uuid": uuid, "annotation": "invalid"}
        resp_invalid = api_utils.post(V2_INVALIDATE_ASSIGNMENT, json=pl_invalid, return_json=False)
        assert_that(resp_invalid.status_code).is_equal_to(200)
        resp_retrain = api_utils.post(V2_RETRAIN, params=pl_general, return_json=False)
        assert_that(resp_retrain.status_code).is_equal_to(200)

        resp_labels = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)
        resp_ds_history_issues_invalidate = helper.get_dataset_history_issues(
            api_utils, pl_general["dataset"]
        )

        assert_that(str(resp_labels["data"]), "UUID not found in labels before rerun").contains(
            uuid
        )

        with soft_assertions():
            assert_that(resp_ds_history_issues_invalidate["score"], "Pre-rerun Score").is_equal_to(
                resp_ds_history_issues["score"] + 1
            )

            assert_that(
                resp_ds_history_issues_invalidate["scoreDatashape"], "Pre-rerun Score Datashape"
            ).is_equal_to(resp_ds_history_issues["scoreDatashape"] - 1)

            assert_that(resp_ds_history_issues_invalidate["shape"], "Pre-rerun Shape").is_equal_to(
                resp_ds_history_issues["shape"] - 1
            )

        resp_source = helper.run_source_job(api_utils, DS_DEF_SHAPE_OP)

        resp_labels_invalid = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)

        assert_that(
            str(resp_labels_invalid["data"]), "UUID not found in labels after re-run"
        ).contains(uuid)

        with soft_assertions():
            assert_that(
                resp_source["score"],
                "Post-rerun Score",
            ).is_equal_to(resp_ds_history_issues_invalidate["score"])

            assert_that(resp_source["scoreDatashape"], "Post-rerun Score Datashape").is_equal_to(
                resp_ds_history_issues_invalidate["scoreDatashape"]
            )

            assert_that(resp_source["shape"], "Post-rerun Shape").is_equal_to(
                resp_ds_history_issues_invalidate["shape"]
            )
