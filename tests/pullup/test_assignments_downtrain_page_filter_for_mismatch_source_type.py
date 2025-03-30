import allure
import pytest
from assertpy import assert_that
from data_test.pullup.data_pg_filter_mismatch_src_type import (
    EXP_PG_DTS_FILTER_MISMATCH_SRC_TYPE,
    EXP_ISSUE_COUNT_FILTER_MISMATCH_SRC_TYPE,
    MISMATCH_LIST_FILTER_MISMATCH_SRC_TYPE,
)
from payloads.pullup.pl_pg_filter_mismatch_src_type import (
    PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE_GENERAL,
    PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE_PAGING,
    PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE,
)
from utils.helper import BaseHelper
from utils.api_utils import APIUtils
from endpoints.v2.controller_hoot import V2_GET_ISSUE_COUNTS
from endpoints.v2.controller_assignment_q import V2_FIND_ALL_PAGING_DATATABLES

helper = BaseHelper()


@pytest.mark.pullup
class TestAssignmentsDowntrainPageFilter:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Assignments / Down-train")
    @pytest.mark.skip(reason="Bug DEV-61462")
    def test_page_filter_for_mismatch_source_type(self, api_utils):
        """Test Assignments page filter for mismatch source type"""

        # Declare vars for sum total expected values for later validation
        exp_sum_mm_src = 0  # Expected
        exp_sum_pg_dts = 0
        exp_sum_iss_counts = 0
        f_sum_pg_dts = 0  # Found
        f_sum_mm_src = 0
        f_sum_iss_count = 0

        # Calculate the total expected value for mismatch, issues, and others
        for key, value in EXP_PG_DTS_FILTER_MISMATCH_SRC_TYPE.items():
            if key in MISMATCH_LIST_FILTER_MISMATCH_SRC_TYPE:
                exp_sum_mm_src += value
            else:
                exp_sum_pg_dts += value

        for key, value in EXP_ISSUE_COUNT_FILTER_MISMATCH_SRC_TYPE.items():
            exp_sum_iss_counts += value

        # Run
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE
        )

        # Find # of issues, sum them, and compare to expected total
        get_iss_count = api_utils.get(
            V2_GET_ISSUE_COUNTS, params=PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE_GENERAL
        )

        for key, value in get_iss_count.items():
            f_sum_iss_count += value  # Sum total for later use
            assert_that(value, f"Issue count {key}").is_equal_to(
                EXP_ISSUE_COUNT_FILTER_MISMATCH_SRC_TYPE[key]
            )

        # Loop through all types in the paging datatables,
        # Validate the value found matches expected
        # and sum them all for comparison to sum issue counts
        for key, value in EXP_PG_DTS_FILTER_MISMATCH_SRC_TYPE.items():
            PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE_PAGING["type"] = key
            get_paging_datatables = api_utils.get(
                V2_FIND_ALL_PAGING_DATATABLES, params=PL_DS_DEF_FILTER_MISMATCH_SRC_TYPE_PAGING
            )

            assert_that(value, f"Paging datatable {key}").is_equal_to(
                get_paging_datatables["recordsFiltered"]
            )

            if key in MISMATCH_LIST_FILTER_MISMATCH_SRC_TYPE:
                f_sum_mm_src += value
            else:
                f_sum_pg_dts += value

        assert_that(exp_sum_iss_counts, "Total issue count").is_equal_to(f_sum_iss_count)
        assert_that(exp_sum_pg_dts, "Total paging datatables").is_equal_to(f_sum_pg_dts)
        assert_that(exp_sum_mm_src, "Total mismatch src").is_equal_to(f_sum_mm_src)
