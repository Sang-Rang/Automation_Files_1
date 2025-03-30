from utils.constants import PROD_RUN_ID

PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION = "APPROVED_SAPHANA_PUSHDOWN"
PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS"
)

PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD = {
    "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
    "runId": PROD_RUN_ID,
    "runIdEnd": "",
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
        "EMPLOYEE_ID",
        "EMAIL"
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
    "user": "anonymous : use -owluser",
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
        "ruleSerial": False
    },
    "pushdown": {
        "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "connectionName": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from TEST.EMPLOYEES",
        "backRuns": 0,
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
            "id": 2352,
            "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "only": False,
            "lookback": 5,
            "lookbackQuery": "",
            "key": None,
            "include": [
                "TIME_IN_SERVICE_YRS"
            ],
            "exclude": [
                "EMPLOYEE_ID",
                "FIRST_NAME",
                "LAST_NAME",
                "EMAIL",
                "GENDER",
                "CITY",
                "DEPARTMENT",
                "LATITUDE",
                "LONGITUDE",
                "HOME_PHONE",
                "POSTAL_CODE",
                "STATE",
                "STREET_ADDRESS",
                "DATE_OF_HIRE"
            ],
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
            "q1": 0.45,
            "q3": 0.55,
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
        "limit": 300
    },
    "profile": {
        "on": True,
        "only": False,
        "include": None,
        "exclude": None,
        "correlation": False,
        "histogram": False,
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
        "adaptiveTier": None,
        "advancedTier": False,
        "filter": ""
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
        "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
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
    "metaTags": None,
    "outlierConfiguration": {
        "columnSensitivitySettings": [],
        "configurations": [
            {
                "id": 2352,
                "dataset": "temDataset_0736eaa44da7498d9ed7722350abb361",
                "only": False,
                "lookback": 5,
                "lookbackQuery": "",
                "key": None,
                "include": [
                    "TIME_IN_SERVICE_YRS"
                ],
                "exclude": [
                    "EMPLOYEE_ID",
                    "FIRST_NAME",
                    "LAST_NAME",
                    "EMAIL",
                    "GENDER",
                    "CITY",
                    "DEPARTMENT",
                    "LATITUDE",
                    "LONGITUDE",
                    "HOME_PHONE",
                    "POSTAL_CODE",
                    "STATE",
                    "STREET_ADDRESS",
                    "DATE_OF_HIRE"
                ],
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
                "q1": 0.45,
                "q3": 0.55,
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
        "enabled": False,
        "totalScore": 0,
        "sensitivity": 0,
        "maxPerCol": 20,
        "maxColSize": 12,
        "granular": None,
        "columnSettings": []
    },
    "jobSchedule": None,
    "connectionType": "PUSHDOWN"
}
