from datetime import datetime, timezone, timedelta

import allure
import pytest
from assertpy import assert_that

from data_test.analyze_estimate_filtergram_file_types.data_aef_athena_up import (
    EXP_JOB_EST,
    PL_JOB_EST,
    PL_DAYS_WITH_DATA,
    EXP_DAYS_WITH,
)
from data_test.pullup.data_audit_trail import (
    CONNECTION,
    DATASET,
    DATASET_EDIT,
    QUERY,
    PL_RENAME_DATASET,
    PL_BU_NAME,
    PL_MANUAL_SETTINGS_PERSIST,
    PL_STRICT_SETTINGS_PERSIST,
    PL_LENIENT_SETTINGS_PERSIST,
    PL_SUPPRESS_SETTINGS_PERSIST,
    PL_BU_TO_DATASET,
    EXP_AUDIT_DS,
    PL_DS_AUDIT_TRAIL,
    DATASET_DS_AUDIT,
    EXP_SECURITY_AUDIT_STRINGS,
    PL_SECURITY_DATA_ASSET,
    PL_SECURITY_AUDIT_TRAIL,
)
from endpoints.v2.controller_audit_trail import (
    V2_GET_AUDIT_TRAIL_ITEMS,
    V2_GET_DATASETS_AUDIT_TRAIL_ITEMS,
)
from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT
from endpoints.v2.controller_business_unit_to_dataset import (
    V2_BUSINESS_UNIT_TO_DS,
)
from endpoints.v2.controller_catalog import (
    V2_GET_DATA_ASSETS_WITH_FILTERS,
    V2_DELETE_DATASET_LIST,
)
from endpoints.v2.controller_dataset import V2_RENAME_DATASET
from endpoints.v2.controller_explorer import V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS
from endpoints.v2.controller_label import (
    V2_SET_BOUNDRY_MANUAL,
    V2_SET_BOUNDRY_TIER,
    V2_SET_BOUNDRY_SUPPRESS,
)
from endpoints.v2.controller_web_log import V2_GET_LIMITED_WEB_LOGS

