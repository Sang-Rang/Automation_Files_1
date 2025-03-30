import allure
import pytest

from payloads.pushdown.dq_job.pl_pd_rs_dq_job_row_limit_sales import (
    PD_RS_DQ_JOB_ROW_LIMIT_SALES_PAYLOAD,
    PD_RS_DQ_JOB_ROW_LIMIT_SALES_ROW_LIMIT,
)
from payloads.pushdown.dq_job.pl_pd_rs_dq_job_runid_timestamp_sales2 import (
    PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_PAYLOAD,
    PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_RUNID,
    PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_RUNID_END,
)
from payloads.pushdown.dq_job.pl_pd_rs_dq_job_sales2 import (
    PD_RS_DQ_JOB_SALES2_PAYLOAD,
)
from payloads.pushdown.dq_job.pl_pd_rs_dq_job_venue import (
    PD_RS_DQ_JOB_VENUE_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import run_and_validate_pd_job

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.redshift
class TestPushdownDqJobRedshift:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_redshift_dq_job_row_limit_sales(self, api_utils):
        """Run a basic DQ job on pushdown Redshift with row limit"""
        run_and_validate_pd_job(
            api_utils,
            PD_RS_DQ_JOB_ROW_LIMIT_SALES_PAYLOAD,
            expected_row_count=PD_RS_DQ_JOB_ROW_LIMIT_SALES_ROW_LIMIT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_redshift_dq_job_runid_timestamp_sales(self, api_utils):
        """Run a basic DQ job on pushdown Redshift with runId and runIdEnd values
        including timestamps"""
        run_and_validate_pd_job(
            api_utils,
            PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_PAYLOAD,
            expected_run_id=PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_RUNID,
            expected_run_id_end=PD_RS_DQ_JOB_RUNID_TIMESTAMP_SALES2_RUNID_END,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_redshift_dq_job_sales(self, api_utils):
        """Run a basic DQ job on pushdown Redshift"""
        run_and_validate_pd_job(api_utils, PD_RS_DQ_JOB_SALES2_PAYLOAD)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_redshift_dq_job_venue(self, api_utils):
        """Run a DQ job on pushdown Redshift with data containing a newline character"""
        run_and_validate_pd_job(api_utils, PD_RS_DQ_JOB_VENUE_PAYLOAD)
