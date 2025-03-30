from payloads.pullup.pl_pullup_rules_s3_to_jdbc import PULLUP_RULES_S3_TO_JDBC_DATASET
from payloads.pullup.pl_pullup_rules_two_jdbc_s3 import PULLUP_RULES_TWO_JDBC_S3_DATASET

PULLUP_RULES_TWO_JDBC_S3_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_TWO_JDBC_S3_DATASET,
        "ruleNm": "sqlf1",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT A.id FROM @{PULLUP_RULES_TWO_JDBC_S3_DATASET} A "
                     f"EXCEPT (select B.newID from @{PULLUP_RULES_S3_TO_JDBC_DATASET} B)\n",
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
        "dataset": PULLUP_RULES_TWO_JDBC_S3_DATASET,
        "ruleNm": "freeform1",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT id FROM @{PULLUP_RULES_TWO_JDBC_S3_DATASET} "
                     f"EXCEPT (select newID from @{PULLUP_RULES_S3_TO_JDBC_DATASET})\n",
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

PULLUP_RULES_TWO_JDBC_S3_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_TWO_JDBC_S3_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf1",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT A.id FROM {PULLUP_RULES_TWO_JDBC_S3_DATASET}_dataset A "
                         f"EXCEPT (select B.newID "
                         f"from {PULLUP_RULES_S3_TO_JDBC_DATASET}_datasetFQ B  )  ",
            "filterQuery": None,
            "score": 5,
            "perc": 5.55555559694767,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443362,
                "uuid": "80f04a27-4f02-488d-9339-2c6ef75447ef"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT A.id FROM @{PULLUP_RULES_TWO_JDBC_S3_DATASET} A "
                             f"EXCEPT (select B.newID from @{PULLUP_RULES_S3_TO_JDBC_DATASET} B)\n",
            "totalCount": 18,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_TWO_JDBC_S3_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "freeform1",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT id FROM {PULLUP_RULES_TWO_JDBC_S3_DATASET}_dataset "
                         f"EXCEPT (select newID "
                         f"from {PULLUP_RULES_S3_TO_JDBC_DATASET}_datasetFQ  )  ",
            "filterQuery": None,
            "score": 5,
            "perc": 5.55555559694767,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 443361,
                "uuid": "bbcac81f-6218-4cdc-bf7a-0df08b82dc1e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT id FROM @{PULLUP_RULES_TWO_JDBC_S3_DATASET} "
                             f"EXCEPT (select newID from @{PULLUP_RULES_S3_TO_JDBC_DATASET})\n",
            "totalCount": 18,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
