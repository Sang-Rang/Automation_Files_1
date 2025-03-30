from utils.constants import \
    BASE_CREDS, PROD_AGENT_ID, PROD_AGENT_UUID, \
    PROD_HOST, PROD_PORT, PROD_RUN_ID

PULLUP_DUPE_CASE_INSENSITIVE_CONNECTION = "APPROVED_BIGQUERY_KEY"
PULLUP_DUPE_CASE_INSENSITIVE_DATASET = "AUTO_DUPE_CASEINSENSITIVE"
USER = BASE_CREDS["username"]

PULLUP_DUPE_CASE_INSENSITIVE_PAYLOAD = {
    "dataset": PULLUP_DUPE_CASE_INSENSITIVE_DATASET,
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
    "datasetSafeOff": True,
    "obslimit": 300,
    "pgUser": "",
    "pgPassword": "",
    "host": PROD_HOST,
    "port": PROD_PORT,
    "user": USER,
    "alertEmail": None,
    "scheduleTime": None,
    "schemaScore": 1,
    "optionAppend": "",
    "keyDelimiter": "~~",
    "agentId": {
        "id": PROD_AGENT_ID,
        "uuid": PROD_AGENT_UUID
    },
    "load": {
        "readonly": False,
        "passwordManager": None,
        "alias": "",
        "query": "select * from samples.JP_DUPLICATE_DATA_CASE_SENSITIVE",
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
        "lib": "/opt/owl/drivers/bigquery/core/",
        "additionalLib": "",
        "driverName": "com.simba.googlebigquery.jdbc42.Driver",
        "connectionName": "APPROVED_BIGQUERY_KEY",
        "connectionUrl": "jdbc:bigquery://https://www.googleapis.com/bigquery/v2:443;"
                         "ProjectId=owl-hadoop-cdh;OAuthType=0;OAuthServiceAcctEmail="
                         "1096839723485-compute@developer.gserviceaccount.com;OAuthPvt"
                         "KeyPath=/tmp/keytab/bigquery.json;Timeout=86400",
        "userName": "admin",
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
        "archiveBreakRecords": False,
        "archiveConnection": "",
        "coreFetchMode": False
    },
    "pushdown": {
        "dataset": PULLUP_DUPE_CASE_INSENSITIVE_DATASET,
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
    "outliers": [],
    "patterns": [],
    "dupe": {
        "on": True,
        "only": False,
        "include": [
            "gender"
        ],
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
        "include": [
            "id",
            "first_name",
            "last_name",
            "email",
            "gender"
        ],
        "exclude": [],
        "shape": True,
        "correlation": None,
        "histogram": None,
        "semantic": None,
        "dataConceptId": None,
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
        "profileStringLength": False,
        "detectStringNumerics": True,
        "detectTopnBotn": True,
        "detectScalePrecision": True,
        "adaptiveTier": None,
        "advancedTier": None
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
        "driverMemory": "2g",
        "executorMemory": "2g",
        "executorCores": 1,
        "conf": "spark.kubernetes.memoryOverheadFactor=0.4,spark.kubernetes.executor."
                "podTemplateFile=local:///opt/owl/config/k8s-executor-template.yml,spark."
                "kubernetes.driver.podTemplateFile=local:///opt/owl/config/k8s-driver-template.yml",
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
        "dataset": PULLUP_DUPE_CASE_INSENSITIVE_DATASET,
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
    "streamDefDTO": None,
    "pipeline": []
}
