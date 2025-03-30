from payloads.pullup.pl_pullup_rules_binary_sales import PULLUP_RULES_BINARY_SALES_DATASET

PULLUP_RULES_BINARY_SALES_RULE_DEFINITIONS = [
  {
    "dataset": PULLUP_RULES_BINARY_SALES_DATASET,
    "ruleNm": "binary_rule_all_table_rows",
    "ruleType": "NATIVE",
    "ruleValue": "SELECT * FROM TEST.SALES",
    "points": 1,
    "perc": 1,
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
    "runTimeLimit": 30,
    "scoringScheme": 0,
    "filterQuery": "",
    "tolerance": 0,
    "active": True
  }
]

PULLUP_RULES_BINARY_SALES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_BINARY_SALES_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "binary_rule_all_table_rows",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM TEST.SALES",
            "filterQuery": "",
            "score": 100,
            "perc": 1,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449789,
                "uuid": "46c1eaf4-6b68-4638-9402-416be094544f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM TEST.SALES",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
