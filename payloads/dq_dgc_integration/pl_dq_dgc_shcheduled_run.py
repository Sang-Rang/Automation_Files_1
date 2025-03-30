import copy
from datetime import datetime

from utils.constants import PROD_RUN_ID

DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME = (
    "AUTO_DQ_DGC_INT_WITH_BU_SCHEDULED" + datetime.now().strftime("%Y%m%d%H%M%S")
)
DS_DEF_DGC_SCHEDULED_JOB_RUN = {
    "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
    "runId": PROD_RUN_ID,
    "runIdEnd": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobDescription": "",
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
    "host": "10.64.2.3:5432/dqqa?currentSchema=automation",
    "port": "5432/dqqa?currentSchema=automation",
    "user": "misha",
    "alertEmail": None,
    "scheduleTime": None,
    "schemaScore": 1.0,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {"id": 6, "uuid": "8eb1f6a8-70ab-4285-a903-b587523ae61e"},
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select * from public.nyse",
        "queryHistory": "",
        "key": "",
        "expression": "",
        "addDateColumn": False,
        "zeroFillNull": False,
        "replaceNulls": "",
        "stringMode": False,
        "operator": None,
        "dateColumn": None,
        "transform": None,
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
        "lib": "/opt/owl/drivers/postgres/",
        "additionalLib": "",
        "driverName": "org.postgresql.Driver",
        "connectionName": "APPROVED_POSTGRES_UP",
        "connectionUrl": "jdbc:postgresql://35.190.143.55:5432/postgres?cs=test&test=test&t2=t2",
        "userName": "owluser",
        "password": "",
        "connectionProperties": {},
        "hiveNative": False,
        "hiveNativeHWC": False,
        "useSql": True,
        "columnName": None,
        "lowerBound": None,
        "upperBound": None,
        "numPartitions": 0,
        "partitionNumber": 0,
        "escapeWithBackTick": False,
        "escapeWithSingleQuote": False,
        "escapeWithDoubleQuote": False,
        "escapeCharacter": "",
        "checkHeader": True,
        "archiveConnection": "",
        "coreFetchMode": False,
        "archiveBreaks": False,
        "ruleSerial": False,
    },
    "pushdown": {
        "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
        "connectionName": "",
        "maxConnections": 10,
        "sourceQuery": "",
        "backRuns": 0,
        "backRunBin": "DAY",
        "dateFormatType": "DATE",
        "threads": 5,
        "manualSourceQuery": False,
        "key": "",
        "sourceOutputSchema": "",
        "sourceBreakRules": False,
        "sourceBreakOutliers": False,
        "sourceBreakDupes": False,
        "sourceBreakShapes": False,
        "sourceBreakResults": False,
        "sqlLoggingToggle": True,
    },
    "outliers": [],
    "patterns": [],
    "dupe": {
        "on": False,
        "only": False,
        "include": None,
        "exclude": None,
        "depth": 0,
        "lowerBound": 99,
        "upperBound": 100,
        "approximate": 1,
        "limitPerDupe": 15,
        "checkHeader": True,
        "filter": None,
        "ignoreCase": True,
        "score": 1.0,
        "limit": 300,
    },
    "profile": {
        "on": True,
        "only": False,
        "include": [
            "exch",
            "symbol",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "part_date_str",
        ],
        "exclude": [],
        "correlation": None,
        "histogram": None,
        "semantic": None,
        "dataConceptId": None,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1.0,
        "shape": False,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0.0,
        "shapeMaxPerCol": 0,
        "shapeMaxColSize": 0,
        "shapeGranular": False,
        "behavioralDimension": "",
        "behavioralDimensionGroup": "",
        "behavioralValueColumn": "",
        "behaviorScoreOff": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profilePushDown": None,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "profileStringLength": False,
        "detectStringNumerics": True,
        "detectTopnBotn": True,
        "detectScalePrecision": True,
        "adaptiveTier": None,
        "advancedTier": None,
        "filter": "",
    },
    "source": {
        "on": False,
        "only": False,
        "validateValues": False,
        "key": None,
        "include": None,
        "exclude": None,
        "includeSrc": None,
        "excludeSrc": None,
        "map": None,
        "score": 1.0,
        "limit": 30,
        "sourcePushDownCount": False,
        "checkType": True,
        "checkCase": False,
        "validateSchemaOrder": False,
        "matches": False,
        "validateValuesThreshold": 0.9,
        "validateValuesThresholdStrictDownScore": False,
        "validateValuesShowAll": False,
        "validateValuesIgnoreNull": False,
        "validateValuesIgnoreEmpty": False,
        "validateValuesIgnorePrecision": False,
        "validateValuesTrim": False,
        "validateValuesShowMissingKeys": False,
        "validateSrcJoinOnly": False,
        "validateValuesFilter": "",
        "dataset": "",
        "driverName": "",
        "user": "",
        "password": "",
        "passwordManager": "",
        "connectionName": "",
        "connectionUrl": "",
        "query": "",
        "lib": "",
        "connectionProperties": {},
        "filePath": "",
        "fileQuery": "",
        "fullFile": False,
        "header": None,
        "skipLines": 0,
        "inferSchema": True,
        "fileType": None,
        "delimiter": ",",
        "fileCharSet": "UTF-8",
        "avroSchema": "",
        "xmlRowTag": "",
        "flatten": False,
        "handleMaps": False,
        "handleMixedJson": False,
        "multiLine": False,
        "filterCols": None,
    },
    "rule": {
        "on": True,
        "only": False,
        "lib": None,
        "name": "",
        "absoluteScoring": False,
        "ruleBreakPreviewLimit": 6,
    },
    "colMatch": {
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
        "connectionList": [],
    },
    "spark": {
        "numExecutors": 1,
        "driverMemory": "1g",
        "executorMemory": "2g",
        "executorCores": 1,
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
    "env": {
        "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_SCHEDULED_JOB_NAME,
        "jdbcPrincipal": "",
        "jdbcKeyTab": "",
    },
    "record": {
        "on": False,
        "in": "",
        "notIn": "",
        "include": None,
        "percDeltaLimit": 0.1,
        "score": 1.0,
        "dataset": None,
        "dateColumn": None,
        "keyColumn": None,
        "timeBin": "DAY",
        "by": None,
    },
    "stream": None,
    "pipeline": [],
    "metaTags": [],
    "outlierConfiguration": None,
    "shape": {
        "enabled": False,
        "totalScore": 0,
        "sensitivity": 0.0,
        "maxPerCol": 0,
        "maxColSize": 0,
        "granular": False,
        "columnSettings": [
            {"enabled": False, "name": "close", "type": "Double, Int"},
            {"enabled": False, "name": "exch", "type": "String"},
            {"enabled": False, "name": "high", "type": "Double, Int"},
            {"enabled": False, "name": "low", "type": "Decimal"},
            {"enabled": False, "name": "open", "type": "Double, Int"},
            {"enabled": False, "name": "part_date_str", "type": "Timestamp"},
            {"enabled": False, "name": "symbol", "type": "String"},
            {"enabled": False, "name": "trade_date", "type": "Timestamp"},
            {"enabled": False, "name": "volume", "type": "Decimal"},
        ],
    },
    "jobSchedule": None,
    "connectionType": "PULLUP",
}


DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME = (
    "AUTO_DQ_DGC_INT_NO_BU_SCHEDULED" + datetime.now().strftime("%Y%m%d%H%M%S")
)

DS_DEF_DGC_SCHEDULED_JOB_RUN_NO_BU = copy.deepcopy(DS_DEF_DGC_SCHEDULED_JOB_RUN)
DS_DEF_DGC_SCHEDULED_JOB_RUN_NO_BU["dataset"] = DS_DEF_DGC_INTEGRATION_NO_BU_SCHEDULED_JOB_NAME
