import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_hoot import ACCESS_MATRIX_HOOT
from endpoints.v2.controller_hoot import (
    V2_GET_HOOT,
    V2_GET_DATA_PREVIEW_1,
    V2_GET_DATASET_ACTIVITY,
    V2_GET_DATASET_SCORING,
    V2_GET_ISSUE_COUNTS,
    V2_GET_OUTLIER_CALIBRATION_ENABLED,
    V2_GET_OWL_CHECK,
    V2_GET_TABLE_STATS,
    V2_GET_OUTLIER,
    V2_GET_OBSERVATIONS_BY_TYPE,
    V2_GET_SOURCE_COUNT_COMPARISON,
    V2_GET_SOURCE_SCHEMA_COMPARISON,
    V2_GET_SOURCE_VALUE_COMPARISON,
    V2_GET_OBSERVATION_DETAILS_2,
    V2_GET_DATA_SHAPES,
    V2_GET_SQL_RESULT,
)
from endpoints.v2.controller_rule import (
    V2_GET_RULE_WITH_DETAILS,
    V2_GET_SHAPE_WITH_DETAILS,
    V2_GET_PATTERN_WITH_DETAILS,
    V2_GET_OUTLIER_WITH_DETAILS,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessHoot:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_data_preview1(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatapreview1"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATA_PREVIEW_1,
            ACCESS_MATRIX_HOOT[V2_GET_DATA_PREVIEW_1],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_ds_activity(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetactivity"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_ACTIVITY,
            ACCESS_MATRIX_HOOT[V2_GET_DATASET_ACTIVITY],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_ds_scoring(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetscoring"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_SCORING,
            ACCESS_MATRIX_HOOT[V2_GET_DATASET_SCORING],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_hoot(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gethoot"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_HOOT,
            ACCESS_MATRIX_HOOT[V2_GET_HOOT],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_issue_counts(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getissuecounts"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ISSUE_COUNTS,
            ACCESS_MATRIX_HOOT[V2_GET_ISSUE_COUNTS],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_outlier_calibration_enabled(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/getoutliercalibrationenabled"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OUTLIER_CALIBRATION_ENABLED,
            ACCESS_MATRIX_HOOT[V2_GET_OUTLIER_CALIBRATION_ENABLED],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_owl_check(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlcheck"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECK,
            ACCESS_MATRIX_HOOT[V2_GET_OWL_CHECK],
            payload=job,
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_table_stats(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettablestats"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TABLE_STATS,
            ACCESS_MATRIX_HOOT[V2_GET_TABLE_STATS],
            payload={"dataset": job["dataset"], "runId": job["runId"], "sense": 3},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_outlier(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getoutlier"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OUTLIER,
            ACCESS_MATRIX_HOOT[V2_GET_OUTLIER],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_observations_by_type(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getobservationsbytype"""
        # Note: This API is used for suggestive, record_changes, schema_evolution findings tabs
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OBSERVATIONS_BY_TYPE,
            ACCESS_MATRIX_HOOT[V2_GET_OBSERVATIONS_BY_TYPE],
            payload={"dataset": job["dataset"], "runId": job["runId"], "type": "SUGGESTIVE"},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_source_count_comparison(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-source-count-comparison"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SOURCE_COUNT_COMPARISON,
            ACCESS_MATRIX_HOOT[V2_GET_SOURCE_COUNT_COMPARISON],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_source_schema_comparison(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-source-schema-comparison"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SOURCE_SCHEMA_COMPARISON,
            ACCESS_MATRIX_HOOT[V2_GET_SOURCE_SCHEMA_COMPARISON],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_source_value_comparison(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-source-value-comparison"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SOURCE_VALUE_COMPARISON,
            ACCESS_MATRIX_HOOT[V2_GET_SOURCE_VALUE_COMPARISON],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_observation_details2(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getobservationdetails2"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OBSERVATION_DETAILS_2,
            ACCESS_MATRIX_HOOT[V2_GET_OBSERVATION_DETAILS_2],
            payload={"dataset": job["dataset"], "runId": job["runId"], "type": "DUPE"},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_data_shapes(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatashapes"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATA_SHAPES,
            ACCESS_MATRIX_HOOT[V2_GET_DATA_SHAPES],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_sql_result(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getsqlresult"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions_post(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SQL_RESULT,
            ACCESS_MATRIX_HOOT[V2_GET_SQL_RESULT],
            payload={"sql": job["query"], "cxn": job["connectionalias"], "limit": 1},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_rule_with_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-rule-with-details"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_WITH_DETAILS,
            ACCESS_MATRIX_HOOT[V2_GET_RULE_WITH_DETAILS],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_shape_with_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-shape-with-details"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_SHAPE_WITH_DETAILS,
            ACCESS_MATRIX_HOOT[V2_GET_SHAPE_WITH_DETAILS],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_pattern_with_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-pattern-with-details"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PATTERN_WITH_DETAILS,
            ACCESS_MATRIX_HOOT[V2_GET_PATTERN_WITH_DETAILS],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Hoot")
    def test_role_access_get_outlier_with_details(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/get-outlier-with-details"""
        job = security_helper.get_pullup_job(api_utils)
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OUTLIER_WITH_DETAILS,
            ACCESS_MATRIX_HOOT[V2_GET_OUTLIER_WITH_DETAILS],
            payload={"dataset": job["dataset"], "runId": job["runId"]},
        )
