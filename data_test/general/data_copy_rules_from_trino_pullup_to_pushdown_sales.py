from payloads.general.pl_copy_rules_from_trino_pullup_to_pushdown_sales import (
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    },
    {
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM public.sales WHERE name = 'John' "
                     "AND trdate = DATE('2022-05-01')",
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    }
]

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429490,
                "uuid": "60f606f2-abac-4127-957a-9f5b2037054a"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * "
                         f"FROM {COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE trdate = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429492,
                "uuid": "02bd977b-a637-4ecc-b449-0c5e6e15c2d4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429484,
                "uuid": "06bdc94f-da85-4b02-b5a2-acbecd03472d"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429483,
                "uuid": "19834648-e852-42dd-8540-8baf9b8400ae"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM public.sales WHERE name = 'John' "
                         "AND trdate = DATE('2022-05-01')",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429491,
                "uuid": "81a6d14e-9b5b-4acf-b5b9-c5d3084af2e0"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE name = 'John' "
                             "AND trdate = DATE('2022-05-01')",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429488,
                "uuid": "e9dd7ad6-0cbf-4cfe-84c5-e7e83c79c8e3"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429485,
                "uuid": "6dc63d2a-08b9-4dab-8189-815dba4ee1ef"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429486,
                "uuid": "93b22189-4e5f-4ffe-af01-36c30781e790"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429487,
                "uuid": "5cb3739d-a292-42b5-b3a8-9cc2b228bbf7"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429489,
                "uuid": "ef7da2d0-8c01-4e83-bc7e-bd03330a1704"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        }
    ]
}

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429522,
                "uuid": "5274fc3b-43ec-4b3b-9c9b-ac54b71c4207"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074634_11776_c8nq2): "
                         "line 1:116: Cannot apply operator: date = varchar(10)\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429521,
                "uuid": "b11ac8fb-40fa-412e-a82e-7580bab609b0"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429525,
                "uuid": "cec62800-678c-4436-a682-4cbc1c2c4ce9"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074633_11774_c8nq2): "
                         "line 1:190: Function 'regexp_instr' not registered\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429519,
                "uuid": "10ac292d-c556-431b-8e4b-7b686c327828"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074634_11876_a3njt): "
                         "line 1:156: mismatched input 'AS'. Expecting: '%', ')', '*', '+', ',', "
                         "'-', '.', '/', 'AND', 'AT', 'OR', '[', '||', <predicate>\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429520,
                "uuid": "46b56363-01e3-4920-91e5-c629492a27c1"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429523,
                "uuid": "7e16932f-5d77-45d3-b126-5a371eb1545e"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074630_11772_c8nq2): "
                         "line 1:188: Function 'regexp_instr' not registered\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429517,
                "uuid": "45109b8d-6c15-47a5-9073-6015c500d23c"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales WHERE name = 'John' "
                         "AND trdate = DATE('2022-05-01' ) ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429518,
                "uuid": "dc40ed09-7866-4465-975c-900f593a8435"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE name = 'John' "
                             "AND trdate = DATE('2022-05-01')",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429524,
                "uuid": "51727ad5-a86f-48cd-bc35-d6afa932b885"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429532,
                "uuid": "baa34b24-fca6-4191-a7d6-4620c2f4f455"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074706_11890_a3njt): "
                         "line 1:513: Cannot apply operator: date = varchar(10)\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429530,
                "uuid": "31e27a2f-3d09-4834-ba5c-75924faf1aa3"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074657_11786_c8nq2): "
                         "line 1:585: Function 'regexp_instr' not registered\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429527,
                "uuid": "a0e7c29a-a668-486c-bef6-c11ed11f632e"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM public.sales WHERE name = 'John' "
                         "AND trdate = DATE('2022-05-01' ) ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429531,
                "uuid": "748ddc88-572b-45ad-89f9-c97e1f79134c"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM public.sales WHERE name = 'John' "
                             "AND trdate = DATE('2022-05-01')",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429534,
                "uuid": "caf9e655-d592-4bad-8da8-8a2d1f01627b"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429535,
                "uuid": "251e69a4-40f5-4e53-9de9-f8edf138d69a"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074701_11788_fyszm): "
                         "line 1:587: Function 'regexp_instr' not registered\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429528,
                "uuid": "963cac2a-db02-4419-a8cc-f98ab6fe5504"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Query failed (#20241112_074705_11889_a3njt): "
                         "line 1:553: mismatched input 'AS'. Expecting: '%', ')', '*', '+', ',', "
                         "'-', '.', '/', 'AND', 'AT', 'OR', '[', '||', <predicate>\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429529,
                "uuid": "1c267a3d-9c42-48d2-bf6a-fa8e1b6f6fa7"
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
            "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429533,
                "uuid": "7a8b1243-c5f2-4ea8-b4cf-61df8098b295"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "name",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 96571563,
        "updts": "2024-07-16T22:10:32.980+0000",
        "job_uuid": "53675a8c-3cde-42da-8dd0-0e92b7c98b27",
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 96571562,
        "updts": "2024-07-16T22:10:23.606+0000",
        "job_uuid": "53675a8c-3cde-42da-8dd0-0e92b7c98b27",
        "dataset": COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    }
]

COPY_RULES_TRINO_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Native_FF_Rule",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "Simple_Spark_Rule",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    }
]
