from payloads.pushdown.rule_validation.pl_pd_trino_rule_validation_sales import (
    PD_TRINO_RULE_VALIDATION_SALES_DATASET,
    PD_TRINO_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET,
)

PD_TRINO_RULE_VALIDATION_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "multi_ds_name_instances",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULE_VALIDATION_SALES_DATASET} WHERE name NOT IN "
                     f"(SELECT name FROM @{PD_TRINO_RULE_VALIDATION_SALES_DATASET} "
                     f"WHERE sales > 0)",
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
        "dataset": PD_TRINO_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "join_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT A.name FROM @{PD_TRINO_RULE_VALIDATION_SALES_DATASET} A, "
                     f"@{PD_TRINO_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET} B "
                     f"WHERE A.name = B.name",
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
        "dataset": PD_TRINO_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "subquery_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT name FROM @{PD_TRINO_RULE_VALIDATION_SALES_DATASET} WHERE name IN "
                     f"(SELECT name "
                     f"FROM @{PD_TRINO_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET})",
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
