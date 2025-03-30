import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_remote_files_alerts import (
    EXPECTED_REMOTE_FILE_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA,
    EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_NEW_ALERT_NOTIFICATION_DATA,
    EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_NEW_ALERT_NOTIFICATION_DATA,
)
from endpoints.v3.alert_api import V3_ALERTS
from payloads.pullup.pl_remotefile_alerts import (
    PL_NEW_REMOTE_JOB_STATUS_FAILURE_ALERT,
    PL_UPDATED_REMOTE_JOB_STATUS_FAILURE_ALERT,
    PL_NEW_REMOTE_JOB_STATUS_SUCCESS_ALERT,
    PL_UPDATED_REMOTE_JOB_STATUS_SUCCESS_ALERT,
)
from payloads.pushdown.alerts.pl_pd_alerts import (
    PL_PD_CONDITION_RULES_FOR_SALES,
    PL_PD_DEFAULT_CONDITION_RULE_ALERT,
)
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator_alerts
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.helper_alerts import AlertsHelper

helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pullup
class TestRFAlerts:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Remote")
    @allure.story("Alerts")
    def test_global_remote_file_job_failure_alert(self, api_utils):
        # This test makes sure a global alert notification is recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack.

        timestamps = helper_alerts.date_time_now()
        job_name = "AUTO_GLOBAL_REMOTE_JOB_FAILURE"
        file_name = "Sales_Data.csv"
        job_query = "selected vks from dataset"
        payload = helper_alerts.get_remote_file_job_payload_for_alerts(
            job_name, job_query, file_name
        )
        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        assert_that(
            len(notifications_today),
            f"Expected only one global alert. But found {len(notifications_today)}",
        ).is_equal_to(1)

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_REMOTE_FILE_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

        ds_alerts = api_utils.get(V3_ALERTS + "/" + payload["dataset"])

        assert_that(
            len(ds_alerts), f"Expected no alerts on the job. But found {len(ds_alerts)}"
        ).is_equal_to(0)

    @allure.feature("Remote")
    @allure.story("Alerts")
    def test_user_defined_remote_file_job_failure_alert(self, api_utils):
        # This test makes sure a user defined alert notification is recorded in
        # the alerts' notification.
        # This test doesn't validate the receiving of email in slack.
        timestamps = helper_alerts.date_time_now()
        job_name = "AUTO_USER_DEFINED_REMOTE_FILE_JOB_FAILURE"
        file_name = "Sales_Data.csv"
        job_query = "selected vks from dataset"
        job_payload = helper_alerts.get_remote_file_job_payload_for_alerts(
            job_name, job_query, file_name
        )
        job_response = helper.setup_dataset(api_utils, job_payload)

        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )
        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        alert_payload = PL_NEW_REMOTE_JOB_STATUS_FAILURE_ALERT
        alert_payload["dataset"] = job_name
        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)

        job_response = helper.setup_dataset(api_utils, job_payload)
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
            [EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_NEW_ALERT_NOTIFICATION_DATA],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )
        alert_payload = PL_UPDATED_REMOTE_JOB_STATUS_FAILURE_ALERT
        alert_payload["dataset"] = job_name
        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)
        job_response = helper.setup_dataset(api_utils, job_payload)
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
            [EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

    @allure.feature("Remote")
    @allure.story("Alerts")
    def test_user_defined_remote_file_job_success_alert(self, api_utils):
        # This test makes sure a user defined alert notification is recorded in
        # the alerts' notification.
        # This test doesn't validate the receiving of email in slack.
        timestamps = helper_alerts.date_time_now()
        job_name = "AUTO_USER_DEFINED_REMOTE_FILE_JOB_SUCCESS"
        file_name = "Sales_Data.csv"
        job_query = "select * from dataset"
        job_payload = helper_alerts.get_remote_file_job_payload_for_alerts(
            job_name, job_query, file_name
        )
        job_response = helper.setup_dataset(api_utils, job_payload)

        assert_that(job_response["status"], "Job failed instead of succeeding").is_equal_to(
            "FINISHED"
        )
        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        alert_payload = PL_NEW_REMOTE_JOB_STATUS_SUCCESS_ALERT
        alert_payload["dataset"] = job_name
        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)

        job_response = helper.setup_dataset(api_utils, job_payload)
        assert_that(job_response["status"], "Job failed instead of succeeding").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_NEW_ALERT_NOTIFICATION_DATA],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )
        alert_payload = PL_UPDATED_REMOTE_JOB_STATUS_SUCCESS_ALERT
        alert_payload["dataset"] = job_name
        helper_alerts.create_alert(api_utils, alert_payload, v2_api=False)
        job_response = helper.setup_dataset(api_utils, job_payload)
        assert_that(job_response["status"], "Job failed instead of succeeding").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

    @allure.feature("Remote")
    @allure.story("Alerts")
    def test_remote_file_job_condition_alerts(self, api_utils):
        # This test makes sure a user defined alert notification is recorded in
        # the alerts' notification.
        # This test doesn't validate the receiving of email in slack.
        timestamps = helper_alerts.date_time_now()
        job_name = "AUTO_REMOTE_FILE_JOB_CONDITION_ALERTS_" + timestamps[1].strftime("%d%m%Y%H%M%S")
        file_name = "Sales_Data.csv"
        job_query = "select * from dataset"
        job_payload = helper_alerts.get_remote_file_job_payload_for_alerts(
            job_name, job_query, file_name
        )
        helper.setup_dataset(api_utils, job_payload)
        helper_alerts.delete_all_alerts(api_utils, job_payload["dataset"])
        simple_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            job_payload["dataset"], PL_PD_CONDITION_RULES_FOR_SALES, "SIMPLE"
        )
        simple_rule_payload["ruleValue"] = "Cost_Description = 'General Electrical'"
        helper.set_rules_on_dataset(api_utils, job_payload["dataset"], [simple_rule_payload])
        alert_payload = PL_PD_DEFAULT_CONDITION_RULE_ALERT
        alert_payload["dataset"] = job_payload["dataset"]
        alert_payload["alertNm"] = job_payload["dataset"]
        alert_condition = simple_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.setup_dataset(api_utils, job_payload)
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
        freeform_rule_payload["ruleValue"] = f"SELECT * FROM @{job_name} where First_Name = 'Ryan'"
        helper.set_rules_on_dataset(api_utils, job_payload["dataset"], [freeform_rule_payload])
        alert_condition = simple_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.setup_dataset(api_utils, job_payload)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
            timestamps,
            alert_payload,
        )
        helper.delete_dataset_if_exists(api_utils, job_payload["dataset"])
