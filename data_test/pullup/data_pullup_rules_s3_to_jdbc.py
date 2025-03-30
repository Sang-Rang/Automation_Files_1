from payloads.pullup.pl_pullup_rules_s3_to_jdbc import PULLUP_RULES_S3_TO_JDBC_DATASET
from payloads.pullup.pl_pullup_rules_two_jdbc_s3 import PULLUP_RULES_TWO_JDBC_S3_DATASET

PULLUP_RULES_S3_TO_JDBC_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_S3_TO_JDBC_DATASET,
        "ruleNm": "sqlf_s32jdbc",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT newID FROM @{PULLUP_RULES_S3_TO_JDBC_DATASET} "
                     f"EXCEPT select id from @{PULLUP_RULES_TWO_JDBC_S3_DATASET}\n",
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
        "dataset": PULLUP_RULES_S3_TO_JDBC_DATASET,
        "ruleNm": "s32jdbc_ff",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT A.newID FROM @{PULLUP_RULES_S3_TO_JDBC_DATASET} A "
                     f"EXCEPT select B.id from @{PULLUP_RULES_TWO_JDBC_S3_DATASET} B",
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
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PULLUP_RULES_S3_TO_JDBC_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_S3_TO_JDBC_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf_s32jdbc",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT newID FROM {PULLUP_RULES_S3_TO_JDBC_DATASET}_dataset "
                         f"EXCEPT select id from {PULLUP_RULES_TWO_JDBC_S3_DATASET}_dataset ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.526315867900848,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443350,
                "uuid": "29486fd4-945c-444b-81c9-82d1e87ebf00"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT newID FROM @{PULLUP_RULES_S3_TO_JDBC_DATASET} "
                             f"EXCEPT select id from @{PULLUP_RULES_TWO_JDBC_S3_DATASET}\n",
            "totalCount": 19,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_S3_TO_JDBC_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "s32jdbc_ff",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT A.newID FROM {PULLUP_RULES_S3_TO_JDBC_DATASET}_dataset A "
                         f"EXCEPT select B.id from {PULLUP_RULES_TWO_JDBC_S3_DATASET}_dataset B ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.526315867900848,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443349,
                "uuid": "8181efd1-10c3-4d5b-81e0-b57b614d3f24"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT A.newID FROM @{PULLUP_RULES_S3_TO_JDBC_DATASET} A "
                             f"EXCEPT select B.id from @{PULLUP_RULES_TWO_JDBC_S3_DATASET} B",
            "totalCount": 19,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
