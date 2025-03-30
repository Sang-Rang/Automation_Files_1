from utils.constants import PROD_RUN_ID

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_DATASET = (
    "AUTO_PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER"
)

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/rc202308?currentSchema=validation",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [
        {
            "on": True,
            "categorical": False,
            "q1": "0.11",
            "q3": "0.89",
            "exclude": [
                "CM_BDOS",
                "CM_CLAIM_STATUS",
                "CM_CLAIMANT_AGE",
                "CM_CLAIMANT_BDATE",
                "CM_CLAIMANT_SEX",
                "CM_CONVERSION_DATE",
                "CM_DATE_CLAIM_PAID",
                "CM_DATE_RECEIVED",
                "CM_DENIED_REASON1",
                "CM_DENIED_REASON2",
                "CM_DIAGNOSIS_CODE",
                "CM_DOC_ORIGIN_DSC",
                "CM_EDOS",
                "CM_EFF_DATE_FAMILY",
                "CM_END_TREATMN_DTE",
                "CM_FICA_DATE",
                "CM_GROUP_NUMBER",
                "CM_HOSPITAL_DAYS",
                "CM_LOB",
                "CM_MEDICARE_NUMBER",
                "CM_PENDING_FLAG1",
                "CM_PENDING_FLAG2",
                "CM_PENDING_FLAG3",
                "CM_PENDING_FLAG4",
                "CM_PROOF_LOSS_DT",
                "CM_RELATIONSHIP",
                "CM_STATE_OF_ISSUE",
                "CM_STATE_OF_RES",
                "CM_TAX_STATUS"
            ],
            "include": [
                "CM_DISAB_DAYS"
            ]
        }
    ],
    "patterns": [],
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
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
        "profileStringLength": False,
        "shape": False,
        "shapeSensitivity": 0,
        "shapeMaxPerCol": 20,
        "shapeMaxColSize": 12,
        "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_DATASET,
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
        "connectionName": "APPROVED_DATABRICKS_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from public.aclaims_master",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "user": ""
}
