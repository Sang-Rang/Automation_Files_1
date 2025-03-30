import allure
import pytest

from assertpy import assert_that

from payloads.pullup.pl_pullup_oracle_dq_job_parallel_jdbc_sales import (
    PULLUP_ORACLE_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD,
)
from payloads.pullup.pl_pullup_snowflake_dq_job_parallel_jdbc_sales import \
    PULLUP_SNOWFLAKE_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD
from payloads.pullup.pl_pullup_trino_dq_job_parallel_jdbc_sales import (
    PULLUP_TRINO_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupDqJob:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Pullup - DQ Job")
    def test_pullup_oracle_dq_job_parallel_jdbc_sales(self, api_utils):
        """Run a basic DQ job on pullup Oracle with parallel jdbc configured"""
        job_response = helper.setup_dataset(
            api_utils, PULLUP_ORACLE_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD
        )
        job_status = job_response["status"]

        expected_job_status = "FINISHED"
        assert_that(
            job_status,
            f"Unexpected job status. Expected status: {expected_job_status}, "
            f"Found status: {job_status} in {job_response}",
        ).is_equal_to(expected_job_status)

    @allure.feature("Pullup")
    @allure.story("Pullup - DQ Job")
    def test_pullup_snowflake_dq_job_parallel_jdbc_sales(self, api_utils):
        """Run a basic DQ job on pullup Snowflake with parallel jdbc configured"""
        job_response = helper.setup_dataset(
            api_utils, PULLUP_SNOWFLAKE_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD
        )
        job_status = job_response["status"]

        expected_job_status = "FINISHED"
        assert_that(
            job_status,
            f"Unexpected job status. Expected status: {expected_job_status}, "
            f"Found status: {job_status} in {job_response}",
        ).is_equal_to(expected_job_status)

    @allure.feature("Pullup")
    @allure.story("Pullup - DQ Job")
    def test_pullup_trino_dq_job_parallel_jdbc_sales(self, api_utils):
        """Run a basic DQ job on pullup Trino with parallel jdbc configured"""
        job_response = helper.setup_dataset(
            api_utils, PULLUP_TRINO_DQ_JOB_PARALLEL_JDBC_SALES_PAYLOAD
        )
        job_status = job_response["status"]

        expected_job_status = "FINISHED"
        assert_that(
            job_status,
            f"Unexpected job status. Expected status: {expected_job_status}, "
            f"Found status: {job_status} in {job_response}",
        ).is_equal_to(expected_job_status)
