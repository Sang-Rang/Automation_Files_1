PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION = "APPROVED_DATABRICKS_PUSHDOWN"
PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS"
)

PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": "2023-01-10",
    "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
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
            "categorical": True,
            "q1": 0.15,
            "q3": 0.85,
            "exclude": [
                "TRADE_DATE",
                "END_DATE",
                "TRADE_ID",
                "TRADE_VALUE",
                "NOTIONAL",
                "EXPOSURE",
                "DELTA_DAYS_COMPUTED",
                "VARIANCE_BUCKET_COMPUTED",
                "TEST_REASON"
            ],
            "include": [
                "NON_ZERO_COMPUTED"
            ],
            "lookback": 5,
            "timeBin": "DAY",
            "dateColumn": "TRADE_DATE"
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
        "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
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
        "connectionName": PD_DBRKS_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from public.ms_trade where TRADE_DATE = '${rd}'",
        "backRuns": 5,
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
        "TRADE_DATE",
        "TRADE_ID"
    ],
    "user": "gaberosenadmin"
}
