PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET = "AUTO_PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE"

PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD = {
    "runId": "2018-01-12",
    "dataset": PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/rc202308?currentSchema=validation",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [
        {
            "on": True,
            "categorical": False,
            "q1": "0.01",
            "q3": "0.99",
            "exclude": [
                "EXCH",
                "SYMBOL",
                "TRADE_DATE",
                "OPEN",
                "HIGH",
                "LOW",
                "CLOSE",
                "PART_DATE_STR"
            ],
            "include": [
                "VOLUME"
            ],
            "dateColumn": "TRADE_DATE",
            "timeBin": "DAY",
            "lookback": 5
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
        "dataset": PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET,
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
        "sourceQuery": "select * from PUBLIC.NYSE where \"TRADE_DATE\" = '${rd}'",
        "backRuns": 5,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "user": ""
}
