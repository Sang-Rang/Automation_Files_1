from utils.constants import PROD_RUN_ID

CONN_DC_RULE_REGEX = "APPROVED_POSTGRES_UP"
RULE_SAVED_MSG = "Rule Saved: Column data class has been automatically updated"
PROD_RUN_ID_FULL = f"{PROD_RUN_ID}T00:00:00.000+0000"

PULLUP_RULES_DATA_CLASS_REGEX_DATASET = "AUTO_RULE_DATACLASS_REGEX"
DS_NAME_RUN_RULE_DISCOVERY = "AUTO_RULE_DISCOVERY"

QUERY_DC_RULE_REGEX = "select * from public.claims_detail"

RULE_NAME_DC_NO_REGEX = "DATACLASS_NO_REGEX"
RULE_NAME_DC_REGEX = "DATACLASS_WITH_REGEX"

PL_V2_CREATE_RULE_DC_REGEX = {
    "ruleRepoId": None,
    "ruleName": RULE_NAME_DC_REGEX,
    "ruleValue": "^\\d{4}-\\d{2}-\\d{2}",
    "isRegex": 1,
    "ruleType": "SQLG",
    "ruleDescription": "",
    "sensitiveLabelId": "None",
    "ruleColumnName": "",
    "ruleColumnType": "",
    "ruleColumnPercentMatch": 75,
    "isEditable": 1,
    "isSemantic": 1,
    "ruleTyp": "SQLG",
    "semanticName": RULE_NAME_DC_REGEX,
    "example_1": "",
    "example_2": "",
    "example_3": "",
    "ruleOperator": "rlike",
    "allowEmpty": 0,
    "allowNull": 0,
}
PL_V2_CREATE_RULE_DC_NO_REGEX = {
    "ruleRepoId": None,
    "ruleName": RULE_NAME_DC_NO_REGEX,
    "ruleValue": "('AFU','RAD','EMR')",
    "isRegex": 0,
    "ruleType": "SQLG",
    "ruleDescription": "",
    "sensitiveLabelId": "None",
    "ruleColumnName": "",
    "ruleColumnType": "",
    "ruleColumnPercentMatch": 75,
    "isEditable": 1,
    "isSemantic": 1,
    "ruleTyp": "SQLG",
    "semanticName": RULE_NAME_DC_NO_REGEX,
    "example_1": "",
    "example_2": "",
    "example_3": "",
    "ruleOperator": "in",
    "allowEmpty": 0,
    "allowNull": 0,
}

PL_V2_ASSIGN_RULE_NO_REGEX = {
    "rulerepo": RULE_NAME_DC_NO_REGEX,
    "dataset": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
    "ruleBar": "Simple Rule",
    "from": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
    "ruletype": "CUSTOM",
    "primarycolumn": "CD_BGN_PAYMENT_DTE ",
    "where": "CD_BGN_PAYMENT_DTE",
    "rulenm": "if_CD_BGN_PAYMENT_DTE_is_DATA_CLASS_WITHOUT_REGEX",
    "dimid": None,
    "businesscat": None,
    "businessdesc": None,
    "previewlimit": None,
    "runTimeLimit": None,
    "points": 1,
    "perc": 1,
}
PL_V2_ASSIGN_RULE_REGEX = {
    "rulerepo": RULE_NAME_DC_REGEX,
    "dataset": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
    "ruleBar": "Simple Rule",
    "from": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
    "ruletype": "CUSTOM",
    "primarycolumn": "CD_BENEFIT_CODE ",
    "where": "CD_BENEFIT_CODE",
    "rulenm": "if_CD_BENEFIT_CODE_is_DATACLASS_WITH_REGEX",
    "dimid": None,
    "businesscat": None,
    "businessdesc": None,
    "previewlimit": None,
    "runTimeLimit": None,
    "points": 1,
    "perc": 1,
}

PULLUP_RULES_DATA_CLASS_REGEX_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "if_CD_BGN_PAYMENT_DTE_is_DATA_CLASS_WITHOUT_REGEX",
            "ruleType": "CUSTOM",
            "ruleValue": "CD_BGN_PAYMENT_DTE",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449623,
                "uuid": "db3d71e4-b575-43c5-a3d9-98cd64b4f447"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "CD_BGN_PAYMENT_DTE",
            "totalCount": 3000,
            "rowsBreaking": 3000,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_DATA_CLASS_REGEX_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "if_CD_BENEFIT_CODE_is_DATACLASS_WITH_REGEX",
            "ruleType": "CUSTOM",
            "ruleValue": "CD_BENEFIT_CODE",
            "filterQuery": None,
            "score": 95,
            "perc": 95.39999961853027,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449622,
                "uuid": "b3b7850b-4f9d-4ee6-b6e8-9d3ae31e8527"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "CD_BENEFIT_CODE",
            "totalCount": 3000,
            "rowsBreaking": 2862,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
