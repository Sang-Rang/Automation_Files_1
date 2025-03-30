from payloads.dq_dgc_integration.pl_dq_dgc_quality_tab_overivew_for_dataset import (
    DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
)

DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_QUERIES = [
    {
        "dataset": DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
        "ruleNm": "sales_rep_rule08",
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

DQ_DGC_QUALITY_TAB_OVERVIEW_RULES_EXPECTED_RESULT = {
    "data": [
        {
            "dataset": DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME,
            "runId": "2024-08-08T00:00:00.000+0000",
            "ruleNm": "sales_rep_rule08",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_QUALITY_TAB_OVERVIEW_FOR_DATASET_NAME}_dataset "
                         f"WHERE sales_rep = 'John' ",
            "filterQuery": None,
            "score": 46,
            "perc": 46.669334173202515,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 434270,
                "uuid": "2ae8561a-8e7d-4d0a-93a2-c3d4c21bc901"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE sales_rep = 'John'",
            "totalCount": 4999,
            "rowsBreaking": 2333,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}
