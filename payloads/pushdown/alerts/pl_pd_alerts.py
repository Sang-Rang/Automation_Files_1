import copy
from datetime import datetime

import pytest

from utils.constants import PROD_RUN_ID

NOW = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

DS_PD_ALERTS_SUCCESS_DATASET = "AUTO_PD_ALERT_JOB_SUCCESS"
DS_PD_ALERTS_FAILURE_JOB = "AUTO_PD_ALERT_JOB_FAILURE"
DS_PD_ALERTS_GLOBAL_FAILURE_JOB = "AUTO_PD_GLOBAL_ALERT_JOB_FAILURE"
DS_QUERY_JOB_SUCCESS = "select * from default.nyse"
DS_QUERY_JOB_FAILURE = "selected vks from default.nyse"

PL_PD_NEW_JOB_SUCCESS = {
    "dataset": DS_PD_ALERTS_SUCCESS_DATASET,
    "runId": PROD_RUN_ID,
    "runIdEnd": None,
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobId": {"id": -1, "uuid": None},
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
    "port": None,
    "user": "autoadmin01@cdq-ad.dq.cp.collibra.dev",
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {"id": 0, "uuid": None},
    "load": {
        "dataset": None,
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "",
        "queryHistory": "",
        "key": "",
        "expression": "",
        "addDateColumn": False,
        "zeroFillNone": False,
        "replaceNones": "",
        "stringMode": False,
        "operator": None,
        "dateColumn": None,
        "transform": None,
        "filter": "",
        "filterNot": "",
        "sample": 1,
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
        "driverName": None,
        "connectionName": "",
        "connectionUrl": "",
        "userName": "",
        "password": "",
        "connectionProperties": {},
        "hiveNative": None,
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
        "ruleSerial": False,
        "coreFetchMode": False,
        "escapeCharacter": "",
        "hasHeader": True,
    },
    "outliers": [],
    "outlier": {
        "id": None,
        "dataset": None,
        "on": False,
        "only": False,
        "lookback": 5,
        "key": None,
        "include": None,
        "exclude": None,
        "dateColumn": None,
        "timeColumn": None,
        "timeBin": "DAY",
        "timeBinQuery": "",
        "categorical": True,
        "by": None,
        "limit": 300,
        "minHistory": 3,
        "historyLimit": 5,
        "score": 1,
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
        "categoricalMinVariance": 0,
        "categoricalMaxCategoryN": 1,
        "categoricalParallel": True,
        "categoricalAlgorithm": "",
        "categoricalAlgorithmParameters": {},
    },
    "pattern": {
        "id": None,
        "dataset": None,
        "only": False,
        "lookback": 5,
        "key": None,
        "dateColumn": None,
        "include": None,
        "exclude": None,
        "score": 1,
        "minSupport": 0.000033,
        "confidence": 0.6,
        "limit": 30,
        "query": "",
        "filter": None,
        "timeBin": "DAY",
        "on": False,
        "match": True,
        "lowFreq": False,
        "bucketLimit": 450000,
        "deDupe": True,
    },
    "patterns": [],
    "dupe": {
        "dataset": None,
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
        "score": 1,
        "limit": 300,
    },
    "pushdown": {
        "dataset": DS_PD_ALERTS_SUCCESS_DATASET,
        "connectionName": "APPROVED_REDSHIFT_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": DS_QUERY_JOB_SUCCESS,
        "backRuns": 0,
        "backRunBin": "DAY",
        "dateFormatType": "DATE",
        "threads": 2,
        "manualSourceQuery": False,
        "key": "",
        "sourceOutputSchema": "",
        "sourceBreakRules": False,
        "sourceBreakOutliers": False,
        "sourceBreakDupes": False,
        "sourceBreakShapes": False,
        "sourceBreakResults": False,
        "sqlLoggingToggle": False,
    },
    "profile": {
        "dataset": DS_PD_ALERTS_SUCCESS_DATASET,
        "on": False,
        "only": False,
        "include": None,
        "exclude": None,
        "filter": "",
        "shape": False,
        "correlation": None,
        "histogram": None,
        "semantic": None,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0,
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
        "detectStringNumerics": False,
        "detectTopnBotn": False,
        "detectScalePrecision": False,
        "dataConceptId": 300,
        "advancedTier": False,
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
        "score": 1,
        "limit": 30,
        "sourcePushDownCount": False,
        "checkType": True,
        "checkCase": False,
        "validateSchemaOrder": False,
        "matches": False,
        "validateValuesThreshold": 0.9,
        "validateValuesThresholdStrictDownScore": False,
        "validateValuesShowAll": False,
        "validateValuesIgnoreNone": False,
        "validateValuesIgnoreEmpty": False,
        "validateValuesIgnorePrecision": False,
        "validateValuesTrim": False,
        "validateValuesShowMissingKeys": False,
        "validateSrcJoinOnly": False,
        "validateValuesFilter": "",
        "dataset": "",
        "datasetSrc": "",
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
        "hasHeader": True,
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
        "dataset": DS_PD_ALERTS_SUCCESS_DATASET,
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
        "connectionList": [],
    },
    "spark": {
        "dataset": None,
        "numExecutors": 3,
        "driverMemory": "",
        "executorMemory": "",
        "executorCores": 1,
        "conf": "",
        "queue": "",
        "master": "local[*]",
        "principal": "",
        "keyTab": "",
        "deployMode": "",
        "jars": None,
        "packages": None,
        "files": None,
    },
    "env": {"dataset": DS_PD_ALERTS_SUCCESS_DATASET, "jdbcPrincipal": "", "jdbcKeyTab": ""},
    "stream": None,
    "record": {
        "dataset": None,
        "on": False,
        "in": "",
        "notIn": "",
        "include": None,
        "percDeltaLimit": 0.1,
        "score": 1,
        "keyColumn": None,
        "dateColumn": None,
        "timeBin": "DAY",
        "by": None,
    },
    "transforms": [],
    "pipeline": [],
    "jobDescription": "",
}
PL_PD_NEW_JOB_FAILURE = copy.deepcopy(PL_PD_NEW_JOB_SUCCESS)
PL_PD_NEW_JOB_FAILURE["dataset"] = DS_PD_ALERTS_FAILURE_JOB
PL_PD_NEW_JOB_FAILURE["pushdown"]["dataset"] = DS_PD_ALERTS_FAILURE_JOB
PL_PD_NEW_JOB_FAILURE["env"]["dataset"] = DS_PD_ALERTS_FAILURE_JOB
PL_PD_NEW_JOB_FAILURE["pushdown"]["sourceQuery"] = DS_QUERY_JOB_FAILURE

