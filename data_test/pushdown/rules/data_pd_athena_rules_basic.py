from payloads.pushdown.rules.pl_pd_athena_rules_basic import PD_ATHENA_RULES_BASIC_DATASET

PD_ATHENA_RULES_BASIC_RULE_DEFINITIONS = [
    {
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
        "ruleNm": "if_zip_code_is_NULL",
        "ruleType": "NULLCHECK",
        "ruleValue": "zip_code",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "zip_code",
        "businessCategory": None,
        "businessDesc": None,
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
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
        "ruleNm": "if_gender_is_GENDER",
        "ruleType": "CUSTOM",
        "ruleValue": "gender",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "GENDER",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "gender",
        "businessCategory": None,
        "businessDesc": None,
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
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
        "ruleNm": "FF_exception",
        "ruleType": "SQLF",
        "ruleValue": "This rule will cause an exception.",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been thrown "
                     "from the AWS Athena client. line 1:69: mismatched input 'will'. Expecting: "
                     "'(', ')', ',', 'AS', 'CROSS', 'EXCEPT', 'FETCH', 'FULL', 'GROUP', 'HAVING', "
                     "'INNER', 'INTERSECT', 'JOIN', 'LEFT', 'LIMIT', 'MATCH_RECOGNIZE', 'NATURAL', "
                     "'OFFSET', 'ORDER', 'RIGHT', 'TABLESAMPLE', 'UNION', 'WHERE', 'WINDOW', <EOF>,"
                     " <identifier> [Execution ID not available]\"",
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
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PD_ATHENA_RULES_BASIC_DATASET} where $rowCount > 1000",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
        "ruleNm": "FF_long",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PD_ATHENA_RULES_BASIC_DATASET} where auto_year = 2001",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_ATHENA_RULES_BASIC_DATASET,
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
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PD_ATHENA_RULES_BASIC_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "select * from (select * from default.customers) where 1044 > 1000",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586124,
                "uuid": "1639f378-b54d-4a55-9f90-0457865f6e2c"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * "
                             f"from @{PD_ATHENA_RULES_BASIC_DATASET} "
                             f"where $rowCount > 1000",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
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
                "id": 1586125,
                "uuid": "b8270051-48ad-460c-9cdc-6c7dd58b7d24"
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
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_zip_code_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "zip_code",
            "filterQuery": None,
            "score": 48,
            "perc": 48.85057471264368,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586127,
                "uuid": "2978fe45-93c4-43ae-9d06-8877f5f4291b"
            },
            "dimId": 1,
            "dimName": "COMPLETENESS",
            "ruleCondition": "zip_code",
            "totalCount": 1044,
            "rowsBreaking": 510,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_gender_is_GENDER",
            "ruleType": "CUSTOM",
            "ruleValue": "gender",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1586129,
                "uuid": "4af613c0-be65-490b-9e2e-4404565361ab"
            },
            "dimId": 4,
            "dimName": "VALIDITY",
            "ruleCondition": "gender",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_long",
            "ruleType": "SQLF",
            "ruleValue": "select * from (select * from default.customers) where auto_year = 2001",
            "filterQuery": None,
            "score": 4,
            "perc": 4.597701149425287,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586128,
                "uuid": "89e23338-a8b3-424b-8524-279abce46dab"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * "
                             f"from @{PD_ATHENA_RULES_BASIC_DATASET} "
                             f"where auto_year = 2001",
            "totalCount": 1044,
            "rowsBreaking": 48,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_exception",
            "ruleType": "SQLF",
            "ruleValue": "This rule will cause an exception.",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Simba][AthenaJDBC](100071) An error has been "
                         "thrown from the AWS Athena client. line 1:69: mismatched input 'will'. "
                         "Expecting: '(', ')', ',', 'AS', 'CROSS', 'EXCEPT', 'FETCH', 'FULL', "
                         "'GROUP', 'HAVING', 'INNER', 'INTERSECT', 'JOIN', 'LEFT', 'LIMIT', "
                         "'MATCH_RECOGNIZE', 'NATURAL', 'OFFSET', 'ORDER', 'RIGHT', 'TABLESAMPLE', "
                         "'UNION', 'WHERE', 'WINDOW', <EOF>, <identifier> "
                         "[Execution ID not available]\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 1586126,
                "uuid": "b6b97283-fcbb-4257-abbe-746541a59ec3"
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
