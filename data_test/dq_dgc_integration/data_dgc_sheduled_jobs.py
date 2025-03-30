import copy
from datetime import datetime, timezone, timedelta

from payloads.dq_dgc_integration.pl_dq_dgc_shcheduled_run import (
    DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
    DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME,
)

# Get current UTC time
now_utc = datetime.now(timezone.utc)
# Add 1 minutes and 0 seconds
new_time = now_utc + timedelta(minutes=1, seconds=00)
# Format the output
formatted_time = new_time.strftime("%H:%M:%S")

SCHEDULE_DATA_PAYLOAD = {
    "agentId": 0,
    "agentUUID": "",
    "dataset": "",
    "scheduledRunTime": formatted_time,
    "runDateFmt": "yyyy-MM-dd",
    "freq": "DAILY",
    "dom": "",
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6,
    "sun": 7,
    "active": 1,
}

SCHEDULE_DATA_PAYLOAD_WITH_BU = copy.deepcopy(SCHEDULE_DATA_PAYLOAD)
SCHEDULE_DATA_PAYLOAD_WITH_BU["dataset"] = DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME

SCHEDULE_DATA_PAYLOAD_NO_BU = copy.deepcopy(SCHEDULE_DATA_PAYLOAD)
SCHEDULE_DATA_PAYLOAD_NO_BU["dataset"] = DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME

DQ_DGC_SCHEDULE_RULE_DEFINITION_WITH_BU = [
    {
        "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
        "ruleNm": "close_is_not_null",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE close is NOT Null",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "close",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True,
    }
]

DQ_DGC_SCHEDULE_RULE_WITH_BU_OUTPUT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
            "runId": "2024-11-22T00:00:00.000+0000",
            "ruleNm": "close_is_not_null",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME}"
            f"_dataset WHERE close is NOT Null ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {"id": 496068, "uuid": "9098e22b-466e-4396-9f74-025f3cc3a7d0"},
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE close is NOT Null",
            "totalCount": 102815,
            "rowsBreaking": 102815,
            "tolerance": 0,
            "ruleStatus": "BREAKING",
        }
    ]
}

DQ_DGC_SCHEDULE_RULE_DEFINITION_NO_BU = [
    {
        "dataset": DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME,
        "ruleNm": "close_is_not_null",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE close is NOT Null",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "close",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True,
    }
]

DQ_DGC_SCHEDULE_RULE_OUTPUT_NO_BU = {
    "data": [
        {
            "dataset": DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "close_is_not_null",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME}_dataset "
            f"WHERE close is NOT Null ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {"id": 434000, "uuid": "14404320-4793-4895-a753-4d41f17c4017"},
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE close is NOT Null",
            "totalCount": 102815,
            "rowsBreaking": 102815,
            "tolerance": 0,
            "ruleStatus": "BREAKING",
        }
    ]
}
