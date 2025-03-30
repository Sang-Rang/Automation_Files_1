from payloads.pushdown.rules.pl_pd_bq_rules_sales_archive_breaks import (
    PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_no_link_column",
        "ruleType": "SQLG",
        "ruleValue": "SALES = 1000",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "SALES",
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
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "TRDATE = '2022-05-03'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "TRDATE",
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
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT SALES FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE SALES = 0",
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
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
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

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES) WHERE 10 > 9",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585955,
                "uuid": "0c0ef9d9-947f-4cac-b524-45e7342027a8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_no_link_column",
            "ruleType": "SQLG",
            "ruleValue": "SALES = 1000",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585956,
                "uuid": "baa175d4-b652-41de-a7a4-2d7f4eae31ce"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "TRDATE = '2022-05-03'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585957,
                "uuid": "6da0b090-f729-4f92-9a28-b32506f9f661"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "TRDATE = '2022-05-03'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT SALES FROM (select * from PUBLIC.SALES) WHERE SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585954,
                "uuid": "5b7d811d-74b2-46eb-8de2-5bb602cdcd37"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT SALES FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES) WHERE NAME = 'John' "
                         "AND TRDATE = '2022-05-01' AND SALES = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585953,
                "uuid": "9c8e62dc-0c86-401c-831f-3d9ab7c931cf"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:19.571+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.346+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.346+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:22.826+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:22.826+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:19.420+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 1,
        "updts": "2023-10-15T03:22:21.192+0000",
        "job_uuid": "55282595-c719-4a5c-8c73-0fdd7d000c7d",
        "dataset": PD_BQ_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02"
    }
]

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "Simple_no_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "Simple_no_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-03",
        "SALES": 1000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-03",
        "SALES": 200
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-02",
        "SALES": 400
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-04",
        "SALES": 2000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-01",
        "SALES": 300
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-04",
        "SALES": 500
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-05",
        "SALES": 10000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-03",
        "SALES": 1000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-02",
        "SALES": 2000
    },
    {
        "rule_name": "Simple_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-03",
        "SALES": 1000
    },
    {
        "rule_name": "Simple_link_column",
        "NAME": "Steve",
        "TRDATE": "2022-05-03",
        "SALES": 200
    },
    {
        "rule_name": "FF_all_columns",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    }
]

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\"",
    "\"John\",0,2022-05-05,\"stat_rule\"",
    "\"John\",1000,2022-05-01,\"FF_all_columns\"",
    "\"John\",1000,2022-05-01,\"Simple_no_link_column\"",
    "\"John\",1000,2022-05-01,\"stat_rule\"",
    "\"John\",1000,2022-05-03,\"Simple_link_column\"",
    "\"John\",1000,2022-05-03,\"Simple_no_link_column\"",
    "\"John\",1000,2022-05-03,\"stat_rule\"",
    "\"John\",2000,2022-05-02,\"stat_rule\"",
    "\"John\",2000,2022-05-04,\"stat_rule\"",
    "\"Steve\",10000,2022-05-05,\"stat_rule\"",
    "\"Steve\",200,2022-05-03,\"Simple_link_column\"",
    "\"Steve\",200,2022-05-03,\"stat_rule\"",
    "\"Steve\",300,2022-05-01,\"stat_rule\"",
    "\"Steve\",400,2022-05-02,\"stat_rule\"",
    "\"Steve\",500,2022-05-04,\"stat_rule\""
]

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_all_columns",
            "TRDATE": "2022-05-01",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-01",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "Simple_no_link_column",
            "TRDATE": "2022-05-01",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-02",
            "SALES": 2000,
            "NAME": "John"
        },
        {
            "rule_name": "Simple_link_column",
            "TRDATE": "2022-05-03",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-03",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "Simple_no_link_column",
            "TRDATE": "2022-05-03",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-04",
            "SALES": 2000,
            "NAME": "John"
        },
        {
            "rule_name": "FF_no_link_column_in_query",
            "TRDATE": "2022-05-05",
            "SALES": 0,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-05",
            "SALES": 0,
            "NAME": "John"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-01",
            "SALES": 300,
            "NAME": "Steve"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-02",
            "SALES": 400,
            "NAME": "Steve"
        },
        {
            "rule_name": "Simple_link_column",
            "TRDATE": "2022-05-03",
            "SALES": 200,
            "NAME": "Steve"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-03",
            "SALES": 200,
            "NAME": "Steve"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-04",
            "SALES": 500,
            "NAME": "Steve"
        },
        {
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-05",
            "SALES": 10000,
            "NAME": "Steve"
        }
    ]
}

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "TRDATE": "2022-05-05",
            "SALES": 0,
            "NAME": "John"
        }
    ]
}

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    }
]

PD_BQ_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]
