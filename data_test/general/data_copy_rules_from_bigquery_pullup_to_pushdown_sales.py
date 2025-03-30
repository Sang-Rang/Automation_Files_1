from payloads.general.pl_copy_rules_from_bigquery_pullup_to_pushdown_sales import (
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    },
    {
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": "Exception with native rule check: No db connection, please check "
                     "connections tab ",
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_SALES_is_NULLCHECK",
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_NAME_is_STRINGCHECK",
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    }
]

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417458,
                "uuid": "ab302b53-f606-42ee-ab28-f8534ed2a1fe"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Exception with native rule check: No db connection, please check "
                         "connections tab ",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 417450,
                "uuid": "82070439-4a98-4714-a47c-705193071f47"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "EXCEPTION"
        },
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417455,
                "uuid": "e7761605-9996-44ed-9e49-4d6169f3f90d"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 417454,
                "uuid": "d2588f3f-adfb-4b72-a799-6f663fa2683b"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417453,
                "uuid": "c8b5c02c-b5a0-4b5b-8082-504408dd100f"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417452,
                "uuid": "a8024c4b-0377-4222-ba0e-549b2b885993"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 417456,
                "uuid": "cdab4fc5-6a65-4b93-a95e-77169ed3c7be"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417457,
                "uuid": "90a2d3bc-02df-45b7-8ffe-5526e8773e3c"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 417449,
                "uuid": "692dc875-6f42-4efb-bc69-95865b087274"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE TRDATE = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 417459,
                "uuid": "0c2859b7-ad25-40af-ad89-e98bf044cf88"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416878,
                "uuid": "de913f53-feed-413a-96e3-234050401da2"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416876,
                "uuid": "ff0160a5-f180-4efc-b480-7e19bb5d5a3d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416883,
                "uuid": "ece17479-0323-4d44-bd9b-56444dc3c2a7"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416882,
                "uuid": "81194cce-5153-434a-8878-60c0429a4685"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416880,
                "uuid": "f0a70ee4-ed7d-4655-8e8c-47fbc95bce39"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416875,
                "uuid": "87f2d49b-9b26-4bed-9340-25229059bcea"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416881,
                "uuid": "b476b9d3-dd78-4a7d-8965-ff7eb75c8b6a"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416879,
                "uuid": "685f41cc-c3c5-408e-a539-96b658df6f74"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416877,
                "uuid": "0d17b761-2e36-4ae1-84cf-0e20b5886809"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416887,
                "uuid": "56f86489-d479-44ae-bab9-f1faa20b2763"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416885,
                "uuid": "9c021251-df07-4940-876a-c04b3a78c4b1"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM PUBLIC.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416891,
                "uuid": "9b155a5e-5d75-4ae9-8276-d86d724ae4e7"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416892,
                "uuid": "81a261e8-3bd3-4f1a-8eb1-269d5c85ea04"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416889,
                "uuid": "671ca5a8-cc87-483b-bc80-c2dc10f3487f"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416884,
                "uuid": "69791d2a-b00c-4171-b97c-05952a3aa222"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416890,
                "uuid": "d57b31eb-f981-42d9-a8fc-9889c00c5fc6"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416888,
                "uuid": "d1e87724-e4e5-4123-9aeb-ae9c6b640dfa"
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
            "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
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
                "id": 416886,
                "uuid": "33aae0f1-cf42-4098-9ce0-c233c1d5b763"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * "
                             f"FROM @{COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:52.119+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:45:02.525+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:45:00.814+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:45:00.814+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 1,
        "updts": "2024-07-03T04:44:50.249+0000",
        "job_uuid": "455a9c3e-83a5-4c64-a7d2-d3ea1c642625",
        "dataset": COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-02T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-02"
    }
]

COPY_RULES_BQ_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
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
        "rule_name": "Simple_Spark_Rule",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    },
    {
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
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