from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.constants import BASE_CREDS
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup
class TestAuditTrail:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def get_and_validate_limited_web_log_item(api_utils, expected):
        """Validate a single record in the getLimitedWebLog return"""
        # Note: Return is always sorted by timestamp by default, the most recent is the 1st.

        now = datetime.now(timezone.utc)
        found_log = None
        logs = api_utils.get(V2_GET_LIMITED_WEB_LOGS)
        assert_that(logs, f"No log data found: {logs}").contains_key("data")

        # Find the first log with the expected descriptions.
        for log in logs["data"]:
            if log["logDesc"] == expected["logDesc"]:
                found_log = log
                break

        assert_that(found_log, "Could not find expected log of job estimate event").is_not_none()
        compare_dicts_are_equal(expected, found_log, ["updtTs", "logId", "logCode"])

        # Variable numbers
        assert_that(found_log["logId"], "Invalid log id").is_greater_than(0)
        assert_that(found_log["logCode"], "Invalid log code").is_greater_than(0)

        # Timestamp within minutes to allow for run/load times
        buffer = timedelta(minutes=5)
        convert_date = datetime.strptime(found_log["updtTs"], "%Y-%m-%dT%H:%M:%S.%f%z")
        assert_that(convert_date, "Updated timestamp not before now").is_close_to(now, buffer)

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    @pytest.mark.skip(reason="Bug DEV-77633, should be fixed in 2024.03")
    @allure.issue(
        "https://engineering-collibra.atlassian.net/browse/DEV-77633",
        "[Dataset Audit Trail] Page items counter returns 0 when 4 items are present.",
    )
    def test_audit_dataset(self, api_utils):
        """Audit Trail - Dataset"""
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            CONNECTION,
            DATASET_DS_AUDIT,
            QUERY,
        )

        # Add rules to validate against in the audit trail
        helper.setup_dataset(api_utils, dataset_defs)
        api_utils.post(V2_SET_BOUNDRY_MANUAL, params=PL_MANUAL_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_TIER, params=PL_STRICT_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_TIER, params=PL_LENIENT_SETTINGS_PERSIST)
        api_utils.post(V2_SET_BOUNDRY_SUPPRESS, params=PL_SUPPRESS_SETTINGS_PERSIST)

        # Get the Audit Trail and validate data.
        audit_trail = api_utils.get(V2_GET_DATASETS_AUDIT_TRAIL_ITEMS, PL_DS_AUDIT_TRAIL)

        assert_that(EXP_AUDIT_DS["recordsTotal"], "No records found").is_greater_than(0)
        assert_that(EXP_AUDIT_DS["draw"], "DS Audit draw").is_equal_to(audit_trail["draw"])
        assert_that(EXP_AUDIT_DS["recordsFiltered"], "DS Audit Records Filtered").is_equal_to(
            audit_trail["recordsFiltered"]
        )

        found_data_asset_list = audit_trail["dataAssetList"]
        exp_data_asset_list = EXP_AUDIT_DS["dataAssetList"]
        for i, audit_str in enumerate(exp_data_asset_list):
            assert_that(found_data_asset_list[i]["activityId"]).is_greater_than(0)

            assert_that(found_data_asset_list[i]["username"]).is_equal_to(BASE_CREDS["username"])
            assert_that(found_data_asset_list[i]["dataset"]).is_equal_to(DATASET_DS_AUDIT)
            assert_that(found_data_asset_list[i]["action"]).is_equal_to(audit_str["action"])
            assert_that(found_data_asset_list[i]["changeDescription"]).is_equal_to(
                audit_str["changeDescription"]
            )

            # The dates that return also include a time (which is not zeros)
            # So check the string contains the expected date
            assert_that(found_data_asset_list[i]["auditTs"]).contains(audit_str["auditTs"])
            assert_that(found_data_asset_list[i]["auditTsStr"]).contains(audit_str["auditTsStr"])

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    def test_audit_trail_security(self, api_utils):
        """Audit Trail - Security"""
        dataset_defs = helper.get_minimum_job_payload(api_utils, CONNECTION, DATASET, QUERY)

        # Get any business unit
        found_business_units = api_utils.get(V2_BUSINESS_UNIT)

        if len(found_business_units["result"]) > 0:
            business_unit_id = found_business_units["result"][0]["id"]
        else:
            # Create BU if none exists
            create_bu = api_utils.post(V2_BUSINESS_UNIT, PL_BU_NAME)
            business_unit_id = create_bu["result"]

        PL_BU_TO_DATASET["business_unit_id"] = business_unit_id

        # Sanity check the business unit found
        assert_that(business_unit_id, "No valid business unit ID found").is_greater_than(0)

        # Create job
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dataset_defs)

        # Update BU
        resp_bu_ds = api_utils.post(V2_BUSINESS_UNIT_TO_DS, params=PL_BU_TO_DATASET)["id"]
        assert_that(
            resp_bu_ds["businessUnitId"], "Business unit updated returned unexpected id"
        ).is_equal_to(business_unit_id)
        assert_that(
            resp_bu_ds["dataset"], "Business unit updated returned unexpected dataset name"
        ).is_equal_to(DATASET)

        # Update the data table name
        patch_response = api_utils.patch(
            V2_RENAME_DATASET, params=PL_RENAME_DATASET, return_json=False
        )
        assert_that(patch_response.status_code).is_equal_to(200)

        # Get the column data via search query again
        get_ds_asset_arr = api_utils.get(
            V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_SECURITY_DATA_ASSET
        )
        asset_arr = get_ds_asset_arr["dataAssetList"][0]

        # Validate the dataset name has been updated
        assert_that(asset_arr["dataset"], "Dataset name did not update correctly").is_equal_to(
            DATASET_EDIT
        )

        # Delete the dataset
        PL_SECURITY_DATA_ASSET["search[value]"] = DATASET_EDIT
        del_ds = api_utils.post(
            V2_DELETE_DATASET_LIST,
            {"datasets": DATASET_EDIT},
            return_json=False,
        )
        assert_that(del_ds.status_code).is_equal_to(200)

        # Search to confirm deleted, no results should return
        get_del_ds = api_utils.get(V2_GET_DATA_ASSETS_WITH_FILTERS, params=PL_SECURITY_DATA_ASSET)
        assert_that(
            get_del_ds["dataAssetList"], "Expected no results after dataset deleted."
        ).is_equal_to([])

        # Get the Audit Trail for given user
        audit_trail = api_utils.get(V2_GET_AUDIT_TRAIL_ITEMS, PL_SECURITY_AUDIT_TRAIL)

        assert_that(audit_trail["recordsTotal"], "No records returned").is_greater_than(0)
        assert_that(audit_trail["recordsFiltered"], "No filtered records returned").is_greater_than(
            0
        )

        return_data = str(audit_trail["dataAssetList"])
        for audit_str in EXP_SECURITY_AUDIT_STRINGS:
            assert_that(return_data).contains(audit_str)

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    def test_user_audit_web_log_job_estimate(self, api_utils):
        """Audit Trail - User Audit Web Logs contains Job Estimate"""
        expected = {
            "itemName": "com.simba.athena.jdbc.Driver",
            "userName": BASE_CREDS["username"],
            "activity": "EXPLORER",
            "stage": "JOB ESTIMATE",
            "logDesc": "select count(1) from ( select CAST(cm_bdos as TIMESTAMP) as cm_bdos, "
            "cm_claim_status, cm_claimant_ag",
            "logHint": "",
            "stageTime": None,
            "prettyStageTime": "",
            "taskName": f"EXPLORER com.simba.athena.jdbc.Driver {BASE_CREDS['username']}",
        }

        aef.job_estimator(api_utils, PL_JOB_EST, EXP_JOB_EST)
        self.get_and_validate_limited_web_log_item(api_utils, expected)

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    def test_user_audit_web_log_analyze(self, api_utils):
        """Audit Trail - User Audit Web Logs contains Analyze"""
        expected = {
            "itemName": "com.simba.athena.jdbc.Driver",
            "userName": BASE_CREDS["username"],
            "activity": "EXPLORER",
            "stage": "ANALYZE",
            "logDesc": "select count(*) rowcount, DATE_TRUNC('day', \"cm_bdos\") days from "
            'default.aclaims_master where "cm_bd',
            "logHint": "",
            "stageTime": None,
            "prettyStageTime": "",
            "taskName": f"EXPLORER com.simba.athena.jdbc.Driver {BASE_CREDS['username']}",
        }

        aef.analyze(api_utils, PL_DAYS_WITH_DATA, EXP_DAYS_WITH)
        self.get_and_validate_limited_web_log_item(api_utils, expected)

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    def test_user_audit_web_log_sql_statement(self, api_utils):
        payload = {
            "table": "PUBLIC.ADMIN_SETTINGS",
            "aliasname": "APPROVED_SNOWFLAKE_UP",
            "hostname": "jdbc:snowflake://owlanalyticspartner.us-east-2.aws.snowflakecomputing.com"
            "?db=owluserdb&warehouse=owluserdb",
            "drivername": "net.snowflake.client.jdbc.SnowflakeDriver",
            "cols": "*",
        }
        expected = {
            "itemName": "net.snowflake.client.jdbc.SnowflakeDriver",
            "userName": BASE_CREDS["username"],
            "activity": "EXPLORER",
            "stage": "SQL STMT",
            "logDesc": 'select * from PUBLIC."ADMIN_SETTINGS" limit 30',
            "logHint": "",
            "stageTime": None,
            "taskName": "EXPLORER net.snowflake.client.jdbc.SnowflakeDriver"
            f" {BASE_CREDS['username']}",
            "prettyStageTime": "",
        }
        api_utils.post(V2_GET_LIST_DATA_SCHEMA_PREVIEW_DB_TABLE_BY_COLS, params=payload)
        self.get_and_validate_limited_web_log_item(api_utils, expected)

    @allure.feature("Admin")
    @allure.story("Audit Trail")
    def test_user_audit_web_logs_full(self, api_utils):
        """Audit Trail - User Audit Web Logs data quality check"""
        valid_activities = ["EXPLORER", "SQL"]
        valid_stages = [
            "ANALYZE",
            "JOB ESTIMATE",
            "SQL",
            "SQL STMT",
            "SQL STMT RAW LIMIT",
            "Driver Connect",
            "Shim Driver",
        ]
        now = datetime.now(timezone.utc)

        logs = api_utils.get(V2_GET_LIMITED_WEB_LOGS)
        assert_that(logs, f"No log data found: {logs}").contains_key("data")
        assert_that(len(logs["data"]), "No log records found").is_greater_than(0)

        for log in logs["data"]:
            convert_date = datetime.strptime(log["updtTs"], "%Y-%m-%dT%H:%M:%S.%f%z")

            # Numbers & Username
            assert_that(log["logId"], "Invalid log id").is_greater_than(0)
            assert_that(log["logCode"], "Invalid log code").is_greater_than(0)
            assert_that(log["userName"], "Unexpected user name").is_equal_to(BASE_CREDS["username"])

            # Check lists
            assert_that(valid_activities, "Unexpected activity").contains(log["activity"])
            assert_that(valid_stages, "Unexpected stage").contains(log["stage"])

            # Strings
            assert_that(log["itemName"], "Item Name is empty").is_not_empty()
            assert_that(log["logDesc"], "Log Desc is empty").is_not_empty()
            assert_that(log["logHint"], "Log hit was not empty").is_empty()
            assert_that(log["stageTime"], "Stage time was not none").is_none()
            assert_that(log["prettyStageTime"], "Pretty Stage Time was not empty").is_empty()
            assert_that(log["taskName"], "Task Name is empty").is_not_empty()

            # Date
            assert_that(convert_date, "Updated timestamp not before now").is_before(now)
