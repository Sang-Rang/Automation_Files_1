AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE = "2022-01-03"
WHERE_DATE_FORMAT = AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE.replace("-", "")
AEF_SAPH_PD_SPECIAL_CHARS_TABLE_NAME = (
    r'TEST.SPECIALCHAR_SALES_DATA_100_ROWS::$/-;@#%^&*?!{}~\+='
)
AEF_SAPH_PD_SPECIAL_CHARS_DATE_COL = "TRANSACTION_DATE"
AEF_SAPH_PD_SPECIAL_CHARS_ROW_COUNT = 10
AEF_SAPH_PD_SPECIAL_CHARS_DATASET = "AUTO_CXN_SAPHANA_PD"
AEF_SAPH_PD_SPECIAL_CHARS_QUERY = (
    f"select * from {AEF_SAPH_PD_SPECIAL_CHARS_TABLE_NAME} "
    f"limit {AEF_SAPH_PD_SPECIAL_CHARS_ROW_COUNT}"
)
AEF_SAPH_PD_SPECIAL_CHARS_CONNECTION = "APPROVED_SAPHANA_PUSHDOWN"

AEF_SAPH_PD_SPECIAL_CHARS_DAYS_WITH_DATA_PARAMS = {
    "cxn": AEF_SAPH_PD_SPECIAL_CHARS_CONNECTION,
    "schemaAndTableNm": AEF_SAPH_PD_SPECIAL_CHARS_TABLE_NAME,
    "colNm": AEF_SAPH_PD_SPECIAL_CHARS_DATE_COL,
    "groupBy": "day",
}
AEF_SAPH_PD_SPECIAL_CHARS_ROW_FILTER_SALE_STATE_PARAMS = {
    "cxn": AEF_SAPH_PD_SPECIAL_CHARS_CONNECTION,
    "schemaAndTableNm": AEF_SAPH_PD_SPECIAL_CHARS_TABLE_NAME,
    "colNm": "SALE_STATE",
    "groupBy": "day",
    "isDate": False,
}
AEF_SAPH_PD_SPECIAL_CHARS_FILTERGRAM_PARAMS = {
    "dataset": AEF_SAPH_PD_SPECIAL_CHARS_DATASET,
    "column": AEF_SAPH_PD_SPECIAL_CHARS_DATE_COL,
    "runid": f"{AEF_SAPH_PD_SPECIAL_CHARS_RUN_DATE}",
    "limit": 500,
}
AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_FILTERGRAM_OUTPUT = {}
AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_SCORE = {}
AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DS_SCAN = {}
AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA = [
    {"rowcount":100,"day_owl_str":"2022-01-03","day":"2022-01-03"}
]

AEF_SAPH_PD_SPECIAL_CHARS_EXPECTED_DAYS_WITH_DATA_ROW_FILTER_SALE_STATE = [
    {
        "rowcount": 10,
        "day_owl_str": "CT",
        "day": "CT"
    },
    {
        "rowcount": 8,
        "day_owl_str": "DE",
        "day": "DE"
    },
    {
        "rowcount": 8,
        "day_owl_str": "NJ",
        "day": "NJ"
    },
    {
        "rowcount": 46,
        "day_owl_str": "NY",
        "day": "NY"
    },
    {
        "rowcount": 28,
        "day_owl_str": "PA",
        "day": "PA"
    }
]
