import re
from datetime import datetime

import allure
import pytest

from assertpy import assert_that
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.constants import PROD_RUN_ID
from endpoints.v2.controller_scheduler import V2_POST_JOB_SCHEDULE
from endpoints.v2.controller_buisness_unit import (
    V2_BUSINESS_UNIT_DATASET_COUNTS,
)
from endpoints.v2.controller_connections import V2_DISTINCT_CXNS
from endpoints.v2.controller_pulse import V2_GET_PULSE
from data_test.pullup.data_pulse_view_filters import (
    DATA_DEFAULT_FILTER,
    EPOCH_DIVIDE_VALUE,
    DATETIME_CONVERT_FORMAT,
    SEARCH_Y_CAT_STRING,
    SEARCH_Y_CAT_GROUP,
    DATA_JOB_SCH_QUERY_DAILY,
    DATA_JOB_SCH_QUERY_MONTHLY,
    DATA_SCHEDULED,
    NM_SCHEDULED,
    CONNECTION,
    DATASET,
    QUERY,
    DATA_LOOK_BACK,
    NM_BUSINESS_UNIT,
)

helper = BaseHelper()


@pytest.mark.pullup
class TestPulseView:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.feature("Pulse View")
    @allure.story("Filters")
    def test_pulse_view_filters(self, api_utils):
        """Test Pulse View Filters"""

        # Notes:
        #   Does not validate the validity of data,
        #   only that present data matches given filters.
        #   Does not validate users or modes because the API does
        #   not return that specific information.

        # > Create job to schedule daily and monthly for later valdiation
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            connection_name=CONNECTION,
            dataset_name=DATASET,
            query=QUERY,
        )

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dataset_defs, PROD_RUN_ID)
        api_utils.post(V2_POST_JOB_SCHEDULE, DATA_JOB_SCH_QUERY_DAILY)
        api_utils.post(V2_POST_JOB_SCHEDULE, DATA_JOB_SCH_QUERY_MONTHLY)

        # Fetch dynamic data (values in dropdowns) to be used for filters
        bu_ds_count = api_utils.get(V2_BUSINESS_UNIT_DATASET_COUNTS)["result"]
        cxns = api_utils.get(V2_DISTINCT_CXNS)

        # DATA FILTER LOOKBACK: Validate results return within LB range.
        df_lb = DATA_DEFAULT_FILTER.copy()

        for look_back_value in DATA_LOOK_BACK:
            # Update filter
            df_lb["lookback"] = look_back_value["timeRange"]
            df_lb["lb_time"] = look_back_value["time"]

            # Fetch data
            pulse_lb = api_utils.get(V2_GET_PULSE, params=df_lb)

            # Validate the dates
            found_x_cat = pulse_lb["xCategories"]
            for found_x_category_item in found_x_cat:
                found_date = datetime.fromtimestamp(
                    found_x_category_item / EPOCH_DIVIDE_VALUE
                ).strftime(DATETIME_CONVERT_FORMAT)

                dt_cd = datetime.strptime(found_date, "%Y-%m-%d").date()
                dt_lbt = datetime.strptime(df_lb["lb_time"], "%Y-%m-%d").date()
                assert_that(dt_cd, "Lookback").is_greater_than_or_equal_to(dt_lbt)

        # DATA FILTER SCHEDULED: Validate Scheduled returns filtered results
        df_sch = DATA_DEFAULT_FILTER.copy()

        for scheduled in DATA_SCHEDULED:
            # Update filter
            df_sch[NM_SCHEDULED] = scheduled[NM_SCHEDULED]
            msg = scheduled["msg"]

            # Fetch data and validate
            pulse_s = api_utils.get(V2_GET_PULSE, params=df_sch)

            for series_data in pulse_s["series"]:
                found_value = series_data["value"]
                if found_value != "Missing" and msg not in found_value:
                    raise AssertionError(
                        f"Error: Unexpected value in pulse series "
                        f"{found_value}, expected 'Missing' or {msg}."
                    )

        # DATA FILTER BUSINESS UNIT
        df_bu = DATA_DEFAULT_FILTER.copy()

        for b_unit in bu_ds_count:
            df_bu[NM_BUSINESS_UNIT] = b_unit["id"]

            pulse_bu = api_utils.get(V2_GET_PULSE, params=df_bu)
            assert_that(str(pulse_bu[NM_BUSINESS_UNIT]), "Business Unit").is_equal_to(
                str(b_unit["id"])
            )

        # DATA FILTER CONNECTIONS
        df_c = DATA_DEFAULT_FILTER.copy()

        for connection in cxns:
            df_c["cxn"] = connection

            pulse_c = api_utils.get(V2_GET_PULSE, params=df_c)

            for found_y_category_item in pulse_c["yCategories"]:
                result = re.search(SEARCH_Y_CAT_STRING, found_y_category_item)
                if result is None:  # Not all connections have icons.
                    found = found_y_category_item
                else:
                    found = result.group(SEARCH_Y_CAT_GROUP)
                assert_that(found, "Connection").is_equal_to(connection)
