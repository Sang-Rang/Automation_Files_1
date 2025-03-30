from payloads.general.pl_copy_rules_from_snowflake_pullup_to_pushdown_sales import (
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                     f"WHERE TRDATE = '2022-05-01'",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Simple_Spark_Rule",
        "ruleType": "SQLG",
        "ruleValue": "SALES = 0",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                     "AND \"TRDATE\" = '2022-05-01'",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_SALES_is_NULL",
        "ruleType": "NULLCHECK",
        "ruleValue": "SALES",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "SALES",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_NAME_is_STRING",
        "ruleType": "STRINGCHECK",
        "ruleValue": "NAME",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "NAME",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_SALES_is_DOUBLECHECK",
        "ruleType": "DOUBLECHECK",
        "ruleValue": "SALES",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "SALES",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_NAME_is_DATATYPECHECK",
        "ruleType": "DATATYPECHECK",
        "ruleValue": "NAME",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "NAME",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_NAME_is_EMPTYCHECK",
        "ruleType": "EMPTYCHECK",
        "ruleValue": "NAME",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "NAME",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_TRDATE_is_DATECHECK",
        "ruleType": "DATECHECK",
        "ruleValue": "TRDATE",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "TRDATE",
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
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_SALES_is_INTCHECK",
        "ruleType": "INTCHECK",
        "ruleValue": "SALES",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "SALES",
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

COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE TRDATE = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429433,
                "uuid": "bc21e112-2837-48e0-a80d-522802691752"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429432,
                "uuid": "c12f3cb4-938f-46a9-8184-00b73dc9b965"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                         "AND \"TRDATE\" = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429427,
                "uuid": "889b036d-3e40-4060-a8ba-ef9491c41f13"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                             "AND \"TRDATE\" = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429428,
                "uuid": "b8a0eec1-88c4-4479-8dc8-d9cfe5b27743"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRING",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429425,
                "uuid": "b63e33e3-55b5-408f-8339-7d128ba7fe57"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429430,
                "uuid": "07ebd5bb-370a-4fac-867d-2fb71f432b00"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_DATATYPECHECK",
            "ruleType": "DATATYPECHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429424,
                "uuid": "86615932-e3ff-416f-aae7-884500ed9fb8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429429,
                "uuid": "3b6c19da-3202-4a20-b95f-88881d665396"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_TRDATE_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "TRDATE",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429426,
                "uuid": "87a361cc-d370-425e-a0ad-bd6dc227b6b6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "TRDATE",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429431,
                "uuid": "628c429a-e79b-40f2-90a8-57fe8553a670"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        }
    ]
}

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRING",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_STRING"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULL",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_NULL"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    }
]

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429437,
                "uuid": "55b818ff-89f8-4614-a357-1bddb85ebeb6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429436,
                "uuid": "9806bea2-3cbc-422a-9f72-354081cf4615"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                         "AND \"TRDATE\" = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429435,
                "uuid": "07f4bca9-c45d-4a4b-9ca3-2dc2f6f0af83"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                             "AND \"TRDATE\" = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429441,
                "uuid": "7936561a-1afd-43b6-8d0c-b0451e33a295"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRING",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429440,
                "uuid": "6b16bfde-15c7-4f34-803e-c16a33d879f9"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429434,
                "uuid": "438c59b9-8286-4dad-86fe-37a9399d6c73"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429438,
                "uuid": "ebbab454-501c-4196-8d8a-f23328b38cbc"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_TRDATE_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "TRDATE",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429442,
                "uuid": "72826cfc-3560-4e77-a29d-e68c43a69355"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "TRDATE",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429439,
                "uuid": "393be926-d096-42da-b6a0-50e4aa21a9ab"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRING",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_STRING"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULL",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_NULL"
    },
    {
        "sourceDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    }
]

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429446,
                "uuid": "e1150d8c-543c-4af0-9c78-ccc916e7709b"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429445,
                "uuid": "70899998-c6ed-4686-93bc-2650110626b5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                         "AND \"TRDATE\" = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429444,
                "uuid": "a95222b2-4f06-4be3-b596-441e50917fc2"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE \"NAME\" = 'John' "
                             "AND \"TRDATE\" = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429450,
                "uuid": "efbef9ac-452e-4c36-a660-ccc694920c7c"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRING",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429449,
                "uuid": "38e4e1cb-b62d-4e95-9e0b-139bea4d296a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429443,
                "uuid": "a22a6068-a9e3-4e42-8dd2-1ac337f0e179"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429447,
                "uuid": "9a33bd73-57a6-4917-bf68-939632823fae"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "NAME",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_TRDATE_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "TRDATE",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429451,
                "uuid": "0b4e761e-a375-4992-bfff-daa2fe22f1c3"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "TRDATE",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429448,
                "uuid": "92100742-701a-43bb-84b6-b7d1b1b244d8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 88578560,
        "updts": "2024-06-29T12:20:28.003+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 88578547,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 88578548,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 88578549,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 88578550,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 88578551,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 88578552,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 88578553,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 88578554,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 88578555,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 88578556,
        "updts": "2024-06-29T12:20:24.912+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 88578557,
        "updts": "2024-06-29T12:20:25.662+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 88578558,
        "updts": "2024-06-29T12:20:27.135+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 88578559,
        "updts": "2024-06-29T12:20:27.135+0000",
        "job_uuid": "1d605461-984b-41f7-bb91-8f826c27de7b",
        "dataset": COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-06-29T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "Steve~|2022-05-01"
    }
]

COPY_RULES_SF_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "Native_FF_Rule",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "FF_Spark_Rule",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-02",
        "SALES": 2000
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-03",
        "SALES": 1000
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-04",
        "SALES": 2000
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    },
    {
        "rule_name": "Simple_Spark_Rule",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "Steve",
        "TRDATE": "2022-05-01",
        "SALES": 300
    },
    {
        "rule_name": "FF_Spark_Rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-01",
        "SALES": 300
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "Steve",
        "TRDATE": "2022-05-02",
        "SALES": 400
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "Steve",
        "TRDATE": "2022-05-03",
        "SALES": 200
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "Steve",
        "TRDATE": "2022-05-04",
        "SALES": 500
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "Steve",
        "TRDATE": "2022-05-05",
        "SALES": 10000
    }
]
