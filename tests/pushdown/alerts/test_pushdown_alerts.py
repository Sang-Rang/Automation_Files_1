from datetime import timedelta, datetime, timezone

import allure
import pytest

from assertpy import assert_that
from data_test.pushdown.alerts.data_pd_alerts import (
    EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    PARAMS_PD_JOB_SUCCESS_ALERT_TESTS,
)

from endpoints.v3.alert_api import V3_ALERTS
from payloads.pushdown.alerts.pl_pd_alerts import (
    PL_PD_NEW_JOB_FAILURE,
    PL_PD_NEW_JOB_STATUS_FAILURE_ALERT,
    PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT,
    PL_PD_NEW_JOB_GLOBAL_FAILURE,
    PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT,
    PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT,
    PL_PD_CONDITION_RULES_FOR_SALES,
    PL_PD_DEFAULT_CONDITION_RULE_ALERT,
    PARAMS_PD_CONDITION_ALERT_TESTS,
)

from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator_alerts
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_alerts import AlertsHelper

helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pushdown
class TestPDAlerts:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.redshift
    def test_global_pd_job_failure_alert(self, api_utils):
        # This test makes sure a global alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.

        utc_now = datetime.now(timezone.utc)
        utc_start = utc_now - timedelta(minutes=5)
        utc_end = utc_now + timedelta(minutes=5)
        job_payload = PL_PD_NEW_JOB_GLOBAL_FAILURE
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils, job_payload["dataset"], job_payload["runId"]
        )

        assert_that(
            len(notifications_today),
            f"Expected only one global alert. But found {len(notifications_today)}",
        ).is_equal_to(1)

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

        ds_alerts = api_utils.get(V3_ALERTS + "/" + job_payload["dataset"])

        assert_that(
            len(ds_alerts), f"Expected no alerts on the job. But found {len(ds_alerts)}"
        ).is_equal_to(0)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.redshift
    def test_alert_user_defined_pd_job_status_failure_alert(self, api_utils):
        # This test makes sure a user defined alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.

        utc_now = datetime.now(timezone.utc)
        utc_start = utc_now - timedelta(minutes=5)
        utc_end = utc_now + timedelta(minutes=5)
        job_payload = PL_PD_NEW_JOB_FAILURE
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )

        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        alert_payload = PL_PD_NEW_JOB_STATUS_FAILURE_ALERT

        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)

        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )
        alert = PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT
        helper_alerts.create_alert(api_utils, alert, v2_api=False)
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(
            job_response["status"], "Job incorrectly succeeded instead of failing"
        ).is_equal_to("FAILED")
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.parametrize(
        "test_data",
        PARAMS_PD_JOB_SUCCESS_ALERT_TESTS,
        ids=lambda val: f"{val['connection']}",
    )
    def test_alert_user_defined_pd_job_status_success_alert(self, api_utils, test_data):
        # This test makes sure a user defined alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        job_payload = helper.get_pd_job_payload_sales(
            test_data["connection_name"],
            test_data["dataset"],
            test_data["include_columns"],
            test_data["source_query"],
        )
        helper.run_pushdown_job_if_dataset_does_not_exist(api_utils, job_payload)
        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        alert_payload = PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT
        alert_payload["dataset"] = job_payload["dataset"]
        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job failed instead of passing").is_equal_to("FINISHED")

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        expected_alert_data = EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA
        expected_alert_data["dataset"] = job_payload["dataset"]

        helper_alerts.validate_alert_notification(
            notifications_today,
            [expected_alert_data],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

        updated_alert_payload = PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT
        updated_alert_payload["dataset"] = job_payload["dataset"]
        helper_alerts.create_alert(api_utils, updated_alert_payload, v2_api=False)
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job failed instead of passing").is_equal_to("FINISHED")

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        expected_updated_alert_data = EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA
        expected_updated_alert_data["dataset"] = job_payload["dataset"]

        helper_alerts.validate_alert_notification(
            notifications_today,
            [expected_updated_alert_data],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        job_response = helper.run_pushdown_job(api_utils, job_payload)
        assert_that(job_response["status"], "Job failed to run after deleting alerts").is_equal_to(
            "FINISHED"
        )

        notifications = helper_alerts.get_alert_notifications(
            api_utils, job_payload["dataset"], job_payload["runId"]
        )

        assert_that(
            len(notifications),
            f"Alert notification was not deleted."
            f"Expected 0 but got {len(notifications)} instead",
        ).is_equal_to(0)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.parametrize(
        "job_test_data",
        PARAMS_PD_CONDITION_ALERT_TESTS,
        ids=lambda val: f"{val['connection']}",
    )
    def test_pd_condition_alerts(self, api_utils, job_test_data):
        # This test makes sure a user defined condition alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        job_payload = helper.get_pd_job_payload_sales(
            job_test_data["connection_name"],
            job_test_data["dataset"],
            job_test_data["include_columns"],
            job_test_data["source_query"],
        )
        job_payload["dataset"] = "AUTO_PD_CONDITION_ALERT_JOB_QA_" + timestamps[1].strftime(
            "%d%m%Y%H%M%S"
        )
        helper.run_pushdown_job_v3(api_utils, job_payload)
        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        simple_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            job_payload["dataset"], PL_PD_CONDITION_RULES_FOR_SALES, "SIMPLE"
        )
        alert_payload = PL_PD_DEFAULT_CONDITION_RULE_ALERT
        alert_payload["dataset"] = job_payload["dataset"]
        alert_payload["alertNm"] = job_payload["dataset"]
        alert_condition = simple_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper.set_rules_on_dataset(api_utils, job_payload["dataset"], [simple_rule_payload])
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.run_pushdown_job_v3(api_utils, job_payload)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
            timestamps,
            alert_payload,
        )
        freeform_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            job_payload["dataset"], PL_PD_CONDITION_RULES_FOR_SALES, "FREEFORM"
        )
        if job_test_data["connection"] == "SQLServer":
            freeform_rule_payload["ruleValue"] = "Select * From dbo.sales where SALES>5000"
        helper.set_rules_on_dataset(api_utils, job_payload["dataset"], [freeform_rule_payload])
        alert_payload = PL_PD_DEFAULT_CONDITION_RULE_ALERT
        alert_payload["dataset"] = job_payload["dataset"]
        alert_payload["alertNm"] = job_payload["dataset"]
        alert_condition = freeform_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.run_pushdown_job_v3(api_utils, job_payload)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
            timestamps,
            alert_payload,
        )
        helper.delete_dataset_if_exists(api_utils, job_payload["dataset"])
