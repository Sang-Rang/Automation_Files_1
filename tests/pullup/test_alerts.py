import copy
from datetime import timedelta, datetime, timezone

import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_alerts import (
    EXPECTED_ALERT_RULES_NOTIFICATION_DATA,
    PULLUP_ALERTS_RULES_EXPECTED_RULE_OUTPUT,
    EXPECTED_DS_ALERT_BUILDER_V2,
    EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA,
    EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA,
    EXPECTED_ROW_COUNT_CONDITION_ALERT,
    EXPECTED_JOB_SCORE_CONDITION_ALERT,
    EXPECTED_RULE_BREAK_ALERT,
)

from endpoints.v3.alert_api import V3_ALERTS
from payloads.pullup.pl_alerts import (
    CONN,
    DS_NAME,
    QUERY,
    PL_NEW_ALERT,
    PL_NEW_ALERT_V2,
    DS_NAME_ALERTS_BUILDER,
    DS_NAME_ALERTS_RULES,
    PULLUP_ALERTS_RULES_RULE_DEFINITIONS,
    PL_NEW_ALERT_RULES_ALERT,
    PL_NEW_ALERT_NOTIFY_MULTI_V2,
    PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2,
    PL_NEW_ALERT_NOTIFY_SINGLE_V2,
    PL_NEW_FAILURE_JOB_ALERT_PAYLOAD,
    PL_NEW_JOB_STATUS_FAILURE_ALERT,
    PL_UPDATED_JOB_STATUS_FAILURE_ALERT,
    PL_NEW_SUCCESS_JOB_ALERT_PAYLOAD,
    PL_NEW_JOB_STATUS_SUCCESS_ALERT,
    PL_UPDATED_JOB_STATUS_SUCCESS_ALERT,
    PL_NEW_GLOBAL_FAILURE_JOB_PAYLOAD,
    PL_CONDITION_ALERTS_JOB_PAYLOAD,
    PL_NEW_CONDITION_ROW_COUNT_ALERT,
    PL_NEW_CONDITION_JOB_SCORE_ALERT,
    PL_NEW_RULE_BREAK_ALERT,
    PL_BREAKING_RULE_FOR_SALES,
    PL_PASSING_RULE_FOR_SALES,
    PL_PU_CONDITION_RULE_FOR_SALES,
)
from payloads.pushdown.alerts.pl_pd_alerts import PL_PD_DEFAULT_CONDITION_RULE_ALERT
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils import validator_alerts
from utils.helper_alerts import AlertsHelper
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

from utils.validator_rules import validate_rules_findings

helper = BaseHelper()
setup_env_helper = SetupEnvHelper()
helper_alerts = AlertsHelper()


