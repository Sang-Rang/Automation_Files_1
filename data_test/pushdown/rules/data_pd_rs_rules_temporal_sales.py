from payloads.pushdown.rules.pl_pd_rs_rules_temporal_sales import (
    PD_RS_RULES_TEMPORAL_SALES_DATASET,
)

PD_RS_RULES_TEMPORAL_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_RS_RULES_TEMPORAL_SALES_DATASET,
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

PD_RS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_29 = {
    "data": [
        {
            "dataset": PD_RS_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586009,
                "uuid": "3c285a85-23f8-4a3f-88f3-a3b489b209ce"
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

PD_RS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_04_30 = {
    "data": [
        {
            "dataset": PD_RS_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586010,
                "uuid": "7ed2ca45-8dd1-4ea8-8f7e-48309fb5b626"
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

PD_RS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_01 = {
    "data": [
        {
            "dataset": PD_RS_RULES_TEMPORAL_SALES_DATASET,
            "runId": "2022-05-01T00:00:00.000+0000",
            "ruleNm": "ff_t1_rowcount_comparison",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales2 "
                         "where trdate = '2022-05-01') WHERE 0 <> 2",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586011,
                "uuid": "6ae658a7-8421-4819-af3e-220eaefb43e3"
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

PD_RS_RULES_TEMPORAL_SALES_EXPECTED_RULE_OUTPUT_2022_05_02 = {
    "data": [
        {
            "dataset": PD_RS_RULES_TEMPORAL_SALES_DATASET,
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
                "id": 1586012,
                "uuid": "ee6342aa-4f9c-4214-834b-8e050141d6b8"
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
