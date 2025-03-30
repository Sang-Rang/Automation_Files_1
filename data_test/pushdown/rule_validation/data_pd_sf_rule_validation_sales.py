from payloads.pushdown.rule_validation.pl_pd_sf_rule_validation_sales import (
    PD_SF_RULE_VALIDATION_SALES_DATASET,
    PD_SF_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET,
)

PD_SF_RULE_VALIDATION_SALES_RULE_DEFINITIONS = [
    {
        "dataset": PD_SF_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "multi_ds_name_instances",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SF_RULE_VALIDATION_SALES_DATASET} WHERE \"NAME\" NOT IN "
                     f"(SELECT \"NAME\" FROM @{PD_SF_RULE_VALIDATION_SALES_DATASET} "
                     "WHERE \"SALES\" > 0)",
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
        "dataset": PD_SF_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "join_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT A.\"NAME\" FROM @{PD_SF_RULE_VALIDATION_SALES_DATASET} A, "
                     f"@{PD_SF_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET} B "
                     f"WHERE A.\"NAME\" = B.\"NAME\"",
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
        "dataset": PD_SF_RULE_VALIDATION_SALES_DATASET,
        "ruleNm": "subquery_secondary_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT \"NAME\" FROM @{PD_SF_RULE_VALIDATION_SALES_DATASET} "
                     f"WHERE \"NAME\" IN (SELECT \"NAME\" FROM "
                     f"@{PD_SF_RULE_VALIDATION_SALES_SECONDARY_DATASET_DATASET})",
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
