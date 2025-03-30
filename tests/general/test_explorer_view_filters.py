import allure
import pytest
from assertpy import assert_that

from endpoints.v2.controller_explorer import V2_GET_EXPLORER_SEARCH
from data_test.general.data_explorer_view_filters import (
    DATA_SEARCH_TEMPLATE,
    DATA_VALIDATE,
)
from utils.api_utils import APIUtils


class TestExplorerView:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Explorer")
    @allure.story("View Filters")
    def test_explorer_view_filters(self, api_utils):
        """Test Explorer - View Filters."""
        # Filters using the catalog, schema, and table search fields and
        # validates expected results. (Per test case)
        for data in DATA_VALIDATE:
            DATA_SEARCH_TEMPLATE["catalogsearch"] = data["catalogsearch"]
            DATA_SEARCH_TEMPLATE["schemasearch"] = data["schemasearch"]
            DATA_SEARCH_TEMPLATE["tablesearch"] = data["tablesearch"]

            for check_item in data["checkvalidations"]:
                found_exists = False
                DATA_SEARCH_TEMPLATE["alias"] = check_item["alias"]
                does_exist = check_item["exists"]

                call_get_search = api_utils.get(
                    V2_GET_EXPLORER_SEARCH,
                    params=DATA_SEARCH_TEMPLATE,
                    return_json=False,
                )
                assert_that(
                    call_get_search.status_code,
                    f"The {V2_GET_EXPLORER_SEARCH} call failed. "
                    f"Found: {str(call_get_search)} from search data {DATA_SEARCH_TEMPLATE}"
                ).is_equal_to(200)

                json_get_search = call_get_search.json()

                if len(json_get_search) > 0:
                    found_exists = True
                assert_that(
                    does_exist,
                    f"Found {found_exists} but expected {does_exist} "
                    f"from search data: {str(DATA_SEARCH_TEMPLATE)}"
                ).is_equal_to(found_exists)
