PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_COUNT = {
    "targetRowCount": 3088,
    "sourceRowCount": 3087,
    "targetColCount": 5,
    "sourceColCount": 9,
    "data": [
        {
            "countType": "Dataset Row Count",
            "targetCount": 3088,
            "sourceCount": 3087,
            "change": 1,
            "percChange": 0.03239,
            "assignmentId": {
                "id": 1625463,
                "uuid": "2fe4a08a-2025-4ed8-af29-98b3d60d0a6b"
            },
            "description": "The row size does not match. Source has 3087 rows. Target has 3088 "
                           "rows. Source-to-target difference: 1 (+0.03%)"
        },
        {
            "countType": "Dataset Column Count",
            "targetCount": 5,
            "sourceCount": 9,
            "change": -4,
            "percChange": -44.44444,
            "assignmentId": {
                "id": 1625464,
                "uuid": "959fac05-3f33-4c6a-ac67-7d47328baccc"
            },
            "description": "The column total does not match. Source has 9 columns. Target has 5 "
                           "columns. Source-to-target difference: -4 (-44.44%)"
        }
    ]
}

PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA = {
    "colOrderPassing": True,
    "percMatching": 100.0,
    "percPassing": 100.0,
    "checkType": True,
    "checkCase": False,
    "checkColOrder": False,
    "targetToSourceMap": "HIGH=HIGH|SYMBOL=SYMBOL|EXCH=EXCH|TRADE_DATE=TRADE_DATE|"
                         "PART_DATE_STR=PART_DATE_STR",
    "colOrderAssignmentId": None,
    "colOrderTarget": "EXCH=0|SYMBOL=1|TRADE_DATE=2|HIGH=4|PART_DATE_STR=7",
    "colOrderSource": "EXCH=0|SYMBOL=1|TRADE_DATE=2|HIGH=4|PART_DATE_STR=8",
    "data": [
        {
            "targetColNm": "EXCH",
            "targetColType": "VARCHAR",
            "targetColOrder": "1",
            "sourceColNm": "EXCH",
            "sourceColType": "VARCHAR",
            "sourceColOrder": "1",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False
        },
        {
            "targetColNm": "SYMBOL",
            "targetColType": "VARCHAR",
            "targetColOrder": "2",
            "sourceColNm": "SYMBOL",
            "sourceColType": "VARCHAR",
            "sourceColOrder": "2",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False
        },
        {
            "targetColNm": "TRADE_DATE",
            "targetColType": "DATE",
            "targetColOrder": "3",
            "sourceColNm": "TRADE_DATE",
            "sourceColType": "DATE",
            "sourceColOrder": "3",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False
        },
        {
            "targetColNm": "HIGH",
            "targetColType": "NUMBER",
            "targetColOrder": "5",
            "sourceColNm": "HIGH",
            "sourceColType": "NUMBER",
            "sourceColOrder": "5",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False
        },
        {
            "targetColNm": "PART_DATE_STR",
            "targetColType": "DATE",
            "targetColOrder": "8",
            "sourceColNm": "PART_DATE_STR",
            "sourceColType": "DATE",
            "sourceColOrder": "9",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False
        }
    ]
}

