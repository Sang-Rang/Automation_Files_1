from payloads.pushdown.rules.pl_pd_saph_rules_sales_archive_breaks import (
    PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_no_link_column",
        "ruleType": "SQLG",
        "ruleValue": "SALES = 1000",
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
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "TRDATE = '2022-05-03'",
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
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT SALES FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES) WHERE 10 > 9",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586029,
                "uuid": "712731de-b7f5-4156-aa15-988069c2162d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586030,
                "uuid": "68e8402f-9e23-4012-8e19-671b410838bb"
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
            "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586031,
                "uuid": "3ff168fc-cf90-439c-8f96-4419c2465da2"
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
            "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT SALES FROM (select * from TEST.SALES) WHERE SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586027,
                "uuid": "23693ab8-cc4a-440f-9a97-89e51779a4c8"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT SALES FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from TEST.SALES) WHERE NAME = 'John' "
                         "AND TRDATE = '2022-05-01' AND SALES = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586028,
                "uuid": "9e97f661-4d42-4022-befc-947903a67dce"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.444+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.558+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.683+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.795+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.795+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.919+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": None,
        "updts": "2024-03-26T21:07:57.919+0000",
        "job_uuid": "c48f0877-3a80-425f-927a-a2c1a691085b",
        "dataset": PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-03-26T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    }
]

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_all_columns",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "Simple_no_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-01",
        "SALES": 1000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-02",
        "SALES": 2000
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-03",
        "SALES": 1000
    },
    {
        "rule_name": "Simple_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-03",
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
        "NAME": "John",
        "TRDATE": "2022-05-04",
        "SALES": 2000
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    },
    {
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
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
        "TRDATE": "2022-05-02",
        "SALES": 400
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-03",
        "SALES": 200
    },
    {
        "rule_name": "Simple_link_column",
        "NAME": "Steve",
        "TRDATE": "2022-05-03",
        "SALES": 200
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-04",
        "SALES": 500
    },
    {
        "rule_name": "stat_rule",
        "NAME": "Steve",
        "TRDATE": "2022-05-05",
        "SALES": 10000
    }
]

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
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

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_all_columns",
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
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-03",
            "SALES": 1000,
            "NAME": "John"
        },
        {
            "rule_name": "Simple_link_column",
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
            "rule_name": "stat_rule",
            "TRDATE": "2022-05-03",
            "SALES": 200,
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

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "TRDATE": "2022-05-05",
            "SALES": 0,
            "NAME": "John"
        }
    ]
}

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    }
]

PD_SAPH_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]
