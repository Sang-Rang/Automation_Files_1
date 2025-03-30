from payloads.pullup.pl_remotefile_alerts import (
    PL_UPDATED_REMOTE_JOB_STATUS_FAILURE_ALERT,
    PL_NEW_REMOTE_JOB_STATUS_FAILURE_ALERT, PL_NEW_REMOTE_JOB_STATUS_SUCCESS_ALERT,
    PL_UPDATED_REMOTE_JOB_STATUS_SUCCESS_ALERT,
)

EXPECTED_REMOTE_FILE_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_GLOBAL_REMOTE_JOB_FAILURE",
    "alertNm": "AUTO_GLOBAL_REMOTE_JOB_FAILURE  (FAILED)",
    "alertCond": "",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "DQ Job did not complete",
}

EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_USER_DEFINED_REMOTE_FILE_JOB_FAILURE",
    "alertNm": PL_UPDATED_REMOTE_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": "N/A",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": PL_UPDATED_REMOTE_JOB_STATUS_FAILURE_ALERT["alertMsg"],
    "alertTypes": ["JOB_FAILURE"],
}

EXPECTED_REMOTE_FILE_JOB_FAILURE_STATUS_NEW_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_USER_DEFINED_REMOTE_FILE_JOB_FAILURE",
    "alertNm": PL_NEW_REMOTE_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": "N/A",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": PL_NEW_REMOTE_JOB_STATUS_FAILURE_ALERT["alertMsg"],
    "alertTypes": ["JOB_FAILURE"],
}

EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_NEW_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_USER_DEFINED_REMOTE_FILE_JOB_SUCCESS",
    "alertNm": PL_NEW_REMOTE_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": "score>=0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": PL_NEW_REMOTE_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
    "alertTypes": ["JOB_COMPLETE"],
}

EXPECTED_REMOTE_FILE_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_USER_DEFINED_REMOTE_FILE_JOB_SUCCESS",
    "alertNm": PL_UPDATED_REMOTE_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": "score>=0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": PL_UPDATED_REMOTE_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
    "alertTypes": ["JOB_COMPLETE"],
}
