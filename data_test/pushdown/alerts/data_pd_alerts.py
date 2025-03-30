import pytest

from payloads.pushdown.alerts.pl_pd_alerts import (
    DS_PD_ALERTS_FAILURE_JOB,
    PL_PD_NEW_JOB_STATUS_FAILURE_ALERT,
    PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT,
    PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT,
    PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT,
)

EXPECTED_GLOBAL_JOB_FAILURE_ALERT_NOTIFICATION_DATA = {
    "dataset": "AUTO_PD_GLOBAL_ALERT_JOB_FAILURE",
    "alertCond": "Failed Job",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": 'Failure: ERROR: syntax error at or near "from" in context '
    '"(selected vks from", at line 1\n  '
    "Position: 29",
}

EXPECTED_JOB_FAILURE_STATUS_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_PD_ALERTS_FAILURE_JOB,
    "alertNm": PL_PD_NEW_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": PL_PD_NEW_JOB_STATUS_FAILURE_ALERT["alertCond"],
    "alertFormat": PL_PD_NEW_JOB_STATUS_FAILURE_ALERT["alertFormat"],
    "alertFormatValue": PL_PD_NEW_JOB_STATUS_FAILURE_ALERT["alertFormatValue"],
    "alertMsg": PL_PD_NEW_JOB_STATUS_FAILURE_ALERT["alertMsg"],
}

EXPECTED_JOB_FAILURE_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": DS_PD_ALERTS_FAILURE_JOB,
    "alertNm": PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT["alertNm"],
    "alertCond": PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT["alertCond"],
    "alertFormat": PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT["alertFormat"],
    "alertFormatValue": PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT["alertFormatValue"],
    "alertMsg": PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT["alertMsg"],
}

EXPECTED_JOB_SUCCESS_STATUS_ALERT_NOTIFICATION_DATA = {
    "dataset": "",
    "alertNm": PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT["alertCond"],
    "alertFormat": PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT["alertFormat"],
    "alertFormatValue": PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT["alertFormatValue"],
    "alertMsg": PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
}

EXPECTED_JOB_SUCCESS_STATUS_UPDATED_ALERT_NOTIFICATION_DATA = {
    "dataset": "",
    "alertNm": PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertNm"],
    "alertCond": PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertCond"],
    "alertFormat": PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertFormat"],
    "alertFormatValue": PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertFormatValue"],
    "alertMsg": PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertMsg"],
}

PARAMS_PD_JOB_SUCCESS_ALERT_TESTS = [
    pytest.param(
        {
            "connection": "Snowflake",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_SNOWFLAKE",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SNOWFLAKE_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.snowflake,
    ),
    pytest.param(
        {
            "connection": "Bigquery",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_BIGQUERY",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_BIGQUERY_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.bigquery,
    ),
    pytest.param(
        {
            "connection": "Trino",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_TRINO",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_TRINO_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.trino,
    ),
    pytest.param(
        {
            "connection": "Saphana",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_SAPHANA",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SAPHANA_PUSHDOWN",
            "source_query": "select * from TEST.SALES",
        },
        marks=pytest.mark.saphana,
    ),
    pytest.param(
        {
            "connection": "Redshift",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_REDSHIFT",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_REDSHIFT_PUSHDOWN",
            "source_query": "select * from public.sales2",
        },
        marks=pytest.mark.redshift,
    ),
    pytest.param(
        {
            "connection": "Databricks",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_DATABRICKS",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_DATABRICKS_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.databricks,
    ),
    pytest.param(
        {
            "connection": "Athena",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_ATHENA",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_ATHENA_PUSHDOWN",
            "source_query": "select * from default.sales",
        },
        marks=pytest.mark.athena,
    ),
    pytest.param(
        {
            "connection": "SQLServer",
            "dataset": "AUTO_PD_ALERT_JOB_SUCCESS_SQLSERVER",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_SQLSERVER_PUSHDOWN",
            "source_query": "select * from dbo.sales",
        },
        marks=pytest.mark.sqlserver,
    ),
]

EXPECTED_PD_JOB_CONDITION_ALERTS = [
    {
        "dataset": "AUTO_PD_FREEFORM_RULE_CONDITION_ALERT_JOB",
        "alertNm": "AUTO_CONDITION_FREEFORM_RULE_ALERT",
        "alertCond": "AUTO_FREEFORM_RULE > 0",
        "alertFormat": "EMAIL",
        "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
        "alertMsg": "Freeform Rule Condition Alert Test!!!",
        "alertTypes": ["CONDITION"],
    },
    {
        "dataset": "AUTO_PD_SIMPLE_RULE_CONDITION_ALERT_JOB",
        "alertNm": "AUTO_CONDITION_SIMPLE_RULE_ALERT",
        "alertCond": "AUTO_SIMPLE_RULE > 0",
        "alertFormat": "EMAIL",
        "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
        "alertMsg": "Simple Rule Condition Alert Test!!!",
        "alertTypes": ["CONDITION"],
    },
]

EXPECTED_PD_JOB_CONDITION_SIMPLE_RULE_ALERT = {
    "dataset": "AUTO_PD_FREEFORM_RULE_CONDITION_ALERT_JOB",
    "alertNm": "AUTO_CONDITION_FREEFORM_RULE_ALERT",
    "alertCond": "AUTO_FREEFORM_RULE > 0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "Freeform Rule Condition Alert Test!!!",
    "alertTypes": ["CONDITION"],
}
