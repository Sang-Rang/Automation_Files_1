from payloads.pushdown.rules.pl_pd_saph_rules_temporal_sales import (
    PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
)

PD_SAPH_RULES_TEMPORAL_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
        "ruleNm": "ff_t1_rowcount_comparison",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
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

PD_SAPH_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29 = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-29T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES where TRDATE = '2022-04-29') "
                         "WHERE 0 <> 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586037,
                "uuid": "f77a5dc9-53ea-496b-8475-ce4bfc719889"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30 = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-30T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES where TRDATE = '2022-04-30') "
                         "WHERE 0 <> 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586038,
                "uuid": "da0a9c33-c022-4729-aa33-b0cd225ae6f6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01 = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-01T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES where TRDATE = '2022-05-01') "
                         "WHERE 0 <> 2",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586039,
                "uuid": "3fcb4d6c-7545-43e9-95dc-7756091ff2c8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 2,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02 = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-02T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES where TRDATE = '2022-05-02') "
                         "WHERE 2 <> 2",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586040,
                "uuid": "9dc5ca5f-d28f-4a17-be6b-2bc4cb2594a4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 2,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
