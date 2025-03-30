from payloads.pushdown.rules.pl_pd_mssql_rules_binary_sales import (
    PD_MSSQL_RULES_BINARY_SALES_DATASET,
)

PD_MSSQL_RULES_BINARY_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_MSSQL_RULES_BINARY_SALES_DATASET,
        "ruleNm": "binary_rule_all_table_rows",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM dbo.sales",
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

PD_MSSQL_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_BINARY_SALES_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "binary_rule_all_table_rows",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales",
            "filterQuery": "",
            "score": 100,
            "perc": 1.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586077,
                "uuid": "485bb2ec-6f6a-4411-8b12-572d3554f828"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
