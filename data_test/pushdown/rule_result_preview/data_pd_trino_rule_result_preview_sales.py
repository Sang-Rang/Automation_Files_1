from payloads.pushdown.rule_result_preview.pl_pd_trino_rule_result_preview_sales import (
    PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
)

PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF = {
    "dataset": PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
    "ruleNm": "ff_result_preview",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT name, sales FROM @{PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET} "
                 f"WHERE trdate = CAST('2022-05-01' AS date) ORDER BY name, sales, trdate",
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

PD_TRINO_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG = {
    "dataset": PD_TRINO_RULE_RESULT_PREVIEW_SALES_DATASET,
    "ruleNm": "simple_result_preview",
    "ruleType": "SQLG",
    "ruleValue": "trdate = CAST('2022-05-01' AS date)",
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

PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF = {
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
                "colValue": 1000,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            }
        ],
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
                "colValue": 300,
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
            "name": "name",
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
            "name": "sales",
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
    "rowCount": 2
}

PD_TRINO_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG = {
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
        ],
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
                "colValue": "2022-05-01",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 300,
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
            "name": "name",
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
            "name": "trdate",
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
            "name": "sales",
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
    "rowCount": 2
}
