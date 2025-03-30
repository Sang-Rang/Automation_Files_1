WHERE_DATE = "2017-12-21"
TABLE_NAME = "data.nyse"
COL_DATE = "TRADE_DATE"
ROW_COUNT = 50
DATASET_NAME = "AUTO_CXN_CDATA_DBRKS"
QUERY = f"select * from {TABLE_NAME} where {COL_DATE} > '{WHERE_DATE}' limit {ROW_COUNT}"
CONN_NAME = "APPROVED_CDATA_DATABRICKS_UP"

PL_DS_RUN_ID = {"dataset": DATASET_NAME, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET_NAME, "runId": WHERE_DATE, "sense": 3}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_DATE,
    "groupBy": "day",
}
PL_JOB_EST = {
    "drivername": "",
    "aliasname": CONN_NAME,
    "hostname": "",
    "cols": "CLOSE,EXCH,HIGH,LOW,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE,VOLUME",
    "table": TABLE_NAME,
    "where": f"{COL_DATE} > {WHERE_DATE}",
    "query": QUERY,
}
PL_FILTERGRAM = {
    "dataset": DATASET_NAME,
    "column": COL_DATE,
    "runid": f"{WHERE_DATE}T00:00:00.000 0000",
    "datevalue": f"{WHERE_DATE} 00:00:00 00",
    "limit": 500,
}
EXP_FILTERGRAM = {"2018-01-11T00:00:00.000+00:00": 50}
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
EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 9}
EXP_DAYS_WITH = [
    {"rowcount": 3127, "day_owl_str": "2017-12-20", "day": "2017-12-20"},
    {"rowcount": 3125, "day_owl_str": "2017-12-21", "day": "2017-12-21"},
    {"rowcount": 3121, "day_owl_str": "2017-12-22", "day": "2017-12-22"},
    {"rowcount": 3119, "day_owl_str": "2017-12-25", "day": "2017-12-25"},
    {"rowcount": 3119, "day_owl_str": "2017-12-26", "day": "2017-12-26"},
    {"rowcount": 3117, "day_owl_str": "2017-12-27", "day": "2017-12-27"},
    {"rowcount": 3117, "day_owl_str": "2017-12-28", "day": "2017-12-28"},
    {"rowcount": 3116, "day_owl_str": "2017-12-29", "day": "2017-12-29"},
    {"rowcount": 3111, "day_owl_str": "2018-01-01", "day": "2018-01-01"},
    {"rowcount": 3113, "day_owl_str": "2018-01-02", "day": "2018-01-02"},
    {"rowcount": 3111, "day_owl_str": "2018-01-03", "day": "2018-01-03"},
    {"rowcount": 3111, "day_owl_str": "2018-01-04", "day": "2018-01-04"},
    {"rowcount": 3111, "day_owl_str": "2018-01-05", "day": "2018-01-05"},
    {"rowcount": 3106, "day_owl_str": "2018-01-08", "day": "2018-01-08"},
    {"rowcount": 3105, "day_owl_str": "2018-01-09", "day": "2018-01-09"},
    {"rowcount": 3107, "day_owl_str": "2018-01-10", "day": "2018-01-10"},
    {"rowcount": 3104, "day_owl_str": "2018-01-11", "day": "2018-01-11"},
    {"rowcount": 3100, "day_owl_str": "2018-01-12", "day": "2018-01-12"},
    {"rowcount": 3087, "day_owl_str": "2018-01-15", "day": "2018-01-15"},
    {"rowcount": 3088, "day_owl_str": "2018-01-16", "day": "2018-01-16"},
]
