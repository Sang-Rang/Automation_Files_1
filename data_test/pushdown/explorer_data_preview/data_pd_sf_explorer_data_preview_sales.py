PD_SF_EXPLORER_DATA_PREVIEW_SALES_CONNECTION = "APPROVED_SNOWFLAKE_PUSHDOWN"
PD_SF_EXPLORER_DATA_PREVIEW_SALES_QUERY = (
    "SELECT * FROM PUBLIC.SALES ORDER BY \"NAME\", \"SALES\", \"TRDATE\"")
PD_SF_EXPLORER_DATA_PREVIEW_SALES_LIMIT = 8
PD_SF_EXPLORER_DATA_PREVIEW_SALES_EXPECTED_DATA = {
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
                "colValue": "2022-05-05",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 0,
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
                "colValue": "John",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-03",
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
                "colValue": "John",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-02",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 2000,
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
                "colValue": "John",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-05-04",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 2000,
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
                "colValue": "2022-05-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 200,
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
                "colValue": "2022-05-02",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 400,
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
    "rowCount": 8
}