PL_PD_NEW_JOB_GLOBAL_FAILURE = copy.deepcopy(PL_PD_NEW_JOB_SUCCESS)
PL_PD_NEW_JOB_GLOBAL_FAILURE["dataset"] = DS_PD_ALERTS_GLOBAL_FAILURE_JOB
PL_PD_NEW_JOB_GLOBAL_FAILURE["pushdown"]["dataset"] = DS_PD_ALERTS_GLOBAL_FAILURE_JOB
PL_PD_NEW_JOB_GLOBAL_FAILURE["env"]["dataset"] = DS_PD_ALERTS_GLOBAL_FAILURE_JOB
PL_PD_NEW_JOB_GLOBAL_FAILURE["pushdown"]["sourceQuery"] = DS_QUERY_JOB_FAILURE

PL_PD_NEW_JOB_STATUS_FAILURE_ALERT = {
    "dataset": DS_PD_ALERTS_FAILURE_JOB,
    "alertNm": "AUTO_ALERT_V3_JOB_STATUS_FAILURE_" + str(NOW),
    "alertCond": "N/A",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "AUTO JOB RUN FAILURE NEW " + str(NOW),
    "batchName": "",
    "alertFormat": "EMAIL",
    "alertTriggerType": "1",
}
PL_PD_UPDATED_JOB_STATUS_FAILURE_ALERT = {
    "dataset": DS_PD_ALERTS_FAILURE_JOB,
    "alertNm": "AUTO_ALERT_V3_JOB_STATUS_FAILURE_" + str(NOW),
    "alertCond": "N/A",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "AUTO JOB RUN FAILURE UPDATE " + str(NOW),
    "batchName": "",
    "alertFormat": "EMAIL",
    "alertTriggerType": "1",
}

PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT = {
    "dataset": "",
    "alertNm": "AUTO_ALERT_V3_JOB_STATUS_SUCCESS_" + str(NOW),
    "alertCond": "score>=0",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "AUTO JOB RUN SUCCESS NEW " + str(NOW),
    "batchName": "",
    "alertFormat": "EMAIL",
    "alertTriggerType": "2",
}

PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT = copy.deepcopy(PL_PD_NEW_JOB_STATUS_SUCCESS_ALERT)
PL_PD_UPDATED_JOB_STATUS_SUCCESS_ALERT["alertMsg"] = "AUTO JOB RUN SUCCESS UPDATED " + str(NOW)


PL_PD_NEW_JOB_DEFAULT = {
    "dataset": "Test",
    "runId": PROD_RUN_ID,
    "runIdEnd": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobDescription": "",
    "jobId": {"id": -1, "uuid": None},
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
    "host": "10.64.2.3:5432/dqqa?currentSchema=validation",
    "port": None,
    "user": "anonymous : use -owluser",
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {"id": 0, "uuid": None},
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "",
        "queryHistory": "",
        "key": "",
        "expression": "",
        "addDateColumn": False,
        "zeroFillNone": False,
        "replaceNones": "",
        "stringMode": False,
        "operator": None,
        "dateColumn": None,
        "transform": None,
        "filter": "",
        "filterNot": "",
        "sample": 1,
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
        "lib": "",
        "additionalLib": "",
        "driverName": None,
        "connectionName": "",
        "connectionUrl": "",
        "userName": "",
        "password": "",
        "connectionProperties": {},
        "hiveNative": None,
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
        "dataset": "PUBLIC.SALES_12",
        "connectionName": "APPROVED_SNOWFLAKE_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.SALES",
        "backRuns": 0,
        "backRunBin": "DAY",
        "dateFormatType": "DATE",
        "threads": 2,
        "manualSourceQuery": False,
        "key": "",
        "sourceOutputSchema": "",
        "sourceBreakRules": False,
        "sourceBreakOutliers": False,
        "sourceBreakDupes": False,
        "sourceBreakShapes": False,
        "sourceBreakResults": False,
        "sqlLoggingToggle": False,
        "unionLookback": False,
        "unionLookbackMin": 0,
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
        "score": 1,
        "limit": 300,
    },
    "profile": {
        "on": False,
        "only": False,
        "include": ["NAME", "TRDATE", "SALES"],
        "exclude": [],
        "correlation": None,
        "histogram": None,
        "semantic": None,
        "dataConceptId": 300,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1,
        "shape": False,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0,
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
        "profileStringLength": False,
        "detectStringNumerics": False,
        "detectTopnBotn": False,
        "detectScalePrecision": False,
        "adaptiveTier": None,
        "advancedTier": False,
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
        "score": 1,
        "limit": 30,
        "sourcePushDownCount": False,
        "checkType": True,
        "checkCase": False,
        "validateSchemaOrder": False,
        "matches": False,
        "validateValuesThreshold": 0.9,
        "validateValuesThresholdStrictDownScore": False,
        "validateValuesShowAll": False,
        "validateValuesIgnoreNone": False,
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
        "numExecutors": 3,
        "driverMemory": "",
        "executorMemory": "",
        "executorCores": 1,
        "conf": "",
        "queue": "",
        "master": "local[*]",
        "principal": "",
        "keyTab": "",
        "deployMode": "",
        "jars": None,
        "packages": None,
        "files": None,
    },
    "env": {"dataset": "PUBLIC.SALES_12", "jdbcPrincipal": "", "jdbcKeyTab": ""},
    "record": {
        "on": False,
        "in": "",
        "notIn": "",
        "include": None,
        "percDeltaLimit": 0.1,
        "score": 1,
        "dataset": None,
        "dateColumn": None,
        "keyColumn": None,
        "timeBin": "DAY",
        "by": None,
    },
    "stream": None,
    "pipeline": [],
    "outlierConfiguration": None,
    "shape": {
        "enabled": False,
        "totalScore": 0,
        "sensitivity": 0,
        "maxPerCol": 20,
        "maxColSize": 12,
        "granular": None,
        "columnSettings": [],
    },
    "metaTags": ["tag-1", "tag-2", "tag-3", "tag-4"],
    "jobSchedule": None,
    "connectionType": "PUSHDOWN",
}

