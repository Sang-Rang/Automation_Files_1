from payloads.pushdown.rules.pl_pd_rs_rules_sales_archive_breaks import (
    PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_RS_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT sales FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE name = 'John' AND trdate = '2022-05-01' AND sales = 1000",
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

PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales2) WHERE 10 > 9",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586001,
                "uuid": "8ce5f335-9891-4084-ad62-21d3f3e56675"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586002,
                "uuid": "3678c3a2-5ae5-4a12-aefd-5dea7fa87b98"
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
            "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586003,
                "uuid": "37957f63-23ff-47d0-9384-521687bdfa56"
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
            "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT sales FROM (select * from public.sales2) WHERE sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585999,
                "uuid": "38cd6ee6-9f2e-462a-bf1e-1de91aaa61c1"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT sales FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales2) WHERE name = 'John' "
                         "AND trdate = '2022-05-01' AND sales = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586000,
                "uuid": "b39cca5c-a37b-42d9-895f-74ca912fcf23"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE name = 'John' AND trdate = '2022-05-01' AND sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1761,
        "updts": "2023-10-20T14:04:11.445+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1763,
        "updts": "2023-10-20T14:04:11.448+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1765,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1769,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1773,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1777,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 1781,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 1785,
        "updts": "2023-10-20T14:04:11.735+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1789,
        "updts": "2023-10-20T14:04:11.851+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1767,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 1771,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 1775,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 1779,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1783,
        "updts": "2023-10-20T14:04:11.639+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 1787,
        "updts": "2023-10-20T14:04:11.735+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1791,
        "updts": "2023-10-20T14:04:11.851+0000",
        "job_uuid": "444d44a6-e2e3-4227-a469-dc256de3e814",
        "dataset": PD_RS_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-20T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    }
]

PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-02",
        "sales": 2000
    },
    {
        "rule_name": "stat_rule",
        "name": "John",
        "trdate": "2022-05-04",
        "sales": 2000
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
        "trdate": "2022-05-03",
        "sales": 200
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
        "trdate": "2022-05-03",
        "sales": 1000
    },
    {
        "rule_name": "Simple_link_column",
        "name": "Steve",
        "trdate": "2022-05-03",
        "sales": 200
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
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
        "trdate": "2022-05-01",
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
        "trdate": "2022-05-05",
        "sales": 0
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
        "trdate": "2022-05-04",
        "sales": 500
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
    }
]

PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_all_columns\",1000,2022-05-01",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05",
    "\"John\",\"Simple_link_column\",1000,2022-05-03",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-01",
    "\"John\",\"Simple_no_link_column\",1000,2022-05-03",
    "\"John\",\"stat_rule\",0,2022-05-05",
    "\"John\",\"stat_rule\",1000,2022-05-01",
    "\"John\",\"stat_rule\",1000,2022-05-03",
    "\"John\",\"stat_rule\",2000,2022-05-02",
    "\"John\",\"stat_rule\",2000,2022-05-04",
    "\"Steve\",\"Simple_link_column\",200,2022-05-03",
    "\"Steve\",\"stat_rule\",10000,2022-05-05",
    "\"Steve\",\"stat_rule\",200,2022-05-03",
    "\"Steve\",\"stat_rule\",300,2022-05-01",
    "\"Steve\",\"stat_rule\",400,2022-05-02",
    "\"Steve\",\"stat_rule\",500,2022-05-04"
]

PD_RS_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_all_columns",
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
            "rule_name": "Simple_link_column",
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

PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]

PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        }
    ]
}

PD_RS_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    }
]

PD_RS_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]
