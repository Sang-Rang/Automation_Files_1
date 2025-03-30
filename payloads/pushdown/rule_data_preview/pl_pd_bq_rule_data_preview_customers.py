from utils.constants import PROD_RUN_ID

PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_DATASET = "AUTO_PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS"

PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
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
        "dataset": PD_BQ_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
        "correlation": False,
        "histogram": False,
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
        "sourceQuery": "select * from PUBLIC.CUSTOMERS",
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
