PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_COUNT = {
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
                "id": 1624576,
                "uuid": "93f66b76-b941-4f89-9846-a1c7cc27d8bb"
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
                "id": 1624577,
                "uuid": "b807a203-22b7-42b0-9e9d-3856aeb4167e"
            },
            "description": "The column total does not match. Source has 9 columns. Target has 5 "
                           "columns. Source-to-target difference: -4 (-44.44%)"
        }
    ]
}

PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_SCHEMA = {
    "colOrderPassing": True,
    "percMatching": 80.0,
    "percPassing": 80.0,
    "checkType": True,
    "checkCase": False,
    "checkColOrder": False,
    "targetToSourceMap": "SYMBOL=SYMBOL|EXCH=CLOSE|TRADE_DATE=TRADE_DATE|"
                         "PART_DATE_STR=PART_DATE_STR|OPEN=OPEN",
    "colOrderAssignmentId": None,
    "colOrderTarget": "EXCH=0|SYMBOL=1|TRADE_DATE=2|OPEN=3|PART_DATE_STR=8",
    "colOrderSource": "SYMBOL=1|TRADE_DATE=2|OPEN=3|CLOSE=6|PART_DATE_STR=8",
    "data": [
        {
            "targetColNm": "EXCH",
            "targetColType": "VARCHAR",
            "targetColOrder": "1",
            "sourceColNm": "CLOSE",
            "sourceColType": "NUMBER",
            "sourceColOrder": "7",
            "matchLevel": 4,
            "itemLabel": "Failing",
            "passStatus": 4,
            "assignmentId": {
                "id": 1624578,
                "uuid": "f11fd7e6-04cc-4db5-9792-e9c0d5a08401"
            },
            "description": "The target column [EXCH] (type: VARCHAR) does not match source column "
                           "[CLOSE] (type: NUMBER)",
            "obsSubType": "SCHEMA_TYPE",
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
            "targetColNm": "OPEN",
            "targetColType": "NUMBER",
            "targetColOrder": "4",
            "sourceColNm": "OPEN",
            "sourceColType": "NUMBER",
            "sourceColOrder": "4",
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
            "targetColOrder": "9",
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

PD_SF_SOURCE_NOKEY_TIME_NYSE_EXPECTED_SOURCE_VALUES = {
    "checkValues": True,
    "validateValuesTrim": False,
    "validateValuesShowMissingKeys": False,
    "countRowMismatch": 6175,
    "countRowTotal": 6175,
    "percRowMatch": 0.0,
    "countColumnShift": 1,
    "colIssueCountMap": "EXCH,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE=6175",
    "data": [
        {
            "id": 0,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Target (snowflake)",
            "key": [
                ""
            ],
            "column": "EXCH,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE",
            "value": [
                "null"
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
                ""
            ],
            "column": "",
            "value": [
                "35.490000000000000000",
                "35.490000000000000000",
                "2018-01-15",
                "XL",
                "2018-01-15"
            ],
            "passStatus": 1,
            "assignmentId": {
                "id": 1624579,
                "uuid": "19510828-2ec2-4878-bec6-a3630bc06693"
            },
            "description": "More than 90% of target column "
                           "[EXCH,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE] values do not match source "
                           "column [] value. For example: [null] vs "
                           "[35.490000000000000000~~35.490000000000000000~~2018-01-15~~"
                           "XL~~2018-01-15]",
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
                "column": "",
                "count": 1,
                "description": "More than 90% of target column "
                               "[EXCH,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE] values do not match "
                               "source column [] value. For example: [null] vs "
                               "[35.490000000000000000~~35.490000000000000000~~2018-01-15~~XL~~"
                               "2018-01-15]",
                "id": 0,
                "value": [
                    "35.490000000000000000",
                    "35.490000000000000000",
                    "2018-01-15",
                    "XL",
                    "2018-01-15"
                ],
                "assignmentId": {
                    "id": 1624579,
                    "uuid": "19510828-2ec2-4878-bec6-a3630bc06693"
                },
                "key": [
                    ""
                ]
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Target (snowflake)",
                "passStatus": 4,
                "column": "EXCH,OPEN,PART_DATE_STR,SYMBOL,TRADE_DATE",
                "count": None,
                "description": "",
                "id": 0,
                "value": [
                    "null"
                ],
                "assignmentId": None,
                "key": [
                    ""
                ]
            }
        ]
    }
}
