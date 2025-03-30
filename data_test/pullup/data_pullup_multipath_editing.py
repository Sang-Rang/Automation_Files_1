# pylint: disable-msg=import-error
from utils.constants import PROD_RUN_ID

RULES_ALL_PATHS_DS = "AUTO_ALL_PATHS_RULES_ORACLE_2"  # Not unique err, will this happen again?
RULES_ALL_PATHS_RUN_ID_FULL = f"{PROD_RUN_ID}T00:00:00.000+0000"
RULES_ALL_PATHS_CONN = "APPROVED_ORACLE_UP"
RULES_ALL_PATHS_QUERY = "select * from OWLUSER.LOAN_CUSTOMER"

RULES_ALL_PATHS_V3_SIMPLE1 =     {
    "dataset": "AUTO_ALL_PATHS_RULES_ORACLE_2",
    "ruleNm": "simple_rule",
    "ruleType": "SQLG",
    "ruleValue": "POST_CD_NUM not rlike '^[0-9]{5}(?:-[0-9]{4})?$'",
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
    "ruleValueBuilder": None,
    "previewLimit": 6,
    "runTimeLimit": 30.0,
    "scoringScheme": 0,
    "filterQuery": None,
    "tolerance": 0,
}

RULES_ALL_PATHS_V3_FREEFORM1 = {
    "dataset": RULES_ALL_PATHS_DS,
    "ruleNm": "if_ADJ_RATE_CHANGE_is_EMPTY_freeform",
    "ruleType": "SQLG",
    "ruleValue": "ADJ_RATE_CHANGE = ''",
    "points": 1,
    "perc": 1.0,
    "ruleRepo": "",
    "isActive": 1,
    "userNm": None,
    "exception": None,
    "columnName": "ADJ_RATE_CHANGE",
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
}

RULES_ALL_PATHS_V3_FREEFORM2 = {
    "dataset": RULES_ALL_PATHS_DS,
    "ruleNm": "if_ADJ_RATE_CHANGE_is_EMPTY_freeform",
    "ruleType": "SQLG",
    "ruleValue": "PRSNL_LN_RATE = ''",
    "points": 1,
    "perc": 1.0,
    "ruleRepo": "",
    "isActive": 1,
    "userNm": None,
    "exception": None,
    "columnName": "ADJ_RATE_CHANGE",
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
}


RULES_ALL_PATHS_V2_RULE = {
    "ruletype": "SQLG",
    "primarycolumn": "ADJ_RATE_CHANGE",
    "dataset": RULES_ALL_PATHS_DS,
    "rulenm": "ADJ_RATE_CHANGE_unique",
    "where": "ADJ_RATE_CHANGE.$uniqueCount != $rowCount",
    "points": 1,
    "perc": 1,
    "previewlimit": 6,
    "runTimeLimit": 30,
}

RULES_ALL_PATHS_V2_QUICK_RULE = {
    "dataset": RULES_ALL_PATHS_DS,
    "ruletype": "NULLCHECK",
    "rulenm": "if_AUTO_LN_RATE_is_NULL",
    "where": "AUTO_LN_RATE",
    "column": "AUTO_LN_RATE",
    "points": 1,
    "rulerepo": None,
    "perc": 1,
    "primarycolumn": "AUTO_LN_RATE",
}

RULES_ALL_PATHS_V2_QUICK_RULE2 = {
    "dataset": RULES_ALL_PATHS_DS,
    "ruletype": "NULLCHECK",
    "rulenm": "if_AUTO_LN_RATE_is_NULL",
    "where": "REFINANCE_RATE",
    "column": "REFINANCE_RATE",
    "points": 1,
    "rulerepo": None,
    "perc": 1,
    "primarycolumn": "REFINANCE_RATE",
}

EXPECTED_RULE_OUT1 = {
    "data": [
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "simple_rule",
            "ruleType": "SQLG",
            "ruleValue": "POST_CD_NUM not rlike '^[0-9]{5}(?:-[0-9]{4})?$'",
            "filterQuery": None,
            "score": 3,
            "perc": 3.864734247326851,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439726,
                "uuid": "7bbc6557-4338-44d0-99d6-4b11068d916f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "POST_CD_NUM not rlike '^[0-9]{5}(?:-[0-9]{4})?$'",
            "totalCount": 207,
            "rowsBreaking": 8,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "ADJ_RATE_CHANGE_unique",
            "ruleType": "SQLG",
            "ruleValue": "117 != 207",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439725,
                "uuid": "4727c3fd-0fb7-468a-bc0d-754b1a94bbe5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "ADJ_RATE_CHANGE.$uniqueCount != $rowCount",
            "totalCount": 207,
            "rowsBreaking": 207,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "if_ADJ_RATE_CHANGE_is_EMPTY_freeform",
            "ruleType": "SQLG",
            "ruleValue": "ADJ_RATE_CHANGE = ''",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 439724,
                "uuid": "3d25f2a1-f5a8-43f3-aada-fe8e260ee67a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "ADJ_RATE_CHANGE = ''",
            "totalCount": 207,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "if_AUTO_LN_RATE_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "AUTO_LN_RATE",
            "filterQuery": None,
            "score": 28,
            "perc": 28.502416610717773,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439723,
                "uuid": "1942620b-fa81-4d50-a3d7-a594f23be9e6"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "AUTO_LN_RATE",
            "totalCount": 207,
            "rowsBreaking": 59,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

EXPECTED_RULE_OUT2 = {
    "data": [
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "simple_rule",
            "ruleType": "SQLG",
            "ruleValue": "POST_CD_NUM not rlike '^[0-9]{5}(?:-[0-9]{4})?$'",
            "filterQuery": None,
            "score": 3,
            "perc": 3.864734247326851,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439854,
                "uuid": "cd172527-041d-4722-8bdf-e5b19e5c4189"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "POST_CD_NUM not rlike '^[0-9]{5}(?:-[0-9]{4})?$'",
            "totalCount": 207,
            "rowsBreaking": 8,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "if_ADJ_RATE_CHANGE_is_EMPTY_freeform",
            "ruleType": "SQLG",
            "ruleValue": "PRSNL_LN_RATE = ''",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 439853,
                "uuid": "d1259bbf-0f62-44b2-950d-4f2966a338a4"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "PRSNL_LN_RATE = ''",
            "totalCount": 207,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": "PASSING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "ADJ_RATE_CHANGE_unique",
            "ruleType": "SQLG",
            "ruleValue": "117 != 207",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439852,
                "uuid": "d5571db7-5c69-413a-93cd-7851daaa2854"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "ADJ_RATE_CHANGE.$uniqueCount != $rowCount",
            "totalCount": 207,
            "rowsBreaking": 207,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": RULES_ALL_PATHS_DS,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "if_AUTO_LN_RATE_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "REFINANCE_RATE",
            "filterQuery": None,
            "score": 28,
            "perc": 28.502416610717773,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 439851,
                "uuid": "49644221-fc07-488c-92ca-6ab9feb17edc"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "REFINANCE_RATE",
            "totalCount": 207,
            "rowsBreaking": 59,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
