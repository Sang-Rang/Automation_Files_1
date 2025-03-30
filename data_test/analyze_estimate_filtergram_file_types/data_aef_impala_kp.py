WHERE_DATE = "2017-12-25"
TABLE_NAME = "default.nyse"
COL_DATE = "trade_date"
ROW_COUNT = 50
DATASET_NAME = "AUTO_CXN_IMPALA_KP"
QUERY = f"select * from {TABLE_NAME} where {COL_DATE} > '{WHERE_DATE}' limit {ROW_COUNT}"
CONN_NAME = "APPROVED_IMPALA_KP"

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
    "cols": "close,day,exch,high,low,month,open,part_date_str,symbol,trade_date,volume,year",
    "table": TABLE_NAME,
    "query": QUERY,
    "where": f"{COL_DATE} > {WHERE_DATE}",
}
PL_FILTERGRAM = {
    "dataset": DATASET_NAME,
    "column": COL_DATE,
    "runid": f"{WHERE_DATE}",
    "limit": 500,
}
EXP_FILTERGRAM = {"2017-12-26 00:00:00.000000000": 50}
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
    "rc": 50,
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
EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 12}
EXP_DAYS_WITH = [
    {"rowcount": 3127, "day_owl_str": "2017-12-20", "day": "2017-12-20T00:00:00.000+0000"},
    {"rowcount": 3125, "day_owl_str": "2017-12-21", "day": "2017-12-21T00:00:00.000+0000"},
    {"rowcount": 3121, "day_owl_str": "2017-12-22", "day": "2017-12-22T00:00:00.000+0000"},
    {"rowcount": 3119, "day_owl_str": "2017-12-25", "day": "2017-12-25T00:00:00.000+0000"},
    {"rowcount": 3119, "day_owl_str": "2017-12-26", "day": "2017-12-26T00:00:00.000+0000"},
    {"rowcount": 3117, "day_owl_str": "2017-12-27", "day": "2017-12-27T00:00:00.000+0000"},
    {"rowcount": 3117, "day_owl_str": "2017-12-28", "day": "2017-12-28T00:00:00.000+0000"},
    {"rowcount": 3116, "day_owl_str": "2017-12-29", "day": "2017-12-29T00:00:00.000+0000"},
    {"rowcount": 3111, "day_owl_str": "2018-01-01", "day": "2018-01-01T00:00:00.000+0000"},
    {"rowcount": 3113, "day_owl_str": "2018-01-02", "day": "2018-01-02T00:00:00.000+0000"},
    {"rowcount": 3111, "day_owl_str": "2018-01-03", "day": "2018-01-03T00:00:00.000+0000"},
    {"rowcount": 3111, "day_owl_str": "2018-01-04", "day": "2018-01-04T00:00:00.000+0000"},
    {"rowcount": 3111, "day_owl_str": "2018-01-05", "day": "2018-01-05T00:00:00.000+0000"},
    {"rowcount": 3106, "day_owl_str": "2018-01-08", "day": "2018-01-08T00:00:00.000+0000"},
    {"rowcount": 3105, "day_owl_str": "2018-01-09", "day": "2018-01-09T00:00:00.000+0000"},
    {"rowcount": 3105, "day_owl_str": "2018-01-10", "day": "2018-01-10T00:00:00.000+0000"},
    {"rowcount": 3104, "day_owl_str": "2018-01-11", "day": "2018-01-11T00:00:00.000+0000"},
    {"rowcount": 3100, "day_owl_str": "2018-01-12", "day": "2018-01-12T00:00:00.000+0000"},
    {"rowcount": 3087, "day_owl_str": "2018-01-15", "day": "2018-01-15T00:00:00.000+0000"},
    {"rowcount": 3088, "day_owl_str": "2018-01-16", "day": "2018-01-16T00:00:00.000+0000"},
]
