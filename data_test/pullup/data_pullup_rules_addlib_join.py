from payloads.pullup.pl_pullup_rules_addlib_join import PULLUP_RULES_ADDLIB_JOIN_DATASET
from payloads.pullup.pl_pullup_rules_addlib_join1 import PULLUP_RULES_ADDLIB_JOIN1_DATASET

PULLUP_RULES_ADDLIB_JOIN_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_ADDLIB_JOIN_DATASET,
        "ruleNm": "ff_intersection_symbol",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT symbol FROM @{PULLUP_RULES_ADDLIB_JOIN_DATASET} "
                     f"INTERSECT select SYMBOL from @{PULLUP_RULES_ADDLIB_JOIN1_DATASET}\n",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "symbol",
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

PULLUP_RULES_ADDLIB_JOIN_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_ADDLIB_JOIN_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "ff_intersection_symbol",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT symbol FROM {PULLUP_RULES_ADDLIB_JOIN_DATASET}_dataset "
                         f"INTERSECT select "
                         f"SYMBOL from {PULLUP_RULES_ADDLIB_JOIN1_DATASET}_dataset ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 448598,
                "uuid": "313dbc29-51d1-4354-acea-1b4e145b6d21"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT symbol FROM @{PULLUP_RULES_ADDLIB_JOIN_DATASET} "
                             f"INTERSECT select SYMBOL from @{PULLUP_RULES_ADDLIB_JOIN1_DATASET}\n",
            "totalCount": 3088,
            "rowsBreaking": 3088,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
