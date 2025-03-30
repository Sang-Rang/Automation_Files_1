# pylint: disable-msg=import-error
from payloads.pullup.pl_assignments_rule_on_hoot import DATASET_NAME_ASSIGNMENTS_HOOT

DATASET_RULE_DEFS = [
    {
        "dataset": DATASET_NAME_ASSIGNMENTS_HOOT,
        "ruleNm": "simple_rule_107",
        "ruleType": "SQLG",
        "ruleValue": "exch='NYSE'",
        "points": 1,
        "ruleRepo": "",
        "perc": 1,
        "columnName": "exch",
        "businessCategory": "",
        "businessDesc": "",
        "dimId": "",
        "previewLimit": 6,
        "runTimeLimit": 30,
    }
]
