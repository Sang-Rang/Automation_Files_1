# pylint: disable-msg=import-error
from payloads.pullup.pl_alerts import (
    PL_NEW_ALERT_NOTIFY_MULTI,
    PL_NEW_ALERT_NOTIFY_SINGLE,
    DS_NAME_ALERTS_BUILDER,
    PL_NEW_ALERT_NOTIFY_MULTI_SEMI,
    DS_NAME_ALERTS_RULES,
    PL_NEW_ALERT_RULES_ALERT,
    PL_NEW_ALERT_NOTIFY_MULTI_V2,
    PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2,
    PL_NEW_ALERT_NOTIFY_SINGLE_V2,
    DS_NAME_ALERTS_JOB_FAILED_STATUS,
    DS_NAME_ALERTS_JOB_SUCCESS_STATUS,
    PL_NEW_JOB_STATUS_FAILURE_ALERT,
    PL_UPDATED_JOB_STATUS_FAILURE_ALERT,
    PL_UPDATED_JOB_STATUS_SUCCESS_ALERT,
    PL_NEW_JOB_STATUS_SUCCESS_ALERT,
    DS_NAME_ALERTS_GLOBAL_JOB_FAILURE,
    PL_NEW_CONDITION_ROW_COUNT_ALERT,
    PL_NEW_CONDITION_JOB_SCORE_ALERT,
)

