from payloads.pushdown.rules.pl_pd_athena_rules_sales_archive_breaks import (
    PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "trdate = CAST('2022-05-01' AS DATE)",
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
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT sales FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE sales = 0",
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
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE name = 'John' AND trdate = CAST('2022-05-01' AS DATE) "
                     f"AND sales = 1000",
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
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE $rowCount > 9",
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
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
    }
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from default.sales) WHERE 10 > 9",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585925,
                "uuid": "0b1dcb5f-db29-40f4-9267-d0fb271f4202"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1585929,
                "uuid": "a0f22454-220f-4aa2-a244-2a47e6c756ba"
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
            "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "trdate = CAST('2022-05-01' AS DATE ) ",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585928,
                "uuid": "63f50cca-e0e1-4f81-9541-d8220f290def"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate = CAST('2022-05-01' AS DATE)",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT sales FROM (select * from default.sales) WHERE sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585926,
                "uuid": "4582aaf9-681e-42e4-b863-930372b162dc"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT sales FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from default.sales) WHERE name = 'John' "
                         "AND trdate = CAST('2022-05-01' AS DATE) AND sales = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585927,
                "uuid": "a0179e46-95a2-428c-927b-d46776cca4db"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE name = 'John' AND trdate = CAST('2022-05-01' AS DATE) "
                             f"AND sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "updts": "2023-10-20T00:53:26.859+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:48.971+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:48.971+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:26.871+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:48.189+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:48.189+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04",
        "run_id": "2023-10-19 00:00:00"
    },
    {
        "updts": "2023-10-20T00:53:37.847+0000",
        "job_uuid": "9e6248e2-fe61-4418-a6ca-1ebbb45ec63b",
        "dataset": PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05",
        "run_id": "2023-10-19 00:00:00"
    }
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Simple_link_column",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "Simple_link_column",
        "name": "Steve",
        "trdate": "2022-05-01",
        "sales": 300
    },
    {
        "rule_name": "FF_all_columns",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-02",
        "sales": 2000
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-03",
        "sales": 1000
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-04",
        "sales": 2000
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    },
    {
        "rule_name": "stat_rule",
        "name": "Steve",
        "trdate": "2022-05-01",
        "sales": 300
    },
    {
        "rule_name": "stat_rule",
        "name": "Steve",
        "trdate": "2022-05-02",
        "sales": 400
    },
    {
        "rule_name": "stat_rule",
        "name": "Steve",
        "trdate": "2022-05-03",
        "sales": 200
    },
    {
        "rule_name": "stat_rule",
        "name": "Steve",
        "trdate": "2022-05-04",
        "sales": 500
    },
    {
        "rule_name": "stat_rule",
        "name": "Steve",
        "trdate": "2022-05-05",
        "sales": 10000
    },
    {
        "rule_name": "Simple_no_link_column",
        "name": "John",
        "trdate": "2022-05-01",
        "sales": 1000
    },
    {
        "rule_name": "Simple_no_link_column",
        "name": "John",
        "trdate": "2022-05-03",
        "sales": 1000
    }
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_all_columns\",1000,2022-05-01",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05",
    "\"John\",\"Simple_link_column\",1000,2022-05-01",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-01",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-03",
    "\"John\",\"stat_rule\",0,2022-05-05",
    "\"John\",\"stat_rule\",1000,2022-05-01",
    "\"John\",\"stat_rule\",1000,2022-05-03",
    "\"John\",\"stat_rule\",2000,2022-05-02",
    "\"John\",\"stat_rule\",2000,2022-05-04",
    "\"Steve\",\"Simple_link_column\",300,2022-05-01",
    "\"Steve\",\"stat_rule\",10000,2022-05-05",
    "\"Steve\",\"stat_rule\",200,2022-05-03",
    "\"Steve\",\"stat_rule\",300,2022-05-01",
    "\"Steve\",\"stat_rule\",400,2022-05-02",
    "\"Steve\",\"stat_rule\",500,2022-05-04"
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "Simple_link_column",
            "name": "John",
            "trdate": "2022-05-01",
            "sales": 1000
        },
        {
            "rule_name": "stat_rule",
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
            "rule_name": "FF_all_columns",
            "name": "John",
            "trdate": "2022-05-01",
            "sales": 1000
        },
        {
            "rule_name": "stat_rule",
            "name": "John",
            "trdate": "2022-05-02",
            "sales": 2000
        },
        {
            "rule_name": "Simple_no_link_column",
            "name": "John",
            "trdate": "2022-05-03",
            "sales": 1000
        },
        {
            "rule_name": "stat_rule",
            "name": "John",
            "trdate": "2022-05-03",
            "sales": 1000
        },
        {
            "rule_name": "stat_rule",
            "name": "John",
            "trdate": "2022-05-04",
            "sales": 2000
        },
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        },
        {
            "rule_name": "stat_rule",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        },
        {
            "rule_name": "Simple_link_column",
            "name": "Steve",
            "trdate": "2022-05-01",
            "sales": 300
        },
        {
            "rule_name": "stat_rule",
            "name": "Steve",
            "trdate": "2022-05-01",
            "sales": 300
        },
        {
            "rule_name": "stat_rule",
            "name": "Steve",
            "trdate": "2022-05-02",
            "sales": 400
        },
        {
            "rule_name": "stat_rule",
            "name": "Steve",
            "trdate": "2022-05-03",
            "sales": 200
        },
        {
            "rule_name": "stat_rule",
            "name": "Steve",
            "trdate": "2022-05-04",
            "sales": 500
        },
        {
            "rule_name": "stat_rule",
            "name": "Steve",
            "trdate": "2022-05-05",
            "sales": 10000
        }
    ]
}

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        }
    ]
}

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    }
]

PD_ATHENA_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT =  [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]