DATA_FOR_SNOWFLAKE_PD_SUCCESS_JOB = {
    "dataset": DS_PD_ALERTS_SUCCESS_DATASET + "_SNOWFLAKE",
    "include_columns": ["NAME", "TRDATE", "SALES"],
    "connection_name": "APPROVED_SNOWFLAKE_PUSHDOWN",
    "source_query": "select * from PUBLIC.SALES",
}

PL_PD_CONDITION_RULES_FOR_SALES = {
    "dataset": "AUTO_PD_CONDITION_ALERT_JOB_QA",
    "ruleNm": "AUTO_SIMPLE_RULE",
    "ruleType": "SQLG",
    "ruleValue": "SALES>5000",
    "filterQuery": "",
    "points": 1,
    "ruleRepo": "",
    "perc": 1,
    "columnName": None,
    "businessCategory": "",
    "businessDesc": "",
    "dimId": None,
    "scoringScheme": 0,
    "tolerance": 0,
}

PARAMS_PD_CONDITION_ALERT_TESTS = [
    pytest.param(
        {
            "connection": "Snowflake",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_SNOWFLAKE",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SNOWFLAKE_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.snowflake,
    ),
    pytest.param(
        {
            "connection": "Bigquery",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_BIGQUERY",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_BIGQUERY_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.bigquery,
    ),
    pytest.param(
        {
            "connection": "Trino",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_TRINO",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_TRINO_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.trino,
    ),
    pytest.param(
        {
            "connection": "Saphana",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_SAPHANA",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SAPHANA_PUSHDOWN",
            "source_query": "select * from TEST.SALES",
        },
        marks=pytest.mark.saphana,
    ),
    pytest.param(
        {
            "connection": "Redshift",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_REDSHIFT",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_REDSHIFT_PUSHDOWN",
            "source_query": "select * from public.sales2",
        },
        marks=pytest.mark.redshift,
    ),
    pytest.param(
        {
            "connection": "Databricks",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_DATABRICKS",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_DATABRICKS_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.databricks,
    ),
    pytest.param(
        {
            "connection": "Athena",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_ATHENA",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_ATHENA_PUSHDOWN",
            "source_query": "select * from default.sales",
        },
        marks=pytest.mark.athena,
    ),
    pytest.param(
        {
            "connection": "SQLServer",
            "dataset": "AUTO_PD_CONDITION_ALERT_JOB_SQLSERVER",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_SQLSERVER_PUSHDOWN",
            "source_query": "select * from dbo.sales",
        },
        marks=pytest.mark.sqlserver,
    ),
]

PL_PD_DEFAULT_CONDITION_RULE_ALERT = {
    "dataset": "AUTO_PD_CONDITION_ALERT_JOB_QA",
    "alertNm": "AUTO_CONDITION_SIMPLE_RULE_ALERT",
    "alertCond": "AUTO_SIMPLE_RULE > 0",
    "alertFormat": "EMAIL",
    "alertFormatValue": "dq-alerts-aaaadzxeeappnuk46h7zzz47uu@collibra.slack.com",
    "alertMsg": "Condition Alert Test!!!",
    "alertTypes": ["CONDITION"],
}
