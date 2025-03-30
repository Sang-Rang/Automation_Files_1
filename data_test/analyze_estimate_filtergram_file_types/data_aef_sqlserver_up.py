WHERE_DATE = "1997-12-08"
TABLE_NAME = "dbo.accounts"
COL_NAME = "date"
DATASET = "AUTO_CXN_SQLSERVER_UP_2"
QUERY = f"select TOP 5 * from {TABLE_NAME} where {COL_NAME} = '{WHERE_DATE}'"
CONN_NAME = "APPROVED_SQLSERVER_UP"
ROW_COUNT = 5
FILTERGRAM_COL = "account_id"

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
    "cols": "account_id,date,district_id,frequency",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} = '{WHERE_DATE}'",
    "query": QUERY,
}

EXP_FILTERGRAM = {
    "276.0": 1,
    "2775.0": 1,
    "673.0": 1,
    "3406.0": 1,
    "2796.0": 1,
}
EXP_JOB_EST = {"rowCount": 5, "colCount": 4}
EXP_DAYS_WITH = [
    {
        "rowcount": 3,
        "day_owl_str": "1997-12-07",
        "day": "1997-12-07T00:00:00.000+0000",
    },
    {
        "rowcount": 6,
        "day_owl_str": "1997-12-08",
        "day": "1997-12-08T00:00:00.000+0000",
    },
    {
        "rowcount": 4,
        "day_owl_str": "1997-12-09",
        "day": "1997-12-09T00:00:00.000+0000",
    },
    {
        "rowcount": 5,
        "day_owl_str": "1997-12-10",
        "day": "1997-12-10T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "1997-12-11",
        "day": "1997-12-11T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "1997-12-13",
        "day": "1997-12-13T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "1997-12-15",
        "day": "1997-12-15T00:00:00.000+0000",
    },
    {
        "rowcount": 4,
        "day_owl_str": "1997-12-16",
        "day": "1997-12-16T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "1997-12-17",
        "day": "1997-12-17T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "1997-12-18",
        "day": "1997-12-18T00:00:00.000+0000",
    },
    {
        "rowcount": 4,
        "day_owl_str": "1997-12-19",
        "day": "1997-12-19T00:00:00.000+0000",
    },
    {
        "rowcount": 4,
        "day_owl_str": "1997-12-20",
        "day": "1997-12-20T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "1997-12-21",
        "day": "1997-12-21T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "1997-12-22",
        "day": "1997-12-22T00:00:00.000+0000",
    },
    {
        "rowcount": 3,
        "day_owl_str": "1997-12-23",
        "day": "1997-12-23T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "1997-12-25",
        "day": "1997-12-25T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "1997-12-26",
        "day": "1997-12-26T00:00:00.000+0000",
    },
    {
        "rowcount": 3,
        "day_owl_str": "1997-12-27",
        "day": "1997-12-27T00:00:00.000+0000",
    },
    {
        "rowcount": 3,
        "day_owl_str": "1997-12-28",
        "day": "1997-12-28T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "1997-12-29",
        "day": "1997-12-29T00:00:00.000+0000",
    },
]
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
