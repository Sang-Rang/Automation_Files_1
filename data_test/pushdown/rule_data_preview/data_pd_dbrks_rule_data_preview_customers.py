from payloads.pushdown.rule_data_preview.pl_pd_dbrks_rule_data_preview_customers import (
    PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
)

PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME = "FF_two_column"

PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_DEFINITIONS = [
    {
        "dataset": PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
        "ruleNm": PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": "SELECT auto_year, auto_make FROM public.customers "
                     "WHERE auto_year = 2004 AND auto_make = 'Honda'",
        "points": 1,
        "ruleRepo": "",
        "perc": 1,
        "columnName": None,
        "businessCategory": "",
        "businessDesc": "",
        "dimId": "",
        "previewLimit": 6,
        "runTimeLimit": 30,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_DATASET,
            "runId": "2024-11-03T00:00:00.000+0000",
            "ruleNm": PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": "SELECT auto_year, auto_make FROM public.customers "
                         "WHERE auto_year = 2004 AND auto_make = 'Honda'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.28735632183908044,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1589712,
                "uuid": "e5663547-bb3a-44e4-9297-2b8a34d6f51a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT auto_year, auto_make FROM public.customers "
                             "WHERE auto_year = 2004 AND auto_make = 'Honda'",
            "totalCount": 1044,
            "rowsBreaking": 3,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_DBRKS_RULE_DATA_PREVIEW_CUSTOMERS_EXP_PREVIEW = {
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
