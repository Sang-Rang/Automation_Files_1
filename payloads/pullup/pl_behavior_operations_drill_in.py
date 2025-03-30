# pylint: disable-msg=import-error

from datetime import datetime
from utils.constants import PROD_AGENT_ID, PROD_AGENT_UUID, PROD_HOST

RULE_BREAK_RUN_ID_BROKEN_RULE = "2018-01-14T00:00:00.000+0000"
TRADE_DATE_START = "2018-01-16"
QUERY = "select * from public.nyse where trade_date = '${rd}' "  # RD required.
DATASET = "AUTO_POSTGRES_BEHAVIOR_INVALIDATE" + datetime.now().strftime(
    "%Y%m%d%H%M%S"
)

CONNECTION = "APPROVED_POSTGRES_UP"

PL_BEH_DETAILS = {
    "dataset": DATASET,
    "runId": RULE_BREAK_RUN_ID_BROKEN_RULE,
    "field": "Row Count",
    "issueType": "ROW_COUNT",
}

PL_BROKEN = {
    "dataset": DATASET,
    "runId": RULE_BREAK_RUN_ID_BROKEN_RULE,
    "sense": 3,
}

# Job Data
DATASET_DEFS = {
    "dataset": DATASET,
    "runId": TRADE_DATE_START,
    "runIdEnd": "",
    "runState": "DRAFT",
    "passFail": 1,
    "passFailLimit": 75,
    "obslimit": 300,
    "host": PROD_HOST,
    "schemaScore": 1,
    "keyDelimiter": "~~",
    "agentId": {"id": PROD_AGENT_ID, "uuid": PROD_AGENT_UUID},
    "load": {
        "dataset": DATASET,
        "query": QUERY,
        "dateColumn": "trade_date",
        "sample": 1,
        "backRun": 10,
        "backRunBin": "DAY",
        "unionLookBack": False,
        "dateFormat": "yyyy-MM-dd",
        "timeFormat": "HH:mm:ss.SSS",
        "delimiter": ",",
        "fileCharSet": "UTF-8",
        "lib": "/opt/owl/drivers/postgres/",
        "driverName": "org.postgresql.Driver",
        "connectionName": CONNECTION,
        "connectionUrl": "jdbc:postgresql://35.190.143.55:5432/"
        "postgres?cs=test&test=test&t2=t2",
        "userName": "owluser",
        "password": "",
        "useSql": True,
    },
    "outliers": [],
    "outlier": {
        "id": None,
        "on": False,
    },
    "pattern": {
        "id": None,
        "only": False,
        "timeBin": "DAY",
        "on": False,
    },
    "patterns": [],
    "dupe": {
        "dataset": None,
        "on": False,
    },
    "profile": {
        "dataset": DATASET,
        "on": False,
        "only": False,
        "include": None,
        "exclude": None,
        "shape": True,
        "limit": 300,
        "histogramLimit": 0,
        "score": 1,
        "behavioralDimension": "",
        "behavioralDimensionGroup": "",
        "behavioralValueColumn": "",
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
    },
    "source": {
        "on": False,
    },
    "rule": {
        "on": True,
        "only": False,
        "lib": None,
        "absoluteScoring": False,
        "ruleBreakPreviewLimit": 6,
    },
    "colMatch": {
        "dataset": DATASET,
        "colMatchParallelProcesses": 3,
        "colMatchDurationMins": 20,
        "colMatchBatchSize": 2,
        "level": "exact",
        "fuzzyDistance": 1,
        "connectionList": [],
    },
    "spark": {
        "dataset": DATASET,
        "numExecutors": 1,
        "driverMemory": "1g",
        "executorMemory": "2g",
        "executorCores": 1,
        "master": "k8s://",
        "deployMode": "cluster",
    },
    "record": {
        "on": False,
    },
}
