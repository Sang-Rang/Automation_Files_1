import allure
import pytest
from assertpy import soft_assertions, assert_that

from data_test.pullup.data_job_schedule import (
    CONNECTION_DEMO_BLOCKS,
    DATASET_DEMO_BLOCKS,
    QUERY_DEMO_BLOCKS,
    SCH_DATA_DEMO_BLOCKS,
    TODAY_FORMAT,
    PL_SCH_RES_CREATE,
    SCH_RES_UPDATE_HOUR_END,
    SCH_RES_UPDATE_HOUR_START,
    SCH_DATA_RES_REFUSED,
    PL_CREATE_RES_REFUSED,
    MSG_RES_REFUSED,
    PL_SCH_RES_CREATE_UPDATE,
    EXP_SCH_DEMO_BLOCKS,
    SCH_RES_HOUR_START_FULL,
    SCH_RES_HOUR_END_FULL,
    PL_SCH_RES_CREATE_MULTI,
    EXP_SCH_RES_MULTI,
    EXP_SCH_DEMO_BLOCKS_RESET,
    SCH_TYPE,
)
from endpoints.v2.controller_scheduler import (
    V2_POST_JOB_SCHEDULE,
    V2_GET_JOB_SCHEDULE,
    V2_DELETE_JOBS_SCHEDULE,
    V2_GET_SCHEDULE_RESTRICTION,
    V2_CREATE_SCHEDULE_RESTRICTION,
    V2_DELETE_SCHEDULE_RESTRICTION,
    V2_UPDATE_SCHEDULER_RESTRICTION,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal

helper = BaseHelper()


@pytest.mark.pullup
class TestDemoBlocksScheduleJobSave:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def create_restriction(api_utils, payload):
        """Create a schedule restriction and validate success"""
        create = api_utils.post(V2_CREATE_SCHEDULE_RESTRICTION, params=payload, return_json=False)
        assert_that(
            create.status_code, f"Create schedule restriction failed for {payload}"
        ).is_equal_to(200)

    @staticmethod
    def get_and_check_count_of_restrictions(api_utils, expected_number):
        """Get all schedule restrictions and validate the expected number"""
        schedules = api_utils.get(V2_GET_SCHEDULE_RESTRICTION)
        assert_that(len(schedules), "Incorrect schedule count").is_equal_to(expected_number)
        return schedules

    @staticmethod
    def get_and_check_all_restriction_ids(api_utils):
        """Extract ids and validate data type for existing schedule restrictions"""
        schedule_ids = []
        schedules = api_utils.get(V2_GET_SCHEDULE_RESTRICTION)

        for schedule in schedules:
            assert_that(schedule, "Unexpected error in get schedule restriction").contains_key("id")
            restriction_id = schedule["id"]
            schedule_ids.append(restriction_id)
            assert_that(restriction_id).is_greater_than(0)
        return schedule_ids

    def delete_all_restrictions(self, api_utils):
        """Delete all existing schedule restrictions"""
        schedule_ids = self.get_and_check_all_restriction_ids(api_utils)
        for s_id in schedule_ids:
            delete = api_utils.post(V2_DELETE_SCHEDULE_RESTRICTION, {"id": s_id}, return_json=False)
            assert_that(delete.status_code, "Delete schedule restriction failed").is_equal_to(200)

        delete = api_utils.get(V2_GET_SCHEDULE_RESTRICTION)
        assert_that(delete, f"Delete all schedules failed. Found: {delete}").is_equal_to([])

    @staticmethod
    def delete_job_schedule(api_utils, dataset_name):
        """'Delete' a job schedule from a job"""

        # Note: The actual behavior is the schedule is reset and made inactive
        delete = api_utils.delete(
            V2_DELETE_JOBS_SCHEDULE, params={"dataset": dataset_name}, return_json=False
        )
        assert_that(delete.status_code, "Delete job schedule fail").is_equal_to(200)

    @staticmethod
    def validate_restriction_data(restriction, expected_type, expected_start, expected_end):
        """Validate specific data within the schedule restriction"""
        assert_that(restriction["id"], "Invalid restriction ID").is_greater_than(0)
        assert_that(restriction["type"], f"Unexpected type in {restriction}").is_equal_to(
            expected_type
        )
        assert_that(
            restriction["start_value"], f"Unexpected start value in {restriction}"
        ).is_equal_to(expected_start)
        assert_that(restriction["end_value"], f"Unexpected end value in {restriction}").is_equal_to(
            expected_end
        )

    @allure.feature("Pullup")
    @allure.story("Job Schedule")
    def test_demo_blocks_schedule_job_save(self, api_utils):
        """Test Demo Blocks Schedule Job Save."""

        # Data setup
        agent_details = helper.get_agent_details_for_connection(api_utils, CONNECTION_DEMO_BLOCKS)
        SCH_DATA_DEMO_BLOCKS["agentId"] = agent_details["agentId"]["id"]
        EXP_SCH_DEMO_BLOCKS["agentId"]["id"] = agent_details["agentId"]["id"]
        sch_data = helper.add_scheduled_run_date_time_zoned_to_parameters(SCH_DATA_DEMO_BLOCKS)
        self.delete_job_schedule(api_utils, DATASET_DEMO_BLOCKS)

        # Run job
        ds_def = helper.get_minimum_job_payload(
            api_utils, CONNECTION_DEMO_BLOCKS, DATASET_DEMO_BLOCKS, QUERY_DEMO_BLOCKS
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_def)

        # Delete resets the data to these values
        schedule_start = api_utils.get(V2_GET_JOB_SCHEDULE, {"dataset": DATASET_DEMO_BLOCKS})
        compare_dicts_are_equal(schedule_start, EXP_SCH_DEMO_BLOCKS_RESET)

        # Post the job
        post = api_utils.post(V2_POST_JOB_SCHEDULE, params=sch_data)
        assert_that(post, "Unexpected error for post job schedule").contains_key("msg")
        assert_that(post["msg"], "Job schedule post failed").is_equal_to("Success")

        # Validate the job has updated
        job_schedule = api_utils.get(V2_GET_JOB_SCHEDULE, {"dataset": DATASET_DEMO_BLOCKS})
        compare_dicts_are_equal(job_schedule, EXP_SCH_DEMO_BLOCKS, ["updtTs"])

        # Cleanup
        self.delete_job_schedule(api_utils, DATASET_DEMO_BLOCKS)

    @allure.feature("Pullup")
    @allure.story("Job Schedule")
    def test_job_schedule_restrictions_add_update_delete(self, api_utils):
        """Test Job schedule restrictions add, update, and delete"""

        # Setup
        self.delete_all_restrictions(api_utils)

        # Create restriction
        self.create_restriction(api_utils, PL_SCH_RES_CREATE)
        restriction = self.get_and_check_count_of_restrictions(api_utils, 1)[0]

        # Validate the info in the created restriction
        self.validate_restriction_data(
            restriction,
            SCH_TYPE,
            f"{TODAY_FORMAT}T{SCH_RES_HOUR_START_FULL}",
            f"{TODAY_FORMAT}T{SCH_RES_HOUR_END_FULL}",
        )
        restriction_id = restriction["id"]
        pl_update = PL_SCH_RES_CREATE_UPDATE
        pl_update["id"] = restriction_id

        # Update the time
        update = api_utils.post(V2_UPDATE_SCHEDULER_RESTRICTION, pl_update, return_json=False)
        assert_that(update.status_code, "Update schedule restriction failed").is_equal_to(200)

        # Validate the info in the updated restriction
        restriction = self.get_and_check_count_of_restrictions(api_utils, 1)[0]
        self.validate_restriction_data(
            restriction,
            SCH_TYPE,
            f"{TODAY_FORMAT}T{SCH_RES_UPDATE_HOUR_START}",
            f"{TODAY_FORMAT}T{SCH_RES_UPDATE_HOUR_END}",
        )

        # Delete the restriction
        self.delete_all_restrictions(api_utils)

    @allure.feature("Pullup")
    @allure.story("Job Schedule")
    def test_job_schedule_restrictions_schedule_job_refused(self, api_utils):
        """Test that scheduling a job during a restriction period is refused"""

        # Data setup
        sch_data = SCH_DATA_RES_REFUSED
        agent_details = helper.get_agent_details_for_connection(api_utils, CONNECTION_DEMO_BLOCKS)
        sch_data["agentId"] = agent_details["agentId"]["id"]
        sch_data = helper.add_scheduled_run_date_time_zoned_to_parameters(sch_data)
        ds_def = helper.get_minimum_job_payload(
            api_utils, CONNECTION_DEMO_BLOCKS, DATASET_DEMO_BLOCKS, QUERY_DEMO_BLOCKS
        )

        self.delete_all_restrictions(api_utils)  # Cleanup prep
        self.create_restriction(api_utils, PL_CREATE_RES_REFUSED)
        self.get_and_check_count_of_restrictions(api_utils, 1)

        # Create job and post schedule
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_def)
        add_schedule = api_utils.post(V2_POST_JOB_SCHEDULE, params=sch_data)  # Should be refused
        assert_that(add_schedule).contains_key("msg")
        assert_that(add_schedule["msg"]).is_equal_to(MSG_RES_REFUSED)

        # Verify job not activated since the request was refused
        job_schedule = api_utils.get(V2_GET_JOB_SCHEDULE, {"dataset": DATASET_DEMO_BLOCKS})
        assert_that(job_schedule["active"]).is_equal_to(0)

        # Cleanup
        self.delete_all_restrictions(api_utils)

    @allure.feature("Pullup")
    @allure.story("Job Schedule")
    def test_job_schedule_restrictions_multi_one_day(self, api_utils):
        """Test multiple schedule restrictions can exist on the same day."""

        # Notes:
        #  - GUI prevents user from making duplicates & start times after end times, not the API
        #  - Values are sorted by schedule ID and will always be in the order of creation

        # Setup - Clear any data
        self.delete_all_restrictions(api_utils)

        # Create restriction
        for pl_item in PL_SCH_RES_CREATE_MULTI:
            self.create_restriction(api_utils, pl_item)
        found_schedules = self.get_and_check_count_of_restrictions(
            api_utils, len(PL_SCH_RES_CREATE_MULTI)
        )

        # Validate the info in the created restriction
        with soft_assertions():
            for i, created_item in enumerate(found_schedules):
                assert_that(created_item["id"]).is_greater_than(0)
                assert_that(created_item["type"]).is_equal_to(EXP_SCH_RES_MULTI[i]["type"])
                assert_that(created_item["start_value"]).is_equal_to(
                    f"{EXP_SCH_RES_MULTI[i]['start_value']}"
                )
                assert_that(created_item["end_value"]).is_equal_to(
                    f"{EXP_SCH_RES_MULTI[i]['end_value']}"
                )

        # Cleanup
        self.delete_all_restrictions(api_utils)
