from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_DATASET = (
    "AUTO_PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE"
)

PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": PROD_HOST,
    "hootOnly": 'false',
    "logLevel": "INFO",
    "outliers": [
        {
            "on": 'true',
            "categorical": 'false',
            "q1": "0.1",
            "q3": "0.9",
            "exclude": [
                "EXCH",
                "SYMBOL",
                "TRADE_DATE",
                "VOLUME",
                "PART_DATE_STR"
            ],
            "include": [
                "OPEN",
                "HIGH",
                "LOW",
                "CLOSE"
            ],
            "key": [
                "SYMBOL"
            ]
        }
    ],
    "patterns": [],
    "profile": {
        "on": 'true',
        "only": 'false',
        "behaviorScoreOff": 'false',
        "behaviorRowCheck": 'true',
        "behaviorTimeCheck": 'false',
        "behaviorMinValueCheck": 'false',
        "behaviorMaxValueCheck": 'false',
        "behaviorMeanValueCheck": 'true',
        "behaviorNullCheck": 'true',
        "behaviorEmptyCheck": 'true',
        "behaviorUniqueCheck": 'true',
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": 'false',
        "shape": 'false',
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "dataset": PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_DATASET,
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
        "shapeGranular": 'null'
    },
    "alertEmail": 'null',
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "pushdown": {
        "connectionName": "APPROVED_SNOWFLAKE_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.NYSE",
        "backRuns": 0,
        "backRunBin": "DAY",
        "threads": 2,
        "key": ""
    },
    "user": BASE_CREDS["username"]
}
