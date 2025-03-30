import allure
import pytest

from payloads.pushdown.dq_job.pl_pd_dbrks_dq_job_row_limit_sales import (
    PD_DBRKS_DQ_JOB_ROW_LIMIT_SALES_PAYLOAD,
    PD_DBRKS_DQ_JOB_ROW_LIMIT_SALES_ROW_LIMIT,
)
from payloads.pushdown.dq_job.pl_pd_dbrks_dq_job_runid_timestamp_sales import (
    PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_PAYLOAD,
    PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID,
    PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END,
)
from payloads.pushdown.dq_job.pl_pd_dbrks_dq_job_sales import (
    PD_DBRKS_DQ_JOB_SALES_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import run_and_validate_pd_job

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.databricks
class TestPushdownDqJobDatabricks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_databricks_dq_job_row_limit_sales(self, api_utils):
        """Run a basic DQ job on pushdown Databricks with row limit"""
        run_and_validate_pd_job(
            api_utils,
            PD_DBRKS_DQ_JOB_ROW_LIMIT_SALES_PAYLOAD,
            expected_row_count=PD_DBRKS_DQ_JOB_ROW_LIMIT_SALES_ROW_LIMIT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_databricks_dq_job_runid_timestamp_sales(self, api_utils):
        """Run a basic DQ job on pushdown Databricks with runId and runIdEnd values
        including timestamps"""
        run_and_validate_pd_job(
            api_utils,
            PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_PAYLOAD,
            expected_run_id=PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID,
            expected_run_id_end=PD_DBRKS_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - DQ Job")
    def test_pushdown_databricks_dq_job_sales(self, api_utils):
        """Run a basic DQ job on pushdown Databricks"""
        run_and_validate_pd_job(api_utils, PD_DBRKS_DQ_JOB_SALES_PAYLOAD)
