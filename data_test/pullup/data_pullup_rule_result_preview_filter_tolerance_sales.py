from payloads.pullup.pl_pullup_rule_result_preview_filter_tolerance_sales import (
    PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET
)

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_RULE_DEFINITION = {
    "dataset": PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    "ruleNm": "FF_filter",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT * FROM @{PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET} "
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

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_RULE_DEFINITION = {
        "dataset": PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
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

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_RULE_DEFINITION = {
    "dataset": PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET,
    "ruleNm": "FF_filter_and_tolerance",
    "ruleType": "SQLF",
    "ruleValue": f"SELECT * FROM @{PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_DATASET} "
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

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_EXPECTED_RESULT_PREVIEW = [
    {
        "TRDATE": {
            "Date": "2022-05-01"
        },
        "SALES": {
            "LongType": "1000"
        },
        "NAME": {
            "StringType": "John"
        }
    }
]

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_SIMPLE_FILTER_EXPECTED_RESULT_PREVIEW = [
    {
        "TRDATE": {
            "Date": "2022-05-01"
        },
        "SALES": {
            "LongType": "1000"
        },
        "NAME": {
            "StringType": "John"
        }
    }
]

PULLUP_RULE_RESULT_PREVIEW_FILTER_TOLERANCE_SALES_FF_FILTER_TOLERANCE_EXP_RESULT_PREVIEW = [
    {
        "TRDATE": {
            "Date": "2022-05-05"
        },
        "SALES": {
            "LongType": "10000"
        },
        "NAME": {
            "StringType": "Steve"
        }
    }
]
