PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION = "APPROVED_BIGQUERY_PUSHDOWN"
PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS"
)

PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD = {
    "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
    "runId": "2023-01-10",
    "runIdEnd": "",
    "runDateAdjustment": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobDescription": "",
    "jobId": {
        "id": -1,
        "uuid": None
    },
    "coreMaxActiveConnections": None,
    "linkId": [
        "TRADE_DATE",
        "TRADE_ID"
    ],
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
    "host": "10.64.2.3:5432/dev?currentSchema=public",
    "port": None,
    "user": "rahul",
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {
        "id": 0,
        "uuid": None
    },
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "",
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
        "connectionProperties": {
        },
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
        "ruleSerial": False
    },
    "pushdown": {
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "connectionName": "APPROVED_BIGQUERY_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.MS_TRADE where TRADE_DATE = '${rd}'",
        "backRuns": 5,
        "backRunBin": "DAY",
        "dateFormatType": "DATE",
        "threads": 2,
        "manualSourceQuery": False,
        "key": "",
        "sourceOutputSchema": "",
        "sourceBreakRules": False,
        "sourceBreakOutliers": True,
        "sourceBreakDupes": False,
        "sourceBreakShapes": False,
        "sourceBreakResults": False,
        "sqlLoggingToggle": False,
        "unionLookback": False,
        "unionLookbackMin": 0
    },
    "outliers": [
        {
            "id": 2637,
            "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "only": False,
            "lookback": 5,
            "lookbackQuery": "",
            "key": None,
            "include": [
                "NON_ZERO_COMPUTED"
            ],
            "exclude": [
                "TRADE_DATE",
                "END_DATE",
                "TRADE_ID",
                "TRADE_VALUE",
                "NOTIONAL",
                "EXPOSURE",
                "DELTA_DAYS_COMPUTED",
                "VARIANCE_BUCKET_COMPUTED",
                "TEST_REASON"
            ],
            "dateColumn": "TRADE_DATE",
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
            "prevRunId": None,
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
            "categoricalAlgorithmParameters": {
            }
        }
    ],
    "patterns": [
    ],
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
        "limit": 300
    },
    "profile": {
        "on": False,
        "only": False,
        "dataConceptId": 300,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1,
        "shape": False,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "behavioralDimension": "",
        "behavioralDimensionGroup": "",
        "behavioralValueColumn": "",
        "behaviorScoreOff": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profilePushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "behaviorRowCheck": False,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": False,
        "behaviorEmptyCheck": False,
        "behaviorUniqueCheck": False,
        "profileStringLength": False,
        "detectStringNumerics": False,
        "detectTopnBotn": False,
        "detectScalePrecision": False,
        "advancedTier": False,
        "filter": "",
        "maskSensitive": False,
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "pushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "shapeGranular": None
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
        "connectionProperties": {
        },
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
        "filterCols": None
    },
    "rule": {
        "on": True,
        "only": False,
        "lib": None,
        "name": "",
        "absoluteScoring": False,
        "ruleBreakPreviewLimit": 6
    },
    "colMatch": {
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
        "connectionList": [
        ]
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
        "files": None
    },
    "env": {
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "jdbcPrincipal": "",
        "jdbcKeyTab": ""
    },
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
        "by": None
    },
    "stream": None,
    "pipeline": [
    ],
    "metaTags": [
    ],
    "outlierConfiguration": {
        "columnSensitivitySettings": [
            {
                "name": "TRADE_DATE",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "END_DATE",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "TRADE_ID",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "TRADE_VALUE",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "NOTIONAL",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "EXPOSURE",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "NON_ZERO_COMPUTED",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "DELTA_DAYS_COMPUTED",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "VARIANCE_BUCKET_COMPUTED",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "TEST_REASON",
                "weight": 1,
                "unit": "DEFAULT"
            }
        ],
        "configurations": [
            {
                "id": 2637,
                "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
                "only": False,
                "lookback": 5,
                "lookbackQuery": "",
                "key": None,
                "include": [
                    "NON_ZERO_COMPUTED"
                ],
                "exclude": [
                    "TRADE_DATE",
                    "END_DATE",
                    "TRADE_ID",
                    "TRADE_VALUE",
                    "NOTIONAL",
                    "EXPOSURE",
                    "DELTA_DAYS_COMPUTED",
                    "VARIANCE_BUCKET_COMPUTED",
                    "TEST_REASON"
                ],
                "dateColumn": "TRADE_DATE",
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
                "prevRunId": None,
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
                "categoricalAlgorithmParameters": {
                }
            }
        ]
    },
    "shape": {
        "enabled": False,
        "totalScore": 0,
        "sensitivity": 0,
        "maxPerCol": 20,
        "maxColSize": 12,
        "granular": None,
        "columnSettings": [
            {
                "enabled": False,
                "name": "DELTA_DAYS_COMPUTED",
                "type": "Long"
            },
            {
                "enabled": False,
                "name": "END_DATE",
                "type": "Date"
            },
            {
                "enabled": False,
                "name": "EXPOSURE",
                "type": "Long"
            },
            {
                "enabled": False,
                "name": "NON_ZERO_COMPUTED",
                "type": "String"
            },
            {
                "enabled": False,
                "name": "NOTIONAL",
                "type": "Long"
            },
            {
                "enabled": False,
                "name": "TEST_REASON",
                "type": "String"
            },
            {
                "enabled": False,
                "name": "TRADE_DATE",
                "type": "Date"
            },
            {
                "enabled": False,
                "name": "TRADE_ID",
                "type": "String"
            },
            {
                "enabled": False,
                "name": "TRADE_VALUE",
                "type": "Decimal"
            },
            {
                "enabled": False,
                "name": "VARIANCE_BUCKET_COMPUTED",
                "type": "String"
            }
        ]
    },
    "jobSchedule": None,
    "connectionType": "PUSHDOWN"
}