EXPECTED_DS_ALERT_BUILDER = [
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_MULTI["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_MULTI["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_MULTI["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_MULTI["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_MULTI["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_MULTI_SEMI["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_MULTI_SEMI["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_MULTI_SEMI["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_MULTI_SEMI["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_MULTI_SEMI["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_SINGLE["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_SINGLE["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_SINGLE["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_SINGLE["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_SINGLE["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
]

EXPECTED_DS_ALERT_BUILDER_V2 = [
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_MULTI_V2["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_MULTI_V2["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_MULTI_V2["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_MULTI_V2["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_MULTI_V2["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_MULTI_SEMI_V2["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
    {
        "dataset": DS_NAME_ALERTS_BUILDER,
        "alertNm": PL_NEW_ALERT_NOTIFY_SINGLE_V2["alertNm"],
        "alertCond": PL_NEW_ALERT_NOTIFY_SINGLE_V2["alertCond"],
        "alertFormat": PL_NEW_ALERT_NOTIFY_SINGLE_V2["alertFormat"],
        "alertFormatValue": PL_NEW_ALERT_NOTIFY_SINGLE_V2["alertFormatValue"],
        "alertMsg": PL_NEW_ALERT_NOTIFY_SINGLE_V2["alertMsg"],
        "alertOutputId": 0,
        "updtTs": "",
    },
]

EXPECTED_ALERT_RULES_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_RULES,
    "alertNm": PL_NEW_ALERT_RULES_ALERT["alertNm"],
    "alertCond": PL_NEW_ALERT_RULES_ALERT["alertCond"],
    "alertFormat": PL_NEW_ALERT_RULES_ALERT["alertFormat"],
    "alertFormatValue": PL_NEW_ALERT_RULES_ALERT["alertFormatValue"],
    "alertMsg": PL_NEW_ALERT_RULES_ALERT["alertMsg"],
    "alertOutputId": 0,
    "updtTs": "",
}

PULLUP_ALERTS_RULES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": DS_NAME_ALERTS_RULES,
            "runId": "2023-08-29T00:00:00.000+0000",
            "ruleNm": "AUTO_BAD_DISTRICT_ID",
            "ruleType": "SQLG",
            "ruleValue": "district_id > 0",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {"id": 431415, "uuid": "9a18febb-012f-4cdd-a222-1b08cdbe50c0"},
            "dimId": None,
            "dimName": None,
            "ruleCondition": "district_id > 0",
            "totalCount": 100,
            "rowsBreaking": 100,
            "tolerance": 0,
            "ruleStatus": "BREAKING",
        }
    ]
}

EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_JOB_FAILED_STATUS,
    "alertNm": PL_NEW_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": PL_NEW_JOB_STATUS_FAILURE_ALERT["alertCond"],
    "alertFormat": PL_NEW_JOB_STATUS_FAILURE_ALERT["alertFormat"],
    "alertFormatValue": PL_NEW_JOB_STATUS_FAILURE_ALERT["alertFormatValue"],
    "alertMsg": PL_NEW_JOB_STATUS_FAILURE_ALERT["alertMsg"],
}

EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_JOB_FAILED_STATUS,
    "alertNm": PL_UPDATED_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": PL_UPDATED_JOB_STATUS_FAILURE_ALERT["alertCond"],
    "alertFormat": PL_UPDATED_JOB_STATUS_FAILURE_ALERT["alertFormat"],
    "alertFormatValue": PL_UPDATED_JOB_STATUS_FAILURE_ALERT["alertFormatValue"],
    "alertMsg": PL_UPDATED_JOB_STATUS_FAILURE_ALERT["alertMsg"],
}

EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_JOB_SUCCESS_STATUS,
    "alertNm": PL_NEW_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": PL_NEW_JOB_STATUS_SUCCESS_ALERT["alertCond"],
    "alertFormat": PL_NEW_JOB_STATUS_SUCCESS_ALERT["alertFormat"],
    "alertFormatValue": PL_NEW_JOB_STATUS_SUCCESS_ALERT["alertFormatValue"],
    "alertMsg": PL_NEW_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
}

EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_JOB_SUCCESS_STATUS,
    "alertNm": PL_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": PL_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertCond"],
    "alertFormat": PL_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertFormat"],
    "alertFormatValue": PL_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertFormatValue"],
    "alertMsg": PL_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
}

EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_NAME_ALERTS_GLOBAL_JOB_FAILURE,
    "alertNm": "AUTO_PU_ALERT_GLOBAL_JOB_FAILURE  (FAILED)",
    "alertCond": "",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "DQ Job did not complete",
}

EXPECTED_ROW_COUNT_CONDITION_ALERT = {
    "dataset": PL_NEW_CONDITION_ROW_COUNT_ALERT["dataset"],
    "alertNm": PL_NEW_CONDITION_ROW_COUNT_ALERT["alertNm"],
    "alertCond": PL_NEW_CONDITION_ROW_COUNT_ALERT["alertCond"],
    "alertFormat": PL_NEW_CONDITION_ROW_COUNT_ALERT["alertFormat"],
    "alertFormatValue": PL_NEW_CONDITION_ROW_COUNT_ALERT["alertFormatValue"],
    "alertMsg": PL_NEW_CONDITION_ROW_COUNT_ALERT["alertMsg"],
    "alertTypes": ["CONDITION"],
}

EXPECTED_JOB_SCORE_CONDITION_ALERT = {
    "dataset": PL_NEW_CONDITION_JOB_SCORE_ALERT["dataset"],
    "alertNm": PL_NEW_CONDITION_JOB_SCORE_ALERT["alertNm"],
    "alertCond": PL_NEW_CONDITION_JOB_SCORE_ALERT["alertCond"],
    "alertFormat": PL_NEW_CONDITION_JOB_SCORE_ALERT["alertFormat"],
    "alertFormatValue": PL_NEW_CONDITION_JOB_SCORE_ALERT["alertFormatValue"],
    "alertMsg": PL_NEW_CONDITION_JOB_SCORE_ALERT["alertMsg"],
    "alertTypes": ["CONDITION"],
}

EXPECTED_RULE_BREAK_ALERT = {
    "dataset": "AUTO_PU_RULE_BREAK_ALERT_JOB",
    "alertNm": "AUTO_RULE_BREAK_ALERT",
    "alertCond": "score>=0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "Rule Break Alert Test!!!",
    "alertTypes": ["BREAKING"],
}

EXPECTED_SIMPLE_RULE_CONDITION_ALERT = {
    "dataset": "AUTO_PU_SIMPLE_RULE_CONDITION_ALERT_JOB",
    "alertNm": "AUTO_CONDITION_SIMPLE_RULE_ALERT",
    "alertCond": "AUTO_SIMPLE_RULE > 0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "Simple Rule Condition Alert Test!!!",
    "alertTypes": ["CONDITION"],
}

EXPECTED_FREEFORM_RULE_CONDITION_ALERT = {
    "dataset": "AUTO_PU_FREEFORM_RULE_CONDITION_ALERT_JOB",
    "alertNm": "AUTO_CONDITION_FREEFORM_RULE_ALERT",
    "alertCond": "AUTO_FREEFORM_RULE > 0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "Freeform Rule Condition Alert Test!!!",
    "alertTypes": ["CONDITION"],
}
