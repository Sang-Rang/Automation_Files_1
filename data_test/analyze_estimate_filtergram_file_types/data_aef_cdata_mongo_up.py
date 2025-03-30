TRADE_DATE = "2015-12-01"
TABLE_NAME = "sample_mflix.movies"
COL_NAME = "released"
DATASET = "AUTO_CONNECTION_CDATA_MONGO_UP"
QUERY = f"select * from {TABLE_NAME} where {COL_NAME} = '{TRADE_DATE} 00:00:00'"
CONN_NAME = "APPROVED_CDATA_MONGO_UP"

ROW_COUNT = 2
FILTERGRAM_COL = "countries"

PL_DS_GEN = {"dataset": DATASET, "runId": TRADE_DATE}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}
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
    "cols": "_id,awards.nominations,awards.text,awards.wins,cast,countries,"
    "directors,fullplot,genres,imdb.id,imdb.rating,imdb.votes,"
    "languages,lastupdated,metacritic,num_mflix_comments,plot,poster,"
    "rated,released,runtime,title,tomatoes.boxOffice,"
    "tomatoes.consensus,tomatoes.critic.meter,"
    "tomatoes.critic.numReviews,tomatoes.critic.rating,tomatoes.dvd,"
    "tomatoes.fresh,tomatoes.lastUpdated,tomatoes.production,"
    "tomatoes.rotten,tomatoes.viewer.meter,tomatoes.viewer.numReviews,"
    "tomatoes.viewer.rating,tomatoes.website,type,writers,year",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} = '{TRADE_DATE}'",
    "query": f"select * from {TABLE_NAME} where {COL_NAME} = '{TRADE_DATE}'",
}

EXP_FILTERGRAM = {'["USA"]': 1, '["UK", "France", "USA"]': 1}
EXP_JOB_EST = {"rowCount": 2, "colCount": 39}
EXP_DAYS_WITH = [
    {
        "rowcount": 2,
        "day_owl_str": "2015-12-01",
        "day": "2015-12-01T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "2015-12-02",
        "day": "2015-12-02T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "2015-12-04",
        "day": "2015-12-04T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-09",
        "day": "2015-12-09T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-10",
        "day": "2015-12-10T00:00:00.000+0000",
    },
    {
        "rowcount": 2,
        "day_owl_str": "2015-12-11",
        "day": "2015-12-11T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-16",
        "day": "2015-12-16T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-18",
        "day": "2015-12-18T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-23",
        "day": "2015-12-23T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2015-12-31",
        "day": "2015-12-31T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-01-13",
        "day": "2016-01-13T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-01-15",
        "day": "2016-01-15T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-01-20",
        "day": "2016-01-20T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-01-27",
        "day": "2016-01-27T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-02-08",
        "day": "2016-02-08T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-02-10",
        "day": "2016-02-10T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-02-19",
        "day": "2016-02-19T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-03-01",
        "day": "2016-03-01T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-03-04",
        "day": "2016-03-04T00:00:00.000+0000",
    },
    {
        "rowcount": 1,
        "day_owl_str": "2016-03-23",
        "day": "2016-03-23T00:00:00.000+0000",
    },
]
EXP_DS_SCAN = {
    "score": 80,
    "rc": 2,
    "passFail": 1,
    "peak": 1,
    "scoreDupe": 0,
    "scoreSource": 0,
    "scoreDatashape": 0,
    "scoreSchema": 20,
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
    "schemaTotalScore": 20,
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
