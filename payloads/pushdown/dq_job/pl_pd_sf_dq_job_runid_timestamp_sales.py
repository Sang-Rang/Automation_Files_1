PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET = "AUTO_PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES"
PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID = "2022-05-02 06:14:00"
PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END = "2022-05-04 12:34:00"

PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_PAYLOAD = {
    "runId": PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID,
    "runIdEnd": PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END,
    "dataset": PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": True,
        "behaviorMaxValueCheck": True,
        "behaviorMeanValueCheck": True,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shape": False,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "dataset": PD_SF_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET,
        "pushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "profilePushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "shapeGranular": None
    },
    "alertEmail": "",
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "pushdown": {
        "connectionName": "APPROVED_SNOWFLAKE_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.SALES",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "user": "gaberosenadmin"
}
