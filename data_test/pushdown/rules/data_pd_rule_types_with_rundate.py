from payloads.pushdown.rules.pl_pd_rule_types_with_rundate import PD_RULE_TYPES_WITH_RUNDATE_DATASET

PD_RULE_WITH_RUNDATE_DEFINITIONS = [
    {
        "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
        "ruleNm": "if_SYMBOL_is_SYMBOL",
        "ruleType": "CUSTOM",
        "ruleValue": "SYMBOL",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "SYMBOL",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "SYMBOL",
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
        "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
        "ruleNm": "DB_RULES_RUNDATE_SQLG_BREAKS",
        "ruleType": "SQLG",
        "ruleValue": "CLOSE >= 25.00 and CLOSE <= 26.00",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "CLOSE",
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
        "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
        "ruleNm": "DB_RULES_RUNDATE",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_RULE_TYPES_WITH_RUNDATE_DATASET} A WHERE A.CLOSE = 25.06",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "CLOSE",
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

PD_RULE_WITH_RUNDATE_DEFINITIONS_OUTPUT = {
    "data": [
        {
            "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "if_SYMBOL_is_SYMBOL",
            "ruleType": "CUSTOM",
            "ruleValue": "SYMBOL not rlike '^([A-Z]{1,4})(:|\\\\.|-){0,1}([A-Z]{1,1})$'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.6800518134715026,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585983,
                "uuid": "b878290d-9217-4d69-94c8-5bf90283ccde"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SYMBOL",
            "totalCount": 3088,
            "rowsBreaking": 21,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "DB_RULES_RUNDATE_SQLG_BREAKS",
            "ruleType": "SQLG",
            "ruleValue": "CLOSE >= 25.00 and CLOSE <= 26.00",
            "filterQuery": None,
            "score": 8,
            "perc": 8.549222797927461,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585984,
                "uuid": "4919f4e5-f892-4ff0-8d63-d1eececd127e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "CLOSE >= 25.00 and CLOSE <= 26.00",
            "totalCount": 3088,
            "rowsBreaking": 264,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_RULE_TYPES_WITH_RUNDATE_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "DB_RULES_RUNDATE",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.nyse where TRADE_DATE = '2018-01-16')"
                         " A WHERE A.CLOSE = 25.06",
            "filterQuery": None,
            "score": 0,
            "perc": 0.2590673575129534,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585982,
                "uuid": "f5cfcd5f-8669-4ad4-b9bd-81b100953a8e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_RULE_TYPES_WITH_RUNDATE_DATASET} A "
                             f"WHERE A.CLOSE = 25.06",
            "totalCount": 3088,
            "rowsBreaking": 8,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
