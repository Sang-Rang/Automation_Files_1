import copy
from datetime import datetime

DS_DEF_DGC_ALL_FEATURES_ON_NAME = "AUTO_DQ_DGC_ALL_FEATURES_ON_" + datetime.now().strftime(
    "%Y%m%d%H%M%S"
)
DS_DEF_DGC_ALL_FEATURES_ON = {
    "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
    "runId": "2022-01-07",
    "runIdEnd": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "jobDescription": "",
    "jobId": None,
    "coreMaxActiveConnections": None,
    "linkId": [
        "firstname"
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
    "host": "10.64.2.3:5432/dqqa?currentSchema=automation",
    "port": "5432/dqqa?currentSchema=automation",
    "user": "misha",
    "alertEmail": None,
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {
        "id": 6,
        "uuid": "8eb1f6a8-70ab-4285-a903-b587523ae61e"
    },
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select * from samples.sales_data where date = '${rd}'",
        "queryHistory": "",
        "key": "salesid",
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
        "ruleSerial": False
    },
    "pushdown": {
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
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
        "sqlLoggingToggle": True
    },
    "outliers": [
        {
            "id": 158,
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "only": False,
            "lookback": 5,
            "key": [
                "dailyid"
            ],
            "include": [
                "salesid",
                "firstname",
                "lastname",
                "email"
            ],
            "exclude": [
                "date",
                "time",
                "dailyid",
                "vendor",
                "cost",
                "costcode",
                "cost_desc",
                "rep",
                "salestate",
                "tax",
                "lost_column"
            ],
            "dateColumn": "date",
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
            "categoricalAlgorithmParameters": {}
        }
    ],
    "patterns": [
        {
            "id": 14,
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "only": False,
            "lookback": 5,
            "key": [
                "salestate"
            ],
            "dateColumn": None,
            "include": [
                "tax"
            ],
            "exclude": [
                "salesid",
                "date",
                "time",
                "dailyid",
                "firstname",
                "lastname",
                "email",
                "vendor",
                "cost",
                "costcode",
                "cost_desc",
                "rep",
                "salestate",
                "lost_column"
            ],
            "score": 1,
            "minSupport": 0.000033,
            "confidence": 0.6,
            "limit": 30,
            "query": "",
            "on": True,
            "filter": None,
            "timeBin": "DAY"
        }
    ],
    "dupe": {
        "on": True,
        "only": False,
        "include": [
            "firstname",
            "lastname",
            "email"
        ],
        "exclude": None,
        "depth": 2,
        "lowerBound": 95,
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
        "on": True,
        "only": False,
        "include": [
            "salesid",
            "date",
            "time",
            "dailyid",
            "firstname",
            "lastname",
            "email",
            "vendor",
            "cost",
            "costcode",
            "cost_desc",
            "rep",
            "salestate",
            "tax",
            "lost_column"
        ],
        "exclude": [],
        "correlation": True,
        "histogram": True,
        "semantic": None,
        "dataConceptId": None,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1,
        "shape": True,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 0,
        "shapeMaxColSize": 0,
        "shapeGranular": True,
        "behavioralDimension": "",
        "behavioralDimensionGroup": "",
        "behavioralValueColumn": "",
        "behaviorScoreOff": False,
        "behaviorLookback": 16,
        "behaviorMinSupport": 3,
        "profilePushDown": None,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": True,
        "behaviorMaxValueCheck": True,
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
        "filter": ""
    },
    "source": {
        "on": True,
        "only": False,
        "validateValues": True,
        "key": None,
        "include": [
            "cost",
            "cost_desc",
            "costcode",
            "dailyid",
            "date",
            "email",
            "firstname",
            "lastname",
            "lost_column",
            "rep",
            "salesid",
            "salestate",
            "tax",
            "time",
            "vendor"
        ],
        "exclude": None,
        "includeSrc": None,
        "excludeSrc": None,
        "map": {
            "date": "date",
            "cost_desc": "cost_desc",
            "firstname": "firstname",
            "cost": "cost",
            "tax": "tax",
            "costcode": "costcode",
            "lastname": "lastname",
            "salesid": "salesid",
            "vendor": "vendor",
            "lost_column": "lost_column",
            "dailyid": "dailyid",
            "time": "time",
            "rep": "rep",
            "email": "email",
            "salestate": "salestate"
        },
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
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
        "driverName": "org.postgresql.Driver",
        "user": "owluser",
        "password": "",
        "passwordManager": None,
        "connectionName": "APPROVED_POSTGRES_UP",
        "connectionUrl": "jdbc:postgresql://35.190.143.55:5432/postgres?cs=test&test=test&t2=t2",
        "query": "select salesid,date,time,dailyid,firstname,lastname,email,cost,costcode,"
        "cost_desc,rep,salestate,tax,lost_column from samples.sales_data "
        "where date = '${rd}' limit 10",
        "lib": "/opt/owl/drivers/postgres/",
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
        "connectionList": []
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
        "files": None
    },
    "env": {
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
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
    "pipeline": [],
    "metaTags": [],
    "outlierConfiguration": {
        "only": False,
        "lookback": 5,
        "dateColumn": "date",
        "timeBin": "DAY",
        "by": None,
        "q1": 0.15,
        "q3": 0.85,
        "categorical": True,
        "columnSensitivitySettings": [
            {
                "name": "date",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "cost_desc",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "firstname",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "cost",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "tax",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "costcode",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "lastname",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "salesid",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "vendor",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "lost_column",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "dailyid",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "time",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "rep",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "email",
                "weight": 1,
                "unit": "DEFAULT"
            },
            {
                "name": "salestate",
                "weight": 1,
                "unit": "DEFAULT"
            }
        ],
        "configurations": [
            {
                "id": 158,
                "key": [
                    "dailyid"
                ],
                "include": [
                    "salesid",
                    "firstname",
                    "lastname",
                    "email"
                ],
                "exclude": [
                    "date",
                    "time",
                    "dailyid",
                    "vendor",
                    "cost",
                    "costcode",
                    "cost_desc",
                    "rep",
                    "salestate",
                    "tax",
                    "lost_column"
                ],
                "timeColumn": None,
                "timeBinQuery": "",
                "limit": 300,
                "minHistory": 3,
                "historyLimit": 5,
                "score": 1,
                "aggFunc": "",
                "aggQuery": "",
                "query": "",
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
                "categoricalAlgorithmParameters": {}
            }
        ]
    },
    "shape": {
        "enabled": True,
        "totalScore": 0,
        "sensitivity": 0,
        "maxPerCol": 0,
        "maxColSize": 0,
        "granular": True,
        "columnSettings": [
            {
                "enabled": True,
                "name": "cost",
                "type": "Decimal"
            },
            {
                "enabled": True,
                "name": "cost_desc",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "costcode",
                "type": "String, Double"
            },
            {
                "enabled": True,
                "name": "dailyid",
                "type": "Long, String, Int"
            },
            {
                "enabled": True,
                "name": "date",
                "type": "Date"
            },
            {
                "enabled": True,
                "name": "email",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "firstname",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "lastname",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "lost_column",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "rep",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "salesid",
                "type": "Int"
            },
            {
                "enabled": True,
                "name": "salestate",
                "type": "String"
            },
            {
                "enabled": True,
                "name": "tax",
                "type": "Decimal"
            },
            {
                "enabled": True,
                "name": "time",
                "type": "Timestamp"
            },
            {
                "enabled": True,
                "name": "vendor",
                "type": "String"
            }
        ]
    },
    "jobSchedule": None,
    "connectionType": "PULLUP"
}

DS_DEF_DGC_ALL_FEATURES_NAME = "AUTO_DQ_DGC_ALL_FEATURES_ON_"
DS_DEF_DGC_ALL_FEATURES_SECONDARY = copy.deepcopy(DS_DEF_DGC_ALL_FEATURES_ON)
DS_DEF_DGC_ALL_FEATURES_SECONDARY["load"]["query"] = (
    "select salesid,date,time,dailyid,firstname,lastname,email,cost,costcode,cost_desc,rep,"
    "salestate,tax,lost_column from samples.sales_data where date = '${rd}'"
)
