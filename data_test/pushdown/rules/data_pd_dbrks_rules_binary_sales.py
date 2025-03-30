from payloads.pushdown.rules.pl_pd_dbrks_rules_binary_sales import (
    PD_DBRKS_RULES_BINARY_SALES_DATASET,
)

PD_DBRKS_RULES_BINARY_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_DBRKS_RULES_BINARY_SALES_DATASET,
        "ruleNm": "binary_rule_all_table_rows",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM public.sales",
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
        "filterQuery": "",
        "tolerance": 0,
        "active": True
    }
]

PD_DBRKS_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_DBRKS_RULES_BINARY_SALES_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "binary_rule_all_table_rows",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales",
            "filterQuery": "",
            "score": 100,
            "perc": 1.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585965,
                "uuid": "7423d44a-5a2e-4719-9ef1-06220663d759"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
