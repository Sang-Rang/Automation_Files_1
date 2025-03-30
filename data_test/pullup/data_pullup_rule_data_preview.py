from payloads.pullup.pl_pullup_rule_data_preview_customers import (
    PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET
)
PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME = "FF_two_column"

PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
        "ruleNm": PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT AUTO_YEAR, AUTO_MAKE "
                     f"FROM @{PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
                     f"WHERE AUTO_YEAR = 2004 AND AUTO_MAKE = 'Honda'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            "runId": "2024-11-03T00:00:00.000+0000",
            "ruleNm": PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": f"SELECT AUTO_YEAR  ,   AUTO_MAKE "
                         f"FROM {PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET}_dataset "
                         f"WHERE AUTO_YEAR = 2004 AND AUTO_MAKE = 'Honda' ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.28735632076859474,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1589766,
                "uuid": "c0cf27be-4402-45e2-b52d-d67ef05f3f2e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT AUTO_YEAR, AUTO_MAKE "
                             f"FROM @{PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
                             f"WHERE AUTO_YEAR = 2004 AND AUTO_MAKE = 'Honda'",
            "totalCount": 1044,
            "rowsBreaking": 3,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

PULLUP_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW = {
    "draw": 1,
    "recordsTotal": 3,
    "recordsFiltered": 3,
    "dataAssetList": [
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004"
        },
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004"
        },
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004"
        }
    ],
    "data": None
}
