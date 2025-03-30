from payloads.general.pl_copy_rules_from_databricks_pullup_to_pushdown_sales import (
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM public.sales WHERE NAME = 'John' AND trdate = '2022-05-01'",
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    }
]

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416909,
                "uuid": "6283d4be-c282-4860-a2e2-3be8cd54b8bd"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM public.sales WHERE NAME = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416911,
                "uuid": "10e56bcb-f0ec-46e2-99b7-6ee3a8ac442f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE NAME = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416908,
                "uuid": "4d15eadc-396a-4f43-be44-35f50cdd22c3"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416905,
                "uuid": "1bca3d85-e43d-427b-b611-195394e7bf1e"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416902,
                "uuid": "85a396cc-938d-41a4-af8a-64f32c742554"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416906,
                "uuid": "91899c77-9e69-4c56-9e5f-f807df2712da"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416907,
                "uuid": "706c9f4f-987c-4238-8ac4-0832f705f435"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416903,
                "uuid": "e4107660-3757-4f28-956e-fab4321a99e4"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 416904,
                "uuid": "4f842580-a7fb-4082-ba32-76bbebcaaa63"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM "
                         f"{COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE TRDATE = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416910,
                "uuid": "82d0b4e1-e383-4582-962e-01aa10d75c02"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416915,
                "uuid": "c4f14261-0fa2-424b-b6b5-7b8b525670cf"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales WHERE NAME = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416912,
                "uuid": "2a2fd25f-7a42-4c9e-80ee-e8513a360510"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE NAME = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416920,
                "uuid": "5c797245-83ca-4219-a184-590f10fa574f"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416919,
                "uuid": "ea478c46-57ce-4671-b83b-86ffa1ba4a3b"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416913,
                "uuid": "e4592b85-864a-4b30-8c26-581360cc03db"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416916,
                "uuid": "5ff2c59a-037d-4aab-b2b6-33133e459429"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416918,
                "uuid": "e82e1046-037b-4f0a-b58a-90350b38ef22"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416917,
                "uuid": "1654cc2b-6a9c-46ff-bc97-30bad1bc5848"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416914,
                "uuid": "bd0d9581-fc79-4abe-9ef8-6b1d3574eeef"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416925,
                "uuid": "59f5a559-1210-40e7-a9a7-23aa8d8a885e"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales WHERE NAME = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416923,
                "uuid": "9998793c-a4c2-4f27-a3b9-95dfdb757862"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE NAME = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416930,
                "uuid": "d0dc3df1-9992-486b-b51c-831c5d73e960"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416929,
                "uuid": "78a6a29f-0494-4cc8-a420-4244633e9f7a"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416922,
                "uuid": "77eafeac-e5cf-4b5d-a2b5-59470d76c7ca"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416926,
                "uuid": "b84ed8aa-3b29-49ed-af57-7c816d6cb2c6"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416928,
                "uuid": "e30e3684-2d1b-4f05-a385-ed1b1923d7cd"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416927,
                "uuid": "4f6effc9-c077-4dc6-8797-4f27e1a67e2d"
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
            "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416924,
                "uuid": "cacbcb21-f0a6-47df-ae48-3ca18cb61d0e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:31.348+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:30.971+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:34.827+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:34.827+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T01:16:36.380+0000",
        "job_uuid": "48f83645-ef4f-4e89-8367-3a884e0c142d",
        "dataset": COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-03T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    }
]

COPY_RULES_DBRKS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Native_FF_Rule",
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
