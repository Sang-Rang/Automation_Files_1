from payloads.pushdown.rule_validation.pl_pd_bq_rule_validation_sales import (
    PD_BQ_RULE_VALIDATION_SALES_DATASET,
    PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET,
)

PD_BQ_RULE_VALIDATION_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "multi_ds_name_instances",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE NAME NOT IN "
                     f"(SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE SALES > 0)",
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
        "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "join_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT A.NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} A, "
                     f"@{PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET} B "
                     f"WHERE A.NAME = B.NAME",
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
        "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "subquery_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE NAME IN "
                     f"(SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET})",
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

PD_BQ_RULE_VALIDATION_SALES_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
            "runId": "2024-03-11T00:00:00.000+0000",
            "ruleNm": "join_secondary_dataset",
            "ruleType": "SQLF",
            "ruleValue": "SELECT A.NAME FROM (select * from PUBLIC.SALES) A, "
                         "(select * from PUBLIC.SALES) B WHERE A.NAME = B.NAME",
            "score": 500,
            "perc": 500.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 63784,
                "uuid": "50ccb875-bc10-492d-9b44-7fec72599e32"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT A.NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} A, "
                             f"@{PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET} B "
                             f"WHERE A.NAME = B.NAME"
        },
        {
            "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
            "runId": "2024-03-11T00:00:00.000+0000",
            "ruleNm": "multi_ds_name_instances",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE NAME NOT IN "
                         f"(SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} "
                         f"WHERE SALES > 0)",
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 63785,
                "uuid": "8cd15f26-4721-4a26-84be-59a86cf2b437"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE NAME "
                             f"NOT IN (SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} "
                             f"WHERE SALES > 0)"
        },
        {
            "dataset": PD_BQ_RULE_VALIDATION_SALES_DATASET,
            "runId": "2024-03-11T00:00:00.000+0000",
            "ruleNm": "subquery_secondary_dataset",
            "ruleType": "SQLF",
            "ruleValue": "SELECT NAME FROM (select * from PUBLIC.SALES) WHERE NAME IN "
                         "(SELECT NAME FROM (select * from PUBLIC.SALES) ) ",
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 63783,
                "uuid": "308e6d97-e58e-4797-aa9b-c5c234f1a4f4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT NAME FROM @{PD_BQ_RULE_VALIDATION_SALES_DATASET} WHERE NAME "
                             f"IN (SELECT NAME FROM "
                             f"@{PD_BQ_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET})"
        }
    ]
}
