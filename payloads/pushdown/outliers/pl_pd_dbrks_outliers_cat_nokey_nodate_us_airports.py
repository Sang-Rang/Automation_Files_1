from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS"
)

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
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
                "OBJECT_ID",
                "GLOBAL_ID",
                "FAA_IDENTIFIER",
                "NAME",
                "LATITUDE",
                "LONGITUDE",
                "AIRPORT_GEOM",
                "ELEVATION",
                "ICAO_ID",
                "SERVICE_CITY",
                "STATE_ABBREVIATION",
                "COUNTRY",
                "OPER_STATUS",
                "AIRPORT_USE",
                "IAP_EXISTS",
                "DOD_HIFLIP",
                "FAR_91",
                "FAR_93",
                "MIL_CODE",
                "AIRSPACE_ANALYSIS",
                "US_HIGH",
                "US_LOW",
                "AK_HIGH",
                "AK_LOW",
                "US_AREA",
                "PACIFIC"
            ],
            "include": [
                "AIRPORT_TYPE"
            ]
        }
    ],
    "patterns": [],
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
        "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
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
        "sourceQuery": "select * from public.us_airports",
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
