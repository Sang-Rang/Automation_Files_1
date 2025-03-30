from payloads.pushdown.rules.pl_pd_trino_rules_sales_archive_breaks import (
    PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "trdate = timestamp '2022-05-03'",
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
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT sales FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE name = 'John' AND trdate = timestamp '2022-05-01' AND sales = 1000",
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

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE 10 > 9",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586107,
                "uuid": "c52b177a-978d-4399-934f-4839c252360e"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586108,
                "uuid": "d0dce825-d52e-4d28-aa72-62985ce32494"
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
            "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "trdate = timestamp '2022-05-03'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586109,
                "uuid": "8a7b6db2-e7b7-4d88-a47b-4e0f81298fb8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "trdate = timestamp '2022-05-03'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT sales FROM (select * from public.sales) WHERE sales = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586105,
                "uuid": "d64bc08a-7513-4213-80b6-83976fc5c9a5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT sales FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) "
                         "WHERE name = 'John' AND trdate = timestamp '2022-05-01' AND sales = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586106,
                "uuid": "f1b57439-c4c4-47e3-95aa-3811a1f299cd"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE name = 'John' AND trdate = timestamp '2022-05-01' "
                             f"AND sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 40361755,
        "updts": "2024-05-29T22:22:37.211+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 40361756,
        "updts": "2024-05-29T22:22:37.211+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 40361757,
        "updts": "2024-05-29T22:22:41.512+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 40361758,
        "updts": "2024-05-29T22:22:41.512+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 40361743,
        "updts": "2024-05-29T22:22:32.225+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 40361745,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 40361746,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 40361747,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 40361748,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 40361749,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 40361750,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 40361751,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 40361752,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 40361753,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 40361754,
        "updts": "2024-05-29T22:22:36.665+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 40361744,
        "updts": "2024-05-29T22:22:32.314+0000",
        "job_uuid": "d7be8a02-0dca-4c38-a047-34fc34fe375a",
        "dataset": PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-05-29T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    }
]

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Simple_no_link_column",
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
        "rule_name": "FF_no_link_column_in_query",
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

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
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

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
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
            "rule_name": "stat_rule",
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
            "rule_name": "Simple_no_link_column",
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
            "rule_name": "Simple_link_column",
            "name": "Steve",
            "trdate": "2022-05-03",
            "sales": 200
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

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "name": "John",
            "trdate": "2022-05-05",
            "sales": 0
        }
    ]
}

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "name": "John",
        "trdate": "2022-05-05",
        "sales": 0
    }
]

PD_TRINO_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"name\",\"rule_name\",\"sales\",\"trdate\"",
    "\"John\",\"FF_no_link_column_in_query\",0,2022-05-05"
]
