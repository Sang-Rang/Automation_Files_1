from payloads.pushdown.rules.pl_pd_mssql_rules_sales_link_id import (
    PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
    PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
)

PD_MSSQL_RULES_SALES_LINK_ID_RULE_DEFINITIONS = [
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "Simple_no_link_column",
        "ruleType": "SQLG",
        "ruleValue": "sales = 1000",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "sales",
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
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "trdate = '2022-05-03'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "trdate",
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
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": "SELECT sales FROM dbo.sales WHERE sales = 0",
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
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' "
                     "AND trdate = '2022-05-01' AND sales = 1000",
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
]

PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_no_link_column",
            "ruleType": "SQLG",
            "ruleValue": "sales = 1000",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586082,
                "uuid": "3d446df2-f5dc-486a-a372-035dfddb9de2"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "trdate = '2022-05-03'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586083,
                "uuid": "5a37b21f-576d-4872-9a84-9cef8b153e6e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate = '2022-05-03'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT sales FROM dbo.sales WHERE sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586081,
                "uuid": "e51a1829-4195-4801-8ca0-d7e79e520ed5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT sales FROM dbo.sales WHERE sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM dbo.sales WHERE name = 'John' "
                         "AND trdate = '2022-05-01' AND sales = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586080,
                "uuid": "95eb6bc6-ba79-4754-b8b1-7c454ef88051"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM dbo.sales WHERE name = 'John' "
                             "AND trdate = '2022-05-01' AND sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_all_columns,John~|2022-05-01,John,2022-05-01",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-01,John,2022-05-01",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-03,John,2022-05-03"
]

PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_all_columns",
        "linkId": "John~|2022-05-01",
        "name": "John",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "name": "John",
        "trdate": "2022-05-05"
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "John~|2022-05-03",
        "name": "John",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "Steve~|2022-05-03",
        "name": "Steve",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-01",
        "name": "John",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-03",
        "name": "John",
        "trdate": "2022-05-03"
    }
]

PD_MSSQL_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]

PD_MSSQL_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_MSSQL_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "name": "John",
        "trdate": "2022-05-05"
    }
]

PD_MSSQL_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_MSSQL_RULES_SALES_LINK_ID_DATASET},{PD_MSSQL_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]
