from utils.constants import PROD_RUN_ID

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_CONNECTION = "APPROVED_SQLSERVER_PUSHDOWN"
PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET = "AUTO_PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS"

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/dev?currentSchema=public",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
        "advancedTier": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": False,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": False,
        "behaviorEmptyCheck": False,
        "behaviorUniqueCheck": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "shape": False,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "histogram": False,
        "pushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "profilePushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "shapeGranular": None
    },
    "alertEmail": "",
    "pushdown": {
        "connectionName": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from dbo.sales",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": True,
        "sourceBreakShapes": False,
        "sourceBreakResults": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False,
        "dateFormatType": "DATE"
    },
    "linkId": [
        "name",
        "trdate"
    ],
    "user": "gaberosenadmin"
}
