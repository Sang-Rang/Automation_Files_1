from payloads.pushdown.rules.pl_pd_saph_rules_sales_link_id import (
    PD_SAPH_RULES_SALES_LINK_ID_DATASET,
    PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
)

PD_SAPH_RULES_SALES_LINK_ID_RULE_DEFINITIONS = [
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} WHERE $rowCount > 9",
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
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT SALES FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} WHERE SALES = 0",
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
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "FF_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} WHERE NAME = 'John' "
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

PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
            "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
            "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT SALES FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
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
            "ruleCondition": f"SELECT * FROM @{PD_SAPH_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}

PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_all_columns,John~|2022-05-01,John,2022-05-01",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-01,John,2022-05-01",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-01,John,2022-05-01",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-02,John,2022-05-02",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-03,John,2022-05-03",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-04,John,2022-05-04",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-05,John,2022-05-05",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-01,Steve,2022-05-01",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-02,Steve,2022-05-02",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-04,Steve,2022-05-04",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-05,Steve,2022-05-05"
]

PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_all_columns",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_link_column",
        "linkId": "Steve~|2022-05-03",
        "NAME": "Steve",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "Simple_no_link_column",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-01",
        "NAME": "John",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-02",
        "NAME": "John",
        "TRDATE": "2022-05-02"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-03",
        "NAME": "John",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-04",
        "NAME": "John",
        "TRDATE": "2022-05-04"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-01",
        "NAME": "Steve",
        "TRDATE": "2022-05-01"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-02",
        "NAME": "Steve",
        "TRDATE": "2022-05-02"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-03",
        "NAME": "Steve",
        "TRDATE": "2022-05-03"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-04",
        "NAME": "Steve",
        "TRDATE": "2022-05-04"
    },
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "stat_rule",
        "linkId": "Steve~|2022-05-05",
        "NAME": "Steve",
        "TRDATE": "2022-05-05"
    }
]

PD_SAPH_RULES_SALES_LINK_ID_SQLF_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]

PD_SAPH_RULES_SALES_LINK_ID_SQLF_EXPECTED_JSON_OUTPUT = [
    {
        "dataset": PD_SAPH_RULES_SALES_LINK_ID_DATASET,
        "runId": PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
        "ruleName": "FF_no_link_column_in_query",
        "linkId": "John~|2022-05-05",
        "NAME": "John",
        "TRDATE": "2022-05-05"
    }
]
PD_SAPH_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PD_SAPH_RULES_SALES_LINK_ID_DATASET},{PD_SAPH_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"FF_no_link_column_in_query,John~|2022-05-05,John,2022-05-05"
]
