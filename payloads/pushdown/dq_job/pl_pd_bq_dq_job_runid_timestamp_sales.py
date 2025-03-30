PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET = "AUTO_PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES"
PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID = "2022-05-02 06:14:00"
PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END = "2022-05-04 12:34:00"

PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_PAYLOAD = {
    "runId": PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID,
    "runIdEnd": PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_RUNID_END,
    "dataset": PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/rc202309?currentSchema=automation",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": False,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": False,
        "behaviorEmptyCheck": False,
        "behaviorUniqueCheck": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shape": False,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "correlation": False,
        "histogram": False,
        "dataset": PD_BQ_DQ_JOB_RUNID_TIMESTAMP_SALES_DATASET,
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
    "pushdown": {
        "connectionName": "APPROVED_BIGQUERY_PUSHDOWN",
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
