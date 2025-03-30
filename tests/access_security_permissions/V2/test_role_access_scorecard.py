import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_scorecard import (
    ACCESS_MATRIX_SCORECARD,
)
from endpoints.v2.controller_scorecard import (
    V2_GET_HEATMAP_BY_DATASET,
    V2_GET_HEATMAP_BY_PAGE,
    V2_PUT_SCORECARD,
    V2_DELETE_SCORECARD,
    V2_UPDATE_SCORECARD,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessScorecard:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Scorecard")
    def test_role_access_get_heatmap_by_ds(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getheatmapbydataset"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_HEATMAP_BY_DATASET,
            ACCESS_MATRIX_SCORECARD[V2_GET_HEATMAP_BY_DATASET],
            payload={"dataset": job["dataset"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Scorecard")
    def test_role_access_add_get_update_delete_scorecard(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/putscorecard, /v2/getheatmapbypage,
        /v2/update-score-card, /v2/deletescorecard"""

        name = "ROLE_ACCESS_SCORECARD"
        name_edit = "ROLE_ACCESS_SCORECARD_EDIT"

        payload = {
            "pageId": 1,
            "groupId": 0,
            "scoreCardName": name,
            "duallistbox_scoreCard[]": "APPROVED_POSTGRES_UP",
        }

        for role in ACCESS_MATRIX_SCORECARD[V2_PUT_SCORECARD]:
            payload["scoreCardName"] = name
            user = security_helper.setup_user(get_auth_headers_multi_user, role)

            # Add scorecard
            add = api_utils.post(
                V2_PUT_SCORECARD, custom_headers=user, params=payload, return_json=False
            )
            security_helper.report_results(role, V2_PUT_SCORECARD, payload, add)

            # Get group ID
            get = api_utils.get(
                V2_GET_HEATMAP_BY_PAGE, custom_headers=user, params=payload, return_json=False
            )
            security_helper.report_results(role, V2_GET_HEATMAP_BY_PAGE, payload, get)
            payload["groupId"] = get.json()[0]["groupId"]

            # Update
            payload["scoreCardName"] = name_edit
            update = api_utils.post(
                V2_UPDATE_SCORECARD, custom_headers=user, params=payload, return_json=False
            )
            security_helper.report_results(role, V2_UPDATE_SCORECARD, payload, update)

            # Delete
            delete = api_utils.post(
                V2_DELETE_SCORECARD, custom_headers=user, params=payload, return_json=False
            )
            security_helper.report_results(role, V2_DELETE_SCORECARD, payload, delete)
