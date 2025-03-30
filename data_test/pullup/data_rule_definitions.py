from payloads.pullup.pl_rule_definitions import RULE_DEFINITIONS_DATASET

RULE_DEFINITIONS_RULE_NAME = "Rule_Definitions_Rule_Name"
INITIAL_BUSINESS_DESCRIPTION = "This rule is used to test rule definitions"
UPDATED_BUSINESS_DESCRIPTION = "This rule has been updated"

RULE_DEFINITIONS_RULE_DEFINITIONS = [
    {
        "dataset": RULE_DEFINITIONS_DATASET,
        "ruleNm": RULE_DEFINITIONS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{RULE_DEFINITIONS_DATASET}",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "name",
        "businessCategory": "Category_string",
        "businessDesc": INITIAL_BUSINESS_DESCRIPTION,
        "dimId": 4,
        "dimName": "VALIDITY",
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]


RULE_DEFINITIONS_RULE_DEFINITIONS_UPDATED = [
    {
        "dataset": RULE_DEFINITIONS_DATASET,
        "ruleNm": RULE_DEFINITIONS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{RULE_DEFINITIONS_DATASET}",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": "Category_string",
        "businessDesc": UPDATED_BUSINESS_DESCRIPTION,
        "dimId": 4,
        "dimName": "VALIDITY",
        "ruleValueBuilder": None,
        "previewLimit": 5,
        "runTimeLimit": 15.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]
