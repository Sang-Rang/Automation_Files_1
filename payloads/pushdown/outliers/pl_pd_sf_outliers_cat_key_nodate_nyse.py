from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET = "AUTO_PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE"

PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": PROD_HOST,
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [
        {
            "on": True,
            "categorical": True,
            "q1": 0.15,
            "q3": 0.85,
            "exclude": [
                "EXCH",
                "TRADE_DATE",
                "OPEN",
                "HIGH",
                "LOW",
                "CLOSE",
                "VOLUME",
                "PART_DATE_STR"
            ],
            "include": [
                "SYMBOL"
            ],
            "key": [
                "EXCH"
            ]
        }
    ],
    "patterns": [],
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
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
        "dataset": PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
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
        "connectionName": "APPROVED_SNOWFLAKE_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.NYSE",
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
