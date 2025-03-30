from payloads.pushdown.rules.pl_pd_trino_rules_sales_link_id import (
    PD_TRINO_RULES_SALES_LINK_ID_DATASET,
    PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
)

PD_TRINO_RULES_SALES_LINK_ID_RULE_DEFINITIONS = [
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} WHERE $rowCount > 9",
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
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT sales FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} WHERE sales = 0",
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
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} "
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

PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT * FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
            "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
            "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT sales FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE sales = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT * FROM @{PD_TRINO_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE name = 'John' AND trdate = timestamp '2022-05-01' "
                             f"AND sales = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_all_columns,John~|2022-05-01,John,2022-05-01",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-01,John,2022-05-01",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-01,John,2022-05-01",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-02,John,2022-05-02",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-03,John,2022-05-03",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-04,John,2022-05-04",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-05,John,2022-05-05",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-01,Steve,2022-05-01",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-02,Steve,2022-05-02",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-04,Steve,2022-05-04",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-05,Steve,2022-05-05"
]

PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_all_columns",
        "linkId": "John~|2022-05-01",
        "name": "John",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "name": "John",
        "trdate": "2022-05-05"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "John~|2022-05-03",
        "name": "John",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "Steve~|2022-05-03",
        "name": "Steve",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-01",
        "name": "John",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-03",
        "name": "John",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-01",
        "name": "John",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-02",
        "name": "John",
        "trdate": "2022-05-02"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-03",
        "name": "John",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-04",
        "name": "John",
        "trdate": "2022-05-04"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-05",
        "name": "John",
        "trdate": "2022-05-05"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-01",
        "name": "Steve",
        "trdate": "2022-05-01"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-02",
        "name": "Steve",
        "trdate": "2022-05-02"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-03",
        "name": "Steve",
        "trdate": "2022-05-03"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-04",
        "name": "Steve",
        "trdate": "2022-05-04"
    },
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-05",
        "name": "Steve",
        "trdate": "2022-05-05"
    }
]

PD_TRINO_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]

PD_TRINO_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_TRINO_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "name": "John",
        "trdate": "2022-05-05"
    }
]

PD_TRINO_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,name,trdate",
    f"{PD_TRINO_RULES_SALES_LINK_ID_DATASET},{PD_TRINO_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]
