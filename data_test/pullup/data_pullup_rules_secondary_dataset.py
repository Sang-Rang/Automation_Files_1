from payloads.pullup.pl_pullup_rules_secondary_dataset import PULLUP_RULES_SECONDARY_DATASET_DATASET
from payloads.pullup.pl_pullup_rules_secondary_dataset_1 import (
    PULLUP_RULES_SECONDARY_DATASET1_DATASET,
)

PULLUP_RULES_SECONDARY_DATASET_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_SECONDARY_DATASET_DATASET,
        "ruleNm": "innerjoin_wb_2tables",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PULLUP_RULES_SECONDARY_DATASET_DATASET} A "
                     f"INNER JOIN @{PULLUP_RULES_SECONDARY_DATASET1_DATASET} B "
                     f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH limit 10\n",
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
        "dataset": PULLUP_RULES_SECONDARY_DATASET_DATASET,
        "ruleNm": "complex_rule_from_jdbc_2_jdbc",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PULLUP_RULES_SECONDARY_DATASET_DATASET} A "
                     f"INNER JOIN @{PULLUP_RULES_SECONDARY_DATASET1_DATASET} B "
                     f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH",
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

PULLUP_RULES_SECONDARY_DATASET_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_SECONDARY_DATASET_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "innerjoin_wb_2tables",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {PULLUP_RULES_SECONDARY_DATASET_DATASET}_dataset A "
                         f"INNER JOIN {PULLUP_RULES_SECONDARY_DATASET1_DATASET}_dataset B "
                         f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH limit 10 ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.32383420038968325,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443400,
                "uuid": "cac4a286-eaa0-40c4-988e-3dfa493dbc2c"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PULLUP_RULES_SECONDARY_DATASET_DATASET} A "
                             f"INNER JOIN @{PULLUP_RULES_SECONDARY_DATASET1_DATASET} B "
                             f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH limit 10\n",
            "totalCount": 3088,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_SECONDARY_DATASET_DATASET,
            "runId": "2018-01-16T00:00:00.000+0000",
            "ruleNm": "complex_rule_from_jdbc_2_jdbc",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {PULLUP_RULES_SECONDARY_DATASET_DATASET}_dataset A "
                         f"INNER JOIN {PULLUP_RULES_SECONDARY_DATASET1_DATASET}_dataset B "
                         f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH ",
            "filterQuery": None,
            "score": 99,
            "perc": 99.96761679649353,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443401,
                "uuid": "33e41677-103e-43d8-b013-bf0c35b90ed5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PULLUP_RULES_SECONDARY_DATASET_DATASET} A "
                             f"INNER JOIN @{PULLUP_RULES_SECONDARY_DATASET1_DATASET} B "
                             f"ON A.symbol = B.SYMBOL where A.exch = B.EXCH",
            "totalCount": 3088,
            "rowsBreaking": 3087,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
