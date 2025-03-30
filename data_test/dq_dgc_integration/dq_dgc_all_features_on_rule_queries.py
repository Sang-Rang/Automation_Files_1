from payloads.dq_dgc_integration.pl_dq_dgc_all_features_on import DS_DEF_DGC_ALL_FEATURES_ON_NAME

DQ_DGC_ALL_FEATURES_ON_QUERIES = [
    {
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
        "ruleNm": "SQLG_FIRSTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586",
        "ruleType": "SQLG",
        "ruleValue": "firstname IS NOT NULL",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "firstname",
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
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
        "ruleNm": "SQLF_RULE_POSTMAN_GOLDEN_RUN_1721685131586",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE firstname IS NOT NULL ",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "firstname",
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
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
        "ruleNm": "SQLG_LASTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586",
        "ruleType": "SQLG",
        "ruleValue": "lastname IS NOT NULL",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "lastname",
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
        "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
        "ruleNm": "if_costcode_is_SALES_CUSTOM_RULE",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE costcode IS NOT null",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "costcode",
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

DQ_DGC_ALL_FEATURES_RULE_DEFINITIONS_OUTPUT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "runId": "2022-01-07T00:00:00.000+0000",
            "ruleNm": "SQLG_LASTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586",
            "ruleType": "SQLG",
            "ruleValue": "lastname IS NOT NULL",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 437021,
                "uuid": "3a693260-a1f1-4b12-a0ec-8b1d877f28ff"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "lastname IS NOT NULL",
            "totalCount": 999,
            "rowsBreaking": 999,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "runId": "2022-01-07T00:00:00.000+0000",
            "ruleNm": "SQLG_FIRSTNAME_NOT_NULL_POSTMAN_GOLDEN_RUN_1721685131586",
            "ruleType": "SQLG",
            "ruleValue": "firstname IS NOT NULL",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 437022,
                "uuid": "3206be40-4404-467e-9987-d5ef4485a9dc"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "firstname IS NOT NULL",
            "totalCount": 999,
            "rowsBreaking": 999,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "runId": "2022-01-07T00:00:00.000+0000",
            "ruleNm": "SQLF_RULE_POSTMAN_GOLDEN_RUN_1721685131586",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_ALL_FEATURES_ON_NAME}_dataset "
                         f"WHERE firstname IS NOT NULL ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 437024,
                "uuid": "768fda5e-ff77-441d-ac30-8529aef66fe7"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE firstname IS NOT NULL ",
            "totalCount": 999,
            "rowsBreaking": 999,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        },
        {
            "dataset": DS_DEF_DGC_ALL_FEATURES_ON_NAME,
            "runId": "2022-01-07T00:00:00.000+0000",
            "ruleNm": "if_costcode_is_SALES_CUSTOM_RULE",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_ALL_FEATURES_ON_NAME}_dataset "
                         f"WHERE costcode IS NOT null ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 437023,
                "uuid": "627127eb-dc43-49ac-873e-9974ae035c38"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE costcode IS NOT null",
            "totalCount": 999,
            "rowsBreaking": 999,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

ADAPTIVE_RULE_EXPECTED_DESCRIPTION = (
    "AdaptiveRule: AdaptiveRules are rules that automatically "
    "observe and adapt to changes in numeric representations of "
    "data over time and down-score any values outside defined "
    "boundaries. AdaptiveRules include common observability "
    "metrics, such as distribution and completeness."
)
SOURCE_RULE_EXPECTED_DESCRIPTION = (
    "Source Rule: Mapping detects row count, schema, and cell "
    "value inconsistencies between the source file or table and "
    "the target file or table and down-scores any observations."
)
SHAPE_RULE_EXPECTED_DESCRIPTION = (
    "Shape Rule: Shape Rules detect inconsistencies in the data "
    "formats of string columns and down-score any observations."
)
SCHEMA_RULE_EXPECTED_DESCRIPTION = (
    "Schema Rule: Schema detects changes to columns and data types and down-score any observations."
)
RECORD_RULE_EXPECTED_DESCRIPTION = (
    "Record Rule: Records detect rows of data that drop out of a "
    "data set and down-score any observations"
)
PATTERN_RULE_EXPECTED_DESCRIPTION = (
    "Pattern Rule: Patterns detect similarities among string "
    "values across columns and down-score any observations."
)
OUTLIER_RULE_EXPECTED_DESCRIPTION = (
    "Outlier Rule: Outliers detect values that differ "
    "significantly from the rest of the data and may indicate "
    "bad or incorrect data, then down-score any values outside "
    "defined boundaries."
)
DUPLICATE_RULE_EXPECTED_DESCRIPTION = (
    "Duplicate Rule: Dupes detect matching data in data sources "
    "and down-score the values above a defined threshold."
)
