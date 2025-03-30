from payloads.pushdown.rules.pl_pd_trino_rules_temporal_sales import (
    PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
)

PD_TRINO_RULES_TEMPORAL_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
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

PD_TRINO_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29 = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-29T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586115,
                "uuid": "d8cca52c-ae29-49dc-ad76-800909416c22"
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

PD_TRINO_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30 = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-30T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586116,
                "uuid": "8be8dc31-d828-4b8e-8382-11db2491e384"
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

PD_TRINO_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01 = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-01T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales "
                         "where trdate = TIMESTAMP '2022-05-01') WHERE 0 <> 2",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586117,
                "uuid": "aec44c8a-99cc-4994-b10f-284d4699adef"
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

PD_TRINO_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02 = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-02T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM @dataset WHERE @t1.$rowCount <> @dataset.$rowCount",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586118,
                "uuid": "21c9756c-e526-4272-b30c-d821146bec04"
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
