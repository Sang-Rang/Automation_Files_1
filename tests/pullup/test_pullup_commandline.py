import allure
import pytest
from assertpy import assert_that

from payloads.pullup.pl_pullup_cmdline_backrun_not_persist import (
    PULLUP_CMDLINE_BACKRUN_NOT_PERSIST_DATASET,
    PULLUP_CMDLINE_BACKRUN_NOT_PERSIST_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

from endpoints.v2.controller_job import V2_GET_JOB_STATUS_BY_DATASET

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupCommandline:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Command Line")
    @pytest.mark.skip(reason="Enable when DEV-102193 is addressed")
    def test_pullup_commandline_backrun_setting_does_not_persist(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_CMDLINE_BACKRUN_NOT_PERSIST_PAYLOAD)
        job_response_status = job_response["status"]

        expected_job_status = "FINISHED"
        assert_that(
            job_response_status,
            f"Unexpected job status. Expected status: {expected_job_status}, "
            f"Found status: {job_response_status} in {job_response}",
        ).is_equal_to(expected_job_status)

        job_status = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET,
            params={
                "dataset": PULLUP_CMDLINE_BACKRUN_NOT_PERSIST_DATASET,
                "runId": job_response["runId"],
            },
        )
        post_job_run_commandline = job_status["cmdLine"]
        # Include spaces to ensure we only flag isolated command line option and not other strings
        backrun_commandline_option = " -br "

        assert_that(
            post_job_run_commandline,
            f"Found backrun option in command line after job run: {post_job_run_commandline}",
        ).does_not_contain(backrun_commandline_option)
