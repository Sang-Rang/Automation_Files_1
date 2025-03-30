import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_missing_endpoints_coverage import DUPE_OPT_RESPONSE
from data_test.pullup.data_pullup_dupe_downtrain_persist_rerun import (
    PL_DUPE_DWTR_DS_DEFS,
    PULLUP_DUPE_DWTR_RETRAIN_DS,
)
from data_test.pullup.data_pullup_dupe_case_insensitive import (
    PULLUP_DUPE_CASE_INSENSITIVE_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupe_case_sensitive import (
    PULLUP_DUPE_CASE_SENSITIVE_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupes_exact_case_employees_dt import (
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupes_exact_case_employees_dt_linkids import (
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupes_exact_nocase_employees_dt import (
    PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupes_score_case_employees_dt import (
    PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from data_test.pullup.data_pullup_dupes_score_nocase_employees_dt import (
    PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
)
from endpoints.v2.controller import V2_GET_LATEST_DATASET_HISTORY
from endpoints.v2.controller_assignment_q import V2_INVALIDATE_ASSIGNMENT
from endpoints.v2.controller_dupe_opt import V2_GET_DUPE_OPT
from endpoints.v2.controller_hoot import (
    V2_GET_ISSUE_COUNTS,
    V2_GET_OBSERVATION_DETAILS_2,
)
from endpoints.v2.controller_label import V2_VIEW_ITEM_LABELS, V2_RETRAIN
from payloads.pullup.pl_pullup_dupe_case_insensitive import (
    PULLUP_DUPE_CASE_INSENSITIVE_PAYLOAD,
    PULLUP_DUPE_CASE_INSENSITIVE_DATASET,
)
from payloads.pullup.pl_pullup_dupe_case_sensitive import (
    PULLUP_DUPE_CASE_SENSITIVE_PAYLOAD,
    PULLUP_DUPE_CASE_SENSITIVE_DATASET,
)
from payloads.pullup.pl_pullup_dupes_exact_case_employees_dt import (
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_DATASET,
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_PAYLOAD,
)
from payloads.pullup.pl_pullup_dupes_exact_case_linkids_employees_dt import (
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_DATASET,
    PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_PAYLOAD,
)
from payloads.pullup.pl_pullup_dupes_exact_nocase_employees_dt import (
    PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_DATASET,
    PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_PAYLOAD,
)
from payloads.pullup.pl_pullup_dupes_limit_accounts import (
    PULLUP_DUPES_LIMIT_ACCOUNTS_DATASET,
    PULLUP_DUPES_LIMIT_ACCOUNTS_PAYLOAD,
)
from payloads.pullup.pl_pullup_dupes_score_case_employees_dt import (
    PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_DATASET,
    PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_PAYLOAD,
)
from payloads.pullup.pl_pullup_dupes_score_nocase_employees_dt import (
    PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_DATASET,
    PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_PAYLOAD,
)
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal
from utils.validator_dupes import (
    validate_dupes_findings,
    validate_dupes_limit,
)

helper = BaseHelper()


@pytest.mark.pullup
class TestPullupDupes:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_exact_case_employees_dt(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_PAYLOAD)
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_exact_case_employees_dt_linkids(self, api_utils):
        job_response = helper.setup_dataset(
            api_utils, PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_PAYLOAD
        )
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_DATASET,
            job_response["runId"],
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_EXPECTED_DUPES,
        )

        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_LINKIDS_DATASET,
            job_response["runId"],
            PULLUP_DUPES_EXACT_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
            compare_link_ds_to_nolink_ds=True,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_exact_nocase_employees_dt(self, api_utils):
        job_response = helper.setup_dataset(
            api_utils, PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_PAYLOAD
        )
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PULLUP_DUPES_EXACT_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_limit_accounts(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_DUPES_LIMIT_ACCOUNTS_PAYLOAD)
        validate_dupes_limit(
            api_utils,
            PULLUP_DUPES_LIMIT_ACCOUNTS_DATASET,
            job_response["runId"],
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_score_case_employees_dt(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_PAYLOAD)
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PULLUP_DUPES_SCORE_CASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupes_score_nocase_employees_dt(self, api_utils):
        job_response = helper.setup_dataset(
            api_utils, PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_PAYLOAD
        )
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_DATASET,
            job_response["runId"],
            PULLUP_DUPES_SCORE_NOCASE_EMPLOYEES_DT_EXPECTED_DUPES,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupe_case_insensitive(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_DUPE_CASE_INSENSITIVE_PAYLOAD)
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPE_CASE_INSENSITIVE_DATASET,
            job_response["runId"],
            PULLUP_DUPE_CASE_INSENSITIVE_EXPECTED_DUPES,
        )

    @allure.feature("Pullup")
    @allure.story("Dupes")
    @pytest.mark.smoke
    @pytest.mark.skip(reason="Undo after DEV-DEV-121690 is fixed")
    def test_pullup_dupe_case_sensitive(self, api_utils):
        job_response = helper.setup_dataset(api_utils, PULLUP_DUPE_CASE_SENSITIVE_PAYLOAD)
        validate_dupes_findings(
            api_utils,
            PULLUP_DUPE_CASE_SENSITIVE_DATASET,
            job_response["runId"],
            PULLUP_DUPE_CASE_SENSITIVE_EXPECTED_DUPES,
        )
        # Add coverage for /v2/dupe-opt/get endpoint, not test related.
        dupe_response = api_utils.get(V2_GET_DUPE_OPT, params={"dataset": job_response["dataset"]})
        compare_dicts_are_equal(dupe_response, DUPE_OPT_RESPONSE)

    @allure.feature("Pullup")
    @allure.story("Dupes")
    def test_pullup_dupe_downtrain_persist_rerun(self, api_utils):
        """Downtrain, Persist, Retrain, and Rerun"""

        pl_general = {
            "dataset": PULLUP_DUPE_DWTR_RETRAIN_DS,
            "runId": PROD_RUN_ID,
        }
        pl_obs = {
            "dataset": PULLUP_DUPE_DWTR_RETRAIN_DS,
            "runId": PROD_RUN_ID,
            "type": "DUPE",
        }

        # Run the job and get the history, issues, and observations
        helper.setup_dataset(api_utils, PL_DUPE_DWTR_DS_DEFS)
        res_ds_hist1 = api_utils.get(V2_GET_LATEST_DATASET_HISTORY, params=pl_general)
        res_icounts1 = api_utils.get(V2_GET_ISSUE_COUNTS, params=pl_general)
        res_obs = api_utils.get(V2_GET_OBSERVATION_DETAILS_2, params=pl_obs)

        uuid = res_obs[0]["data"][0]["assignment_uuid"]
        assert_that(len(res_obs)).is_greater_than(0)

        pl_assign = {"uuid": uuid, "annotation": "invalid"}

        # Invalidate a dupe and retrain the job
        api_utils.post(V2_INVALIDATE_ASSIGNMENT, json=pl_assign, return_json=False)
        api_utils.post(V2_RETRAIN, pl_general, return_json=False)

        res_labels = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)
        res_ds_hist2 = api_utils.get(V2_GET_LATEST_DATASET_HISTORY, params=pl_general)
        res_icounts2 = api_utils.get(V2_GET_ISSUE_COUNTS, params=pl_general)

        # Validate job data has been modified from the invalidation
        obs_uuids = []
        for i in res_labels["data"]:
            obs_uuids.append(i["assignmentId"]["uuid"])

        assert_that(obs_uuids, "Pre-Rerun, Invalidation observation not in labels").contains(uuid)
        assert_that(
            res_ds_hist2["score"], "Pre-Rerun, Invalidation did not modify score"
        ).is_equal_to(res_ds_hist1["score"] + 1)
        assert_that(
            res_icounts2["DUPE"], "Pre-Rerun, Invalidation did not modify dupes."
        ).is_equal_to(res_icounts1["DUPE"] - 1)
        assert_that(
            res_ds_hist2["scoreDupe"], "Pre-rerun, Invalidation did not modify score dupe."
        ).is_equal_to(res_ds_hist1["scoreDupe"] - 1)

        # Rerun and refresh data
        helper.setup_dataset(api_utils, PL_DUPE_DWTR_DS_DEFS)
        res_icounts3 = api_utils.get(V2_GET_ISSUE_COUNTS, params=pl_general)
        res_ds_hist3 = api_utils.get(V2_GET_LATEST_DATASET_HISTORY, params=pl_general)
        res_labels = api_utils.get(V2_VIEW_ITEM_LABELS, params=pl_general)

        # Revalidate the data
        obs_post_rerun = []
        for i in res_labels["data"]:
            obs_post_rerun.append(i["assignmentId"]["uuid"])

        assert_that(obs_post_rerun, "Post-Rerun, Invalidation observation not in labels").contains(
            uuid
        )
        assert_that(
            res_ds_hist3["score"], "Post-Rerun, Invalidation did not modify score"
        ).is_equal_to(res_ds_hist2["score"])
        assert_that(
            res_icounts3["DUPE"], "Post-Rerun, Invalidation did not modify dupes"
        ).is_equal_to(res_icounts2["DUPE"])
        assert_that(
            res_ds_hist3["scoreDupe"], "Post-rerun, Invalidation did not modify score dupe."
        ).is_equal_to(res_ds_hist2["scoreDupe"])
