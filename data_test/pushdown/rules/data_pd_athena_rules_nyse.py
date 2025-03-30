from payloads.pushdown.rules.pl_pd_athena_rules_nyse import PD_ATHENA_RULES_NYSE_DATASET

PD_ATHENA_RULES_NYSE_RULE_DEFINITIONS = [
    {
        "dataset": PD_ATHENA_RULES_NYSE_DATASET,
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
        "dataset": PD_ATHENA_RULES_NYSE_DATASET,
        "ruleNm": "ff_stat_rule_column_mean",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @AUTO_PD_ATHENA_RULES_NYSE WHERE close.$mean > 125",
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

PD_ATHENA_RULES_NYSE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_ATHENA_RULES_NYSE_DATASET,
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
                "id": 1585909,
                "uuid": "7b80ef7f-5aa8-4e9a-9b3f-7b0b86725950"
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
            "dataset": PD_ATHENA_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "ff_stat_rule_column_mean",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from default.nyse) "
                         "WHERE 139.744919821624828579 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585910,
                "uuid": "03d3ed1a-5d35-4328-b130-52d5b9d59b47"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_ATHENA_RULES_NYSE_DATASET} "
                             f"WHERE close.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
