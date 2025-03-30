# pylint: disable-msg=import-error
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
CONNECTION = "APPROVED_POSTGRES_UP"
QUERY = "select * from samples.nyse"

DATASET_RENAME = f"AUTO_DATASET_RENAME_{now}"
DATASET_BULK_DELETE1 = f"AUTO_DATASET_RENAME_{now}"
DATASET_BULK_DELETE2 = f"AUTO_DATASET_RENAME_{now}"
DS_BULK_1 = "AUTO_BULK_ACTIONS_1"
DS_BULK_2 = "AUTO_BULK_ACTIONS_2"


PL_FILTER_DS = {
    "draw": 3,
    "start": 0,
    "length": 50,
    "filterColumn": "",
    "search[value]": DATASET_RENAME,
    "search[regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
}

# Searches for dataset name and column name
PL_FILTER_COL = {
    "draw": 4,
    "start": 0,
    "length": 50,
    "search[value]": DATASET_RENAME,
    "filterColumn": "exch",
    "search[regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
}

# Filters for: Run Mode = Draft, Source Type awsathena, Row Count 1001 -
# 100000, Col Count 11-40
PL_FILTER_SOURCE_COUNTS = {
    "draw": 1,
    "start": 0,
    "length": 50,
    "search[value]": DATASET_RENAME,
    "filterColumn": "",
    "search[regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
    "filterRunMode": "draft",
    "filterSource": "Postgres",
    "filterRowCountOptions": "1m",
    "filterColumnCountOptions": "0_10",
}

PL_FILTER_BULK_DELETE1 = {
    "draw": 4,
    "start": 0,
    "length": 50,
    "search[value]": DATASET_BULK_DELETE1,
    "filterColumn": "",
    "search[regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
}
PL_FILTER_BULK_DELETE2 = {
    "draw": 4,
    "start": 0,
    "length": 50,
    "search[value]": DATASET_BULK_DELETE2,
    "filterColumn": "",
    "search[regex]": False,
    "order[0][column]": 0,
    "order[0][dir]": "asc",
}

PL_UPDATE_METADATA = {
    "dataset": DS_BULK_1,
    "col": "volume",
    "semantic": "CELSIUS",  # Data Class
    "sensitivity": -1,  # Sensitive Label
}

PL_FILTER_MULTI = {
    "draw": "11",
    "start": "0",
    "length": "50",
    "search[value]": "",
    "filterColumn": "",
    "search[regex]": False,
    "order[0][column]": "1",
    "order[0][dir]": "asc",
    "filterSensitivity": "-1",  # Sensitivity, out of the box
    "filterRunMode": "draft",
    "filterSource": "Postgres",
    "filterSemantic": "CELSIUS",  # Data Class, out of the box
    "filterBusinessUnits": "1",
    "filterDataConcepts": "-1",  # Data Category, out of the box
    "filterRowCountOptions": "1m",
    "filterColumnCountOptions": "0_10",
    "filterIntegrations": "",
    "filterDqScanCountOptions": "",
}

# Data class (DC) and sensitive label (SL) test
# ---------------------------------------
FIELD1_DC_SL = "open"
FIELD2_DC_SL = "close"
PL_DC_SL = {
    "catalogRows": [
        {"dataset": DS_BULK_2, "colNm": FIELD1_DC_SL},
        {"dataset": DS_BULK_2, "colNm": FIELD2_DC_SL},
    ],
    "idToUpdate": None,  # Updated in test
}

PL_DC_SEARCH = {
    "draw": 9,
    "start": 0,
    "length": 300,
    "search[value]": DS_BULK_2,
    "order[0][column]": "updtTs",
    "order[0][dir]": "desc",
}
