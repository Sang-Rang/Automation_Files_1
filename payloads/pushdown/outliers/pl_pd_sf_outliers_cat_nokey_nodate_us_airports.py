from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET = (
    "AUTO_PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS"
)

PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
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
        "categorical": 'true',
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
      "shapeSensitivity": 0,
      "shapeMaxPerCol": 20,
      "shapeMaxColSize": 12,
      "dataset": PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
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
      "shape": 'null',
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
      "sourceQuery": "select * from PUBLIC.US_AIRPORTS",
      "backRuns": 0,
      "backRunBin": "DAY",
      "threads": 2,
      "key": ""
    },
    "user": BASE_CREDS["username"]
    }
