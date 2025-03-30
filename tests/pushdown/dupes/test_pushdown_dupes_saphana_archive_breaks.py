import allure
import pytest

from data_test.pushdown.dupes.data_pd_saph_dupes_exact_case_employees_dt import (
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pushdown.dupes.data_pd_saph_dupes_exact_case_employees_dt_archive_breaks import (
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DUPES,
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.dupes.data_pd_saph_dupes_exact_nocase_employees_dt import (
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pushdown.dupes.data_pd_saph_dupes_exact_nocase_employees_dt_archive_breaks import (
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DUPES,
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from payloads.pushdown.dupes.pl_pd_saph_dupes_exact_case_employees_dt_archive_breaks import (
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
    PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.dupes.pl_pd_saph_dupes_exact_nocase_employees_dt_archive_breaks import (
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
    PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_dupes import (
    validate_dupes_findings,
    validate_pushdown_dupes_archived_break_records,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.saphana
class TestPushdownDupesSAPHANAArchiveBreaks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Dupes - Archive Break Records")
    def test_pushdown_saphana_dupes_exact_case_employees_dt_archive_breaks(self, api_utils):
        job_response = helper.run_pushdown_job(
            api_utils, PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_dupes_findings(
            api_utils,
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DUPES,
        )

        validate_dupes_findings(
            api_utils,
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_pushdown_dupes_archived_break_records(
            api_utils,
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_SAPH_DUPES_EXACT_CASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Dupes - Archive Break Records")
    def test_pushdown_saphana_dupes_exact_nocase_employees_dt_archive_breaks(self, api_utils):
        job_response = helper.run_pushdown_job(
            api_utils, PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_dupes_findings(
            api_utils,
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DUPES,
        )

        validate_dupes_findings(
            api_utils,
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_pushdown_dupes_archived_break_records(
            api_utils,
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_SAPH_DUPES_EXACT_NOCASE_EMPLOYEES_DT_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )
