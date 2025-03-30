import allure
import pytest
from assertpy import assert_that, soft_assertions

from data_test.pullup.data_assignmnets_hoot import DATASET_RULE_DEFS
from endpoints.v2.controller_assignment_q import (
    V2_FIND_ALL_PAGING_DATATABLES,
    V2_ASSIGN_TO_USER,
    V2_RESOLVE_ASSIGNMENT,
    V2_INVALIDATE_ASSIGNMENT,
    V2_ASSIGNMENT_Q_GET,
)
from endpoints.v2.controller_hoot import V2_GET_DATA_SHAPES
from endpoints.v2.controller_label import (
    V2_RETRAIN,
    V2_VIEW_ITEM_LABELS,
    V2_REMOVE_ITEM_LABEL,
)
from payloads.pullup.pl_assigments_delete_label_retrain import (
    DATASET_DEFS_ASSIGNMENT_LABEL,
    DATASET_ASSIGNMENT_LABEL,
)
from payloads.pullup.pl_assignments_rule_on_hoot import DATASET_DEFS_ASSIGNMENTS_HOOT
from utils.api_utils import APIUtils
from utils.constants import BASE_CREDS
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestAssignmentsRuleAndLabel:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def remove_all_labels(api_utils, dataset_name, run_id):
        """Remove any existing labels on job findings"""
        labels = api_utils.get(V2_VIEW_ITEM_LABELS, params={"dataset": dataset_name})
        assert_that(labels, "Unexpected view item labels error").contains_key("data")
        if len(labels["data"]) > 0:
            for label in labels["data"]:
                pl_remove_label = {
                    "dataset": dataset_name,
                    "runid": f"{run_id}T00:00:00.000 0000",
                    "itemkey": label["itemKey"],
                    "itemtype": label["itemType"],
                    "itemvalue": label["itemValue"],
                    "itemcount": label["itemCount"],
                }
                resp_remove = api_utils.post(V2_REMOVE_ITEM_LABEL, params=pl_remove_label)
                assert_that(resp_remove, "Unexpected remove item label error").contains_key("msg")
                assert_that(resp_remove["msg"], "Remove item label failed").is_equal_to(
                    "Item Label Removed"
                )

    @staticmethod
    def get_shapes_and_check_count(api_utils, payload, expected_number):
        """Validate the count of shapes and return the shapes data"""
        shapes = api_utils.get(V2_GET_DATA_SHAPES, params=payload)
        assert_that(shapes).contains_key("data")
        assert_that(len(shapes["data"]), "Unexpected number of shapes").is_equal_to(expected_number)
        return shapes

    @allure.feature("Pullup")
    @allure.story("Assignments / Down-train")
    @pytest.mark.smoke
    def test_assignments_rule_on_hoot_page(self, api_utils):
        """ASSIGNMENTS - Rule on Hoot page > annotate > assign > resolve."""
        dataset = DATASET_DEFS_ASSIGNMENTS_HOOT["dataset"]
        user_name = BASE_CREDS["username"]

        find_observations_params = {
            "draw": "0",
            "type": "RULE",
            "start": "0",
            "length": "0",
            "search[value]": dataset,
        }
        helper.setup_dataset(api_utils, DATASET_DEFS_ASSIGNMENTS_HOOT)
        helper.set_rules_on_dataset(api_utils, dataset, DATASET_RULE_DEFS)
        helper.setup_dataset(api_utils, DATASET_DEFS_ASSIGNMENTS_HOOT)

        observations_after_job_run = api_utils.get(
            V2_FIND_ALL_PAGING_DATATABLES, params=find_observations_params
        )

        # Each time the rules are reset and a job is run,
        # assignments and resolved status are cleared for that runId
        for observation in observations_after_job_run["data"]:
            if DATASET_DEFS_ASSIGNMENTS_HOOT["runId"] in observation["runId"]:
                observation_uuid = observation["id"]["uuid"]
                break
        else:
            observation_uuid = ""

        assign_params = {
            "uuid": observation_uuid,
            "description": "valid",
            "serviceType": "COLLIBRA_DQ",
            "assignedTo": user_name,
            "additionalFields": "",
        }

        # Validating rule observation and verifying the status in assignments page
        api_utils.post(V2_ASSIGN_TO_USER, json=assign_params)
        observations_after_assign = api_utils.get(
            V2_FIND_ALL_PAGING_DATATABLES, params=find_observations_params
        )
        for observation in observations_after_assign["data"]:
            if observation["id"]["uuid"] == observation_uuid:
                assigned_observation = observation
                break
        else:
            assigned_observation = ""
        with soft_assertions():
            assert_that(
                assigned_observation["state"],
                f"State of Assignment is {assigned_observation['state']}",
            ).is_equal_to("ASSIGNED")
            assert_that(
                assigned_observation["assignedTo"],
                f"Invalid assignment, assigned to {assigned_observation['assignedTo']}",
            ).is_equal_to(user_name)
            assert_that(
                assigned_observation["description"],
                "Invalid description of assignment, "
                f"actual is: {assigned_observation['description']}",
            ).is_equal_to("valid")

            # Resolving rule observation and verifying the status in assignments page
            resolve_assignment_params = {"uuid": observation_uuid}

            api_utils.put(V2_RESOLVE_ASSIGNMENT, params=resolve_assignment_params)
            observations_after_resolve = api_utils.get(
                V2_FIND_ALL_PAGING_DATATABLES, params=find_observations_params
            )
            for observation in observations_after_resolve["data"]:
                if observation["id"]["uuid"] == observation_uuid:
                    resolved_observation = observation
                    break
            else:
                resolved_observation = ""
            assert_that(
                resolved_observation["state"],
                f"State of assignment does not equal to 'RESOLVED', "
                f"actual is: {resolved_observation['state']}",
            ).is_equal_to("RESOLVED")

    @allure.feature("Pullup")
    @allure.story("Assignments / Down-train")
    def test_assignments_delete_label_retrain(self, api_utils):
        # Setup
        ds_run_id = {
            "dataset": DATASET_ASSIGNMENT_LABEL,
            "runId": DATASET_DEFS_ASSIGNMENT_LABEL["runId"],
        }
        helper.setup_dataset(api_utils, DATASET_DEFS_ASSIGNMENT_LABEL)
        self.remove_all_labels(
            api_utils, DATASET_ASSIGNMENT_LABEL, DATASET_DEFS_ASSIGNMENT_LABEL["runId"]
        )

        # Get shapes and assignment info
        shapes = self.get_shapes_and_check_count(api_utils, ds_run_id, 10)
        shape = shapes["data"][0]
        uuid = shape["assignmentId"]["uuid"]
        assignment_q = api_utils.get(V2_ASSIGNMENT_Q_GET, params={"uuid": uuid})
        pl_invalidate = {"annotation": "Invalidated Shape", "uuid": uuid}

        # Invalidate the shape
        invalidate = api_utils.post(V2_INVALIDATE_ASSIGNMENT, json=pl_invalidate)
        assert_that(invalidate, "Unexpected failure in invalidate").contains_key("result")
        assert_that(invalidate["result"], f"Invalidate failed for {pl_invalidate}").is_true()

        # Retrain (returns no response data)
        retrain = api_utils.post(V2_RETRAIN, params=ds_run_id, return_json=False)
        assert_that(retrain.status_code, "Retain failure").is_equal_to(200)
        self.get_shapes_and_check_count(api_utils, ds_run_id, 9)

        # Validate the label generated from invalidate/retrain
        labels = api_utils.get(V2_VIEW_ITEM_LABELS, params=ds_run_id)
        assert_that(labels, "Unexpected failure in view labels").contains_key("data")
        assert_that(len(labels["data"])).is_equal_to(1)
        label = labels["data"][0]

        # Validate the label data
        assert_that(label["dataset"]).is_equal_to(ds_run_id["dataset"])
        assert_that(label["itemKey"]).is_equal_to(shape["colName"])
        assert_that(label["itemType"]).is_equal_to(assignment_q["result"]["type"])
        assert_that(label["itemValue"]).is_equal_to(shape["colFormat"])
        assert_that(label["itemCount"]).is_equal_to(1)
        assert_that(label["userNm"]).is_equal_to(BASE_CREDS["username"])
        assert_that(label["assignmentId"]["id"]).is_greater_than(0)
        assert_that(label["assignmentId"]["uuid"]).is_equal_to(uuid)
        assert_that(label["annotation"]).is_equal_to(pl_invalidate["annotation"])

        # Remove, retrain again, validate shapes data returns to start value
        self.remove_all_labels(api_utils, ds_run_id["dataset"], ds_run_id["runId"])
        retrain_post_remove = api_utils.post(V2_RETRAIN, params=ds_run_id, return_json=False)
        assert_that(retrain_post_remove.status_code, "Retain failure").is_equal_to(200)
        self.get_shapes_and_check_count(api_utils, ds_run_id, 10)
