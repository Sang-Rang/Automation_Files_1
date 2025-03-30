from payloads.pushdown.rules.pl_pd_sf_rules_sales_archive_breaks import (
    PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
)

PD_SF_RULES_SALES_ARCHIVE_BREAKS_RULE_DEFINITIONS = [
    {
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
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
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_no_link_column",
        "ruleType": "SQLG",
        "ruleValue": "\"SALES\" = 1000",
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
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "Simple_link_column",
        "ruleType": "SQLG",
        "ruleValue": "\"TRDATE\" = '2022-05-03'",
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
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT \"SALES\" FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE \"SALES\" = 0",
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
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                     f"WHERE \"NAME\" = 'John' AND TRDATE = '2022-05-01' AND \"SALES\" = 1000",
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

PD_SF_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
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
                "id": 1586057,
                "uuid": "b4385cb1-2221-4f28-8983-8f41e91be756"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_no_link_column",
            "ruleType": "SQLG",
            "ruleValue": "\"SALES\" = 1000",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586058,
                "uuid": "af9e0e79-dee8-4112-9bd9-1ff9fd3e992d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "\"SALES\" = 1000",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "\"TRDATE\" = '2022-05-03'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586059,
                "uuid": "a74c25dc-aec0-411b-ab0a-bb74cd3dfedb"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "\"TRDATE\" = '2022-05-03'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT \"SALES\" FROM (select * from PUBLIC.SALES) WHERE \"SALES\" = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586055,
                "uuid": "3162d967-8c74-4289-ad5f-7cd9c082fd70"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT \"SALES\" FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE \"SALES\" = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from PUBLIC.SALES) WHERE \"NAME\" = 'John' "
                         "AND TRDATE = '2022-05-01' AND \"SALES\" = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1586056,
                "uuid": "efaf7c08-4d4e-456b-b1cb-506327bd4983"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET} "
                             f"WHERE \"NAME\" = 'John' AND TRDATE = '2022-05-01' "
                             f"AND \"SALES\" = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SF_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 3219702,
        "updts": "2023-10-14T10:47:54.397+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "FF_all_columns",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 3219714,
        "updts": "2023-10-14T10:47:55.328+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 3219715,
        "updts": "2023-10-14T10:47:55.328+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_no_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 3219704,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-01"
    },
    {
        "seqno": 3219705,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-02"
    },
    {
        "seqno": 3219706,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 3219707,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-04"
    },
    {
        "seqno": 3219708,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 3219709,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-01"
    },
    {
        "seqno": 3219710,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-02"
    },
    {
        "seqno": 3219711,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-03"
    },
    {
        "seqno": 3219712,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-04"
    },
    {
        "seqno": 3219713,
        "updts": "2023-10-14T10:47:55.034+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "stat_rule",
        "link_id": "Steve~|2022-05-05"
    },
    {
        "seqno": 3219703,
        "updts": "2023-10-14T10:47:54.397+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "FF_no_link_column_in_query",
        "link_id": "John~|2022-05-05"
    },
    {
        "seqno": 3219716,
        "updts": "2023-10-14T10:47:55.650+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "John~|2022-05-03"
    },
    {
        "seqno": 3219717,
        "updts": "2023-10-14T10:47:55.650+0000",
        "job_uuid": "5a31b666-1356-43a1-8c4e-419763e48031",
        "dataset": PD_SF_RULES_SALES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-14T00:00:00.000+0000",
        "rule_name": "Simple_link_column",
        "link_id": "Steve~|2022-05-03"
    }
]

PD_SF_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
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
        "rule_name": "Simple_no_link_column",
        "NAME": "John",
        "TRDATE": "2022-05-03",
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
        "rule_name": "stat_rule",
        "NAME": "John",
        "TRDATE": "2022-05-04",
        "SALES": 2000
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
    },
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
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
    }
]

PD_SF_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_CSV_OUTPUT = [
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
PD_SF_RULES_SALES_ARCHIVE_BREAKS_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "Simple_no_link_column",
            "TRDATE": "2022-05-01",
            "SALES": 1000,
            "NAME": "John"
        },
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
            "rule_name": "Simple_no_link_column",
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

PD_SF_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]

PD_SF_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_JSON_OUTPUT = {
    "Rules": [
        {
            "rule_name": "FF_no_link_column_in_query",
            "TRDATE": "2022-05-05",
            "SALES": 0,
            "NAME": "John"
        }
    ]
}

PD_SF_RULES_SALES_ARCHIVE_BREAKS_SQLF_EXPECTED_QUERY_RESULT = [
    {
        "rule_name": "FF_no_link_column_in_query",
        "NAME": "John",
        "TRDATE": "2022-05-05",
        "SALES": 0
    }
]

PD_SF_RULES_SALES_ARCHIVE_BREAKS_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "\"NAME\",\"SALES\",\"TRDATE\",\"rule_name\"",
    "\"John\",0,2022-05-05,\"FF_no_link_column_in_query\""
]
