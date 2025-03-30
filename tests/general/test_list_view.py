from datetime import datetime, timedelta
import random
import allure
import pytest
import dateutil.relativedelta
from assertpy import assert_that
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from endpoints.v2.controller_dq_inbox import V2_GET_DQ_INBOX

helper = BaseHelper()


class TestListView:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("List View")
    @allure.story("Filters")
    def test_list_view_filters(self, api_utils):
        """Test List View Filters DEV-490234"""

        # NOTES:
        # No data generated since all jobs ran fall into at least one category
        # Only validating that existing data returns matching the filter
        # Does not cover the textbox search field, not part of API

        nm_filter_limit = "limit"
        nm_item_type = "itemType"
        nm_time_range = "timeRange"
        dt_format_full = "%Y-%m-%dT%H:%M:%S.%f%z"
        dt_format = "%Y-%m-%d"
        random_loop_number = 5
        data_limits = [100, 300, 500, 1000]  # When 'ALL', exclude value.

        data_item_types = [
            "BEHAVIOR",
            "DUPE",
            "SUGGESTIVE",  # = Patterns
            "RECORD_CHANGES",
            "RULE",
            "SCHEMA_EVOLUTION",
            "SHAPE",
            "MISMATCH_SRC",  # = Source
            "OUTLIER",
        ]

        # Filters UpdatedTs. Ignores times as filters are higher in scale
        data_time_range = [
            {
                "timeRange": "1 Day",
                "time": (datetime.now() - timedelta(1)).strftime(dt_format),
            },
            {
                "timeRange": "5 Day",  # NOT plural
                "time": (datetime.now() - timedelta(5)).strftime(dt_format),
            },
            {
                "timeRange": "1 Month",
                "time": (datetime.now() - dateutil.relativedelta.relativedelta(months=1)).strftime(
                    dt_format
                ),
            },
        ]

        # Sanity check. Data must exist with no filters.
        inbox1 = api_utils.get(V2_GET_DQ_INBOX)
        assert_that(len(inbox1), "No data in list view").is_greater_than(0)

        # ROW LIMIT - Verify search results are within row limit
        for data_expected in data_limits:
            inbox2 = api_utils.get(V2_GET_DQ_INBOX, params={nm_filter_limit: data_expected})
            assert_that(len(inbox2), "Row Limit").is_less_than_or_equal_to(data_expected)

        # ITEM TYPE: Search for each and verify the results match.
        for data_expected in data_item_types:
            inbox3 = api_utils.get(V2_GET_DQ_INBOX, params={nm_item_type: data_expected})

            for record_item_type in inbox3:
                data_row_found = record_item_type["itemType"]
                assert_that(data_expected, "Item Type").is_equal_to(data_row_found)

        # DATE RANGE: Search and verify the results return
        for data_expected in data_time_range:
            expected_time = data_expected["time"]

            inbox4 = api_utils.get(
                V2_GET_DQ_INBOX,
                params={nm_time_range: data_expected["timeRange"]},
            )

            for record_time_range in inbox4:
                data_row_found = record_time_range["itemDt"]

                # Convert to date format for value comparison
                assert_that(
                    datetime.strptime(data_row_found, dt_format_full).date(), "Record Time Range"
                ).is_greater_than_or_equal_to(datetime.strptime(expected_time, dt_format).date())

        # Randomize all filter data and validate.
        # Note: Since this is random combos,
        # it could legitimately return no results, therefore repeating.
        count_zero_results = 0
        for _ in range(0, random_loop_number):
            # Randomize combos of available data
            r_limit = random.randint(0, len(data_limits) - 1)
            r_type = random.randint(0, len(data_item_types) - 1)
            r_time = random.randint(0, len(data_time_range) - 1)

            # Pick 1 randomly of each filter option
            obj_random = {
                nm_filter_limit: data_limits[r_limit],
                nm_item_type: data_item_types[r_type],
                nm_time_range: data_time_range[r_time]["timeRange"],
            }
            expected_time = data_time_range[r_time]["time"]

            # Search with all filters and get results
            data_found = api_utils.get(V2_GET_DQ_INBOX, params=obj_random)

            # If no results found, increment counter.
            # If all random combos return 0, test will fail.
            if len(data_found) == 0:
                count_zero_results += 1

            # Check records are within limit
            found_limit = len(data_found)
            assert_that(
                found_limit,
                f"Expected limit {str(found_limit)} to be <="
                f" {str(obj_random[nm_filter_limit])} with random filters:"
                f" {r_limit}, {r_type}, {r_time}",
            ).is_less_than_or_equal_to(obj_random[nm_filter_limit])

            # Loop through all results to ensure they match all filter data
            for found_record in data_found:
                f_type = found_record["itemType"]
                f_time = found_record["itemDt"]

                # Check type
                assert_that(
                    f_type,
                    f"Expected type {obj_random[nm_item_type]} but found"
                    f" {f_type} with random filters:"
                    f" {r_limit}, {r_type}, {r_time}",
                ).is_equal_to(obj_random[nm_item_type])

                rng_date1 = datetime.strptime(f_time, dt_format_full).date()
                rng_date2 = datetime.strptime(expected_time, dt_format).date()
                assert_that(
                    rng_date1,
                    f"Expected date range  {rng_date1} but found {rng_date2}"
                    " with random filters:"
                    f" {r_limit}, {r_type}, {r_time}",
                ).is_greater_than_or_equal_to(rng_date2)

        assert_that(
            count_zero_results,
            "Filtering by random combos returned nothing after"
            f" {str(random_loop_number)} loops.",
        ).is_less_than(random_loop_number)
