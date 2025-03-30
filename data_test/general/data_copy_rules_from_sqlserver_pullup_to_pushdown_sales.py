from payloads.general.pl_copy_rules_from_sqlserver_pullup_to_pushdown_sales import (
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' AND trdate = '2022-05-01'",
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    }
]

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429461,
                "uuid": "ada287cf-09fd-47c0-944d-10f631545172"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429457,
                "uuid": "2fad662b-4cca-4b01-b1b7-251bafb19d51"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429456,
                "uuid": "1f07ef6b-4217-47a4-8382-9b56f922e94f"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * "
                         f"FROM {COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE trdate = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429462,
                "uuid": "8fca9b90-942d-4174-9fb3-7d5915ade67d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429459,
                "uuid": "f8bc8809-70e6-4eff-951f-d31832b29209"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429453,
                "uuid": "2dfaa952-efde-4603-bdae-f0e05df587b9"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429455,
                "uuid": "5ce04bb2-6f29-49fd-9c1e-abd7e6978d34"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429460,
                "uuid": "48f2e3b5-ad7f-47e2-8784-9223a4fa65e0"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429454,
                "uuid": "39ace733-60d6-4016-81b1-e6afe1baaf1e"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429458,
                "uuid": "b4c0ef05-68df-4d8d-bdd1-5a827ffb6fda"
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

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 429470,
                "uuid": "a083d1a5-aa78-48b4-8e53-7d83007f022a"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from dbo.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Incorrect syntax near the keyword 'WHERE'.\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429471,
                "uuid": "64dfba3b-eec7-49ee-acd8-3eecd1bb7d7f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429464,
                "uuid": "3f13de6d-6d2c-4bd8-a82f-000b871c904c"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429466,
                "uuid": "66c8dce3-595c-44d5-aaee-f04d39003280"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429467,
                "uuid": "542005d6-6339-4ef6-80b5-a65cb740b025"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_trdate_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "trdate",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429468,
                "uuid": "a6f24ebb-3f99-43f7-a022-223403238f74"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429465,
                "uuid": "2a732c37-8378-47ed-84f8-9eed3a0279f9"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_name_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429469,
                "uuid": "6d558146-3046-4d37-980c-187284efaf29"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_name_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "name",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429463,
                "uuid": "4c0d2ffb-c2bb-4bee-8231-684e912da62c"
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

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_INTCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_NULLCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_trdate_is_DATECHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_trdate_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_sales_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_sales_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_STRINGCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_name_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_name_is_EMPTYCHECK"
    }
]

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429475,
                "uuid": "68891169-3f36-42ae-8110-48aaa66ca669"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from dbo.sales) WHERE trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"Incorrect syntax near the keyword 'WHERE'.\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 429472,
                "uuid": "a24f1473-caa3-4418-88eb-e5f0d9d8e696"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429476,
                "uuid": "e6d209ae-1315-4dfd-b0fe-a7f035f4d4be"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429478,
                "uuid": "e763e879-7e49-4580-a809-deb91f502b64"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' AND trdate = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429473,
                "uuid": "f10833be-b790-4498-a018-d0f20ddfe2f4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE name = 'John' "
                             "AND trdate = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429479,
                "uuid": "f35bf0dc-84a4-4019-b650-5cd1614c218a"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_sales_is_DOUBLECHECK",
            "ruleType": "DOUBLECHECK",
            "ruleValue": "sales",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429474,
                "uuid": "259d7fb7-3225-4267-84d1-a44eb71b7d10"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429480,
                "uuid": "8601ec68-e3a8-4c33-9383-8bc20ed8f29a"
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
            "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429477,
                "uuid": "dd20ddec-9378-4407-ad91-13068cb6e32a"
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

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.000+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.210+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2024-07-16T22:03:36.037+0000",
        "job_uuid": "626dfafc-ba29-42c9-8567-e018524ad123",
        "dataset": COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-16T00:00:00.000+0000",
        "rule_name": "if_sales_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-05"
    }
]

COPY_RULES_MSSQL_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Native_FF_Rule",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "John",
        "trdate": "2022-05-02",
        "sales": 2000
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "John",
        "trdate": "2022-05-03",
        "sales": 1000
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "John",
        "trdate": "2022-05-04",
        "sales": 2000
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
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "Steve",
        "trdate": "2022-05-01",
        "sales": 300
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "Steve",
        "trdate": "2022-05-02",
        "sales": 400
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "Steve",
        "trdate": "2022-05-03",
        "sales": 200
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "Steve",
        "trdate": "2022-05-04",
        "sales": 500
    },
    {
        "rule_name": "if_sales_is_DOUBLECHECK",
        "name": "Steve",
        "trdate": "2022-05-05",
        "sales": 10000
    }
]
