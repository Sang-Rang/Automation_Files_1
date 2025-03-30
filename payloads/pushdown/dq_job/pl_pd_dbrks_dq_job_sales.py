from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_DBRKS_DQ_JOB_SALES_DATASET = "AUTO_PD_DBRKS_DQ_JOB_SALES"

PD_DBRKS_DQ_JOB_SALES_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_DQ_JOB_SALES_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": PROD_HOST,
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
        "dataset": PD_DBRKS_DQ_JOB_SALES_DATASET,
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
        "connectionName": "APPROVED_DATABRICKS_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from public.sales",
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
    "user": BASE_CREDS["username"]
}