@pytest.mark.pullup
class TestAlerts:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_create_update_delete_alert_v2(self, api_utils):
        """Test create, update, and delete an alert for v2 api"""

        # CREATE uses "datasetName" and GET uses "dataset". Otherwise, the GET output matches the PL
        expected_data = PL_NEW_ALERT_V2.copy()
        expected_data["dataset"] = PL_NEW_ALERT_V2["datasetName"]
        del expected_data["datasetName"]  # Delete so not compared during validation

        # Setup job
        ds_defs = helper.get_minimum_job_payload(api_utils, CONN, DS_NAME, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        helper_alerts.delete_all_alerts(api_utils, DS_NAME_ALERTS_BUILDER)
        helper_alerts.check_alert(api_utils, DS_NAME, [], v2_api=True)

        # Create, update, and delete alert
        helper_alerts.create_alert(api_utils, PL_NEW_ALERT_V2, v2_api=True)
        helper_alerts.check_alert(api_utils, DS_NAME, [expected_data], v2_api=True)

        PL_NEW_ALERT_V2["alertCond"] = "score > 2"  # Update data
        expected_data["alertCond"] = PL_NEW_ALERT_V2["alertCond"]  # Update data
        helper_alerts.update_alert_v2(api_utils, PL_NEW_ALERT_V2)
        helper_alerts.check_alert(api_utils, DS_NAME, [expected_data], v2_api=True)

        helper_alerts.delete_alert(api_utils, DS_NAME, PL_NEW_ALERT_V2["alertNm"], v2_api=True)
        helper_alerts.check_alert(api_utils, DS_NAME, [], v2_api=True)

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_create_update_delete_alert_v3(self, api_utils):
        """Test create, update, and delete an alert for v3 api"""

        # Setup job
        ds_defs = helper.get_minimum_job_payload(api_utils, CONN, DS_NAME, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        helper_alerts.delete_all_alerts(api_utils, DS_NAME_ALERTS_BUILDER)
        helper_alerts.check_alert(api_utils, DS_NAME, [], v2_api=False)

        # Create, update, and delete
        helper_alerts.create_alert(api_utils, PL_NEW_ALERT, v2_api=False)
        helper_alerts.check_alert(api_utils, DS_NAME, [PL_NEW_ALERT], v2_api=False)

        # V3 updating alert is an overwrite of existing data using same post
        PL_NEW_ALERT["alertCond"] = "score > 2"  # Update data
        helper_alerts.create_alert(api_utils, PL_NEW_ALERT, v2_api=False)
        helper_alerts.check_alert(api_utils, DS_NAME, [PL_NEW_ALERT], v2_api=False)

        helper_alerts.delete_alert(api_utils, DS_NAME, PL_NEW_ALERT["alertNm"], v2_api=False)
        helper_alerts.check_alert(api_utils, DS_NAME, [], v2_api=False)

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_alert_notifications_builder_v2(self, api_utils):
        """Validate the alert rule builder functionality, minus emails"""
        # Note: If configured, emails will send to #dq_alerts in slack.

        # Setup
        utc_now = datetime.now(
            timezone.utc
        )  # This is the time we expect the notification to be around
        utc_start = utc_now - timedelta(minutes=5)  # 5 minute buffer because it may vary slightly
        utc_end = utc_now + timedelta(minutes=5)
        expected_ds_alert_builder = sorted(EXPECTED_DS_ALERT_BUILDER_V2, key=lambda x: x["alertNm"])

        # Create job if it doesn't already exist.
        ds_defs = helper.get_minimum_job_payload(api_utils, CONN, DS_NAME_ALERTS_BUILDER, QUERY)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        helper_alerts.delete_all_alerts(api_utils, DS_NAME_ALERTS_BUILDER)

        # Create new alerts
        for new_alert in [
            PL_NEW_ALERT_NOTIFY_MULTI_V2,
            PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2,
            PL_NEW_ALERT_NOTIFY_SINGLE_V2,
        ]:
            helper_alerts.create_alert(api_utils, new_alert, v2_api=True)

        # Run the job to trigger the alerts to send
        # Past bugs caused the job to fail, so this is important to validate.
        job_response = helper.setup_dataset(api_utils, ds_defs)
        assert_that(job_response["status"], "Job failed to run after adding alerts").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils, DS_NAME_ALERTS_BUILDER, ds_defs["runId"]
        )
        helper_alerts.validate_alert_notification(
            notifications_today, expected_ds_alert_builder, utc_start, utc_now, utc_end
        )

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_alert_notifications_rules(self, api_utils):
        """Validate the notification functionality from failed rules, minus emails"""
        # Note: If configured, emails will send to #dq_alerts in slack.

        run_date = "2023-08-29"
        run_date_full = f"{run_date}T00:00:00.000+0000"

        # Setup
        utc_now = datetime.now(
            timezone.utc
        )  # This is the time we expect the notification to be around
        utc_start = utc_now - timedelta(minutes=5)  # 5 minute buffer because it may vary slightly
        utc_end = utc_now + timedelta(minutes=5)
        helper_alerts.delete_all_alerts(api_utils, DS_NAME_ALERTS_BUILDER)

        # Create job if it doesn't already exist and add rules
        ds_defs = helper.get_minimum_job_payload(
            api_utils, CONN, DS_NAME_ALERTS_RULES, QUERY, run_date
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, ds_defs)
        helper.set_rules_on_dataset(
            api_utils, DS_NAME_ALERTS_RULES, PULLUP_ALERTS_RULES_RULE_DEFINITIONS
        )

        # The user can create an alert from the rules tab on a dataset's alert page.
        # This action calls v2 upsert in react
        helper_alerts.update_alert_v2(api_utils, PL_NEW_ALERT_RULES_ALERT)

        # Run the job to trigger the alerts to send
        # Past bugs caused the job to fail, so this is important to validate.
        job_response = helper.setup_dataset(api_utils, ds_defs)
        assert_that(job_response["status"], "Job failed to run after adding alerts").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils, DS_NAME_ALERTS_RULES, ds_defs["runId"]
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_ALERT_RULES_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

        validate_rules_findings(
            api_utils, DS_NAME_ALERTS_RULES, run_date_full, PULLUP_ALERTS_RULES_EXPECTED_RULE_OUTPUT
        )

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_alert_user_defined_pu_job_status_failure_alert(self, api_utils):
        # Validate the user defined notification functionality from failed job runs, minus emails
        # Note: If configured, emails will send to #dq_alerts in slack.
        utc_now = datetime.now(
            timezone.utc
        )  # This is the time we expect the notification to be around
        utc_start = utc_now - timedelta(minutes=5)  # 5 minute buffer because it may vary slightly
        utc_end = utc_now + timedelta(minutes=5)
        payload = PL_NEW_FAILURE_JOB_ALERT_PAYLOAD

        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, payload)
        helper_alerts.delete_all_alerts(api_utils, payload["dataset"])
        alert = PL_NEW_JOB_STATUS_FAILURE_ALERT
        helper_alerts.create_alert(api_utils, alert, v2_api=False)

        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(job_response["status"], "Job succeeded instead of failing").is_equal_to(
            "FAILED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )
        alert = PL_UPDATED_JOB_STATUS_FAILURE_ALERT
        helper_alerts.create_alert(api_utils, alert, v2_api=False)
        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(
            job_response["status"], "Job incorrectly succeeded instead of failing"
        ).is_equal_to("FAILED")

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_alert_user_defined_pu_job_status_success_alert(self, api_utils):
        # Validate the user defined notification functionality from failed job runs, minus emails
        # Note: If configured, emails will send to #dq_alerts in slack.
        utc_now = datetime.now(
            timezone.utc
        )  # This is the time we expect the notification to be around
        utc_start = utc_now - timedelta(minutes=5)  # 5 minute buffer because it may vary slightly
        utc_end = utc_now + timedelta(minutes=5)
        payload = PL_NEW_SUCCESS_JOB_ALERT_PAYLOAD
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, payload)
        helper_alerts.delete_all_alerts(api_utils, payload["dataset"])
        alert = PL_NEW_JOB_STATUS_SUCCESS_ALERT
        helper_alerts.create_alert(api_utils, alert, v2_api=False)

        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(job_response["status"], "Job failed to run after adding alerts").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

        alert = PL_UPDATED_JOB_STATUS_SUCCESS_ALERT
        helper_alerts.create_alert(api_utils, alert, v2_api=False)

        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(job_response["status"], "Job failed to run after updating alerts").is_equal_to(
            "FINISHED"
        )

        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

        helper_alerts.delete_all_alerts(api_utils, payload["dataset"])
        job_response = helper.setup_dataset(api_utils, payload)
        assert_that(job_response["status"], "Job failed to run after deleting alerts").is_equal_to(
            "FINISHED"
        )

        notifications = helper_alerts.get_alert_notifications(
            api_utils, payload["dataset"], payload["runId"]
        )

        assert_that(
            len(notifications),
            f"Alert notification was not deleted."
            f"Expected 0 but got {len(notifications)} instead",
        ).is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_global_pu_job_failure_alert(self, api_utils):
        # This test makes sure a global alert notification is recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack.

        utc_now = datetime.now(
            timezone.utc
        )  # This is the time we expect the notification to be around
        utc_start = utc_now - timedelta(minutes=5)  # 5 minute buffer because it may vary slightly
        utc_end = utc_now + timedelta(minutes=5)
        payload = PL_NEW_GLOBAL_FAILURE_JOB_PAYLOAD
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
            [EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA],
            utc_start,
            utc_now,
            utc_end,
        )

        ds_alerts = api_utils.get(V3_ALERTS + "/" + payload["dataset"])

        assert_that(
            len(ds_alerts), f"Expected no alerts on the job. But found {len(ds_alerts)}"
        ).is_equal_to(0)

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_pu_condition_row_count_alert(self, api_utils):
        timestamps = helper_alerts.date_time_now()
        payload = PL_CONDITION_ALERTS_JOB_PAYLOAD
        payload["dataset"] = "AUTO_PU_CONDITION_ALERT_ROW_COUNT"
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, payload)
        helper_alerts.delete_all_alerts(api_utils, payload["dataset"])
        helper_alerts.create_alert(api_utils, PL_NEW_CONDITION_ROW_COUNT_ALERT)
        helper.setup_dataset(api_utils, payload)
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_ROW_COUNT_CONDITION_ALERT],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_pu_condition_job_score_alert(self, api_utils):
        timestamps = helper_alerts.date_time_now()
        payload = PL_CONDITION_ALERTS_JOB_PAYLOAD
        payload["dataset"] = "AUTO_PU_CONDITION_ALERT_JOB_SCORE"
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, payload)
        helper_alerts.delete_all_alerts(api_utils, payload["dataset"])
        helper_alerts.create_alert(api_utils, PL_NEW_CONDITION_JOB_SCORE_ALERT)
        helper.setup_dataset(api_utils, payload)
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )

        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_JOB_SCORE_CONDITION_ALERT],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_pu_rule_break_alert(self, api_utils):
        timestamps = helper_alerts.date_time_now()
        ds_name = "AUTO_PU_RULE_BREAK_ALERT_JOB"
        payload = helper.get_pu_job_payload_sales(ds_name)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, payload)
        helper_alerts.delete_all_alerts(api_utils, ds_name)
        helper.set_rules_on_dataset(api_utils, ds_name, PL_BREAKING_RULE_FOR_SALES)
        alert_payload = copy.deepcopy(PL_NEW_RULE_BREAK_ALERT)
        alert_payload["dataset"] = ds_name
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.setup_dataset(api_utils, payload)
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )
        alert_notification_timestamp = notifications_today[0]["updtTs"]
        helper_alerts.validate_alert_notification(
            notifications_today,
            [EXPECTED_RULE_BREAK_ALERT],
            timestamps[0],
            timestamps[1],
            timestamps[2],
        )
        helper.update_rules_on_dataset(api_utils, ds_name, PL_PASSING_RULE_FOR_SALES)
        helper.setup_dataset(api_utils, payload)
        notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
            api_utils,
            payload["dataset"],
            payload["runId"],
        )
        assert_that(
            alert_notification_timestamp, "Alert notification is triggered incorrectly"
        ).is_not_equal_to(notifications_today[0]["updtTs"])

    @allure.feature("Pullup")
    @allure.story("Alerts")
    def test_pullup_rule_condition_alert(self, api_utils):
        timestamps = helper_alerts.date_time_now()
        ds_name = "AUTO_PULLUP_CONDITION_ALERT_JOB_" + timestamps[1].strftime(
            "%d%m%Y%H%M%S"
        )
        job_payload = helper_alerts.get_pu_job_payload_for_alerts(ds_name)
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, job_payload)
        helper_alerts.delete_all_alerts(api_utils, ds_name)
        simple_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            ds_name,
            PL_PU_CONDITION_RULE_FOR_SALES,
            "SIMPLE"
        )
        helper.set_rules_on_dataset(api_utils, ds_name, [simple_rule_payload])
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
            alert_payload
        )
        freeform_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            ds_name,
            PL_PU_CONDITION_RULE_FOR_SALES,
            "FREEFORM"
        )
        helper.set_rules_on_dataset(api_utils, ds_name, [freeform_rule_payload])
        alert_condition = freeform_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.setup_dataset(api_utils, job_payload)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
            timestamps,
            alert_payload
        )
        native_rule_payload = helper_alerts.set_rule_name_and_condition_for_sales(
            ds_name,
            PL_PU_CONDITION_RULE_FOR_SALES,
            "NATIVE"
        )
        helper.set_rules_on_dataset(api_utils, ds_name, [native_rule_payload])
        alert_condition = native_rule_payload["ruleNm"]
        alert_payload["alertCond"] = f"{alert_condition}>0"
        helper_alerts.create_alert(api_utils, alert_payload)
        helper.setup_dataset(api_utils, job_payload)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            job_payload["dataset"],
            job_payload["runId"],
            timestamps,
            alert_payload
        )
        helper.delete_dataset_if_exists(api_utils, job_payload["dataset"])
