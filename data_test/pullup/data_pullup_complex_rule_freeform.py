from payloads.pullup.pl_pullup_complex_rule_freeform import (
    PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
    PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET,
)

PULLUP_COMPLEX_RULE_FREEFORM_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
        "ruleNm": "sqlf_2tables_dataset",
        "ruleType": "SQLF",
        "ruleValue": f"select A.* from @dataset A where A.district > 1 AND A.district IN "
                     f"(select B.district from @{PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET} B "
                     f"where B.district <= 88)",
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
        "previewLimit": 30,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
        "ruleNm": "sqlf_2tablefromsamesource",
        "ruleType": "SQLF",
        "ruleValue": f"select A.* from @{PULLUP_COMPLEX_RULE_FREEFORM_DATASET} A "
                     f"where A.district > 1 AND A.district IN (select B.district "
                     f"from @{PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET} B "
                     f"where B.district <= 88)",
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
        "previewLimit": 30,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PULLUP_COMPLEX_RULE_FREEFORM_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf_2tables_dataset",
            "ruleType": "SQLF",
            "ruleValue": f"select A.* from {PULLUP_COMPLEX_RULE_FREEFORM_DATASET}_dataset A "
                         f"where A.district > 1 AND A.district IN (select B.district "
                         f"from {PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET}_dataset B "
                         f"where B.district <= 88  )  ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.02228412195108831,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 434488,
                "uuid": "c9540f88-7fd0-43c5-b710-1150357f252f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select A.* from @dataset A where A.district > 1 "
                             f"AND A.district IN (select B.district "
                             f"from @{PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET} B "
                             f"where B.district <= 88)",
            "totalCount": 116675,
            "rowsBreaking": 26,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_COMPLEX_RULE_FREEFORM_DATASET,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "sqlf_2tablefromsamesource",
            "ruleType": "SQLF",
            "ruleValue": f"select A.* from {PULLUP_COMPLEX_RULE_FREEFORM_DATASET}_dataset A "
                         f"where A.district > 1 AND A.district IN (select B.district "
                         f"from {PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET}_dataset B "
                         f"where B.district <= 88  )  ",
            "filterQuery": None,
            "score": 0,
            "perc": 0.02228412195108831,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 434489,
                "uuid": "c788b2f0-a955-4ed4-be25-790b9a833cf8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select A.* from @{PULLUP_COMPLEX_RULE_FREEFORM_DATASET} A "
                             f"where A.district > 1 AND A.district IN (select B.district "
                             f"from @{PULLUP_COMPLEX_RULE_FREEFORM_SECONDARY_DATASET} B "
                             f"where B.district <= 88)",
            "totalCount": 116675,
            "rowsBreaking": 26,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
