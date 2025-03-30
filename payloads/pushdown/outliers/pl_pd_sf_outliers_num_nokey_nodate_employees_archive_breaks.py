from utils.constants import PROD_RUN_ID

PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION = "APPROVED_SNOWFLAKE_PUSHDOWN"
PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS"
)

PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
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
            "q1": "0.45",
            "q3": "0.55",
            "exclude": [
                "EMPLOYEE_ID",
                "FIRST_NAME",
                "LAST_NAME",
                "EMAIL",
                "GENDER",
                "CITY",
                "DEPARTMENT",
                "LATITUDE",
                "LONGITUDE",
                "HOME_PHONE",
                "POSTAL_CODE",
                "STATE",
                "STREET_ADDRESS",
                "DATE_OF_HIRE"
            ],
            "include": [
                "TIME_IN_SERVICE_YRS"
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
        "dataset": PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
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
        "connectionName": PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.EMPLOYEES",
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
        "EMPLOYEE_ID",
        "EMAIL"
    ],
    "user": "gaberosenadmin"
}
