from datetime import datetime
import allure
import pytest
from assertpy import assert_that
from utils.api_utils import APIUtils
from endpoints.v2.controller_page import (
    V2_ADD_PAGE,
    V2_GET_PAGES,
    V2_DELETE_PAGE,
)
from endpoints.v2.controller_scorecard import (
    V2_PUT_SCORECARD,
    V2_UPDATE_SCORECARD,
    V2_DELETE_SCORECARD,
    V2_GET_DATASET_NAMES,
    V2_GET_HEATMAP_BY_PAGE,
)


class TestViewScorecard:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Scorecard")
    @allure.story("Page and Card")
    @pytest.mark.cloud
    @pytest.mark.smoke
    def test_view_score_card_operations(self, api_utils):
        """Test View Scorecard - Page & Scorecard - Add, Update, Delete."""
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        page_name = "AUTO_ScoreView_" + str(now)  # Name should be unique.
        max_datasets = 50

        # API Calls
        api_get_heat_map = f"{V2_GET_HEATMAP_BY_PAGE}?pageId="

        # Data
        data_create_page = {"pageNm": page_name}

        # Scorecard data content
        # This data is also used for DELETE
        # -1 & None are added later in test.
        data_create_scorecard1 = {
            "pageId": -1,
            "scoreCardName": page_name + "_scorecard1",
            "duallistbox_scoreCard[]": None,
            "groupId": -1,
        }

        data_create_scorecard2 = {
            "pageId": -1,
            "scoreCardName": page_name + "_scorecard2",
            "duallistbox_scoreCard[]": None,
            "groupId": -1,
        }

        # Create a scorecard page
        call_add_page = api_utils.post(V2_ADD_PAGE, params=data_create_page, return_json=False)
        assert call_add_page.status_code == 200, f"The addPage call failed. Found: {call_add_page}"
        json_add_page = call_add_page.json()
        assert_that(
            str(json_add_page),
            f"Add page failed to be created. Response: {str(json_add_page)}",
        ).is_equal_to("1")

        # Get created scorecard page for validation
        call_get_page = api_utils.get(V2_GET_PAGES, return_json=False)
        assert call_get_page.status_code == 200, f"getPages call failed. Found: {call_get_page}"
        json_get_page = call_get_page.json()

        # Verify the page was created.
        for page in json_get_page:
            if page["pageNm"] == data_create_page["pageNm"]:
                page_id = page["pageId"]
                break
        else:
            raise AssertionError(
                f"Failure: The scorecard page was not created. "
                f"Expected {data_create_page['pageNm']} "
                f"in data: {json_get_page}"
            )

        # Duplicate page names are not allowed.
        # Verify error on duplicate page creation attempt.
        # (Duplicate scorecards are allowed.)
        call_add_page = api_utils.post(V2_ADD_PAGE, params=data_create_page, return_json=False)
        assert call_add_page.status_code == 500, (
            f"Expected addPage call failed on duplicate. " f"Found: {str(call_add_page)}"
        )

        # Verify a new page has zero scorecards.
        call_get_heat_map0 = api_utils.get(api_get_heat_map + str(page_id), return_json=False)
        assert call_get_heat_map0.status_code == 200, (
            f"The getHeatmap #0 call failed. " f"Found: {str(call_get_heat_map0.status_code)}"
        )
        assert_that(
            len(call_get_heat_map0.json()),
            f"Heatmap #0 failed. Expected 0 score_cards but "
            f"found: {str(len(call_get_heat_map0.json()))}",
        ).is_equal_to(0)

        # Get dataset data to use. (Sanity check. As long as 1 job has been run
        # in the environment, datasets must exist.)
        call_get_datasets = api_utils.get(V2_GET_DATASET_NAMES, return_json=False)
        assert (
            call_get_datasets.status_code == 200
        ), f"The getDataAssetNames call failed. Found: {call_get_datasets}"
        json_get_datasets = call_get_datasets.json()
        assert_that(
            len(json_get_datasets),
            "Call getDataAssetNames found no existing data.",
        ).is_greater_than(0)

        # If there are less than the given datasets, add all available.
        max_datasets_check = len(json_get_datasets)
        if max_datasets_check < max_datasets:
            max_datasets = max_datasets_check

        # Make a list of datasets to use later
        dataset_list = []
        for dataset in range(0, max_datasets):
            dataset_list.append(json_get_datasets[dataset]["dataset"])

        # Create data for add scorecard.
        # Not testing data validity here. Only scorecard functionality.
        data_create_scorecard1["pageId"] = page_id
        data_create_scorecard2["pageId"] = page_id
        data_create_scorecard1["duallistbox_scoreCard[]"] = dataset_list
        data_create_scorecard2["duallistbox_scoreCard[]"] = dataset_list

        # if debugCreateData:
        # Add 2 scorecards
        call_post_scorecard1 = api_utils.post(
            V2_PUT_SCORECARD, params=data_create_scorecard1, return_json=False
        )
        assert (
            call_post_scorecard1.status_code == 200
        ), f"The putScorecard call 1 failed. Found: {call_post_scorecard1}"

        call_post_scorecard2 = api_utils.post(
            V2_PUT_SCORECARD, params=data_create_scorecard2, return_json=False
        )
        assert (
            call_post_scorecard2.status_code == 200
        ), f"The putScorecard call 2 failed. Found: {call_post_scorecard2}"

        # Validate there are 2 scorecards.
        call_get_heatmap1 = api_utils.get(api_get_heat_map + str(page_id), return_json=False)
        assert (
            call_get_heatmap1.status_code == 200
        ), f"The getHeatmap #1 call failed. Found: {call_get_heatmap1}"
        json_heatmap1 = call_get_heatmap1.json()
        assert_that(
            len(json_heatmap1),
            f"Heatmap #1 failed. Expected 2 score_cards but " f"found: {json_heatmap1}",
        ).is_equal_to(2)

        # Save the groupId
        data_create_scorecard1["groupId"] = json_heatmap1[0]["groupId"]
        data_create_scorecard2["groupId"] = json_heatmap1[1]["groupId"]

        # Edit scorecard
        data_create_scorecard2["scoreCardName"] = (
            data_create_scorecard2["scoreCardName"] + "_edited"
        )
        call_update_scorecard2 = api_utils.post(
            V2_UPDATE_SCORECARD,
            params=data_create_scorecard2,
            return_json=False,
        )
        assert (
            call_update_scorecard2.status_code == 200
        ), f"The updateScorecard call failed. Found: {call_update_scorecard2}"

        # Refresh data
        call_get_heat_map2 = api_utils.get(api_get_heat_map + str(page_id), return_json=False)
        assert (
            call_get_heat_map2.status_code == 200
        ), f"The getHeatmap #2 call failed. Found: {call_get_heat_map2}"
        json_heatmap2 = call_get_heat_map2.json()
        assert_that(
            json_heatmap2[1]["title"],
            f"Heatmap #2 failed. Expected title to be: "
            f"{data_create_scorecard2['scoreCardName']} "
            f"but found: {json_heatmap2[1]['title']}",
        ).is_equal_to(data_create_scorecard2["scoreCardName"])

        # Delete scorecard
        # Reusing the creation data in this call as it has all the
        # necessary parameters.
        call_delete_scorecard = api_utils.post(
            V2_DELETE_SCORECARD,
            params=data_create_scorecard1,
            return_json=False,
        )
        assert (
            call_delete_scorecard.status_code == 200
        ), f"The deleteScorecard call failed. Found: {call_delete_scorecard}"

        # Check delete successful
        call_get_heat_map3 = api_utils.get(api_get_heat_map + str(page_id), return_json=False)
        assert (
            call_get_heat_map3.status_code == 200
        ), f"The getHeatmap #3 call failed. Found: {call_get_heat_map3}"
        json_heatmap3 = call_get_heat_map3.json()
        assert_that(
            len(json_heatmap3),
            f"Heatmap #3 call failed. Expected 1 scorecards " f"but found: {json_heatmap3}",
        ).is_equal_to(1)

        # Delete page (with scorecard still on it)
        call_delete_scorecard = api_utils.delete(
            f"{V2_DELETE_PAGE}?page={page_name}", return_json=False
        )
        assert (
            call_delete_scorecard.status_code == 200
        ), f"The deleteScorecard call failed. Found: {call_delete_scorecard}"

        # Verify deleted
        call_get_page2 = api_utils.get(V2_GET_PAGES, return_json=False)
        assert (
            call_get_page2.status_code == 200
        ), f"The getPage 2 call failed. Found: {call_get_page2}"
        json_get_page2 = call_get_page2.json()

        for page in json_get_page2:
            if page["pageNm"] == data_create_page["pageNm"]:
                raise AssertionError(
                    f"ERROR: Page was expected to be deleted, but still found."
                    f" Result {str(page)}"
                )
