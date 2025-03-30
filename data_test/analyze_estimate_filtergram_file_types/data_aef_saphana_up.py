WHERE_DATE_FORMAT = "20120411"
WHERE_DATE = "2012-04-11"
TABLE_NAME = "SFLIGHT.SBOOK"
COL_DATE = "FLDATE"
ROW_COUNT = 50
DATASET_NAME = "AUTO_CXN_SAPHANA"
QUERY = f"select * from {TABLE_NAME} where {COL_DATE} = '{WHERE_DATE_FORMAT}' limit {ROW_COUNT}"
CONN_NAME = "APPROVED_SAPHANA_UP"

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
    "cols": "AGENCYNUM,BOOKID,CANCELLED,CARRID,CLASS,CONNID,COUNTER,CUSTOMID,CUSTTYPE,FLDATE,"
    "FORCURAM,FORCURKEY,INVOICE,LOCCURAM,LOCCURKEY,LUGGWEIGHT,MANDT,ORDER_DATE,PASSBIRTH,"
    "PASSFORM,PASSNAME,RESERVED,SMOKER,WUNIT",
    "table": TABLE_NAME,
    "query": QUERY,
    "where": f"{COL_DATE} = {WHERE_DATE_FORMAT}",
}
PL_FILTERGRAM = {
    "dataset": DATASET_NAME,
    "column": COL_DATE,
    "runid": f"{WHERE_DATE}",
    "limit": 500,
}
EXP_FILTERGRAM = {"20120411": 50}
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
EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 24}
EXP_DAYS_WITH = [
    {"rowcount": 242, "day_owl_str": "20120406", "day": "20120406"},
    {"rowcount": 166, "day_owl_str": "20120407", "day": "20120407"},
    {"rowcount": 263, "day_owl_str": "20120409", "day": "20120409"},
    {"rowcount": 89, "day_owl_str": "20120410", "day": "20120410"},
    {"rowcount": 282, "day_owl_str": "20120411", "day": "20120411"},
    {"rowcount": 203, "day_owl_str": "20120412", "day": "20120412"},
    {"rowcount": 224, "day_owl_str": "20120413", "day": "20120413"},
    {"rowcount": 177, "day_owl_str": "20120414", "day": "20120414"},
    {"rowcount": 245, "day_owl_str": "20120416", "day": "20120416"},
    {"rowcount": 119, "day_owl_str": "20120417", "day": "20120417"},
    {"rowcount": 194, "day_owl_str": "20120418", "day": "20120418"},
    {"rowcount": 98, "day_owl_str": "20120419", "day": "20120419"},
    {"rowcount": 169, "day_owl_str": "20120420", "day": "20120420"},
    {"rowcount": 121, "day_owl_str": "20120421", "day": "20120421"},
    {"rowcount": 188, "day_owl_str": "20120423", "day": "20120423"},
    {"rowcount": 124, "day_owl_str": "20120424", "day": "20120424"},
    {"rowcount": 231, "day_owl_str": "20120425", "day": "20120425"},
    {"rowcount": 57, "day_owl_str": "20120426", "day": "20120426"},
    {"rowcount": 150, "day_owl_str": "20120427", "day": "20120427"},
    {"rowcount": 148, "day_owl_str": "20120428", "day": "20120428"},
]
