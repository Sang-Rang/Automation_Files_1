from datetime import datetime
# pylint: disable-msg=import-error
from utils.constants import PROD_RUN_ID

# Setup
NOW = datetime.now().strftime("%Y%m%d%H%M%S")
DATASET_SETTINGS_PERSIST = (
    "AUTO_POSTGRES_BEHAVIOR_SETTINGS_PERSIST"
    + NOW
)
CONNECTION_SETTINGS_PERSIST = "APPROVED_POSTGRES_UP"
QUERY_SETTINGS_PERSIST = "select * from public.nyse"
EXP_RULES_SETTINGS_PERSIST = 47

PL_GENERAL_SETTINGS_PERSIST = {
    "dataset": DATASET_SETTINGS_PERSIST,
    "runDate": PROD_RUN_ID,
    "runId": PROD_RUN_ID
}

# There are multiples of each by default,
# so using index to ensure test references the correct one
INDEX_STRICT_SETTINGS_PERSIST = 1
INDEX_ISMANUAL_SETTINGS_PERSIST = 2
INDEX_LENIENT_SETTINGS_PERSIST = 3
INDEX_SUPPRESS_SETTINGS_PERSIST = 4

PL_MANUAL_SETTINGS_PERSIST = {
    "dataset": DATASET_SETTINGS_PERSIST,
    "runId": PROD_RUN_ID,
    "item": "open",
    "metricType": "DATA_TYPE",
    "suppress": 0,
    "score": 0,
    "lbAbsVal": 8,
    "ubAbsVal": 10,
}

PL_STRICT_SETTINGS_PERSIST = {
    "dataset": DATASET_SETTINGS_PERSIST,
    "runId": PROD_RUN_ID,
    "item": "close",
    "metricType": "EMPTY",
    "suppress": 0,
    "adaptiveTier": "NARROW",
    "lbAbs": 0.0,
    "ubAbs": 3.0,
}

PL_LENIENT_SETTINGS_PERSIST = {
    "dataset": DATASET_SETTINGS_PERSIST,
    "runId": PROD_RUN_ID,
    "item": "exch",
    "metricType": "DATA_TYPE",
    "suppress": 0,
    "adaptiveTier": "WIDE",
    "lbAbs": -40.0,
    "ubAbs": 40.0,
}

PL_SUPPRESS_SETTINGS_PERSIST = {
    "dataset": DATASET_SETTINGS_PERSIST,
    "runId": PROD_RUN_ID,  # Will update later
    "item": "high",
    "metricType": "MAX VALUE",
    "suppress": "1",
    "lbAbs": 0.0,
    "ubAbs": 0.0,
}
EXP_SUPPRESS_LBABS = 0
EXP_SUPPRESS_UBABS = 0
EXP_SUPPRESS_STATUS = "Suppressed"
