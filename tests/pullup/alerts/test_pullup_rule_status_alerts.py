import allure
import pytest

from payloads.pullup.alerts.pl_pullup_rule_status_alerts import (
    PU_RULE_STATUS_ALERTS_JOB_PAYLOAD,
    PU_RULE_STATUS_ALERTS_DATASET,
    PU_SINGLE_PASSING_RULE_PAYLOAD,
    PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
    PU_SINGLE_BREAKING_RULE_PAYLOAD,
    PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
    PU_SINGLE_EXCEPTION_RULE_PAYLOAD,
    PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
    PU_DEFAULT_MULTIPLE_RULE_STATUS_ALERT_PAYLOAD,
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
class TestPullupRuleAlerts:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Pullup - Alerts")
    def test_pullup_single_rule_passing_status_alert(self, api_utils):
        # This test makes sure a rule status alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pullup_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_PASSING_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    def test_pullup_single_rule_breaking_status_alert(self, api_utils):
        # This test makes sure a rule status alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_BREAKING_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    def test_pullup_single_rule_exception_status_alert(self, api_utils):
        # This test makes sure a rule status alert notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_EXCEPTION_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    def test_pullup_multiple_rule_multiple_status_single_alert(self, api_utils):
        # This test makes sure rule status alerts' notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_SINGLE_PASSING_RULE_PAYLOAD,
                PU_SINGLE_BREAKING_RULE_PAYLOAD,
                PU_SINGLE_EXCEPTION_RULE_PAYLOAD,
            ],
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [PU_DEFAULT_MULTIPLE_RULE_STATUS_ALERT_PAYLOAD],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_MULTIPLE_RULE_STATUS_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    @pytest.mark.skip(reason="Undo after DEV-125688 is fixed.")
    def test_pullup_single_passing_rule_multiple_status_single_alert(self, api_utils):
        # This test makes sure rule status alerts' notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_PASSING_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
            ],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    @pytest.mark.skip(reason="Undo after DEV-125688 is fixed.")
    def test_pullup_single_breaking_rule_multiple_status_single_alert(self, api_utils):
        # This test makes sure rule status alerts' notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_BREAKING_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
            ],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    @pytest.mark.skip(reason="Undo after DEV-125688 is fixed.")
    def test_pullup_single_exception_rule_multiple_status_single_alert(self, api_utils):
        # This test makes sure rule status alerts' notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils, PU_RULE_STATUS_ALERTS_DATASET, [PU_SINGLE_EXCEPTION_RULE_PAYLOAD]
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
            ],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_alert_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Alerts")
    @pytest.mark.snowflake
    def test_pullup_multiple_rules_multiple_status_multiple_alerts(self, api_utils):
        # This test makes sure rule status alerts' notification is triggered
        # and recorded in the alerts' notification.
        # This test doesn't validate the receiving of email in slack or inbox.
        timestamps = helper_alerts.date_time_now()
        helper.run_pushdown_job_if_dataset_does_not_exist(
            api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD
        )
        helper.set_rules_on_dataset(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_SINGLE_BREAKING_RULE_PAYLOAD,
                PU_SINGLE_EXCEPTION_RULE_PAYLOAD,
                PU_SINGLE_PASSING_RULE_PAYLOAD,
            ],
        )
        helper_alerts.create_alerts_with_unique_name(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            [
                PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
            ],
            timestamps,
        )
        helper.setup_dataset(api_utils, PU_RULE_STATUS_ALERTS_JOB_PAYLOAD)
        validator_alerts.validate_multiple_alerts_notification_data(
            api_utils,
            PU_RULE_STATUS_ALERTS_DATASET,
            PU_RULE_STATUS_ALERTS_JOB_PAYLOAD["runId"],
            timestamps,
            [
                PU_DEFAULT_RULE_STATUS_SINGLE_BREAKING_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_EXCEPTION_ALERT_PAYLOAD,
                PU_DEFAULT_RULE_STATUS_SINGLE_PASSING_ALERT_PAYLOAD,
            ],
        )
