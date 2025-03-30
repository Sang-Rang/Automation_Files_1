# pylint: disable-msg=import-error

from datetime import datetime
from utils.constants import BASE_CREDS, PROD_RUN_ID

UTCNOW = datetime.utcnow()
UTCNOW_UNIQUE = UTCNOW.strftime("%Y%m%d%H%M%S")  # Format: 20020102
UTCNOW_DATE = UTCNOW.strftime("%Y-%m-%d")  # Format: 2000-01-02
UTCNOW_DAY = UTCNOW.strftime("%a, %d-%b %-y")  # Format: Tue, 15-Aug 23
CONNECTION = "APPROVED_POSTGRES_UP"
DATASET = "AUTO_SECURITY_AUDIT" + UTCNOW_UNIQUE
DATASET_DS_AUDIT = "AUTO_DS_AUDIT" + UTCNOW_UNIQUE
DATASET_EDIT = "AUTO_SECURITY_AUDIT_" + UTCNOW_UNIQUE + "_edited2"
QUERY = "select * from samples.nyse"

PL_RENAME_DATASET = {"sourceDataset": DATASET, "targetDataset": DATASET_EDIT}
PL_BU_NAME = {"name": "AUTO_BU_" + UTCNOW_UNIQUE}
PL_SECURITY_DATA_ASSET = {
    "draw": 3,
    "start": 0,
    "length": 50,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
    "search[value]": DATASET,
}
PL_SECURITY_AUDIT_TRAIL = {
    "draw": 3,
    "start": 0,
    "length": 99999,
    "search[value]": DATASET,
    "order[0][column]": 4,
    "order[0][dir]": "desc",
}
PL_BU_TO_DATASET = {"business_unit_id": -1, "dataset": DATASET}  # Add later
PL_MANUAL_SETTINGS_PERSIST = {
    "dataset": DATASET_DS_AUDIT,
    "runId": PROD_RUN_ID,
    "item": "open",
    "metricType": "DATA_TYPE",
    "suppress": 0,
    "score": 0,
    "lbAbsVal": 8,
    "ubAbsVal": 10,
}
PL_STRICT_SETTINGS_PERSIST = {
    "dataset": DATASET_DS_AUDIT,
    "runId": PROD_RUN_ID,
    "item": "close",
    "metricType": "EMPTY",
    "suppress": 0,
    "adaptiveTier": "NARROW",
    "lbAbs": 0.0,
    "ubAbs": 3.0,
}
PL_LENIENT_SETTINGS_PERSIST = {
    "dataset": DATASET_DS_AUDIT,
    "runId": PROD_RUN_ID,
    "item": "exch",
    "metricType": "DATA_TYPE",
    "suppress": 0,
    "adaptiveTier": "WIDE",
    "lbAbs": -40.0,
    "ubAbs": 40.0,
}
PL_SUPPRESS_SETTINGS_PERSIST = {
    "dataset": DATASET_DS_AUDIT,
    "runId": PROD_RUN_ID,
    "item": "high",
    "metricType": "MAX VALUE",
    "suppress": "1",
    "lbAbs": 0.0,
    "ubAbs": 0.0,
}
PL_DS_AUDIT_TRAIL = {
    "draw": 3,
    "start": 0,
    "length": 99999,
    "search[value]": DATASET_DS_AUDIT,
    "order[0][column]": 4,
    "order[0][dir]": "desc",
}

EXP_SECURITY_AUDIT_STRINGS = [
    f"Updated user profile persona Id: {BASE_CREDS['username']} with values:"
    f"  Dataset: {DATASET}",
    f"User profiles updated where owned datasets contained '{DATASET}'."
    f" Replaced with '{DATASET_EDIT}'",
    f"Delete request for dataset: {DATASET}",
    f"Insert business unit to dataset: null for dataset: {DATASET}",
]
EXP_AUDIT_DS = {
    "draw": 3,
    "recordsTotal": 4232,
    "recordsFiltered": 4,
    "dataAssetList": [
        {
            "activityId": 0,
            "username": "",
            "dataset": "",
            "action": "BEHAVIOR",
            "changeDescription": f"Suppress:: runId: {PROD_RUN_ID}, Item: high, "
                                 f"MetricType: MAX VALUE, Retrain: true",
            "auditTs": UTCNOW_DATE,
            "auditTsStr": UTCNOW_DAY,
        },
        {
            "activityId": 0,
            "username": "",
            "dataset": "",
            "action": "BEHAVIOR",
            "changeDescription": f"Manual:: runId: {PROD_RUN_ID}, Item: open, "
                                 f"MetricType: DATA_TYPE, Lower Bound: 8.0, Upper Bound: 10.0, "
                                 f"Score: 0, Retrain: true",
            "auditTs": UTCNOW_DATE,
            "auditTsStr": UTCNOW_DAY,
        },
        {
            "activityId": 0,
            "username": "",
            "dataset": "",
            "action": "BEHAVIOR",
            "changeDescription": f"Adaptive:: runId: {PROD_RUN_ID}, Item: exch, "
                                 f"MetricType: DATA_TYPE, AdaptiveTier: WIDE, Retrain: true",
            "auditTs": UTCNOW_DATE,
            "auditTsStr": UTCNOW_DAY,
        },
        {
            "activityId": 0,
            "username": "",
            "dataset": "",
            "action": "BEHAVIOR",
            "changeDescription": f"Adaptive:: runId: {PROD_RUN_ID}, Item: close, MetricType: EMPTY,"
                                 f" AdaptiveTier: NARROW, Retrain: true",
            "auditTs": UTCNOW_DATE,
            "auditTsStr": UTCNOW_DAY,
        },
    ],
}
