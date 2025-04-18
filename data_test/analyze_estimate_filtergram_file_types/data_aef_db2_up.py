TRADE_DATE = "2017-12-20"
TABLE_NAME = "OWLDB2.NYSE_STOCKS"
COL_NAME = "TRADE_DATE"
DATASET = "AUTO_CONNECTION_DB2"
QUERY = (
    f"select * from {TABLE_NAME} where {COL_NAME} = '{TRADE_DATE} "
    "00:00:00' fetch first 100 rows only"
)
CONN_NAME = "APPROVED_DB2_UP"
ROW_COUNT = 100
FILTERGRAM_COL = "close"

PL_DS_GEN = {"dataset": DATASET, "runId": TRADE_DATE}
PL_DS_STATS = {"dataset": DATASET, "runId": TRADE_DATE, "sense": 3}
PL_FILTERGRAM = {
    "dataset": DATASET,
    "column": FILTERGRAM_COL,
    "runid": f"{TRADE_DATE}T00:00:00.000 0000",
    "datevalue": f"{TRADE_DATE} 00:00:00 00",
    "limit": 500,
}
PL_JOB_EST = {
    "drivername": "",
    "aliasname": CONN_NAME,
    "hostname": "",
    "cols": "CLOSE,EXCH,HIGH,LOW,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE,VOLUME",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} = '{TRADE_DATE}'",
    "query": f"select * from {TABLE_NAME} where {COL_NAME} = '{TRADE_DATE}' "
    f"fetch first {ROW_COUNT} rows only",
}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}

