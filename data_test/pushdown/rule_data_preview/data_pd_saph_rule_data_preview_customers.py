from payloads.pushdown.rule_data_preview.pl_pd_saph_rule_data_preview_customers import (
    PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
)

PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME = "FF_two_column"

PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
        "ruleNm": PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT AUTO_YEAR, AUTO_MAKE "
                     f"FROM @{PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
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

PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            "runId": "2024-11-03T00:00:00.000+0000",
            "ruleNm": PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": "SELECT AUTO_YEAR, AUTO_MAKE FROM (select * from TEST.CUSTOMERS) "
                         "WHERE AUTO_YEAR = 2004 AND AUTO_MAKE = 'Honda'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.28735632183908044,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1589714,
                "uuid": "82dcdf66-b6d1-410d-93ae-2939d1e9a6ab"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT AUTO_YEAR, AUTO_MAKE "
                             f"FROM @{PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
                             f"WHERE AUTO_YEAR = 2004 AND AUTO_MAKE = 'Honda'",
            "totalCount": 1044,
            "rowsBreaking": 3,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW = {
    "draw": 1,
    "recordsTotal": 3,
    "recordsFiltered": 3,
    "dataAssetList": [
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004",
        },
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004",
        },
        {
            "AUTO_MAKE": "Honda",
            "AUTO_YEAR": "2004",
        }
    ],
    "data": None
}
