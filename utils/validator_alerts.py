from assertpy import assert_that

from utils.helper_alerts import AlertsHelper

helper_alerts = AlertsHelper()


def validate_alert_notification_data(api_utils, dataset_name, run_id, timestamps, alert_data):
    """
    Retrieves and validates single alert notification.
    """

    notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
        api_utils,
        dataset_name,
        run_id,
    )
    assert_that(
        len(notifications_today),
        f"Expected 1 alert notification, but found {len(notifications_today)}",
    ).is_equal_to(1)
    helper_alerts.validate_alert_notification(
        notifications_today,
        [alert_data],
        timestamps[0],
        timestamps[1],
        timestamps[2],
    )


def validate_multiple_alerts_notification_data(
    api_utils, dataset_name, run_id, timestamps, alert_data
):
    """
    Retrieves and validates multiple alert notifications.
    """
    notifications_today = helper_alerts.get_and_sort_alert_notifications_today(
        api_utils,
        dataset_name,
        run_id,
    )
    assert_that(
        len(notifications_today),
        f"Expected multiple alert notification, but found {len(notifications_today)}",
    ).is_equal_to(len(alert_data))

    helper_alerts.validate_multiple_alert_notifications(
        notifications_today,
        alert_data,
        timestamps[0],
        timestamps[1],
        timestamps[2],
    )
