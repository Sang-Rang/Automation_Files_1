# pylint: disable-msg=import-error
from utils.constants import PROD_HOST, PROD_PORT, PROD_AGENT_ID, PROD_AGENT_UUID

WHERE_DATE = "1993-11-11"
TABLE_NAME = "PUBLIC.ACCOUNTS"
COL_NAME = "date"
DATASET_NAME_NO_PROFILE = "AUTO_CXN_SNOWFLAKE_UP_NO_PROFILE"
DATASET_NAME_FULL_PROFILE = "AUTO_CXN_SNOWFLAKE_UP_FULL_PROFILE"
DATASET_NAME_COUNT_PROFILE = "AUTO_CXN_SNOWFLAKE_UP_COUNT_PROFILE"
QUERY = f"select * from {TABLE_NAME} where {COL_NAME} = '{WHERE_DATE}' limit 5"
CONN_NAME = "APPROVED_SNOWFLAKE_UP"
ROW_COUNT = 5

PL_DS_GEN = {"dataset": DATASET_NAME_FULL_PROFILE, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET_NAME_FULL_PROFILE, "runId": WHERE_DATE, "sense": 3}
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

EXP_JOB_EST = {"rowCount": 5, "colCount": 4}
EXP_DAYS_WITH = [
    {"rowcount": 3, "day_owl_str": "1997-12-07", "day": "1997-12-07"},
    {"rowcount": 6, "day_owl_str": "1997-12-08", "day": "1997-12-08"},
    {"rowcount": 4, "day_owl_str": "1997-12-09", "day": "1997-12-09"},
    {"rowcount": 5, "day_owl_str": "1997-12-10", "day": "1997-12-10"},
    {"rowcount": 1, "day_owl_str": "1997-12-11", "day": "1997-12-11"},
    {"rowcount": 2, "day_owl_str": "1997-12-13", "day": "1997-12-13"},
    {"rowcount": 1, "day_owl_str": "1997-12-15", "day": "1997-12-15"},
    {"rowcount": 4, "day_owl_str": "1997-12-16", "day": "1997-12-16"},
    {"rowcount": 1, "day_owl_str": "1997-12-17", "day": "1997-12-17"},
    {"rowcount": 1, "day_owl_str": "1997-12-18", "day": "1997-12-18"},
    {"rowcount": 4, "day_owl_str": "1997-12-19", "day": "1997-12-19"},
    {"rowcount": 4, "day_owl_str": "1997-12-20", "day": "1997-12-20"},
    {"rowcount": 2, "day_owl_str": "1997-12-21", "day": "1997-12-21"},
    {"rowcount": 2, "day_owl_str": "1997-12-22", "day": "1997-12-22"},
    {"rowcount": 3, "day_owl_str": "1997-12-23", "day": "1997-12-23"},
    {"rowcount": 2, "day_owl_str": "1997-12-25", "day": "1997-12-25"},
    {"rowcount": 1, "day_owl_str": "1997-12-26", "day": "1997-12-26"},
    {"rowcount": 3, "day_owl_str": "1997-12-27", "day": "1997-12-27"},
    {"rowcount": 3, "day_owl_str": "1997-12-28", "day": "1997-12-28"},
    {"rowcount": 2, "day_owl_str": "1997-12-29", "day": "1997-12-29"},
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
DS_DEFS_COUNT_PROFILE = ["count"]
DS_DEFS_FULL_PROFILE = {
    "dataset": DATASET_NAME_FULL_PROFILE,
    "runId": WHERE_DATE,
    "runIdEnd": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobId": None,
    "coreMaxActiveConnections": None,
    "linkId": None,
    "licenseKey": "",
    "logFile": "",
    "logLevel": "INFO",
    "hootOnly": False,
    "prettyPrint": True,
    "useTemplate": False,
    "parallel": False,
    "plan": False,
    "dataPreviewOff": False,
    "datasetSafeOff": False,
    "obslimit": 300,
    "pgUser": "",
    "pgPassword": "",
    "host": PROD_HOST,
    "port": PROD_PORT,
    "user": "anonymous : use -owluser",
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1.0,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {"id": PROD_AGENT_ID, "uuid": PROD_AGENT_UUID},
    "load": {
        "dataset": DATASET_NAME_FULL_PROFILE,
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": QUERY,
        "queryHistory": "",
        "key": "",
        "expression": "",
        "addDateColumn": False,
        "zeroFillNone": False,
        "replaceNones": "",
        "stringMode": False,
        "operator": "=",
        "dateColumn": "",
        "transform": "",
        "filter": "",
        "filterNot": "",
        "sample": 1.0,
        "backRun": 0,
        "backRunBin": "DAY",
        "unionLookBack": False,
        "unionLookBackMinRow": 0,
        "cache": True,
        "dateFormat": "yyyy-MM-dd",
        "timeFormat": "HH:mm:ss.SSS",
        "timestamp": False,
        "filePath": "",
        "fileQuery": "",
        "fullFile": False,
        "fileHeader": None,
        "checkHeader": True,
        "inferSchema": True,
        "fileType": None,
        "delimiter": ",",
        "fileCharSet": "UTF-8",
        "skipLines": 0,
        "avroSchema": "",
        "xmlRowTag": "",
        "flatten": False,
        "handleMaps": False,
        "handleMixedJson": False,
        "multiLine": False,
        "lib": "",
        "additionalLib": "",
        "driverName": "",
        "connectionName": CONN_NAME,
        "connectionUrl": "",
        "userName": "KHASLBECK",
        "password": "",
        "connectionProperties": {},
        "hiveNative": False,
        "hiveNativeHWC": False,
        "useSql": True,
        "columnName": None,
        "lowerBound": None,
        "upperBound": None,
        "numPartitions": 0,
        "escapeWithBackTick": False,
        "escapeWithSingleQuote": False,
        "escapeWithDoubleQuote": False,
        "partitionNumber": 0,
        "archiveBreaks": False,
        "archiveConnection": "",
        "escapeCharacter": "",
        "hasHeader": True,
    },
    "profile": {
        "dataset": DATASET_NAME_FULL_PROFILE,
        "on": True,
        "only": False,
        "include": ["account_id", "date", "district_id", "frequency"],
        "exclude": None,
        "filter": "",
        "shape": None,
        "correlation": None,
        "histogram": None,
        "semantic": None,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1.0,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0.0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "shapeGranular": None,
        "behavioralDimension": "",
        "behavioralDimensionGroup": "",
        "behavioralValueColumn": "",
        "behaviorScoreOff": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profilePushDown": ["count", "distinct", "mean", "minmax", "quality"],
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNoneCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "adaptiveTier": None,
        "profileStringLength": False,
        "dataConceptId": None,
    },
    "spark": {
        "dataset": DATASET_NAME_FULL_PROFILE,
        "numExecutors": 1,
        "driverMemory": "1g",
        "executorMemory": "1g",
        "executorCores": 2,
        "conf": "",
        "queue": "",
        "master": "k8s://",
        "principal": "",
        "keyTab": "",
        "deployMode": "cluster",
        "jars": None,
        "packages": None,
        "files": None,
    },
    "env": {"jdbcPrincipal": "", "jdbcKeyTab": ""},
    "stream": None,
    "record": {
        "dataset": None,
        "on": False,
        "in": "",
        "notIn": "",
        "include": None,
        "percDeltaLimit": 0.1,
        "score": 1.0,
        "keyColumn": None,
        "dateColumn": None,
        "timeBin": "DAY",
        "by": None,
    },
    "transforms": [],
    "pipeline": [],
    "jobDescription": "",
}
