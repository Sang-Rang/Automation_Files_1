# pylint: disable-msg=import-error
from utils.constants import (
    PROD_RUN_ID,
    PROD_HOST,
    PROD_PORT,
    BASE_CREDS,
)

CONNECTION = "APPROVED_ATHENA_UP"
OUTLIERS_NO_DC_DATASET = "AUTO_OUTLIERS_NODC"

OUTLIERS_NO_DC_PAYLOAD = {
    "dataset": OUTLIERS_NO_DC_DATASET,
    "runId": PROD_RUN_ID,
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
    "user": BASE_CREDS["username"],
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {
        "id": 8,
        "uuid": "5e1ad2be-e28e-444a-ac96-fe2368dd4696",
    },
    "load": {
        "dataset": OUTLIERS_NO_DC_DATASET,
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select CAST(cm_bdos as TIMESTAMP) as cm_bdos, cm_claim_status, cm_claimant_age, "
        "CAST(cm_claimant_bdate as TIMESTAMP) as cm_claimant_bdate, cm_claimant_sex, "
        "CAST(cm_conversion_date as TIMESTAMP) as cm_conversion_date, "
        "CAST(cm_date_claim_paid as TIMESTAMP) as cm_date_claim_paid, "
        "CAST(cm_date_received as TIMESTAMP) as cm_date_received, cm_denied_reason1, "
        "cm_denied_reason2, cm_diagnosis_code, cm_disab_days, cm_doc_origin_dsc, "
        "CAST(cm_edos as TIMESTAMP) as cm_edos, CAST(cm_eff_date_family as TIMESTAMP) "
        "as cm_eff_date_family, CAST(cm_end_treatmn_dte as TIMESTAMP) "
        "as cm_end_treatmn_dte, CAST(cm_fica_date as TIMESTAMP) as cm_fica_date, "
        "cm_group_number, cm_hospital_days, cm_lob, cm_medicare_number, cm_pending_flag1, "
        "cm_pending_flag2, cm_pending_flag3, cm_pending_flag4, "
        "CAST(cm_proof_loss_dt as TIMESTAMP) as cm_proof_loss_dt, cm_relationship, "
        "cm_state_of_issue, cm_state_of_res, cm_tax_status from default.aclaims_master",
        "queryHistory": "",
        "key": "",
        "expression": "",
        "addDateColumn": False,
        "zeroFillNull": False,
        "replaceNulls": "",
        "stringMode": False,
        "operator": "=",
        "dateColumn": "",
        "transform": "",
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
        "lib": "/opt/owl/drivers/athena/",
        "additionalLib": "",
        "driverName": "com.simba.athena.jdbc.Driver",
        "connectionName": CONNECTION,
        "connectionUrl": "",
        "userName": "AKIAQM6KV6N2QDIGYVHZ",
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
        "escapeCharacter": "",
        "hasHeader": True,
    },
    "outliers": [
        {
            "id": 18,
            "on": True,
            "only": False,
            "lookback": 5,
            "key": [
                "cm_medicare_number",
            ],
            "include": [
                "cm_bdos",
                "cm_claim_status",
                "cm_claimant_age",
                "cm_claimant_bdate",
                "cm_claimant_sex",
                "cm_conversion_date",
                "cm_date_claim_paid",
                "cm_date_received",
                "cm_denied_reason1",
                "cm_denied_reason2",
                "cm_diagnosis_code",
                "cm_disab_days",
                "cm_doc_origin_dsc",
                "cm_edos",
                "cm_eff_date_family",
                "cm_end_treatmn_dte",
                "cm_fica_date",
                "cm_group_number",
                "cm_hospital_days",
                "cm_lob",
                "cm_medicare_number",
                "cm_pending_flag1",
                "cm_pending_flag2",
                "cm_pending_flag3",
                "cm_pending_flag4",
                "cm_proof_loss_dt",
                "cm_relationship",
                "cm_state_of_issue",
                "cm_state_of_res",
                "cm_tax_status",
            ],
            "exclude": None,
            "dateColumn": None,
            "timeColumn": None,
            "timeBin": "DAY",
            "timeBinQuery": "",
            "categorical": False,
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
    ],
    "outlier": {
        "id": None,
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
        "connectionName": "",
        "maxConnections": 10,
        "sourceQuery": "",
        "backRuns": 0,
        "backRunBin": "DAY",
        "dateFormatType": "DATE",
        "threads": 5,
        "manualSourceQuery": False,
        "key": "",
    },
    "profile": {
        "dataset": OUTLIERS_NO_DC_DATASET,
        "on": True,
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
        "adaptiveTier": None,
        "profileStringLength": False,
        "dataConceptId": None,
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
        "validateValuesShowAll": False,
        "validateValuesIgnoreNull": False,
        "validateValuesIgnoreEmpty": False,
        "validateValuesTrim": False,
        "validateValuesShowMissingKeys": False,
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
        "dataset": OUTLIERS_NO_DC_DATASET,
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
        "connectionList": [],
    },
    "spark": {
        "dataset": OUTLIERS_NO_DC_DATASET,
        "numExecutors": 1,
        "driverMemory": "1g",
        "executorMemory": "1g",
        "executorCores": 2,
        "conf": "spark.executor.memoryOverhead=1g",
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
        "jdbcPrincipal": "",
        "jdbcKeyTab": "",
    },
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
