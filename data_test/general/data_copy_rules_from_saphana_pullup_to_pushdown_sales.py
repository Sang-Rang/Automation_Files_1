from payloads.general.pl_copy_rules_from_saphana_pullup_to_pushdown_sales import (
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
    COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
)

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_RULE_DEFINITIONS = [
    {
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "FF_Spark_Rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "ruleNm": "Native_FF_Rule",
        "ruleType": "NATIVE",
        "ruleValue": "SELECT * FROM TEST.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
    }
]

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429335,
                "uuid": "a0c13bd1-9286-4528-b637-162c70a40687"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429332,
                "uuid": "f15d2ac2-e29b-441f-9a61-7d3524c2c976"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429331,
                "uuid": "d66fbc9b-d301-4362-b8f8-2020f916df12"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429339,
                "uuid": "29fdf4e8-8fa8-48aa-88e6-7f9e4a2edc4e"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * "
                         f"FROM {COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET}_dataset "
                         f"WHERE TRDATE = '2022-05-01' ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429340,
                "uuid": "7062a0cd-651e-4e2a-a5d4-08e461b59981"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429334,
                "uuid": "d5db81bc-d112-42e6-aadd-d6df50d65d44"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "NATIVE",
            "ruleValue": "SELECT * FROM TEST.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429336,
                "uuid": "07e9784c-50c3-4a0e-8492-2cc0900a6a6c"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM TEST.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429333,
                "uuid": "3b702d2d-ebc5-44e8-b251-27550476dd34"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429337,
                "uuid": "61664ab1-db92-4937-89bc-0773d8f06ff0"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
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
                "id": 429338,
                "uuid": "ad11031e-5690-469d-9f81-17a1b740a03f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_STRINGCHECK",
            "ruleType": "STRINGCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429345,
                "uuid": "721aa962-295b-4316-b922-c3a2419fcf15"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_NAME_is_EMPTYCHECK",
            "ruleType": "EMPTYCHECK",
            "ruleValue": "NAME",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429342,
                "uuid": "d12ea9e7-162a-4207-af57-4f019562ad6d"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 429347,
                "uuid": "a70241fd-3419-4865-a2b7-0d3124a48e16"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429346,
                "uuid": "25caa026-706d-4410-bafc-86f803baf63b"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_INTCHECK",
            "ruleType": "INTCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429343,
                "uuid": "a2aa1347-56a8-4d95-a2e3-0f01b593e1c4"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM TEST.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429344,
                "uuid": "817690b0-a721-4996-85f9-59090d9bd8d6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM TEST.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_SALES_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "SALES",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429348,
                "uuid": "e408bf01-0240-4957-be90-b7ae800326dc"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "if_TRDATE_is_DATECHECK",
            "ruleType": "DATECHECK",
            "ruleValue": "TRDATE",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 429349,
                "uuid": "315cf363-5f45-4318-ba86-ac0b5a62acde"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_DATASET,
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
                "id": 429341,
                "uuid": "2f541a1a-ca09-43e8-940e-a7313f844532"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_COPY_OUTPUT = [
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Simple_Spark_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Simple_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "FF_Spark_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "FF_Spark_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_INTCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_INTCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "Native_FF_Rule",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "Native_FF_Rule"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_NULLCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_NULLCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_TRDATE_is_DATECHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_TRDATE_is_DATECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_SALES_is_DOUBLECHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_SALES_is_DOUBLECHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_STRINGCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_STRINGCHECK"
    },
    {
        "sourceDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PULLUP_DATASET,
        "sourceRuleName": "if_NAME_is_EMPTYCHECK",
        "targetDataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "generatedRuleName": "if_NAME_is_EMPTYCHECK"
    }
]

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429361,
                "uuid": "7748a721-a979-4056-8f7e-2aa7e4960058"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429353,
                "uuid": "e9642dd1-43a2-4ebf-99ff-539f8d2af801"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "Native_FF_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM TEST.SALES WHERE NAME = 'John' AND TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429354,
                "uuid": "ea356cfc-1bd9-4cd3-b01e-f03c919ec93f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM TEST.SALES WHERE NAME = 'John' "
                             "AND TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429360,
                "uuid": "faf4a2da-de12-4dcb-b277-53183396a399"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
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
                "id": 429359,
                "uuid": "cd6110c6-e96b-4198-92e7-70e50c16800a"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429357,
                "uuid": "3840b28f-9b9c-4bce-b2a3-de7644caffc9"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429356,
                "uuid": "3d32f44f-d697-4e9d-b3fc-91b7f83804ed"
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
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": "FF_Spark_Rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES) WHERE TRDATE = '2022-05-01'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 429355,
                "uuid": "df933fcc-1d1d-49af-9ef8-59907e520020"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM "
                             f"@{COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE TRDATE = '2022-05-01'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
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
                "id": 429358,
                "uuid": "d7a52baf-ab3b-41ab-b17a-be1481e46c53"
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

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:28.954+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "if_SALES_is_DOUBLECHECK",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:29.188+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "Native_FF_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:29.425+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:29.425+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "FF_Spark_Rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-07-04T23:21:29.535+0000",
        "job_uuid": "e6febda5-4000-47e6-a78b-4a2dadd233f4",
        "dataset": COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-07-04T00:00:00.000+0000",
        "rule_name": "Simple_Spark_Rule",
        "link_id": "John~|2022-05-05"
    }
]

COPY_RULES_SAPH_PULLUP_TO_PD_SALES_PD_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
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
        "rule_name": "Native_FF_Rule",
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
