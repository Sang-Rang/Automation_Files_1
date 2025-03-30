from payloads.pullup.pl_pullup_rules_sales_link_id import (
    PULLUP_RULES_SALES_LINK_ID_DATASET,
    PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID,
)

PULLUP_RULES_SALES_LINK_ID_RULE_DEFINITIONS = [
    {
        "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} WHERE $rowCount > 9",
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
        "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
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
        "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "ff_no_link_column_in_query",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT SALES FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} WHERE SALES = 0",
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
        "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
        "ruleNm": "ff_all_columns",
        "ruleType": "SQLF",
        "ruleValue": f"SELECT * FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} "
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

PULLUP_RULES_SALES_LINK_ID_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {PULLUP_RULES_SALES_LINK_ID_DATASET}_dataset "
                         f"WHERE 10 > 9 ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449796,
                "uuid": "8769bae2-7dab-4f86-813a-6e5bd7611b26"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE $rowCount > 9",
            "totalCount": 10,
            "rowsBreaking": 10,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "Simple_no_link_column",
            "ruleType": "SQLG",
            "ruleValue": "SALES = 1000",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449798,
                "uuid": "ab512587-a138-4ab2-93ef-43be4cb08793"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "Simple_link_column",
            "ruleType": "SQLG",
            "ruleValue": "TRDATE = '2022-05-03'",
            "filterQuery": None,
            "score": 20,
            "perc": 20.000000298023224,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449797,
                "uuid": "e92ac192-32e8-4393-bdc3-6e69ca8fc04d"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "TRDATE = '2022-05-03'",
            "totalCount": 10,
            "rowsBreaking": 2,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "ff_no_link_column_in_query",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT SALES FROM {PULLUP_RULES_SALES_LINK_ID_DATASET}_dataset "
                         f"WHERE SALES = 0 ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449799,
                "uuid": "c188ef8e-6ae4-4387-8ee6-a6d9ae68e9a5"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT SALES FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE SALES = 0",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": PULLUP_RULES_SALES_LINK_ID_DATASET,
            "runId": "2024-11-14T00:00:00.000+0000",
            "ruleNm": "ff_all_columns",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {PULLUP_RULES_SALES_LINK_ID_DATASET}_dataset "
                         f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000 ",
            "filterQuery": None,
            "score": 10,
            "perc": 10.000000149011612,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 449800,
                "uuid": "9bbab5df-6083-4006-88fd-47a71d7df805"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"SELECT * FROM @{PULLUP_RULES_SALES_LINK_ID_DATASET} "
                             f"WHERE NAME = 'John' AND TRDATE = '2022-05-01' AND SALES = 1000",
            "totalCount": 10,
            "rowsBreaking": 1,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

PULLUP_RULES_SALES_LINK_ID_FF_ALL_COLUMNS_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"ff_all_columns,John~|2022-05-01,John,2022-05-01"
]

PULLUP_RULES_SALES_LINK_ID_FF_NO_LINK_COLUMN_IN_QUERY_EXPECTED_CSV_OUTPUT = []

PULLUP_RULES_SALES_LINK_ID_SIMPLE_LINK_COLUMN_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,John~|2022-05-03,John,2022-05-03",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_link_column,Steve~|2022-05-03,Steve,2022-05-03"
]

PULLUP_RULES_SALES_LINK_ID_SIMPLE_NO_LINK_COLUMN_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-01,John,2022-05-01",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"Simple_no_link_column,John~|2022-05-03,John,2022-05-03"
]

PULLUP_RULES_SALES_LINK_ID_STAT_RULE_EXPECTED_CSV_OUTPUT = [
    "dataset,runId,ruleName,linkId,NAME,TRDATE",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-01,John,2022-05-01",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-02,John,2022-05-02",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-03,John,2022-05-03",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-04,John,2022-05-04",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,John~|2022-05-05,John,2022-05-05",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-01,Steve,2022-05-01",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-02,Steve,2022-05-02",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-03,Steve,2022-05-03",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-04,Steve,2022-05-04",
    f"{PULLUP_RULES_SALES_LINK_ID_DATASET},{PULLUP_RULES_SALES_LINK_ID_EXPECTED_RUN_ID},"
    f"stat_rule,Steve~|2022-05-05,Steve,2022-05-05"
]
