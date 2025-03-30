WHERE_DATE = "2021-12-15"
TABLE_NAME = "public.aclaims_master_run"
COL_NAME = "Report_Date"
DATASET = "AUTO_CXN_POSTGRES_PWDMGR"
QUERY = "select * from public.aclaims_master_run where Report_Date = '${rd}' limit 100"
CONN_NAME = "APPROVED_POSTGRES_PWDMGR"
ROW_COUNT = 100
FILTERGRAM_COL = COL_NAME

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
    "cols": "Employee_AddressCity,Employee_AddressState,Employee_AddressStreet,Employee_"
    "AddressZipCode,Employee_ContractPermanent,Employee_Department,Employee_Division,"
    "Employee_Email,Employee_FirstName,Employee_ID,Employee_JobLevel,Employee_JobTitle,"
    "Employee_LastName,Employee_LeaveDate,Employee_Office,Employee_Salary,Employee_SSN,"
    "Employee_StartDate,Employee_Status,Report_Date",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} >= '{WHERE_DATE}'",
    "query": QUERY.replace("${rd}", str(WHERE_DATE)),
}

EXP_FILTERGRAM = {f"{WHERE_DATE}": ROW_COUNT}
EXP_JOB_EST = {"rowCount": ROW_COUNT, "colCount": 20}
EXP_DAYS_WITH = [
    {"rowcount": 989, "day_owl_str": "2021-12-15", "day": "2021-12-15T00:00:00.000+0000"},
    {"rowcount": 990, "day_owl_str": "2021-12-16", "day": "2021-12-16T00:00:00.000+0000"},
    {"rowcount": 994, "day_owl_str": "2021-12-17", "day": "2021-12-17T00:00:00.000+0000"},
    {"rowcount": 994, "day_owl_str": "2021-12-18", "day": "2021-12-18T00:00:00.000+0000"},
    {"rowcount": 994, "day_owl_str": "2021-12-19", "day": "2021-12-19T00:00:00.000+0000"},
    {"rowcount": 996, "day_owl_str": "2021-12-20", "day": "2021-12-20T00:00:00.000+0000"},
    {"rowcount": 997, "day_owl_str": "2021-12-21", "day": "2021-12-21T00:00:00.000+0000"},
    {"rowcount": 998, "day_owl_str": "2021-12-22", "day": "2021-12-22T00:00:00.000+0000"},
    {"rowcount": 999, "day_owl_str": "2021-12-23", "day": "2021-12-23T00:00:00.000+0000"},
    {"rowcount": 999, "day_owl_str": "2021-12-24", "day": "2021-12-24T00:00:00.000+0000"},
    {"rowcount": 999, "day_owl_str": "2021-12-25", "day": "2021-12-25T00:00:00.000+0000"},
    {"rowcount": 999, "day_owl_str": "2021-12-26", "day": "2021-12-26T00:00:00.000+0000"},
    {"rowcount": 1000, "day_owl_str": "2021-12-27", "day": "2021-12-27T00:00:00.000+0000"},
    {"rowcount": 1000, "day_owl_str": "2021-12-28", "day": "2021-12-28T00:00:00.000+0000"},
]
EXP_DS_SCAN = {
    "runId": f"{WHERE_DATE}T00:00:00.000+0000",
    "dataset": DATASET,
    "score": 100,
    "rc": 100,
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
    "dataset": DATASET,
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
