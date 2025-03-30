from utils.constants import PROD_RUN_ID

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION = (
    "APPROVED_DATABRICKS_PUSHDOWN"
)
PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS"
)

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
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
        "connectionName": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from public.us_airports",
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
        "GLOBAL_ID"
    ],
    "user": "gaberosenadmin"
}
