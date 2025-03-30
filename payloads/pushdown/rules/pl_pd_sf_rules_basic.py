from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_SF_RULES_BASIC_DATASET = "AUTO_PD_SF_RULES_BASIC"

PD_SF_RULES_BASIC_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_RULES_BASIC_DATASET,
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
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": True,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "dataset": PD_SF_RULES_BASIC_DATASET,
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
        "shape": False,
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
        "sourceQuery": "select * from PUBLIC.CUSTOMERS",
        "backRuns": 0,
        "backRunBin": "DAY",
        "threads": 2,
        "key": ""
    },
    "user": BASE_CREDS["username"]
}
