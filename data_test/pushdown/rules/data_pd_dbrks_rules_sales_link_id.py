from payloads.pushdown.rules.pl_pd_dbrks_rules_sales_link_id import (
    PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
    PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
)

PD_DBRKS_RULES_SALES_LINK_ID_RULE_DEFINITIONS = [
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} WHERE $rowCount > 9",
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
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT SALES FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} WHERE SALES = 0",
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
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} WHERE NAME = 'John' "
                     f"AND TRDATE = '2022-05-01' AND SALES = 1000",
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

PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
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
                "id": 1585975,
                "uuid": "3fe233fe-af80-480a-9942-89dc062b7dde"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
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
                "id": 1585976,
                "uuid": "f8d60a65-9db2-4407-9758-502dd7587a61"
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
            "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
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
                "id": 1585977,
                "uuid": "9d84a0d8-103a-4539-8744-c60b1bb88f2b"
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
            "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": "SELECT SALES FROM (select * from public.sales) WHERE SALES = 0",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585973,
                "uuid": "c430638d-e22f-4691-b12e-b452d46de98f"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT SALES FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_all_columns",
            "ruleType": "SQLF",
            "ruleValue": "SELECT * FROM (select * from public.sales) WHERE NAME = 'John' "
                         "AND TRDATE = '2022-05-01' AND SALES = 1000",
            "filterQuery": None,
            "score": 10,
            "perc": 10.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585974,
                "uuid": "fb9fa815-0bf8-4d8a-a8b9-83cc30491262"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PD_DBRKS_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_all_columns,John~|2022-05-01,John,2022-05-01",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-01,John,2022-05-01",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-01,John,2022-05-01",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-02,John,2022-05-02",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-03,John,2022-05-03",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-04,John,2022-05-04",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-05,John,2022-05-05",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-01,Steve,2022-05-01",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-02,Steve,2022-05-02",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-04,Steve,2022-05-04",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-05,Steve,2022-05-05"
]

PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_all_columns",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "Steve~|2022-05-03",
        "NAME": "Steve",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-02",
        "NAME": "John",
        "TRDATE": "2022-05-02"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-04",
        "NAME": "John",
        "TRDATE": "2022-05-04"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-01",
        "NAME": "Steve",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-02",
        "NAME": "Steve",
        "TRDATE": "2022-05-02"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-03",
        "NAME": "Steve",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-04",
        "NAME": "Steve",
        "TRDATE": "2022-05-04"
    },
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-05",
        "NAME": "Steve",
        "TRDATE": "2022-05-05"
    }
]

PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]

PD_DBRKS_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_DBRKS_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    }
]
PD_DBRKS_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_DBRKS_RULES_SALES_LINK_ID_DATASET},{PD_DBRKS_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]
