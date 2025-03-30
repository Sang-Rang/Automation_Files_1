from payloads.pullup.pl_pullup_rule_result_preview_sales import (
    PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
)

PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLF = {
    "dataset": PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
    "ruleNm": "ff_result_preview",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT NAME, SALES FROM @{PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET} "
                 f"WHERE TRDATE = '2022-05-01' ORDER BY NAME, SALES, TRDATE",
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

PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_SQLG = {
    "dataset": PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
    "ruleNm": "simple_result_preview",
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
    "filterQuery": None,
    "tolerance": 0,
    "active": True
}

PULLUP_RULE_RESULT_PREVIEW_SALES_RULE_DEFINITION_NATIVE = {
    "dataset": PULLUP_RULE_RESULT_PREVIEW_SALES_DATASET,
    "ruleNm": "native_result_preview",
    "ruleType": "NATIVE",
    "ruleValue": "SELECT NAME FROM TEST.SALES WHERE TRDATE = '2022-05-01' ORDER BY NAME",
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

PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLF = [
    {
        "SALES": {
            "IntegerType": "1000"
        },
        "NAME": {
            "StringType": "John"
        }
    },
    {
        "SALES": {
            "IntegerType": "300"
        },
        "NAME": {
            "StringType": "Steve"
        }
    }
]

PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_SQLG = [
    {
        "TRDATE": {
            "Date": "2022-05-01"
        },
        "SALES": {
            "IntegerType": "1000"
        },
        "NAME": {
            "StringType": "John"
        }
    },
    {
        "TRDATE": {
            "Date": "2022-05-01"
        },
        "SALES": {
            "IntegerType": "300"
        },
        "NAME": {
            "StringType": "Steve"
        }
    }
]

PULLUP_RULE_RESULT_PREVIEW_SALES_EXPECTED_RESULT_PREVIEW_NATIVE = {
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
        }
    ],
    "exception": None,
    "rowCount": 2
}
