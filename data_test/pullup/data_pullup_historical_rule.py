from payloads.pullup.pl_pullup_historical_rule import PULLUP_HISTORICAL_RULE_DATASET

PULLUP_HISTORICAL_RULE_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_HISTORICAL_RULE_DATASET,
        "ruleNm": "sqlf_lookuprule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PULLUP_HISTORICAL_RULE_DATASET} A, @t1 B "
                     f"where A.SYMBOL=B.SYMBOL and A.CLOSE=B.CLOSE",
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

PULLUP_HISTORICAL_RULE_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_HISTORICAL_RULE_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "sqlf_lookuprule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {PULLUP_HISTORICAL_RULE_DATASET}_dataset A  ,   @t1 B "
                         f"where A.SYMBOL=B.SYMBOL and A.CLOSE=B.CLOSE ",
            "filterQuery": None,
            "score": 4,
            "perc": 4.404145106673241,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 448891,
                "uuid": "6979d521-b918-4136-93c6-a3c2d0aa722d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PULLUP_HISTORICAL_RULE_DATASET} A, @t1 B "
                             f"where A.SYMBOL=B.SYMBOL and A.CLOSE=B.CLOSE",
            "totalCount": 3088,
            "rowsBreaking": 136,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
