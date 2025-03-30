from payloads.pullup.pl_pullup_rules_link_id_breaks import PULLUP_RULES_LINK_ID_BREAKS_DATASET

PULLUP_RULES_LINK_ID_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
        "ruleNm": "freeform_symbol_tradedate_35",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PULLUP_RULES_LINK_ID_BREAKS_DATASET} A "
                     f"where A.SYMBOL = 'DD-A'and A.TRADE_DATE != '2023-12-19 00:00:00.0'  ",
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
        "previewLimit": 35,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
        "ruleNm": "volume_close_sqlg",
        "ruleType": "SQLG",
        "ruleValue": "CLOSE = '25.30' and VOLUME > 0",
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
        "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
        "ruleNm": "symbol_tradedate_sqlgchk",
        "ruleType": "SQLG",
        "ruleValue": "SYMBOL = 'DD-A'and TRADE_DATE != '2023-12-19 00:00:00.0'",
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
        "previewLimit": 40,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "freeform_symbol_tradedate_35",
            "ruleType": "SQLF",
            "ruleValue": f"select * from {PULLUP_RULES_LINK_ID_BREAKS_DATASET}_dataset A "
                         f"where A.SYMBOL = 'DD-A'and A.TRADE_DATE != '2023-12-19 00:00:00.0' ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.03374925290700048,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443391,
                "uuid": "4fcaaf94-2d0f-4721-9a1f-a2676500d319"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * from @{PULLUP_RULES_LINK_ID_BREAKS_DATASET} A "
                             f"where A.SYMBOL = 'DD-A'"
                             f"and A.TRADE_DATE != '2023-12-19 00:00:00.0'  ",
            "totalCount": 103706,
            "rowsBreaking": 35,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "volume_close_sqlg",
            "ruleType": "SQLG",
            "ruleValue": "CLOSE = '25.30' and VOLUME > 0",
            "filterQuery": None,
            "score": 0,
            "perc": 0.1745318528264761,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443390,
                "uuid": "752f70db-e2c6-4aa6-ba85-62f1c4b5ab9f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "CLOSE = '25.30' and VOLUME > 0",
            "totalCount": 103706,
            "rowsBreaking": 181,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "symbol_tradedate_sqlgchk",
            "ruleType": "SQLG",
            "ruleValue": "SYMBOL = 'DD-A'and TRADE_DATE != '2023-12-19 00:00:00.0'",
            "filterQuery": None,
            "score": 0,
            "perc": 0.03374925290700048,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443389,
                "uuid": "aaf70013-37cb-4178-9e6d-64e85b0184d8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SYMBOL = 'DD-A'and TRADE_DATE != '2023-12-19 00:00:00.0'",
            "totalCount": 103706,
            "rowsBreaking": 35,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS = [
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-07 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-25 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2022-05-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2022-05-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-07 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-25 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2022-05-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2022-05-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AB~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AB~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AFSS~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AFST~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGO-F~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGO-F~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHL-D~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHT-F~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHT-F~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AJXA~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AJXA~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AMH-G~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ARNC~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ARR~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2017-12-07 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB-D~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ATU~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-D~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-E~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-F~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-G~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BFR~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BK-C~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BXP-B~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CDR-B~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CDR-B~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CFR-A~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CIM-A~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-B~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-H~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-I~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-J~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-J~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CMR-B~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-G~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-P~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-P~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COR-Z~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2022-05-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2022-05-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-A~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-A~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-B~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DCM~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DDR-K~|2018-01-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DLR-G~|2018-01-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DS-C~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DSXN~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DTW~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DTW~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DX-A~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ECCY~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ECCY~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ENO~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EPR-F~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EPR-F~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EQCO~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EQCO~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ETO~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "FRT-C~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GMR-A~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GPJA~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HCC~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HT-E~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HTH~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "IVR-A~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "JBK~|2018-01-03 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "JMPD~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KAP~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KAP~|2022-05-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KIM-J~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KYN-F~|2018-01-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-15 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-27 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MCV~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MCV~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2017-12-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2018-01-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MIT-A~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MLR~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MSCA~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MSCA~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-07 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NI~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2018-01-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-E~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NNN-E~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NS-C~|2017-12-14 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OAK-A~|2017-12-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OMF~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OSLE~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OSLE~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PFK~|2017-12-06 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PMT-B~|2017-12-18 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PMT-B~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PNC-Q~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-B~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-C~|2017-12-22 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-F~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-U~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2018-01-10 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "REX-A~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "REX-A~|2018-01-16 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2017-12-20 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-29 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2018-01-04 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RTEC~|2018-01-08 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SBBC~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SCA~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SCA~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SGZA~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SLDA~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SOJC~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SSWN~|2017-12-05 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SSWN~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-B~|2017-12-21 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-B~|2018-01-11 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-D~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STL~|2017-12-01 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STL~|2017-12-13 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SWJ~|2017-12-19 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TCO-K~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TCO-K~|2018-01-09 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "THGA~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TNP-B~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TNP-E~|2017-12-28 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VNO-K~|2017-12-26 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VNO-L~|2017-12-12 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VPG~|2018-01-02 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VR-A~|2017-12-07 00:00:00.0"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-05-21T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "WFC-X~|2018-01-02 00:00:00.0"
  }
]

