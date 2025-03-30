from payloads.general.pl_copy_rules_from_redshift_pullup_to_pushdown_sales import (
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                     f"WHERE trdate = '2022-05-01'",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_sales_is_INTCHECK",
        "ruleType": "INTCHECK",
        "ruleValue": "sales",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "sales",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM public.sales2 WHERE name = 'John' AND trdate = '2022-05-01'",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_sales_is_NULLCHECK",
        "ruleType": "NULLCHECK",
        "ruleValue": "sales",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "sales",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_trdate_is_DATECHECK",
        "ruleType": "DATECHECK",
        "ruleValue": "trdate",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "trdate",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_sales_is_DOUBLECHECK",
        "ruleType": "DOUBLECHECK",
        "ruleValue": "sales",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "sales",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_name_is_STRINGCHECK",
        "ruleType": "STRINGCHECK",
        "ruleValue": "name",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "name",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_name_is_EMPTYCHECK",
        "ruleType": "EMPTYCHECK",
        "ruleValue": "name",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "name",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "if_name_is_DATATYPECHECK",
        "ruleType": "DATATYPECHECK",
        "ruleValue": "name",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "name",
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
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Simple_Spark_Rule",
        "ruleType": "SQLG",
        "ruleValue": "sales = 0",
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

COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416944,
                "uuid": "4d39d9c0-2d17-451b-a3d7-5e5b3b3ef812"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM public.sales2 WHERE name = 'John' "
                         "AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416936,
                "uuid": "2a369daa-fa6b-45b0-96ff-4d92f5ca177d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales2 WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_trdate_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "trdate",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416942,
                "uuid": "7b98bd6f-9a07-4143-9a6f-d6f72e1f69fa"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416939,
                "uuid": "401ec50d-9437-4523-b180-acb6a8329107"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416938,
                "uuid": "f5cc184e-162f-4f55-99f7-b85092a7715d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416941,
                "uuid": "c59ea510-67c8-49b5-998f-151ca5385530"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416943,
                "uuid": "9500a986-d09e-4a71-a8c5-bee6b822bac8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416940,
                "uuid": "e95c15d7-13ea-4bea-ad9b-4dfc1a6d6e3e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_DATATYPECHECK",
            "ruleType": "DATATYPECHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416937,
                "uuid": "c7ec005d-024d-439d-a593-dbdf85f8109f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE trdate = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416945,
                "uuid": "95c785e4-844e-4e59-a5e7-e3d29fe0d63a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416949,
                "uuid": "8d5a178c-cfb0-4bdb-98b1-67383b1f2312"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales2 WHERE name = 'John' "
                         "AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416947,
                "uuid": "f1e59f57-be98-4a02-a0f1-8a79688b98da"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales2 WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_trdate_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "trdate",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416953,
                "uuid": "f36727d8-a803-494d-a110-e64a302c50ca"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416952,
                "uuid": "d208758c-0679-4849-b847-340a19759c17"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416950,
                "uuid": "281e6168-5871-4639-90f4-dcdab90bb3a2"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416946,
                "uuid": "6cd2f868-650a-48c3-9fcd-22320f430a79"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416954,
                "uuid": "b73a9990-1aa2-404d-ac0d-e2a9c265bec4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416951,
                "uuid": "f00149a5-fbe7-4dff-b3e3-d52c16b52d2d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales2) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416948,
                "uuid": "5774343c-1f0a-4dd8-909a-4f87013556ff"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Simple_Spark_Rule",
            "ruleType": "SQLG",
            "ruleValue": "sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416963,
                "uuid": "c6378b84-0030-4cef-ae3a-627ab5d20b13"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales2 WHERE name = 'John' "
                         "AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416960,
                "uuid": "a15779cf-685e-4a53-bd98-6521d025803e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales2 WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_trdate_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "trdate",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416966,
                "uuid": "8dd3776b-3dd5-4a2c-9c0d-e6e0ce0ee4a8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416967,
                "uuid": "a1c64b41-be9c-46a7-a1d6-9e435be5d8aa"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416964,
                "uuid": "0c3a256e-c8ad-4fe9-9f89-30af6c4ebe5f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416961,
                "uuid": "be90bef6-183b-4464-8f26-e689aa6b1518"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416968,
                "uuid": "024065f4-d76b-4304-8899-1557afab0449"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 416965,
                "uuid": "9911922c-6ca4-4be7-8b53-a866847936c5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales2) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416962,
                "uuid": "5d6a87a6-6d57-4140-99d5-8c62fb8a557d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 570237,
        "updts": "2024-07-04T19:23:07.465+0000",
        "job_uuid": "e0e524fb-b98c-47c4-af41-db2811389e36",
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 570231,
        "updts": "2024-07-04T19:23:06.512+0000",
        "job_uuid": "e0e524fb-b98c-47c4-af41-db2811389e36",
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 570233,
        "updts": "2024-07-04T19:23:06.769+0000",
        "job_uuid": "e0e524fb-b98c-47c4-af41-db2811389e36",
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 570235,
        "updts": "2024-07-04T19:23:07.465+0000",
        "job_uuid": "e0e524fb-b98c-47c4-af41-db2811389e36",
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 570239,
        "updts": "2024-07-04T19:23:07.620+0000",
        "job_uuid": "e0e524fb-b98c-47c4-af41-db2811389e36",
        "dataset": COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    }
]

COPY_RULES_RS_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Native_FF_Rule",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "FF_Spark_Rule",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    },
    {
        "rule_name": "Simple_Spark_Rule",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    },
    {
        "rule_name": "FF_Spark_Rule",
        "name": "Steve",
        "trdate": "2022-05-01",
        "sales": 300
    }
]
