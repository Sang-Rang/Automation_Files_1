from utils.constants import PROD_RUN_ID

PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION = "APPROVED_DATABRICKS_PUSHDOWN"
PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS"
)


PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/rc202309?currentSchema=validation",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [
        {
            "on": True,
            "categorical": False,
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
        "dataset": PD_DBRKS_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
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
        "connectionName": "APPROVED_DATABRICKS_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from public.nyse",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": True,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "linkId": [
        "EXCH",
        "SYMBOL",
        "TRADE_DATE"
    ],
    "user": "gaberosenadmin"
}
