WHERE_DATE = "2021-06-03"
TABLE_NAME = "public.aclaims_master"
COL_NAME = "CM_DATE_RECEIVED"
DATASET = "AUTO_CXN_POSTGRES_UP"
ROW_COUNT = 100
QUERY = f"select * from {TABLE_NAME} where {COL_NAME} = '{WHERE_DATE}' limit {ROW_COUNT}"
CONN_NAME = "APPROVED_POSTGRES_UP"

PL_DS_GEN = {"dataset": DATASET, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET, "runId": WHERE_DATE, "sense": 3}
PL_FILTERGRAM = {
    "dataset": DATASET,
    "column": COL_NAME,
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
    "cols": "CM_BDOS,CM_CLAIM_STATUS,CM_CLAIMANT_AGE,CM_CLAIMANT_BDATE,CM_CLAIMANT_SEX,"
    "CM_CONVERSION_DATE,CM_DATE_CLAIM_PAID,CM_DATE_RECEIVED,CM_DENIED_REASON1,"
    "CM_DENIED_REASON2,CM_DIAGNOSIS_CODE,CM_DISAB_DAYS,CM_DOC_ORIGIN_DSC,CM_EDOS,"
    "CM_EFF_DATE_FAMILY,CM_END_TREATMN_DTE,CM_FICA_DATE,CM_GROUP_NUMBER,CM_HOSPITAL_DAYS,"
    "CM_LOB,CM_MEDICARE_NUMBER,CM_PENDING_FLAG1,CM_PENDING_FLAG2,CM_PENDING_FLAG3,"
    "CM_PENDING_FLAG4,CM_PROOF_LOSS_DT,CM_RELATIONSHIP,CM_STATE_OF_ISSUE,"
    "CM_STATE_OF_RES,CM_TAX_STATUS",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} = '{WHERE_DATE}'",
    "query": QUERY,
}

EXP_FILTERGRAM = {f"{WHERE_DATE}": ROW_COUNT}
EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 30}
EXP_DAYS_WITH = [
    {"rowcount": 4, "day_owl_str": "2021-05-15", "day": "2021-05-15T00:00:00.000+0000"},
    {"rowcount": 6, "day_owl_str": "2021-05-16", "day": "2021-05-16T00:00:00.000+0000"},
    {"rowcount": 29, "day_owl_str": "2021-05-17", "day": "2021-05-17T00:00:00.000+0000"},
    {"rowcount": 17, "day_owl_str": "2021-05-18", "day": "2021-05-18T00:00:00.000+0000"},
    {"rowcount": 28, "day_owl_str": "2021-05-19", "day": "2021-05-19T00:00:00.000+0000"},
    {"rowcount": 33, "day_owl_str": "2021-05-20", "day": "2021-05-20T00:00:00.000+0000"},
    {"rowcount": 41, "day_owl_str": "2021-05-21", "day": "2021-05-21T00:00:00.000+0000"},
    {"rowcount": 11, "day_owl_str": "2021-05-22", "day": "2021-05-22T00:00:00.000+0000"},
    {"rowcount": 7, "day_owl_str": "2021-05-23", "day": "2021-05-23T00:00:00.000+0000"},
    {"rowcount": 44, "day_owl_str": "2021-05-24", "day": "2021-05-24T00:00:00.000+0000"},
    {"rowcount": 43, "day_owl_str": "2021-05-25", "day": "2021-05-25T00:00:00.000+0000"},
    {"rowcount": 71, "day_owl_str": "2021-05-26", "day": "2021-05-26T00:00:00.000+0000"},
    {"rowcount": 234, "day_owl_str": "2021-05-27", "day": "2021-05-27T00:00:00.000+0000"},
    {"rowcount": 218, "day_owl_str": "2021-05-28", "day": "2021-05-28T00:00:00.000+0000"},
    {"rowcount": 8, "day_owl_str": "2021-05-29", "day": "2021-05-29T00:00:00.000+0000"},
    {"rowcount": 3, "day_owl_str": "2021-05-30", "day": "2021-05-30T00:00:00.000+0000"},
    {"rowcount": 2, "day_owl_str": "2021-05-31", "day": "2021-05-31T00:00:00.000+0000"},
    {"rowcount": 46, "day_owl_str": "2021-06-01", "day": "2021-06-01T00:00:00.000+0000"},
    {"rowcount": 956, "day_owl_str": "2021-06-02", "day": "2021-06-02T00:00:00.000+0000"},
    {"rowcount": 931, "day_owl_str": "2021-06-03", "day": "2021-06-03T00:00:00.000+0000"},
]
EXP_DS_SCAN = {
    "score": 98,
    "rc": 100,
    "passFail": 1,
    "peak": 1,
    "scoreDupe": 0,
    "scoreSource": 0,
    "scoreDatashape": 2,
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
    "datashapeTotalScore": 2,
    "datashapeMaxPerCol": 20,
    "datashapeMaxColSize": 12,
    "datashapeSensitivity": 0,
    "behaviorScoreOff": False,
    "lbAbsRowCnt": None,
    "ubAbsRowCnt": None,
    "lbZscoreRowCnt": None,
    "ubZscoreRowCnt": None,
}
