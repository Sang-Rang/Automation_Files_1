from payloads.pushdown.rules.pl_pd_saph_rules_nyse import PD_SAPH_RULES_NYSE_DATASET

PD_SAPH_RULES_NYSE_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULES_NYSE_DATASET,
        "ruleNm": "simple_stat_rule_column_mean",
        "ruleType": "SQLG",
        "ruleValue": "CLOSE.$mean > 125",
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
    },
    {
        "dataset": PD_SAPH_RULES_NYSE_DATASET,
        "ruleNm": "ff_stat_rule_column_mean",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_NYSE_DATASET} WHERE CLOSE.$mean > 125",
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

PD_SAPH_RULES_NYSE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "simple_stat_rule_column_mean",
            "ruleType": "SQLG",
            "ruleValue": "139.74491982 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586026,
                "uuid": "6b591245-3440-4be1-aeae-bb001ede0480"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "CLOSE.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "ff_stat_rule_column_mean",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.NYSE) WHERE 139.74491982 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586025,
                "uuid": "9a7d19b4-c474-4f80-95a2-5c69ec3cc41a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_NYSE_DATASET} WHERE CLOSE.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
