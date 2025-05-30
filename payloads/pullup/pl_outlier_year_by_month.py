# pylint: disable-msg=import-error
from utils.constants import PROD_AGENT_UUID, PROD_AGENT_ID, PROD_HOST, PROD_PORT

CONN_OUTLIER_YEAR_BY_MONTH = "APPROVED_ORACLE_UP"
DS_OUTLIER_YEAR_BY_MONTH = "AUTO_OUTLIERS_YEAR_MONTH"
RUN_DATE_OUTLIER_YEAR_BY_MONTH = "2018-01-16"
RUN_DATE_OUTLIER_YEAR_BY_MONTH_FULL = f"{RUN_DATE_OUTLIER_YEAR_BY_MONTH}T00:00:00.000+0000"
QUERY_OUTLIER_YEAR_BY_MONTH = "select * from OWLUSER.NYSE where TRADE_DATE = '${rd}' limit 500"
COL_OUTLIER_YEAR_BY_MONTH = "TRADE_DATE"

DS_DEFS_OUTLIER_YEAR_BY_MONTH = {
    "dataset": DS_OUTLIER_YEAR_BY_MONTH,
    "runId": RUN_DATE_OUTLIER_YEAR_BY_MONTH,
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "hootOnly": False,
    "parallel": False,
    "plan": False,
    "dataPreviewOff": False,
    "datasetSafeOff": False,
    "obslimit": 300,
    "host": PROD_HOST,
    "port": PROD_PORT,
    "schemaScore": 1,
    "keyDelimiter": "~~",
    "agentId": {"id": PROD_AGENT_ID, "uuid": PROD_AGENT_UUID},
    "load": {
        "dataset": DS_OUTLIER_YEAR_BY_MONTH,
        "query": QUERY_OUTLIER_YEAR_BY_MONTH,
        "operator": "=",
        "dateColumn": COL_OUTLIER_YEAR_BY_MONTH,
        "sample": 1.0,
        "backRun": 0,
        "backRunBin": "DAY",
        "cache": True,
        "dateFormat": "yyyy-MM-dd",
        "timeFormat": "HH:mm:ss.SSS",
        "checkHeader": True,
        "inferSchema": True,
        "delimiter": ",",
        "fileCharSet": "UTF-8",
        "flatten": False,
        "handleMaps": False,
        "handleMixedJson": False,
        "multiLine": False,
        "lib": "/opt/owl/drivers/oracle",
        "driverName": "oracle.jdbc.OracleDriver",
        "connectionName": CONN_OUTLIER_YEAR_BY_MONTH,
        "connectionUrl": "jdbc:oracle:thin:@10.150.0.31:1521:OWL",
        "userName": "owluser",
        "useSql": True,
        "numPartitions": 0,
        "escapeWithBackTick": False,
        "escapeWithSingleQuote": False,
        "escapeWithDoubleQuote": False,
        "partitionNumber": 0,
        "archiveBreaks": False,
        "hasHeader": True,
    },
    "outliers": [
        {
            "id": 215,
            "on": True,
            "only": False,
            "lookback": 5,
            "key": ["SYMBOL"],
            "include": [
                "CLOSE",
                "EXCH",
                "HIGH",
                "LOW",
                "OPEN",
                "PART_DATE_STR",
                "SYMBOL",
                "TRADE_DATE",
                "VOLUME",
            ],
            "exclude": None,
            "dateColumn": "TRADE_DATE",
            "timeBin": "YEAR",
            "categorical": False,
            "by": "MONTH",
            "limit": 300,
            "minHistory": 3,
            "historyLimit": 5,
            "score": 1,
            "q1": 0.15,
            "q3": 0.85,
            "categoricalColumnConcatenation": False,
            "multiplierUpper": 1.35,
            "multiplierLower": 1.35,
            "record": True,
            "combine": True,
            "categoricalTopN": 3,
            "categoricalBottomN": 2,
            "categoricalMaxConfidence": 0.02,
            "categoricalMaxFrequencyPercentile": 0.25,
            "categoricalMinFrequency": 1,
            "categoricalMinVariance": 0,
            "categoricalMaxCategoryN": 1,
            "categoricalParallel": True,
        }
    ],
    "outlier": {
        "id": None,
        "on": False,
        "only": False,
        "lookback": 5,
        "timeBin": "DAY",
        "categorical": True,
        "limit": 300,
        "minHistory": 3,
        "historyLimit": 5,
        "score": 1,
        "q1": 0.15,
        "q3": 0.85,
        "categoricalColumnConcatenation": False,
        "multiplierUpper": 1.35,
        "multiplierLower": 1.35,
        "record": True,
        "combine": True,
        "categoricalTopN": 3,
        "categoricalBottomN": 2,
        "categoricalMaxConfidence": 0.02,
        "categoricalMaxFrequencyPercentile": 0.25,
        "categoricalMinFrequency": 1,
        "categoricalMinVariance": 0,
        "categoricalMaxCategoryN": 1,
        "categoricalParallel": True,
    },
    "profile": {
        "dataset": DS_OUTLIER_YEAR_BY_MONTH,
        "on": False,
        "only": False,
        "shape": True,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1.0,
        "shapeTotalScore": 0,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 0,
        "shapeMaxColSize": 0,
        "behaviorScoreOff": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "profileStringLength": False,
    },
    "rule": {
        "on": True,
        "only": False,
        "lib": None,
        "absoluteScoring": False,
        "ruleBreakPreviewLimit": 6,
    },
    "colMatch": {
        "dataset": DS_OUTLIER_YEAR_BY_MONTH,
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
    },
    "spark": {
        "dataset": DS_OUTLIER_YEAR_BY_MONTH,
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
    },
}
