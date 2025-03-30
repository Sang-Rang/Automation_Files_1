from payloads.general.pl_copy_rules_from_athena_pullup_to_pushdown_sales import (
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM default.sales WHERE name = 'John' "
                     "AND trdate = CAST('2022-05-01' AS DATE)",
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417446,
                "uuid": "87c19249-2db5-4f2f-b81f-ae99fb34c7fb"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM default.sales WHERE name = 'John' "
                         "AND trdate = CAST('2022-05-01' AS DATE)",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 417447,
                "uuid": "4380b870-c34b-42d6-b277-3166828ac854"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM default.sales WHERE name = 'John' "
                             "AND trdate = CAST('2022-05-01' AS DATE)",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417443,
                "uuid": "5d5813fb-bdf2-49db-9ef9-c15cfe264a6f"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417441,
                "uuid": "e07bea96-d658-44a1-ae35-61f46d62955c"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417440,
                "uuid": "a911511f-7b87-436f-b840-8cbf571e2663"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417444,
                "uuid": "56fb8d2e-9232-4ea2-99e4-b8dd455520e8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417442,
                "uuid": "5ed4b9d6-a44d-47c8-948e-63e00de02316"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417445,
                "uuid": "67a83ae1-b7a6-42c2-b86f-56c9041792a3"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 417439,
                "uuid": "0532ce0e-0e68-44ae-8e2e-efbf2520dfe3"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * "
                         f"FROM {COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE trdate = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 417448,
                "uuid": "2a792a11-4ec6-4e73-8f3b-cc692556e990"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * "
                             f"FROM @{COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416782,
                "uuid": "55c371bb-d3df-4a8f-98cf-1f24073cc25f"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM default.sales WHERE name = 'John' "
                         "AND trdate = CAST('2022-05-01' AS DATE ) ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416779,
                "uuid": "b9bb80f6-46e0-45e0-a58f-64a3dc9ab038"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM default.sales WHERE name = 'John' "
                             "AND trdate = CAST('2022-05-01' AS DATE)",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416785,
                "uuid": "f7184231-1bb0-4fff-9818-a3a702f303ee"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416784,
                "uuid": "10cd1125-1745-458e-8d11-06359105aca7"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. FUNCTION_NOT_FOUND: line 1:189: "
                         "Function 'regexp_instr' not registered [Execution ID: "
                         "b06bd188-fbc1-4845-bd8b-4d82ba78cb7f]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416777,
                "uuid": "9200135e-7556-4104-a9ee-87312c16de79"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. FUNCTION_NOT_FOUND: line 1:191: "
                         "Function 'regexp_instr' not registered [Execution ID: "
                         "3e7355b0-4ec2-4b9a-92be-8d17891762c7]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416778,
                "uuid": "d4c44603-4fde-4065-87f8-b4e073a9573b"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. line 1:157: mismatched input 'AS'. "
                         "Expecting: ')', ',', '.', '[' [Execution ID not available]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416780,
                "uuid": "bcea8e3d-a792-4ccc-be0a-920b6b719407"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 416783,
                "uuid": "3ed6af4d-c136-450c-b342-2c14954f8574"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from default.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. TYPE_MISMATCH: line 1:117: Cannot "
                         "apply operator: date = varchar(10) [Execution ID: "
                         "b31d86e0-c1d8-456c-8f56-da5bccfefd6f]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416781,
                "uuid": "d727f2b1-0d18-4334-99de-283185ce00d3"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416855,
                "uuid": "351e3068-11f2-4058-a7ba-9f52f9879421"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM default.sales WHERE name = 'John' "
                         "AND trdate = CAST('2022-05-01' AS DATE ) ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 416854,
                "uuid": "9cf42566-7114-4696-844b-9f45b3f57e13"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM default.sales WHERE name = 'John' "
                             "AND trdate = CAST('2022-05-01' AS DATE)",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416858,
                "uuid": "9fc63d1c-2b65-4ecd-a2d8-2c5f74d11ef7"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416857,
                "uuid": "c90a34ac-dd1f-495c-a31f-40c70013a2a0"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. FUNCTION_NOT_FOUND: line 1:541: "
                         "Function 'regexp_instr' not registered. If a data manifest file was "
                         "generated at 's3://aws-athena-query-results-880607122989-us-east-1/"
                         "372669aa-47e1-40fe-89b3-69d5b18c18fc-manifest.csv', you may need to "
                         "manually clean the data from locations specified in the manifest. "
                         "Athena will not delete data in your account. [Execution ID: "
                         "372669aa-47e1-40fe-89b3-69d5b18c18fc]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416850,
                "uuid": "3662acad-a480-4a21-84a7-c9f76adda093"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. FUNCTION_NOT_FOUND: line 1:543: "
                         "Function 'regexp_instr' not registered. If a data manifest file was "
                         "generated at 's3://aws-athena-query-results-880607122989-us-east-1/"
                         "cdb3b5f6-255b-40a0-b16a-78becd789ba7-manifest.csv', you may need to "
                         "manually clean the data from locations specified in the manifest. "
                         "Athena will not delete data in your account. [Execution ID: "
                         "cdb3b5f6-255b-40a0-b16a-78becd789ba7]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416851,
                "uuid": "8d0af694-f311-47bc-84e7-b17f07662cb1"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. line 1:509: mismatched input 'AS'. "
                         "Expecting: ')', ',', '.', '[' [Execution ID not available]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416852,
                "uuid": "15a8a171-ca2e-4620-ad66-3d2858e58b63"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 416856,
                "uuid": "b0d80abe-ea1b-48fc-af4d-f115cbbf8097"
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
            "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-11T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from default.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. TYPE_MISMATCH: line 1:469: Cannot "
                         "apply operator: date = varchar(10). If a data manifest file was "
                         "generated at 's3://aws-athena-query-results-880607122989-us-east-1/"
                         "80b8dc49-efc5-42ac-b26f-7cb0b8fb8c81-manifest.csv', you may need to "
                         "manually clean the data from locations specified in the manifest. "
                         "Athena will not delete data in your account. [Execution ID: "
                         "80b8dc49-efc5-42ac-b26f-7cb0b8fb8c81]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 416853,
                "uuid": "22f3dd4e-5f63-4860-bb8c-e51ce93ae156"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "updts": "2024-07-09T04:33:55.021+0000",
        "job_uuid": "7e7aa6e4-c59b-4bc6-837a-6f86573c64ba",
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01",
        "run_id": "2024-07-08 00:00:00"
    },
    {
        "updts": "2024-07-09T04:34:01.264+0000",
        "job_uuid": "7e7aa6e4-c59b-4bc6-837a-6f86573c64ba",
        "dataset": COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05",
        "run_id": "2024-07-08 00:00:00"
    }
]

COPY_RULES_ATHENA_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
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
