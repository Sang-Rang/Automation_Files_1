# pylint: disable-msg=import-error
from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

TABLE_NAME = "public.sales"
WHERE_DATE = "2022-05-04"
COL_NAME = "TRDATE"
DATASET = "AUTO_CXN_DBRKS_PD"
QUERY = f"select * from {TABLE_NAME} where \"{COL_NAME}\" > '{WHERE_DATE}' limit 50"
CONN_NAME = "APPROVED_DATABRICKS_PUSHDOWN"
ROW_COUNT = 10

PL_DS_RUN_ID = {"dataset": DATASET, "runId": PROD_RUN_ID}
PL_DS_STATS = {"dataset": DATASET, "runId": PROD_RUN_ID, "sense": 3}
PL_FILTERGRAM = {
    "dataset": DATASET,
    "column": COL_NAME,
    "runid": f"{PROD_RUN_ID}T00:00:00.000 0000",
    "datevalue": f"{PROD_RUN_ID} 00:00:00 00",
    "limit": 500,
}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}

EXP_FILTERGRAM = {f"{WHERE_DATE}": ROW_COUNT}
EXP_DAYS_WITH = [
    {"rowcount": 2, "day_owl_str": "2022-05-01", "day": "2022-05-01"},
    {"rowcount": 2, "day_owl_str": "2022-05-02", "day": "2022-05-02"},
    {"rowcount": 2, "day_owl_str": "2022-05-03", "day": "2022-05-03"},
    {"rowcount": 2, "day_owl_str": "2022-05-04", "day": "2022-05-04"},
    {"rowcount": 2, "day_owl_str": "2022-05-05", "day": "2022-05-05"},
]
EXP_DS_SCAN = {
    "score": 100,
    "rc": 10,
    "passFail": 1,
    "peak": 1,
    "scoreDupe": 0,
    "scoreSource": 0,
    "scoreDatashape": 0,
    "scoreSchema": 0,
    "scoreRecord": 0,
    "scoreOutlier": 0,
    "scorePattern": 0,
    "scoreRule": 0,
    "scoreBehavior": 0,
    "passFailAvg": 0,
    "physicalName": None,
    "userLabel": None,
    "rcSrc": None,
    "passFailRc": 1,
    "pushDownOptions": None,
    "daysWithoutData": 0,
    "runsWithoutData": 0,
    "daysSinceLastRun": 0,
}
EXP_DS_SCORE = {
    "failScore": 75,
    "datashapeScore": 1,
    "dupeScore": 1,
    "schemaScore": 1,
    "recordScore": 1,
    "outlierScore": 1,
    "fpgScore": 1,
    "validateSrcScore": 1,
    "behaviorScore": 1,
    "rulesTotalScore": 0,
    "validateSrcTotalScore": 0,
    "dupeTotalScore": 0,
    "fpgTotalScore": 0,
    "behaviorTotalScore": 0,
    "outlierTotalScore": 0,
    "schemaTotalScore": 0,
    "recordTotalScore": 0,
    "datashapeTotalScore": 0,
    "datashapeMaxPerCol": 20,
    "datashapeMaxColSize": 12,
    "datashapeSensitivity": 0,
    "behaviorScoreOff": False,
    "lbAbsRowCnt": None,
    "ubAbsRowCnt": None,
    "lbZscoreRowCnt": None,
    "ubZscoreRowCnt": None,
}

DSDEFS = {
    "runId": PROD_RUN_ID,
    "dataset": DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {"id": -1},
    "host": PROD_HOST,
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": True,
        "behaviorMaxValueCheck": True,
        "behaviorMeanValueCheck": True,
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
        "dataset": DATASET,
        "pushDown": ["count", "distinct", "mean", "minmax", "quality"],
        "profilePushDown": ["count", "distinct", "mean", "minmax", "quality"],
        "shapeGranular": None,
    },
    "alertEmail": "",
    "agentId": {"id": 0, "uuid": ""},
    "pushdown": {
        "connectionName": CONN_NAME,
        "maxConnections": 10,
        "sourceQuery": QUERY,
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False,
    },
    "user": BASE_CREDS["username"],
}
