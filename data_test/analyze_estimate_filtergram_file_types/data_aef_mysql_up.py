WHERE_DATE = "2022-01-10"
TABLE_NAME = "sys.sys_config"
COL_NAME = "set_time"
DATASET = "AUTO_CXN_MYSQL_UP_2"
QUERY = f"select * from {TABLE_NAME} where {COL_NAME} >= '{WHERE_DATE}' limit 5"
CONN_NAME = "APPROVED_MYSQL_UP"
ROW_COUNT = 5
FILTERGRAM_COL = "value"

PL_DS_GEN = {"dataset": DATASET, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET, "runId": WHERE_DATE, "sense": 3}
PL_FILTERGRAM = {
    "dataset": DATASET,
    "column": FILTERGRAM_COL,
    "runid": f"{WHERE_DATE}T00:00:00.000 0000",
    "datevalue": f"{WHERE_DATE} 00:00:00 00",
    "limit": 500,
}
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
    "cols": "set_by,set_time,value,variable",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} = '{WHERE_DATE}'",
    "query": QUERY,
}

EXP_FILTERGRAM = {"OFF": 2, "65535": 1, "null": 1, "100": 1}
EXP_JOB_EST = {"rowCount": 5, "colCount": 4}
EXP_DAYS_WITH = [{"rowcount": 6, "day_owl_str": "2022-01-10", "day": "2022-01-10"}]
EXP_DS_SCAN = {
    "score": 100,
    "rc": 5,
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
    "loadTimeDiff": 0,
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
