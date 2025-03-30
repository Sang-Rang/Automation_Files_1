from datetime import datetime, timedelta
import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_agent import V2_GET_AGENT
from endpoints.v2.controller_job import V2_GET_OWL_CHECK_Q, V2_JOB_CHART_SERIES
from endpoints.v3.dataset_def_api import V3_DATASETDEFS
from endpoints.v3.job_api import V3_JOBS_JOBID_WAITFORCOMPLETION, V3_RUN_CMD_LINE
from payloads.general.pl_run_job_via_cmd_line import RUN_JOB_VIA_CMD_LINE_DATASET_DEFS
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


class TestJobStatus:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def count_jobs_by_date_in_status(api_utils, status, parsing_obj):
        """Parse and store dates & counts of jobs of a given status on each date"""

        # Note: On average, automation tenant runs <6000 jobs across 7 days.
        # 50,000 should be an adequate buffer, but can be upped in the future as needed
        pl_job = {"jobStatus": status.upper(), "limit": 50000}
        found_jobs = api_utils.get(V2_GET_OWL_CHECK_Q, params=pl_job)["data"]

        for job in found_jobs:
            date_full = datetime.strptime(job["updtTs"], "%Y-%m-%dT%H:%M:%S.%f%z")
            format_date = datetime.strftime(date_full, "%Y-%m-%d")
            if format_date in parsing_obj[status]:
                parsing_obj[status][format_date] += 1
            else:
                parsing_obj[status][format_date] = 1
        parsing_obj[status] = dict(sorted(parsing_obj[status].items(), reverse=False))

    @staticmethod
    def check_job_status_results(api_utils, status, maximum=5, minimum=0):
        """Get and validate the job status query and result limit"""
        pl_job = {"jobStatus": status, "limit": maximum}
        job_status_all = api_utils.get(V2_GET_OWL_CHECK_Q, params=pl_job)
        assert_that(job_status_all, f"Job status search call for {pl_job} failed").contains_key(
            "data"
        )
        assert_that(
            len(job_status_all["data"]), "Incorrect maximum number of records returned"
        ).is_less_than_or_equal_to(maximum)

        assert_that(
            len(job_status_all["data"]), "Incorrect minimum number of records returned"
        ).is_greater_than_or_equal_to(minimum)

    @allure.feature("Jobs")
    @allure.story("Job Chart")
    def test_job_chart_series(self, api_utils):
        parsed_chart = {"finished": {}, "failed": {}, "submitted": {}}
        parsed_jobs = {"finished": {}, "failed": {}, "submitted": {}}

        # The Job Status chart shows the last 35 days of data.
        date_earliest = (datetime.today() - timedelta(days=35)).strftime("%Y-%m-%d")
        today = datetime.today().strftime("%Y-%m-%d")

        # Take the data from the job chart and convert it into days
        # Then calculate the total jobs of each status
        job_chart_series = api_utils.get(V2_JOB_CHART_SERIES + "?timeBin=day")

        for status, value in job_chart_series.items():
            for found_date, qty in value:
                epoc_to_utc = datetime.utcfromtimestamp(int(found_date) / 1000)
                converted_date = datetime.strftime(epoc_to_utc, "%Y-%m-%d")

                # If the key already exists, increase the qty. Otherwise, set a new key.
                if converted_date in parsed_chart[status]:
                    parsed_chart[status][converted_date] += int(qty)
                else:
                    parsed_chart[status][converted_date] = int(qty)

        self.count_jobs_by_date_in_status(api_utils, "failed", parsed_jobs)
        self.count_jobs_by_date_in_status(api_utils, "submitted", parsed_jobs)
        self.count_jobs_by_date_in_status(api_utils, "finished", parsed_jobs)

        # Validate that the number of each status matches between the chart and
        # the total qty of jobs run on each date
        for status, date_count in parsed_chart.items():
            for key, val in date_count.items():

                # date_earliest - Ignored because as new jobs are run, the earliest jobs get
                # removed from these totals. These counts can be observed decreasing in these calls
                # manually through the api throughout the day.

                # today - Ignored because of new jobs being started, jobs changing status from
                # submitted to done/failed, parallel execution, and delay in chart updating latency,
                # today's numbers are constantly changing.

                if key not in (date_earliest, today):
                    assert_that(val, f"Unexpected value for {date_count}").is_equal_to(
                        parsed_jobs[status][key]
                    )

    @allure.feature("Jobs")
    @allure.story("Job Status")
    def test_job_status_results(self, api_utils):
        self.check_job_status_results(api_utils, "")  # Empty = All
        self.check_job_status_results(api_utils, "FAILED")
        self.check_job_status_results(api_utils, "UNKNOWN")
        self.check_job_status_results(api_utils, "RUNNING")
        self.check_job_status_results(api_utils, "FINISHED", minimum=1)
        self.check_job_status_results(api_utils, "SUBMITTED")

    @allure.feature("Jobs")
    @allure.story("Job CMD")
    @pytest.mark.pullup
    def test_run_job_via_cmd_line(self, api_utils):
        """Run the job via cmdLine, /v3/jobs/runCmdLine."""
        helper.setup_dataset(api_utils, RUN_JOB_VIA_CMD_LINE_DATASET_DEFS)
        cmd_line_resp = api_utils.get(
            V3_DATASETDEFS + "/" + RUN_JOB_VIA_CMD_LINE_DATASET_DEFS["dataset"] + "/cmdLine"
        )
        agent_name = api_utils.get(
            V2_GET_AGENT, params={"agentid": RUN_JOB_VIA_CMD_LINE_DATASET_DEFS["agentId"]["id"]}
        )["agentName"]
        run_cmd = api_utils.post(
            V3_RUN_CMD_LINE, params={"agentName": agent_name}, json=cmd_line_resp
        )
        assert_that(run_cmd["status"], "Job failed to submit").is_equal_to("SUBMITTED")

        job_id = run_cmd["jobId"]
        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=job_id))
        assert_that(job_output["status"], "Job was not finished").is_equal_to("FINISHED")
