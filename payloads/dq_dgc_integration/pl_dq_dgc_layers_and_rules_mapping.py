from datetime import datetime
from utils.constants import (
    PROD_RUN_ID,
)

DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME = (
    "AUTO_DQ_DGC_LAYERS_RULES_MAPPING_" + datetime.now().strftime("%Y%m%d%H%M%S")
)

POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"

DS_DEF_DGC_LAYERS_RULES_INTEGRATION = {
    "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
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
    "agentId": {"id": 0, "uuid": None},
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select exch, open, high, low, close, part_date_str from public.nyse",
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
        "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
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
    "outliers": [
        {
            "id": 957,
            "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
            "only": False,
            "lookback": 5,
            "key": ["close"],
            "include": ["open", "high", "low"],
            "exclude": ["symbol", "trade_date", "volume", "exch", "close", "part_date_str"],
            "dateColumn": None,
            "timeColumn": None,
            "timeBin": "DAY",
            "timeBinQuery": "",
            "categorical": False,
            "by": None,
            "limit": 300,
            "minHistory": 3,
            "historyLimit": 5,
            "score": 1.0,
            "aggFunc": "",
            "aggQuery": "",
            "query": "",
            "q1": 0.15,
            "q3": 0.85,
            "categoricalColumnConcatenation": False,
            "limitCategorical": None,
            "measurementUnit": "",
            "multiplierUpper": 1.35,
            "multiplierLower": 1.35,
            "record": True,
            "filter": None,
            "combine": True,
            "categoricalConfidenceType": "",
            "categoricalTopN": 3,
            "categoricalBottomN": 2,
            "categoricalMaxConfidence": 0.02,
            "categoricalMaxFrequencyPercentile": 0.25,
            "categoricalMinFrequency": 1,
            "categoricalMinVariance": 0.0,
            "categoricalMaxCategoryN": 1,
            "categoricalParallel": True,
            "categoricalAlgorithm": "",
            "categoricalAlgorithmParameters": {},
        }
    ],
    "patterns": [
        {
            "id": 91,
            "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
            "only": False,
            "lookback": 5,
            "key": ["exch"],
            "dateColumn": "part_date_str",
            "include": ["open", "high", "low"],
            "exclude": ["symbol", "trade_date", "volume", "exch", "close", "part_date_str"],
            "score": 1.0,
            "minSupport": 3.3e-5,
            "confidence": 0.6,
            "limit": 30,
            "on": True,
            "query": "",
            "filter": None,
            "timeBin": "DAY",
        }
    ],
    "dupe": {
        "on": True,
        "only": False,
        "include": ["exch", "high", "close"],
        "exclude": None,
        "depth": 2,
        "lowerBound": 95,
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
        "include": ["exch", "open", "high", "low", "close", "part_date_str"],
        "exclude": [],
        "correlation": True,
        "histogram": True,
        "semantic": None,
        "dataConceptId": None,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1.0,
        "shape": True,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0.0,
        "shapeMaxPerCol": 0,
        "shapeMaxColSize": 0,
        "shapeGranular": True,
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
    "env": {"dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME, "jdbcPrincipal": "", "jdbcKeyTab": ""},
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
    "outlierConfiguration": {
        "columnSensitivitySettings": [
            {"name": "part_date_str", "weight": 1.0, "unit": "DEFAULT"},
            {"name": "exch", "weight": 1.0, "unit": "DEFAULT"},
            {"name": "open", "weight": 1.0, "unit": "DEFAULT"},
            {"name": "high", "weight": 1.0, "unit": "DEFAULT"},
            {"name": "low", "weight": 1.0, "unit": "DEFAULT"},
            {"name": "close", "weight": 1.0, "unit": "DEFAULT"},
        ],
        "configurations": [
            {
                "id": 957,
                "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
                "only": False,
                "lookback": 5,
                "key": ["close"],
                "include": ["open", "high", "low"],
                "exclude": ["symbol", "trade_date", "volume", "exch", "close", "part_date_str"],
                "dateColumn": None,
                "timeColumn": None,
                "timeBin": "DAY",
                "timeBinQuery": "",
                "categorical": False,
                "by": None,
                "limit": 300,
                "minHistory": 3,
                "historyLimit": 5,
                "score": 1.0,
                "aggFunc": "",
                "aggQuery": "",
                "query": "",
                "q1": 0.15,
                "q3": 0.85,
                "categoricalColumnConcatenation": False,
                "limitCategorical": None,
                "measurementUnit": "",
                "multiplierUpper": 1.35,
                "multiplierLower": 1.35,
                "record": True,
                "filter": None,
                "combine": True,
                "categoricalConfidenceType": "",
                "categoricalTopN": 3,
                "categoricalBottomN": 2,
                "categoricalMaxConfidence": 0.02,
                "categoricalMaxFrequencyPercentile": 0.25,
                "categoricalMinFrequency": 1,
                "categoricalMinVariance": 0.0,
                "categoricalMaxCategoryN": 1,
                "categoricalParallel": True,
                "categoricalAlgorithm": "",
                "categoricalAlgorithmParameters": {},
            }
        ],
    },
    "shape": {
        "enabled": True,
        "totalScore": 0,
        "sensitivity": 0.0,
        "maxPerCol": 0,
        "maxColSize": 0,
        "granular": True,
        "columnSettings": [
            {"enabled": False, "name": "close", "type": "Double, Int"},
            {"enabled": True, "name": "exch", "type": "String"},
            {"enabled": True, "name": "high", "type": "Double, Int"},
            {"enabled": False, "name": "low", "type": "Decimal"},
            {"enabled": False, "name": "open", "type": "Double, Int"},
            {"enabled": False, "name": "part_date_str", "type": "Timestamp"},
        ],
    },
    "jobSchedule": None,
    "connectionType": "PUSHDOWN",
}


# ----------------------- Basic Job with no findings on ------------------------------------------

DS_DEF_DGC_LAYERS_RULES_INTEGRATION_BASIC = {
    "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
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
        "query": "select exch, open, high, low, close, part_date_str from public.nyse",
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
        "dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME,
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
        "include": ["exch", "open", "high", "low", "close", "part_date_str"],
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
    "env": {"dataset": DS_DEF_DGC_LAYERS_AND_RULES_JOB_NAME, "jdbcPrincipal": "", "jdbcKeyTab": ""},
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
        ],
    },
    "jobSchedule": None,
    "connectionType": "PULLUP",
}
