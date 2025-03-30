DATA_SEARCH_TEMPLATE = {
    "alias": "",
    "catalogsearch": "",
    "schemasearch": "",
    "tablesearch": "",
    "showstats": 0,
    "showviews": 0,
    "eagerfetch": 0,
}

# NOTE: Capitalization matters
DATA_VALIDATE = [
    {
        "catalogsearch": "public",
        "schemasearch": "public",
        "tablesearch": "nyse",
        "checkvalidations": [
            {"alias": "APPROVED_POSTGRES_UP", "exists": True},
            {"alias": "APPROVED_ORACLE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_PUSHDOWN", "exists": False},
        ],
    },
    {
        "catalogsearch": "public",
        "schemasearch": "public",
        "tablesearch": "",
        "checkvalidations": [
            {"alias": "APPROVED_POSTGRES_UP", "exists": True},
            {"alias": "APPROVED_ORACLE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_PUSHDOWN", "exists": False},
        ],
    },
    {
        "catalogsearch": "",
        "schemasearch": "",
        "tablesearch": "nyse",
        "checkvalidations": [
            {"alias": "APPROVED_POSTGRES_UP", "exists": True},
            {"alias": "APPROVED_ORACLE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_PUSHDOWN", "exists": False},
        ],
    },
    {
        "catalogsearch": "OWLUSER",
        "schemasearch": "OWLUSER",
        "tablesearch": "NYSE",
        "checkvalidations": [
            {"alias": "APPROVED_POSTGRES_UP", "exists": False},
            {"alias": "APPROVED_ORACLE_UP", "exists": True},
            {"alias": "APPROVED_SNOWFLAKE_UP", "exists": False},
            {"alias": "APPROVED_SNOWFLAKE_PUSHDOWN", "exists": False},
        ],
    },
]
