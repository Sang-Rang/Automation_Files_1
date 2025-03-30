from payloads.dq_dgc_integration.pl_dq_dgc_complex_rule_querie import (
    DS_DEF_DGC_COMPLEX_RULE_NAME,
    DS_DEF_DGC_COMPLEX_RULE_SECONDARY_NAME,
)

DERIVED_RULE_NAME = "derivedrule_symbol_open_close_br"
ALIAS_RULE_NAME = "ff_alias_br"
INNERJOIN_RULE_NAME = "Innerjoin"
LOOKUP_RULE_NAME = "lookuprule"


DQ_DGC_COMPLEX_RULE_DEFINITIONS = [
    {
        "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
        "ruleNm": LOOKUP_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} a,@t1 b "
                     f"where a.symbol = b.symbol and a.close = b.close and a.symbol = 'COL'",
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
        "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
        "ruleNm": INNERJOIN_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} A "
                     f"INNER JOIN @{DS_DEF_DGC_COMPLEX_RULE_SECONDARY_NAME} B "
                     f"ON A.exch = B.exch AND A.symbol = 'COL'",
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
        "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
        "ruleNm": ALIAS_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT close AS NYSE_CLOSE , symbol AS NYSE_SYMBOL "
                     f"FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} where symbol like 'CM%'",
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
        "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
        "ruleNm": DERIVED_RULE_NAME,
        "ruleType": "SQLF",
        "ruleValue": f"SELECT symbol,((close-open) /open) * 100 AS price_change_percentage "
                     f"FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME}",
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


DQ_DGC_COMPLEX_RULE_DEFINITIONS_OUTPUT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": LOOKUP_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_COMPLEX_RULE_NAME}_dataset a   ,   @t1 b "
                         f"where a.symbol = b.symbol and a.close = b.close and a.symbol = 'COL' ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.03987744858022779,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 427713,
                "uuid": "3579c93a-0b9b-433c-8b55-3420925cc08a"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} a,@t1 b "
                             f"where a.symbol = b.symbol and a.close = b.close "
                             f"and a.symbol = 'COL'",
            "totalCount": 102815,
            "rowsBreaking": 41,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": INNERJOIN_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_COMPLEX_RULE_NAME}_dataset A "
                         f"INNER JOIN {DS_DEF_DGC_COMPLEX_RULE_SECONDARY_NAME}_dataset B "
                         f"ON A.exch = B.exch AND A.symbol = 'COL' ",
            "filterQuery": None,
            "score": 3300,
            "perc": 3300.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 427714,
                "uuid": "4f6b3060-0669-43dd-b528-2dcb46e07908"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} A "
                             f"INNER JOIN @{DS_DEF_DGC_COMPLEX_RULE_SECONDARY_NAME} B "
                             f"ON A.exch = B.exch AND A.symbol = 'COL'",
            "totalCount": 102815,
            "rowsBreaking": 3392895,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": ALIAS_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": f"SELECT close AS NYSE_CLOSE   ,   symbol AS NYSE_SYMBOL "
                         f"FROM {DS_DEF_DGC_COMPLEX_RULE_NAME}_dataset where symbol like 'CM%' ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.5777366925030947,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 427694,
                "uuid": "7042abdc-7176-4104-afc5-efd03cdbc944"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT close AS NYSE_CLOSE , symbol AS NYSE_SYMBOL "
                             f"FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME} where symbol like 'CM%'",
            "totalCount": 102815,
            "rowsBreaking": 594,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_COMPLEX_RULE_NAME,
            "runId": "2024-11-12T00:00:00.000+0000",
            "ruleNm": DERIVED_RULE_NAME,
            "ruleType": "SQLF",
            "ruleValue": f"SELECT symbol  ,  ((close-open) /open) * 100 AS price_change_percentage "
                         f"FROM {DS_DEF_DGC_COMPLEX_RULE_NAME}_dataset ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 427693,
                "uuid": "1023a14c-e0c7-4957-8556-b3baedea30d0"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT symbol,((close-open) /open) * 100 AS price_change_percentage "
                             f"FROM @{DS_DEF_DGC_COMPLEX_RULE_NAME}",
            "totalCount": 102815,
            "rowsBreaking": 102815,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
