from payloads.pushdown.rules.pl_pd_mssql_rules_nyse import PD_MSSQL_RULES_NYSE_DATASET

PD_MSSQL_RULES_NYSE_RULE_DEFINITIONS = [
    {
        "dataset": PD_MSSQL_RULES_NYSE_DATASET,
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
        "dataset": PD_MSSQL_RULES_NYSE_DATASET,
        "ruleNm": "ff_stat_rule_column_mean",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM dbo.nyse WHERE close.$mean > 125",
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

PD_MSSQL_RULES_NYSE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "simple_stat_rule_column_mean",
            "ruleType": "SQLG",
            "ruleValue": "139 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586079,
                "uuid": "d31ec6f5-d5fe-4097-85a3-d6f4db327ed1"
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
            "dataset": PD_MSSQL_RULES_NYSE_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "ff_stat_rule_column_mean",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.nyse WHERE 139 > 125",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586078,
                "uuid": "4512f8a9-45d1-4a38-9478-36f28f6f036d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.nyse WHERE close.$mean > 125",
            "totalCount": 102817,
            "rowsBreaking": 102817,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
