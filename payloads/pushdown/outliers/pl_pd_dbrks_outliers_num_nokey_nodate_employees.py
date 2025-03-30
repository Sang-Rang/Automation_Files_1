from utils.constants import PROD_RUN_ID

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES"
)

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_PAYLOAD = {
  "runId": PROD_RUN_ID,
  "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
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
    "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
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
    "sourceQuery": "select * from public.employees",
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
  "user": ""
}
