from utils.constants import PROD_RUN_ID

PULLUP_RULES_BINARY_SALES_DATASET = "AUTO_PULLUP_RULES_BINARY_SALES"

PULLUP_RULES_BINARY_SALES_PAYLOAD = {
    "dataset": PULLUP_RULES_BINARY_SALES_DATASET,
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
    "host": "10.64.2.3:5432/dev?currentSchema=public",
    "port": None,
    "user": "anonymous : use -owluser",
    "alertEmail": "",
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {
        "id": 1,
        "uuid": "f736b2f6-a9ea-4c91-901b-1df25768cc9b"
    },
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select * from TEST.SALES where 0 = 1",
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
        "lib": "/opt/owl/drivers/sap/",
        "additionalLib": "",
        "driverName": "com.sap.db.jdbc.Driver",
        "connectionName": "APPROVED_SAPHANA_UP",
        "connectionUrl": "jdbc:sap://18.196.139.248:30015/",
        "userName": "gaberosenadmin",
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
        "dataset": PULLUP_RULES_BINARY_SALES_DATASET,
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
        "unionLookback": False,
        "unionLookbackMin": 5
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
        "shape": True,
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
        "profilePushDown": None,
        "behaviorRowCheck": False,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": False,
        "behaviorEmptyCheck": False,
        "behaviorUniqueCheck": False,
        "profileStringLength": False,
        "detectStringNumerics": True,
        "detectTopnBotn": True,
        "detectScalePrecision": True,
        "adaptiveTier": None,
        "advancedTier": None,
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
        "numExecutors": 1,
        "driverMemory": "1g",
        "executorMemory": "1g",
        "executorCores": 1,
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
        "dataset": PULLUP_RULES_BINARY_SALES_DATASET,
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
    "outlierConfiguration": None,
    "shape": {
        "enabled": True,
        "totalScore": 0,
        "sensitivity": 0,
        "maxPerCol": 20,
        "maxColSize": 12,
        "granular": None,
        "columnSettings": []
    },
    "jobSchedule": None,
    "connectionType": "PULLUP"
}
