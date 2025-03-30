from payloads.dq_dgc_integration.pl_dq_dgc_dataset_updates_in_dic_querie import (
    DS_DEF_DGC_DATASET_UPDATES_NAME,
)

POSTGRES_SCHEMA_NAME = "public"
POSTGRES_TABLE_NAME = "nyse"

DQ_DGC_RULES_DEFINITIONS = [
    {
        "dataset": DS_DEF_DGC_DATASET_UPDATES_NAME,
        "ruleNm": "simple_rule_example",
        "ruleType": "SQLG",
        "ruleValue": "close > 20",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "close",
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
        "dataset": DS_DEF_DGC_DATASET_UPDATES_NAME,
        "ruleNm": "open_less_than_10",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE open < 10",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "open",
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

DQ_DGC_RULES_EXPECTED_RESULT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_DATASET_UPDATES_NAME,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "simple_rule_example",
            "ruleType": "SQLG",
            "ruleValue": "close > 20",
            "filterQuery": None,
            "score": 61,
            "perc": 61.587315797805786,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 438153,
                "uuid": "f2494edb-e778-4136-b325-951b0f6fba6a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "close > 20",
            "totalCount": 102815,
            "rowsBreaking": 63321,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_DATASET_UPDATES_NAME,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "open_less_than_10",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_DATASET_UPDATES_NAME}_dataset "
                         f"WHERE open < 10 ",
            "filterQuery": None,
            "score": 14,
            "perc": 14.624325931072235,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 438154,
                "uuid": "7d3028f3-7c39-45e4-b4e4-119ba4d48527"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE open < 10",
            "totalCount": 102815,
            "rowsBreaking": 15036,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