PD_SF_SOURCE_KEY_TIME_NYSE_EXPECTED_SOURCE_VALUES = {
    "checkValues": True,
    "validateValuesTrim": False,
    "validateValuesShowMissingKeys": False,
    "countRowMismatch": 3088,
    "countRowTotal": 3088,
    "percRowMatch": 0.0,
    "countColumnShift": 3,
    "colIssueCountMap": "\"EXCH\"=1|\"HIGH\"=2990|\"TRADE_DATE\"=3088|\"PART_DATE_STR\"=3088",
    "data": [
        {
            "id": 0,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Target (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"HIGH\"",
            "value": [
                "35.760000000000000000"
            ],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None
        },
        {
            "id": 0,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Source (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"HIGH\"",
            "value": [
                "35.490000000000000000"
            ],
            "passStatus": 1,
            "assignmentId": {
                "id": 1625465,
                "uuid": "84ec36b8-d1d4-48a7-ad44-eda844f687b8"
            },
            "description": "More than 90% of target column [\"HIGH\"] values do not match source "
                           "column [\"HIGH\"] value. For example: [35.760000000000000000] vs "
                           "[35.490000000000000000]",
            "count": 1
        },
        {
            "id": 1,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Target (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"PART_DATE_STR\"",
            "value": [
                "2018-01-16"
            ],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None
        },
        {
            "id": 1,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Source (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"PART_DATE_STR\"",
            "value": [
                "2018-01-15"
            ],
            "passStatus": 1,
            "assignmentId": {
                "id": 1625466,
                "uuid": "a05097a0-d003-4379-957b-fcf1d64cb85d"
            },
            "description": "More than 90% of target column [\"PART_DATE_STR\"] values do not match "
                           "source column [\"PART_DATE_STR\"] value. For example: [2018-01-16] vs "
                           "[2018-01-15]",
            "count": 1
        },
        {
            "id": 2,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Target (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"TRADE_DATE\"",
            "value": [
                "2018-01-16"
            ],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None
        },
        {
            "id": 2,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Source (snowflake)",
            "key": [
                "XL"
            ],
            "column": "\"TRADE_DATE\"",
            "value": [
                "2018-01-15"
            ],
            "passStatus": 1,
            "assignmentId": {
                "id": 1625467,
                "uuid": "bacd7b38-77a5-48a0-828f-541038bcc021"
            },
            "description": "More than 90% of target column [\"TRADE_DATE\"] values do not match "
                           "source column [\"TRADE_DATE\"] value. For example: [2018-01-16] vs "
                           "[2018-01-15]",
            "count": 1
        }
    ],
    "dataOld": {
        "columns": [
            {
                "title": "id",
                "name": "id",
                "data": "id"
            },
            {
                "title": "system",
                "name": "system",
                "data": "system"
            },
            {
                "title": "key",
                "name": "key",
                "data": "key"
            },
            {
                "title": "column",
                "name": "column",
                "data": "column"
            },
            {
                "title": "value",
                "name": "value",
                "data": "value"
            },
            {
                "title": "passStatus",
                "name": "passStatus",
                "data": "passStatus"
            },
            {
                "title": "assignmentId",
                "name": "assignmentId",
                "data": "assignmentId"
            }
        ],
        "data": [
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Source (snowflake)",
                "passStatus": 1,
                "column": "\"HIGH\"",
                "count": 1,
                "description": "More than 90% of target column [\"HIGH\"] values do not match "
                               "source column [\"HIGH\"] value. For example: "
                               "[35.760000000000000000] vs [35.490000000000000000]",
                "id": 0,
                "value": [
                    "35.490000000000000000"
                ],
                "assignmentId": {
                    "id": 1625465,
                    "uuid": "84ec36b8-d1d4-48a7-ad44-eda844f687b8"
                },
                "key": [
                    "XL"
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Target (snowflake)",
                "passStatus": 4,
                "column": "\"HIGH\"",
                "count": None,
                "description": "",
                "id": 0,
                "value": [
                    "35.760000000000000000"
                ],
                "assignmentId": None,
                "key": [
                    "XL"
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Source (snowflake)",
                "passStatus": 1,
                "column": "\"PART_DATE_STR\"",
                "count": 1,
                "description": "More than 90% of target column [\"PART_DATE_STR\"] values do not "
                               "match source column [\"PART_DATE_STR\"] value. For example: "
                               "[2018-01-16] vs [2018-01-15]",
                "id": 1,
                "value": [
                    "2018-01-15"
                ],
                "assignmentId": {
                    "id": 1625466,
                    "uuid": "a05097a0-d003-4379-957b-fcf1d64cb85d"
                },
                "key": [
                    "XL"
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Target (snowflake)",
                "passStatus": 4,
                "column": "\"PART_DATE_STR\"",
                "count": None,
                "description": "",
                "id": 1,
                "value": [
                    "2018-01-16"
                ],
                "assignmentId": None,
                "key": [
                    "XL"
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Source (snowflake)",
                "passStatus": 1,
                "column": "\"TRADE_DATE\"",
                "count": 1,
                "description": "More than 90% of target column [\"TRADE_DATE\"] values do not "
                               "match source column [\"TRADE_DATE\"] value. For example: "
                               "[2018-01-16] vs [2018-01-15]",
                "id": 2,
                "value": [
                    "2018-01-15"
                ],
                "assignmentId": {
                    "id": 1625467,
                    "uuid": "bacd7b38-77a5-48a0-828f-541038bcc021"
                },
                "key": [
                    "XL"
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Target (snowflake)",
                "passStatus": 4,
                "column": "\"TRADE_DATE\"",
                "count": None,
                "description": "",
                "id": 2,
                "value": [
                    "2018-01-16"
                ],
                "assignmentId": None,
                "key": [
                    "XL"
                ]
            }
        ]
    }
}
