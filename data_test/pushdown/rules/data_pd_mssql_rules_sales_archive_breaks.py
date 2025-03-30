from payloads.pushdown.rules.pl_pd_mssql_rules_sales_archive_breaks import (
    PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
            "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
            "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
            "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.463+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.463+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.463+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.463+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.427+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2024-01-16T16:37:39.427+0000",
        "job_uuid": "edeb47bc-2896-440b-8ed9-f1b47a53dd8a",
        "dataset": PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-01-16T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    }
]

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_all_columns",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "Simple_no_link_column",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "Simple_link_column",
        "name": "John",
        "trdate": "2022-05-03",
        "sales": 1000
    },
    {
        "rule_name": "Simple_no_link_column",
        "name": "John",
        "trdate": "2022-05-03",
        "sales": 1000
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    },
    {
        "rule_name": "Simple_link_column",
        "name": "Steve",
        "trdate": "2022-05-03",
        "sales": 200
    }
]

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_all_columns\",1000,2022-05-01",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05",
    "\"John\",\"Simple_link_column\",1000,2022-05-03",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-01",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-03",
    "\"Steve\",\"Simple_link_column\",200,2022-05-03"
]

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "Simple_no_link_column",
            "name": "John",
            "trdate": "2022-05-01",
            "sales": 1000
        },
        {
            "rule_name": "FF_all_columns",
            "name": "John",
            "trdate": "2022-05-01",
            "sales": 1000
        },
        {
            "rule_name": "Simple_no_link_column",
            "name": "John",
            "trdate": "2022-05-03",
            "sales": 1000
        },
        {
            "rule_name": "Simple_link_column",
            "name": "John",
            "trdate": "2022-05-03",
            "sales": 1000
        },
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        },
        {
            "rule_name": "Simple_link_column",
            "name": "Steve",
            "trdate": "2022-05-03",
            "sales": 200
        }
    ]
}

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        }
    ]
}

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    }
]

PD_MSSQL_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]
