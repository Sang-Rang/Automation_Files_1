from payloads.pushdown.rules.pl_pd_trino_rules_nyse import PD_TRINO_RULES_NYSE_DATASET

PD_TRINO_RULES_NYSE_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULES_NYSE_DATASET,
        "ruleNm": "simple_stat_rule_column_mean",
        "ruleType": "SQLG",
        "ruleValue": "close.$mean > 125",
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
        "dataset": PD_TRINO_RULES_NYSE_DATASET,
        "ruleNm": "ff_stat_rule_column_mean",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULES_NYSE_DATASET} WHERE close.$mean > 125",
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

PD_TRINO_RULES_NYSE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "simple_stat_rule_column_mean",
            "ruleType": "SQLG",
            "ruleValue": "139.744919821624828579 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586103,
                "uuid": "c3168622-ec4a-46ed-98a4-744c3793db29"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "close.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "ff_stat_rule_column_mean",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.nyse) "
                         "WHERE 139.744919821624828579 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586104,
                "uuid": "9dd38325-2a19-476a-bcbb-a7b82588d8ea"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_TRINO_RULES_NYSE_DATASET} "
                             f"WHERE close.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