EXP_FILTERGRAM = {
    "25.58": 2,
    "24.82": 1,
    "65.30": 1,
    "21.95": 1,
    "25.56": 1,
    "98.59": 1,
    "58.69": 1,
    "4.80": 1,
    "4.05": 1,
    "80.91": 1,
    "6.26": 1,
    "14.42": 1,
    "6.24": 1,
    "8.49": 1,
    "10.82": 1,
    "21.82": 1,
    "67.40": 1,
    "15.07": 1,
    "51.29": 1,
    "45.55": 1,
    "22.55": 1,
    "26.97": 1,
    "57.02": 1,
    "10.28": 1,
    "49.26": 1,
    "52.69": 1,
    "51.13": 1,
    "23.55": 1,
    "25.74": 1,
    "26.43": 1,
    "9.73": 1,
    "13.97": 1,
    "22.70": 1,
    "87.36": 1,
    "12.39": 1,
    "26.33": 1,
    "26.34": 1,
    "74.74": 1,
    "40.68": 1,
    "17.47": 1,
    "110.24": 1,
    "26.61": 1,
    "44.33": 1,
    "13.38": 1,
    "25.91": 1,
    "165.71": 1,
    "97.41": 1,
    "39.87": 1,
    "5.96": 1,
    "31.80": 1,
    "6.62": 1,
    "25.16": 1,
    "12.65": 1,
    "21.41": 1,
    "25.80": 1,
    "20.75": 1,
    "34.03": 1,
    "34.05": 1,
    "74.50": 1,
    "27.21": 1,
    "26.56": 1,
    "25.00": 1,
    "77.54": 1,
    "72.37": 1,
    "13.22": 1,
    "15.49": 1,
    "151.75": 1,
    "27.50": 1,
    "37.07": 1,
    "20.21": 1,
    "247.15": 1,
    "24.67": 1,
    "25.35": 1,
    "26.00": 1,
    "25.32": 1,
    "26.01": 1,
    "25.33": 1,
    "25.30": 1,
    "591.03": 1,
    "8.65": 1,
    "33.45": 1,
    "40.15": 1,
    "179.55": 1,
    "106.19": 1,
    "40.10": 1,
    "38.55": 1,
    "20.92": 1,
    "10.58": 1,
    "25.24": 1,
    "24.55": 1,
    "25.20": 1,
    "16.30": 1,
    "93.74": 1,
    "25.27": 1,
    "18.53": 1,
    "7.81": 1,
    "16.36": 1,
    "37.98": 1,
    "6.34": 1,
}
EXP_JOB_EST = {"rowCount": 100, "colCount": 9}
EXP_DAYS_WITH = [
    {
        "rowcount": 3127,
        "day_owl_str": "2017-12-20",
        "day": "2017-12-20T00:00:00.000+0000",
    },
    {
        "rowcount": 3125,
        "day_owl_str": "2017-12-21",
        "day": "2017-12-21T00:00:00.000+0000",
    },
    {
        "rowcount": 3121,
        "day_owl_str": "2017-12-22",
        "day": "2017-12-22T00:00:00.000+0000",
    },
    {
        "rowcount": 3119,
        "day_owl_str": "2017-12-25",
        "day": "2017-12-25T00:00:00.000+0000",
    },
    {
        "rowcount": 3119,
        "day_owl_str": "2017-12-26",
        "day": "2017-12-26T00:00:00.000+0000",
    },
    {
        "rowcount": 3117,
        "day_owl_str": "2017-12-27",
        "day": "2017-12-27T00:00:00.000+0000",
    },
    {
        "rowcount": 3117,
        "day_owl_str": "2017-12-28",
        "day": "2017-12-28T00:00:00.000+0000",
    },
    {
        "rowcount": 3116,
        "day_owl_str": "2017-12-29",
        "day": "2017-12-29T00:00:00.000+0000",
    },
    {
        "rowcount": 3111,
        "day_owl_str": "2018-01-01",
        "day": "2018-01-01T00:00:00.000+0000",
    },
    {
        "rowcount": 3113,
        "day_owl_str": "2018-01-02",
        "day": "2018-01-02T00:00:00.000+0000",
    },
    {
        "rowcount": 3111,
        "day_owl_str": "2018-01-03",
        "day": "2018-01-03T00:00:00.000+0000",
    },
    {
        "rowcount": 3111,
        "day_owl_str": "2018-01-04",
        "day": "2018-01-04T00:00:00.000+0000",
    },
    {
        "rowcount": 3111,
        "day_owl_str": "2018-01-05",
        "day": "2018-01-05T00:00:00.000+0000",
    },
    {
        "rowcount": 3106,
        "day_owl_str": "2018-01-08",
        "day": "2018-01-08T00:00:00.000+0000",
    },
    {
        "rowcount": 3105,
        "day_owl_str": "2018-01-09",
        "day": "2018-01-09T00:00:00.000+0000",
    },
    {
        "rowcount": 3105,
        "day_owl_str": "2018-01-10",
        "day": "2018-01-10T00:00:00.000+0000",
    },
    {
        "rowcount": 3104,
        "day_owl_str": "2018-01-11",
        "day": "2018-01-11T00:00:00.000+0000",
    },
    {
        "rowcount": 3100,
        "day_owl_str": "2018-01-12",
        "day": "2018-01-12T00:00:00.000+0000",
    },
    {
        "rowcount": 3087,
        "day_owl_str": "2018-01-15",
        "day": "2018-01-15T00:00:00.000+0000",
    },
    {
        "rowcount": 3088,
        "day_owl_str": "2018-01-16",
        "day": "2018-01-16T00:00:00.000+0000",
    },
]
EXP_DS_SCAN = {
    "score": 99,
    "rc": 100,
    "passFail": 1,
    "peak": 1,
    "scoreDupe": 0,
    "scoreSource": 0,
    "scoreDatashape": 1,
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
    "datashapeTotalScore": 1,
    "datashapeMaxPerCol": 20,
    "datashapeMaxColSize": 12,
    "datashapeSensitivity": 0,
    "behaviorScoreOff": False,
    "lbAbsRowCnt": None,
    "ubAbsRowCnt": None,
    "lbZscoreRowCnt": None,
    "ubZscoreRowCnt": None,
}
