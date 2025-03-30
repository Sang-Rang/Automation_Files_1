# pylint: disable-next=line-too-long
from payloads.pushdown.rule_result_preview.pl_pd_sf_rule_result_preview_filter_tolerance_sales import (
    PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
)

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION = {
    "dataset": PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    "ruleNm": "FF_filter",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT * FROM @{PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET} "
                 f"WHERE TRDATE = '2022-05-01'",
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
    "filterQuery": "SALES = 1000",
    "tolerance": 0,
    "active": True
}

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION = {
    "dataset": PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    "ruleNm": "Simple_filter",
    "ruleType": "SQLG",
    "ruleValue": "TRDATE = '2022-05-01'",
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
    "filterQuery": "SALES = 1000",
    "tolerance": 0,
    "active": True
}

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION = {
    "dataset": PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    "ruleNm": "FF_filter_and_tolerance",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT * FROM @{PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET} "
                 f"WHERE SALES > 1000",
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
    "filterQuery": "NAME = 'Steve'",
    "tolerance": 30,
    "active": True
}

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW = {
    "rows": [
        [
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "John",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-01",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 1000,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            }
        ]
    ],
    "schema": [
        {
            "type": None,
            "typeDesc": None,
            "name": "NAME",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "TRDATE",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "SALES",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        }
    ],
    "exception": None,
    "rowCount": 1
}

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW = {
    "rows": [
        [
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "John",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-01",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 1000,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            }
        ]
    ],
    "schema": [
        {
            "type": None,
            "typeDesc": None,
            "name": "NAME",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "TRDATE",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "SALES",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        }
    ],
    "exception": None,
    "rowCount": 1
}

PD_SF_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW = {
    "rows": [
        [
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Steve",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-05",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 10000,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            }
        ]
    ],
    "schema": [
        {
            "type": None,
            "typeDesc": None,
            "name": "NAME",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "TRDATE",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        },
        {
            "type": None,
            "typeDesc": None,
            "name": "SALES",
            "semantic": None,
            "isPii": 0,
            "isMnpi": 0,
            "sensitiveLabelId": None,
            "sensitiveLabelName": None,
            "isMasked": 0,
            "stats": None,
            "cardinality": 0.0,
            "nullPercent": 0.0,
            "emptyPercent": 0.0,
            "isKey": 0
        }
    ],
    "exception": None,
    "rowCount": 1
}
