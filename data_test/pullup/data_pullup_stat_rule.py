from payloads.pullup.pl_pullup_stat_rule import PULLUP_STAT_RULE_DATASET

PULLUP_STAT_RULE_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "sqlg_rulebreak_minchk",
        "ruleType": "SQLG",
        "ruleValue": "auto_make.$min = 'Acura'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "auto_make",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "sqlf_automake_br_rule",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PULLUP_STAT_RULE_DATASET} where auto_make.$min = 'Acura'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "auto_make",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "sqlg_idmeanchk_br_rule",
        "ruleType": "SQLG",
        "ruleValue": "id.$mean < 500",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "id_stat_passrule",
        "ruleType": "SQLG",
        "ruleValue": "id.$mean > 500",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "sqlf_stat_pass_rule",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PULLUP_STAT_RULE_DATASET} where auto_make.$min != 'Acura'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_STAT_RULE_DATASET,
        "ruleNm": "sqlg_min_rulepass",
        "ruleType": "SQLG",
        "ruleValue": "auto_make.$min != 'Acura'  ",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "auto_make",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "{\"condition\":\"AND\",\"rules\":[{\"id\":null,\"field\":null,"
                            "\"type\":null,\"input\":null,\"operator\":null}],\"not\":false,"
                            "\"valid\":false}",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PULLUP_STAT_RULE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlg_min_rulepass",
            "ruleType": "SQLG",
            "ruleValue": "'Acura' != 'Acura'  ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 443384,
                "uuid": "46407a33-2d30-46fd-a99a-7c5d95b46979"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "auto_make.$min != 'Acura'  ",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf_stat_pass_rule",
            "ruleType": "SQLF",
            "ruleValue": f"select * from {PULLUP_STAT_RULE_DATASET}_dataset "
                         f"where 'Acura' != 'Acura' ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 443383,
                "uuid": "919e7102-b16f-455c-af93-2635613d3ff6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * from @{PULLUP_STAT_RULE_DATASET} "
                             f"where auto_make.$min != 'Acura'",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "id_stat_passrule",
            "ruleType": "SQLG",
            "ruleValue": "479.65900383141764 > 500",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 443385,
                "uuid": "38f76011-47ec-48a2-b9c4-96f55e16c518"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "id.$mean > 500",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlg_idmeanchk_br_rule",
            "ruleType": "SQLG",
            "ruleValue": "479.65900383141764 < 500",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443387,
                "uuid": "4fff5fd9-64b0-46ad-a586-643ef85fd0b0"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "id.$mean < 500",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf_automake_br_rule",
            "ruleType": "SQLF",
            "ruleValue": f"select * from {PULLUP_STAT_RULE_DATASET}_dataset "
                         f"where 'Acura' = 'Acura' ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443388,
                "uuid": "7bf351a1-7d4c-4de4-a9e2-073c68dda638"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * from @{PULLUP_STAT_RULE_DATASET} "
                             f"where auto_make.$min = 'Acura'",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_STAT_RULE_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlg_rulebreak_minchk",
            "ruleType": "SQLG",
            "ruleValue": "'Acura' = 'Acura'",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443386,
                "uuid": "0aababd1-0c4d-4dce-83d3-2bc8518a4d32"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "auto_make.$min = 'Acura'",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
