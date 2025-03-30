# pylint: disable-msg=import-error
# pylint: disable=anomalous-backslash-in-string

# Note: Regex string for test triggers anomalous backslash error, so disabled.

from datetime import datetime
from utils.constants import PROD_RUN_ID

NOW = datetime.now().strftime("%Y%m%d%H%M%S")
INPUTS_TEMPLATE = "2018-01-05 00:00:00.0"
PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET = "AUTO__POSTGRES_RULE_TEMPLATE" + NOW
RUN_ID_FULL_TEMPLATE = f"{PROD_RUN_ID}T00:00:00.000+0000"
RULE_NAME_TEMPLATE = "AutoTemplate_" + str(NOW)
RULE_DESC_TEMPLATE = "AutoTemplateDesc_" + str(NOW)
CONNECTION_TEMPLATE = "APPROVED_POSTGRES_UP"
QUERY_TEMPLATE = "select * from public.nyse"
COLUMN_TEMPLATE = "trade_date"
COLUMN_BREAK_TEMPLATE = "symbol"

# Matches: 2017-01-31 11:22:33.0
REGEX_TEMPLATE = r"^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{1}$"

# Matches: 2017-01-31 11:22:33.0
RULE_REGEX_TEMPLATE = r"^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{1}$"

PL_GENERAL = {"dataset": PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET, "runId": PROD_RUN_ID}
PL_VALIDATE_TEMPLATE = {
    "regex": REGEX_TEMPLATE,
    "inputs": f"{INPUTS_TEMPLATE}",
}
PL_CREATE_CUSTOM_TEMPLATE = {
    "autoScan": 0,
    "isEditable": 1,
    "isRegex": 1,
    "isSemantic": 0,
    "ruleAssert": 0,
    "ruleDescription": RULE_DESC_TEMPLATE,
    "ruleName": RULE_NAME_TEMPLATE,
    "ruleTyp": "SQLG",
    "ruleValue": REGEX_TEMPLATE,
}
PL_DELETE_CUSTOM_TEMPLATE = {"customrulename": RULE_NAME_TEMPLATE}
PL_ADD_RULE_TEMPLATE = {
    "dataset": PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
    "ruleNm": RULE_NAME_TEMPLATE,
    "ruleType": "CUSTOM",
    "ruleValue": COLUMN_TEMPLATE,
    "points": 1,
    "ruleRepo": RULE_NAME_TEMPLATE,
    "perc": 1,
    "columnName": COLUMN_TEMPLATE,
    "isActive": 1,
    "scoringScheme": 0,
    "filterQuery": None,
    "tolerance": 0
}
PL_ADD_RULE_BREAK_TEMPLATE = {
    "dataset": PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
    "ruleNm": f"if_{COLUMN_BREAK_TEMPLATE}_is_{COLUMN_BREAK_TEMPLATE.upper()}",
    "ruleType": "CUSTOM",
    "ruleValue": COLUMN_BREAK_TEMPLATE,
    "points": 1,
    "ruleRepo": COLUMN_BREAK_TEMPLATE.upper(),
    "perc": 1,
    "columnName": COLUMN_BREAK_TEMPLATE,
    "previewLimit": 6,
    "runTimeLimit": 30,
    "isActive": 1,
    "scoringScheme": 0,
    "filterQuery": None,
    "tolerance": 0
}
EX_RESPONSE_TEMPLATE = {
    "condition": f"$colNm not rlike '{REGEX_TEMPLATE}'",
    "breaks": "Record Passing",
}
EX_CREATE_RULE = {
    "ruleType": "CUSTOM",
    "ruleValue": "trade_date",
    "points": 1,
    "perc": 1.0,
    "isActive": 1,
    "userNm": None,
    "exception": None,
    "columnName": "trade_date",
    "businessCategory": None,
    "businessDesc": None,
    "dimId": None,
    "dimName": None,
    "ruleValueBuilder": None,
    "previewLimit": 6,
    "runTimeLimit": 30.0,
    "scoringScheme": 0,
}
EX_CREATE_RULE2 = {
    "ruleNm": "if_symbol_is_SYMBOL",
    "ruleType": "CUSTOM",
    "ruleValue": "symbol",
    "points": 1,
    "perc": 1.0,
    "ruleRepo": "SYMBOL",
    "isActive": 1,
    "userNm": None,
    "exception": None,
    "columnName": "symbol",
    "businessCategory": None,
    "businessDesc": None,
    "dimId": None,
    "dimName": None,
    "ruleValueBuilder": None,
    "previewLimit": 6,
    "runTimeLimit": 30.0,
    "scoringScheme": 0,
}
PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "if_symbol_is_SYMBOL",
            "ruleType": "CUSTOM",
            "ruleValue": "symbol",
            "filterQuery": None,
            "score": 0,
            "perc": 0.6740261800587177,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449553,
                "uuid": "ff0d23dc-c189-4fe8-a75b-4152cb772940"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "symbol",
            "totalCount": 102815,
            "rowsBreaking": 693,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_CREATE_APPLY_TEMPLATE_RULE_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": RULE_NAME_TEMPLATE,
            "ruleType": "CUSTOM",
            "ruleValue": "trade_date",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 449552,
                "uuid": "bb6bc2ba-86f5-40af-995d-2357cc0a15ca"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trade_date",
            "totalCount": 102815,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        }
    ]
}
