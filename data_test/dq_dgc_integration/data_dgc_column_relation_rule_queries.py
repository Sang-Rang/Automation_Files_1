from payloads.dq_dgc_integration.pl_dq_dgc_column_relation_in_dic import (
    DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
)

DQ_DGC_COLUMN_RELATION_RULE_DEFINITIONS = [
    {
        "dataset": DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
        "ruleNm": "sales_rep_rule",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE sales_rep = 'John'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "sales_rep",
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


DQ_DGC_COLUMN_RELATION_RULE_OUTPUT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
            "runId": "2022-01-07T00:00:00.000+0000",
            "ruleNm": "sales_rep_rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_COLUMN_RELATION_JOB_NAME}_dataset "
                         f"WHERE sales_rep = 'John' ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 420035,
                "uuid": "13a55364-f5e7-4824-828f-5cd4cf03fec3"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE sales_rep = 'John'",
            "totalCount": 999,
            "rowsBreaking": 999,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