PULLUP_RULES_LINK_ID_BREAKS_EXPECTED_BREAKS_V2 = [
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-07 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-25 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2022-05-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "freeform_symbol_tradedate_35",
    "linkId": "DD-A~|2022-05-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-07 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-25 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2022-05-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "symbol_tradedate_sqlgchk",
    "linkId": "DD-A~|2022-05-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AB~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AB~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-A~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ABR-B~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AFSS~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AFST~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGM-A~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGO-F~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AGO-F~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHL-D~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHT-F~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AHT-F~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AJXA~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AJXA~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "AMH-G~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ARNC~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ARR~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2017-12-07 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ASB-D~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ATU~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-D~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-E~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-F~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BBT-G~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BFR~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BK-C~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "BXP-B~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CDR-B~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CDR-B~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CEQP~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CFR-A~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CIM-A~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-B~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-H~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-I~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-J~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CLN-J~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CMR-B~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-G~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-P~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COF-P~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "COR-Z~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2022-05-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CTW~|2022-05-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-A~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-A~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "CYS-B~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DCM~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DDR-K~|2018-01-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DLR-G~|2018-01-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DS-C~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DSXN~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DTW~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DTW~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "DX-A~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EAE~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ECCY~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ECCY~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ELJ~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ENO~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EPR-F~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EPR-F~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EQCO~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "EQCO~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "ETO~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "FRT-C~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GDV-G~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GMR-A~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "GPJA~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HCC~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HT-E~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "HTH~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "INN-D~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "IVR-A~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "JBK~|2018-01-03 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "JMPD~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KAP~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KAP~|2022-05-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KIM-J~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "KYN-F~|2018-01-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-15 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-27 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "LMHB~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MCV~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MCV~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2017-12-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MDLQ~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MFA-B~|2018-01-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MIT-A~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MLR~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MSCA~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MSCA~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-07 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "MVCB~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NI~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-C~|2018-01-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NLY-E~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NNN-E~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "NS-C~|2017-12-14 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OAK-A~|2017-12-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OMF~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OSLE~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "OSLE~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PFK~|2017-12-06 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PMT-B~|2017-12-18 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PMT-B~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PNC-Q~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-B~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-C~|2017-12-22 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSA-F~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-U~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "PSB-V~|2018-01-10 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "REX-A~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "REX-A~|2018-01-16 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2017-12-20 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RF-A~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2017-12-29 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RMP.P~|2018-01-04 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "RTEC~|2018-01-08 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SBBC~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SCA~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SCA~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SGZA~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SLDA~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SOJC~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SSWN~|2017-12-05 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SSWN~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-B~|2017-12-21 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-B~|2018-01-11 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STA-D~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STL~|2017-12-01 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "STL~|2017-12-13 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "SWJ~|2017-12-19 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TCO-K~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TCO-K~|2018-01-09 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "THGA~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TNP-B~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "TNP-E~|2017-12-28 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VNO-K~|2017-12-26 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VNO-L~|2017-12-12 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VPG~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "VR-A~|2017-12-07 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  },
  {
    "dataset": PULLUP_RULES_LINK_ID_BREAKS_DATASET,
    "runId": "2023-09-26T00:00:00.000+0000",
    "ruleNm": "volume_close_sqlg",
    "linkId": "WFC-X~|2018-01-02 00:00:00.0",
    "runIdStr": "2023-09-26 00:00:00"
  }
]
