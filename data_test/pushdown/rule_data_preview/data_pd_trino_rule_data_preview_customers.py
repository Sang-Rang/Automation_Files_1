from payloads.pushdown.rule_data_preview.pl_pd_trino_rule_data_preview_customers import (
    PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_DATASET
)

PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME = "FF_two_column"

PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
        "ruleNm": PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT auto_year, auto_make "
                     f"FROM @{PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
                     f"WHERE auto_year = 2004 AND auto_make = 'Honda'",
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

PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            "runId": "2024-11-03T00:00:00.000+0000",
            "ruleNm": PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": "SELECT auto_year, auto_make FROM (select * from public.customers) "
                         "WHERE auto_year = 2004 AND auto_make = 'Honda'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.28735632183908044,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1589717,
                "uuid": "d1b24388-1785-457b-84f8-6871952e4d72"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT auto_year, auto_make "
                             f"FROM @{PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_DATASET} "
                             f"WHERE auto_year = 2004 AND auto_make = 'Honda'",
            "totalCount": 1044,
            "rowsBreaking": 3,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_TRINO_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW = {
    "draw": 1,
    "recordsTotal": 3,
    "recordsFiltered": 3,
    "dataAssetList": [
        {
            "auto_make": "Honda",
            "auto_year": "2004",
        },
        {
            "auto_make": "Honda",
            "auto_year": "2004",
        },
        {
            "auto_make": "Honda",
            "auto_year": "2004",
        }
    ],
    "data": None
}
