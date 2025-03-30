from payloads.pushdown.rules.pl_pd_sf_rules_temporal_sales import PD_SF_RULES_TEMPORAL_SALES_DATASET

PD_SF_RULES_TEMPORAL_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_SF_RULES_TEMPORAL_SALES_DATASET,
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

PD_SF_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29 = {
    "data": [
        {
            "dataset": PD_SF_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586065,
                "uuid": "3125b169-7bba-4528-8987-ffeed80cfdee"
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

PD_SF_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30 = {
    "data": [
        {
            "dataset": PD_SF_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586066,
                "uuid": "3de828ad-3c21-4236-bf3f-a77d3481ecd2"
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

PD_SF_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01 = {
    "data": [
        {
            "dataset": PD_SF_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-01T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES "
                         "where \"TRDATE\" = '2022-05-01') WHERE 0 <> 2",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586067,
                "uuid": "8ef30ebc-3940-46d8-8aef-6b42580e817c"
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

PD_SF_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02 = {
    "data": [
        {
            "dataset": PD_SF_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586068,
                "uuid": "137b4a7b-e606-47eb-abe9-c5f5e951cd32"
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
