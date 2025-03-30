from payloads.pushdown.rules.pl_pd_mssql_rules_temporal_sales import (
    PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
)

PD_MSSQL_RULES_TEMPORAL_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
        "ruleNm": "ff_t1_rowcount_comparison",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM dbo.sales WHERE @t1.$rowCount <> @dataset.$rowCount",
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

PD_MSSQL_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29 = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-29T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE 0 <> 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586088,
                "uuid": "7860f14a-e4a5-4ab2-b14f-bb27d2d3830a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_MSSQL_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30 = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-04-30T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE 0 <> 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586089,
                "uuid": "63a91054-4bd2-42b4-8490-b4ee7885567f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 0,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_MSSQL_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01 = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-01T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE 0 <> 2",
            "filterQuery": None,
            "score": 500,
            "perc": 500.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586090,
                "uuid": "5c425536-ed88-4f2c-a4ce-0549613f4dad"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 2,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_MSSQL_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02 = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-02T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE 2 <> 2",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586091,
                "uuid": "85d25b42-0c81-4bff-ad5a-06a629dd9daf"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE @t1.$rowCount <> @dataset.$rowCount",
            "totalCount": 2,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
