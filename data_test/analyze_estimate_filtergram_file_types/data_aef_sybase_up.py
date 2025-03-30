from utils.constants import PROD_RUN_ID

TABLE_NAME = "mydb.dbo.sales"
COL_NAME = "trdate"
DATASET_NAME = "AUTO_CXN_SYBASE_UP"
ROW_COUNT = 10
QUERY = f"select * from {TABLE_NAME}"
CONN_NAME = "APPROVED_SYBASE_UP"

PL_DS_RUN_ID = {"dataset": DATASET_NAME, "runId": PROD_RUN_ID}
PL_DS_STATS = {"dataset": DATASET_NAME, "runId": PROD_RUN_ID, "sense": 3}
PL_FILTERGRAM = {"dataset": DATASET_NAME, "runid": PROD_RUN_ID, "column": COL_NAME, "limit": 500}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}
PL_JOB_EST = {
    "drivername": "",
    "aliasname": CONN_NAME,
    "hostname": "",
    "cols": "name,sales,trdate",
    "table": TABLE_NAME,
    "query": QUERY,
}

EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 3}
EXP_FILTERGRAM = {
  "2022-05-01": 2,
  "2022-05-02": 2,
  "2022-05-04": 2,
  "2022-05-03": 2,
  "2022-05-05": 2
}
EXP_DAYS_WITH = [
  {
    "rowcount": 2,
    "day_owl_str": "2022-05-01",
    "day": "2022-05-01T00:00:00.000+0000"
  },
  {
    "rowcount": 2,
    "day_owl_str": "2022-05-02",
    "day": "2022-05-02T00:00:00.000+0000"
  },
  {
    "rowcount": 2,
    "day_owl_str": "2022-05-03",
    "day": "2022-05-03T00:00:00.000+0000"
  },
  {
    "rowcount": 2,
    "day_owl_str": "2022-05-04",
    "day": "2022-05-04T00:00:00.000+0000"
  },
  {
    "rowcount": 2,
    "day_owl_str": "2022-05-05",
    "day": "2022-05-05T00:00:00.000+0000"
  }
]
EXP_DS_SCAN = {
    "score": 100,
    "rc": ROW_COUNT,
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
