import allure
import pytest

from data_test.access_security_permissions.v2.data_role_access_usage_stats import (
    ACCESS_MATRIX_USAGE_STATS,
)
from endpoints.v2.controller_usage_stats import (
    V2_GET_DATASET_COUNT,
    V2_GET_ALERT_COUNT,
    V2_GET_RULE_COUNT,
    V2_GET_OWL_CHECK_COUNT,
    V2_GET_EMAIL_COUNT,
    V2_GET_TOTAL_RECORDS,
    V2_GET_TOTAL_OWL_CHECKS,
    V2_GET_OWL_USAGE_LAST_30_DAYS,
    V2_GET_FAILING_DATASET,
    V2_GET_PASSING_DATASET,
    V2_GET_OWL_USAGE_MONTHLY,
    V2_GET_DATASET_USAGE_COUNT,
    V2_GET_BILLING_USAGE,
    V2_GET_TOTAL_ACTIVE_RULES,
    V2_GET_MAX_JOB_CHECK,
    V2_GET_TOTAL_JOB_CHECKS_CURR_MONTH,
    V2_GET_USER_PROFILE_COUNT,
    V2_GET_COLUMNS_COUNT,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_security import SecurityHelper

security_helper = SecurityHelper()
helper = BaseHelper()


class TestRoleAccessUsageStats:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_dataset_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetcount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_DATASET_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_alert_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getalertcount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_ALERT_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_ALERT_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_rule_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getrulecount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_RULE_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_RULE_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_owl_check_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlcheckcount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_CHECK_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_OWL_CHECK_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_email_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getemailcount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_EMAIL_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_EMAIL_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_total_records(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettotalrecords"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TOTAL_RECORDS,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_TOTAL_RECORDS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_total_owl_checks(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettotalowlchecks"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TOTAL_OWL_CHECKS,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_TOTAL_OWL_CHECKS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_owl_usage_last_30_days(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlusagelast30days"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_USAGE_LAST_30_DAYS,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_OWL_USAGE_LAST_30_DAYS],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_failing_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getfailingdataset"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_FAILING_DATASET,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_FAILING_DATASET],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_passing_dataset(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getpassingdataset"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_PASSING_DATASET,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_PASSING_DATASET],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_owl_monthly_usage(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getowlusagemonthly"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_OWL_USAGE_MONTHLY,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_OWL_USAGE_MONTHLY],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    @pytest.mark.skip(reason="Undo after DEV-124635 is fixed")
    def test_role_access_get_dataset_usage_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getdatasetusagecount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_DATASET_USAGE_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_DATASET_USAGE_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_billing_usage(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getbillingusage"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_BILLING_USAGE,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_BILLING_USAGE],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_total_active_rules(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/gettotalactiverules"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TOTAL_ACTIVE_RULES,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_TOTAL_ACTIVE_RULES],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_max_job_check(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getmaxjobcheck"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_MAX_JOB_CHECK,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_MAX_JOB_CHECK],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_total_job_checks_curr_month(
        self, api_utils, get_auth_headers_multi_user
    ):
        """Test Access for all roles against /v2/gettotaljobcheckscurrmonth"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_TOTAL_JOB_CHECKS_CURR_MONTH,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_TOTAL_JOB_CHECKS_CURR_MONTH],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_user_profile_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getuserprofilecount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_USER_PROFILE_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_USER_PROFILE_COUNT],
        )

    @allure.feature("User Role Access")
    @allure.story("User Roles Access - Usage Stats")
    def test_role_access_get_columns_count(self, api_utils, get_auth_headers_multi_user):
        """Test Access for all roles against /v2/getcolumnscount"""
        security_helper.check_role_permissions(
            api_utils,
            get_auth_headers_multi_user,
            V2_GET_COLUMNS_COUNT,
            ACCESS_MATRIX_USAGE_STATS[V2_GET_COLUMNS_COUNT],
        )
