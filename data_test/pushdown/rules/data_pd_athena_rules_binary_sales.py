from payloads.pushdown.rules.pl_pd_athena_rules_binary_sales import (
    PD_ATHENA_RULES_BINARY_SALES_DATASET,
)

PD_ATHENA_RULES_BINARY_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_ATHENA_RULES_BINARY_SALES_DATASET,
        "ruleNm": "binary_rule_all_table_rows",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM default.sales",
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

PD_ATHENA_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_ATHENA_RULES_BINARY_SALES_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "binary_rule_all_table_rows",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM default.sales",
            "filterQuery": "",
            "score": 100,
            "perc": 1.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585908,
                "uuid": "48b6c099-cba4-4cd2-837c-40d72caf3cbb"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM default.sales",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
