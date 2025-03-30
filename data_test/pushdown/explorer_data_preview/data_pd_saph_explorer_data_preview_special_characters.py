PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_CONNECTION = "APPROVED_SAPHANA_PUSHDOWN"
PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_QUERY = (
    r"SELECT * "
    r'FROM TEST."SPECIALCHAR_SALES_DATA_10_ROWS_NO_SEMICOLON::$/-@#%^&*?!{}~\+=" '
    r"ORDER BY SALES_ID"
)
PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_LIMIT = 5
PD_SAPH_EXPLORER_DATA_PREVIEW_SPECIAL_CHARS_EXPECTED_DATA = {
    "rows": [
        [
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 1,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-01-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "8:00 AM",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "1",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Waly",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Measor",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "wmeasoro@wordpress.org",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Electrician",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 1000.53,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "General Electrical",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "16-000",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Kal",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "DE",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "0.000",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
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
                "colValue": 2,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-01-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "8:01 AM",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Dani",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Kinkead",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "dkinkeadce@sitemeter.com",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Engineer",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 8979.99,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Wood Fences and Gates",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "02-825",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Sara",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "PA",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "0.085",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
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
                "colValue": 3,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-01-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "8:01 AM",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "3",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Ryan",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Bleiman",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "rbleimancs@arstechnica.com",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Surveyor",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 2886.53,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "General Electrical",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "16-000",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Kal",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "NY",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "0.115",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
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
                "colValue": 4,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-01-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "8:01 AM",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "4",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Henry",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Putton",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "hputtonqs@amazon.com",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Construction Worker",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 4607.17,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Transportation Control Instrumentation",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "13-550",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
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
                "colValue": "NY",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "0.115",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
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
                "colValue": 5,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "2022-01-03",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "8:02 AM",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "5",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Sterne",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Telford",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "stelford5e@army.mil",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Construction Expeditor",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": 1852.66,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Plumbing Fixtures and Equipment",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "15-400",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "Sara",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "DE",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": "0.000",
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
                "isKey": False,
                "isNullOrEmpty": False,
                "issueType": None,
                "color": None
            },
            {
                "colNm": None,
                "isInvalid": False,
                "colValue": None,
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
            "name": "SALES_ID",
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
            "name": "TRANSACTION_DATE",
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
            "name": "TRANSACTION_TIME",
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
            "name": "DAILY_ID",
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
            "name": "FIRST_NAME",
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
            "name": "LAST_NAME",
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
            "name": "EMAIL",
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
            "name": "VENDOR_TYPE",
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
            "name": "COST",
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
            "name": "COST_DESCRIPTION",
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
            "name": "COST_CODE",
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
            "name": "SALES_REP",
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
            "name": "SALE_STATE",
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
            "name": "STATE_TAX",
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
            "name": "CRM_ID",
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
            "name": "LOST_COLUMN",
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
            "name": "TEMP",
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
    "rowCount": 5
}
