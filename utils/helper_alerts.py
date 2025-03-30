import copy
from datetime import timedelta, datetime, timezone
import pytest

from assertpy import assert_that

from endpoints.v2.controller_alert import (
    V2_CREATE_ALERT,
    V2_GET_ALERTS,
    V2_REMOVE_ALERT,
    V2_UPSERT_ALERT,
)
from endpoints.v3.alert_api import V3_ALERTS
from payloads.pullup.pl_alerts import PL_JOB_PAYLOAD_DEFAULT

from payloads.pullup.pl_remotefile_alerts import PL_NEW_REMOTE_JOB_DEFAULT, FILEPATH
from payloads.pushdown.alerts.pl_pd_alerts import PL_PD_NEW_JOB_DEFAULT
from utils.validator import validate_array_dict
from utils.api_utils import APIUtils


class AlertsHelper:
    """Helper methods for Alerts"""

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def delete_alert(api_utils, ds_name, alert_nm, v2_api=False):
        """Delete an existing alert and validate response"""
        if v2_api:
            resp_delete = api_utils.post(
                V2_REMOVE_ALERT, params={"dataset": ds_name, "alertNm": alert_nm}, return_json=False
            )
        else:
            resp_delete = api_utils.delete(
                V3_ALERTS + "/" + ds_name + "/" + alert_nm, return_json=False
            )

        assert_that(resp_delete.status_code, f"Delete alert {alert_nm} failed").is_equal_to(200)
        return resp_delete

    def delete_all_alerts(self, api_utils, ds_name):
        # Delete any existing alerts on this job
        found_alerts_setup = api_utils.get(V3_ALERTS + "/" + ds_name)
        for found_alert in found_alerts_setup:
            self.delete_alert(api_utils, ds_name, found_alert["alertNm"], v2_api=False)

    @staticmethod
    def validate_alert_notification(
        found_notifications, expected_notifications, utc_start, utc_now, utc_end
    ):
        # Validate the data within an alert notification, including the timestamp within limits
        for i, expected_notification in enumerate(expected_notifications):
            for key, value in expected_notification.items():
                if key == "alertOutputId":
                    assert_that(
                        found_notifications[i][key], "Invalid Alert Output ID"
                    ).is_greater_than(0)
                elif key == "updtTs":
                    # When a notification is generated, this updates to that time with seconds
                    # Confirm it's updated within a few minutes of the test execution
                    # This allows for variation of job runtime and
                    # speeds of notification generation
                    check_time = utc_start <= utc_now <= utc_end
                    assert_that(
                        check_time,
                        "Updated Timestamp data wasn't within expected range. "
                        f"Start: {utc_start}, Expected: {utc_now}, End: {utc_end}",
                    ).is_true()
                else:
                    assert_that(
                        value, f"Unexpected notification data for item {i} in {key}"
                    ).is_equal_to(found_notifications[i][key])

    @staticmethod
    def validate_multiple_alert_notifications(
        found_notifications, expected_notifications, utc_start, utc_now, utc_end
    ):
        """
        Validates multiple alert notifications by comparing
        corresponding elements in found and expected lists.
        """
        assert_that(
            len(found_notifications),
            f"Expected {len(expected_notifications)} notifications, "
            f"but found {len(found_notifications)}",
        ).is_equal_to(len(expected_notifications))

        for i, (found, expected) in enumerate(zip(found_notifications, expected_notifications)):
            for key, value in expected.items():
                if key == "alertOutputId":
                    assert_that(
                        found[key], f"Invalid Alert Output ID at index {i}"
                    ).is_greater_than(0)

                elif key == "updtTs":
                    check_time = utc_start <= utc_now <= utc_end
                    assert_that(
                        check_time,
                        f"Updated Timestamp data wasn't within expected range for index {i}. "
                        f"Start: {utc_start}, Expected: {utc_now}, End: {utc_end}",
                    ).is_true()

                else:
                    assert_that(
                        found[key], f"Unexpected notification data for item {i} in {key}"
                    ).is_equal_to(value)

    @staticmethod
    def get_and_sort_alert_notifications_today(api_utils, ds_name, run_id):
        """Fetch existing notifications, sort, and filter to the given run date"""
        ds_notifications = api_utils.get(V3_ALERTS + "/" + ds_name + "/notifications")
        assert_that(len(ds_notifications), "No alert notifications found").is_greater_than(0)
        ds_notifications_sorted = sorted(ds_notifications, key=lambda x: x["alertNm"])
        ds_notifications_sorted_today = []

        # Only look at ones with today's run id.
        # Each day creates 1 notification record, even if multiple notifications are generated.
        for i, notification in enumerate(ds_notifications_sorted):
            if run_id in notification["runId"]:
                ds_notifications_sorted_today.append(ds_notifications_sorted[i])
        return ds_notifications_sorted_today

    @staticmethod
    def create_alert(api_utils, payload, v2_api=False):
        """Create a new alert and validate response"""
        if v2_api:
            resp_new_alert = api_utils.post(V2_CREATE_ALERT, params=payload, return_json=False)
        else:
            resp_new_alert = api_utils.post(V3_ALERTS, json=payload, return_json=False)

        assert_that(
            resp_new_alert.status_code,
            f"Alert creation failed. "
            f"Expected status code: 200, but got {resp_new_alert.status_code} instead.",
        ).is_equal_to(200)

        return resp_new_alert

    @staticmethod
    def check_alert(api_utils, ds_name, expected_data_array, v2_api=False):
        """Grab and validate the alert data"""
        if v2_api:
            found_alerts = api_utils.get(V2_GET_ALERTS, params={"dataset": ds_name})
        else:
            found_alerts = api_utils.get(V3_ALERTS + "/" + ds_name)

        # if expected data is not zero alerts, check contents
        if expected_data_array == {}:
            assert_that(len(found_alerts), "Expected no data").is_equal_to(0)
        else:
            validate_array_dict(expected_data_array, found_alerts, "Alert creation failed")

        return found_alerts

    @staticmethod
    def update_alert_v2(api_utils, payload):
        """Update a v2 alert and validate response"""
        # To update v3, create alert overrides the existing alert
        resp_update_alert = api_utils.post(V2_UPSERT_ALERT, params=payload, return_json=False)

        assert_that(
            resp_update_alert.status_code, f"New alert creation failed for {payload}"
        ).is_equal_to(200)

        return resp_update_alert

    @staticmethod
    def get_alert_notifications(api_utils, ds_name, run_id):
        """Fetch & return existing notifications for a given dataset"""
        ds_notifications = api_utils.get(V3_ALERTS + "/" + ds_name + "/notifications")
        ds_notifications_today = []
        if len(ds_notifications) > 0:
            for i, notification in enumerate(ds_notifications):
                if run_id in notification["runId"]:
                    ds_notifications_today.append(ds_notifications[i])

        return ds_notifications_today

    @staticmethod
    def date_time_now():
        utc_now = datetime.now(timezone.utc)
        utc_start = utc_now - timedelta(minutes=5)
        utc_end = utc_now + timedelta(minutes=5)
        return utc_start, utc_now, utc_end

    @staticmethod
    def get_remote_file_job_payload_for_alerts(dataset_name, job_query, file_name):
        """Returns the job payload for remote file job
        based on the connection, dataset name and job query."""
        job_payload = copy.deepcopy(PL_NEW_REMOTE_JOB_DEFAULT)
        filepath = f"{FILEPATH}/{file_name}"
        job_payload["dataset"] = dataset_name
        job_payload["load"]["dataset"] = dataset_name
        job_payload["load"]["filePath"] = filepath
        job_payload["load"]["fileQuery"] = job_query
        job_payload["pushdown"]["dataset"] = dataset_name
        job_payload["profile"]["dataset"] = dataset_name
        job_payload["colMatch"]["dataset"] = dataset_name
        job_payload["spark"]["dataset"] = dataset_name
        job_payload["env"]["dataset"] = dataset_name
        return job_payload

    @staticmethod
    def get_pd_job_payload_for_alerts(connection, dataset_name, include_columns, source_query):
        """Returns the job payload for PD job
        based on the connection, dataset name, table columns and source query."""
        job_payload = copy.deepcopy(PL_PD_NEW_JOB_DEFAULT)
        job_payload["dataset"] = dataset_name
        job_payload["env"]["dataset"] = dataset_name
        job_payload["profile"]["include"] = include_columns
        job_payload["pushdown"]["connectionName"] = connection
        job_payload["pushdown"]["dataset"] = dataset_name
        job_payload["pushdown"]["sourceQuery"] = source_query
        return job_payload

    @staticmethod
    def set_rule_name_and_condition_for_sales(dataset_name, rule_payload, rule_type):
        rule_payload["dataset"] = dataset_name
        rule_payload["ruleNm"] = dataset_name
        if rule_type == "SIMPLE":
            rule_payload["ruleValue"] = "SALES>5000"
            rule_payload["ruleType"] = "SQLG"
        elif rule_type == "FREEFORM":
            rule_payload["ruleValue"] = f"Select * From @{dataset_name} where SALES>5000"
            rule_payload["ruleType"] = "SQLF"
        elif rule_type == "NATIVE":
            rule_payload["ruleValue"] = "select NAME, SALES from PUBLIC.SALES where SALES > 1000"
            rule_payload["ruleType"] = "NATIVE"
        return rule_payload

    @staticmethod
    def get_pu_job_payload_for_alerts(dataset_name):
        """Returns the job payload for a PU job by setting the given DS name"""
        job_payload = copy.deepcopy(PL_JOB_PAYLOAD_DEFAULT)
        job_payload["dataset"] = dataset_name
        job_payload["load"]["dataset"] = dataset_name
        job_payload["pushdown"]["dataset"] = dataset_name
        job_payload["profile"]["dataset"] = dataset_name
        job_payload["colMatch"]["dataset"] = dataset_name
        job_payload["spark"]["dataset"] = dataset_name
        job_payload["env"]["dataset"] = dataset_name
        return job_payload

    @staticmethod
    def set_unique_name_for_alerts(dataset_name, timestamps, alert_payload):
        alert_payload["alertNm"] = dataset_name + timestamps[1].strftime("%d%m%Y%H%M%S")
        return alert_payload

    def create_alerts_with_unique_name(self, api_utils, dataset_name, alerts_payload, timestamps):
        self.delete_all_alerts(api_utils, dataset_name)
        for alert in alerts_payload:
            alert["dataset"] = dataset_name
            alert["alertNm"] += timestamps[1].strftime("%d%m%Y%H%M%S")
            self.create_alert(api_utils, alert)
