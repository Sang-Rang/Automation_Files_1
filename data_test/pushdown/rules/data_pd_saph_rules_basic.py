from payloads.pushdown.rules.pl_pd_saph_rules_basic import PD_SAPH_RULES_BASIC_DATASET

PD_SAPH_RULES_BASIC_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "if_ZIP_CODE_is_NULLCHECK",
        "ruleType": "NULLCHECK",
        "ruleValue": "ZIP_CODE",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "ZIP_CODE",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": 1,
        "dimName": "COMPLETENESS",
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "if_GENDER_is_GENDER",
        "ruleType": "CUSTOM",
        "ruleValue": "GENDER",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "GENDER",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "GENDER",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": 4,
        "dimName": "VALIDITY",
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "FF_exception",
        "ruleType": "SQLF",
        "ruleValue": "This rule will cause an exception.",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": "Unexpected exception: \"SAP DBTech JDBC: [257] (at 69): sql syntax error: "
                     "incorrect syntax near \"will\": line 1 col 69 (at pos 69)\"",
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
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_BASIC_DATASET} WHERE $rowCount  > 1000",
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
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "FF_long",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_BASIC_DATASET} WHERE AUTO_YEAR = 2001",
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
        "dataset": PD_SAPH_RULES_BASIC_DATASET,
        "ruleNm": "SIMPLE_STRING",
        "ruleType": "SQLG",
        "ruleValue": "auto_make = 'Ford'",
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

PD_SAPH_RULES_BASIC_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.CUSTOMERS) WHERE 1044  > 1000",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586019,
                "uuid": "a9cfcd8b-bd21-43f1-ae7a-31f183de1697"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_BASIC_DATASET} "
                             f"WHERE $rowCount  > 1000",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "SIMPLE_STRING",
            "ruleType": "SQLG",
            "ruleValue": "auto_make = 'Ford'",
            "filterQuery": None,
            "score": 8,
            "perc": 8.237547892720306,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586020,
                "uuid": "57ad7c33-feb8-4516-8a30-aa0272baf949"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "auto_make = 'Ford'",
            "totalCount": 1044,
            "rowsBreaking": 86,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_ZIP_CODE_is_NULLCHECK",
            "ruleType": "NULLCHECK",
            "ruleValue": "ZIP_CODE",
            "filterQuery": None,
            "score": 48,
            "perc": 48.85057471264368,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586022,
                "uuid": "18c88170-b4aa-484f-92af-35c2243ec411"
            },
            "dimId": 1,
            "dimName": "COMPLETENESS",
            "ruleCondition": "ZIP_CODE",
            "totalCount": 1044,
            "rowsBreaking": 510,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_GENDER_is_GENDER",
            "ruleType": "CUSTOM",
            "ruleValue": "not OCCURRENCES_REGEXPR('^(m|M|male|Male|MALE|f|F|female|Female|FEMALE)$'"
                         " IN \"GENDER\") > 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586018,
                "uuid": "1c2d4fe0-e843-40a2-80c1-7a59e8ced3d5"
            },
            "dimId": 4,
            "dimName": "VALIDITY",
            "ruleCondition": "GENDER",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_long",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.CUSTOMERS) WHERE AUTO_YEAR = 2001",
            "filterQuery": None,
            "score": 4,
            "perc": 4.597701149425287,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586023,
                "uuid": "21569529-d1ae-4d32-8ef5-aff52d54285b"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_BASIC_DATASET} WHERE AUTO_YEAR = 2001",
            "totalCount": 1044,
            "rowsBreaking": 48,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_exception",
            "ruleType": "SQLF",
            "ruleValue": "This rule will cause an exception.",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"SAP DBTech JDBC: [257] (at 69): sql syntax error:"
                         " incorrect syntax near \"will\": line 1 col 69 (at pos 69)\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 1586021,
                "uuid": "74587144-1d37-49d9-a0ae-99934eef3f50"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "This rule will cause an exception.",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
