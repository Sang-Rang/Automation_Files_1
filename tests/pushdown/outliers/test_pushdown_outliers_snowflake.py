import allure
from assertpy import assert_that
import pytest

from data_test.pushdown.outliers.data_pd_sf_outliers_cat_key_date_ms_trade import (
    PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_cat_key_nodate_nyse import (
    PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_cat_key_nodate_us_airports import (
    PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_cat_nokey_date_ms_trade import (
    PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_cat_nokey_nodate_nyse import (
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_cat_nokey_nodate_us_airports import (
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_key_date_ms_trade import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_key_date_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_key_date_union_lookback_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_key_nodate_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_nokey_date_nyse import (
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_nokey_nodate_aclaims_master import (
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_sf_outliers_num_nokey_nodate_employees import (
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS,
)
from endpoints.v2.controller_hoot import (
    V2_GET_ISSUE_COUNTS,
)
from endpoints.v2.controller_admin import V2_GET_ADMIN_CONFIG
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_key_date_ms_trade import (
    PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
    PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_nokey_date_ms_trade import (
    PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET,
    PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_date_ms_trade import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
    PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_key_nodate_nyse import (
    PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
    PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_key_nodate_us_airports import (
    PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_DATASET,
    PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_nokey_nodate_nyse import (
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_nokey_nodate_us_airports import (
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_date_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_DATASET,
    PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_date_union_lookback_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET,
    PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_nodate_nyse import (
    PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_DATASET,
    PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_nokey_date_nyse import (
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET,
    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_nokey_nodate_aclaims_master import (
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_DATASET,
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_nokey_nodate_employees import (
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
    PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_sf_outliers_num_storage_limit import (
    PD_SF_OUTLIERS_NUM_STORAGE_LIMIT_DATASET,
    PD_SF_OUTLIERS_NUM_STORAGE_LIMIT_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_outliers import (
    validate_outliers_findings,
    validate_outliers_findings_not_present,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.snowflake
class TestPushdownOutliersSnowflake:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_key_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET
        )

        helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-10T00:00:00.000+0000",
            PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_key_nodate_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_key_nodate_us_airports(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_nokey_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET
        )

        helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-10T00:00:00.000+0000",
            PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_SF_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_nokey_nodate_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_categorical_nokey_nodate_us_airports(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_key_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-06",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET
        )

        helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-05T00:00:00.000+0000",
            PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_key_date_nyse(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers": PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers": PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers": PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers": PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
            {
                "run_id": "2018-01-12",
                "expected_outliers": PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_DATASET
        )

        helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD)

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"
            validate_outliers_findings(
                api_utils,
                PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_SF_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_key_date_union_lookback_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET
        )

        helper.delete_dataset_if_exists(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET
        )

        lookback_run_id_values = [
            "2017-12-05",
            "2017-12-12",
            "2017-12-19",
            "2017-12-26",
            "2017-12-31",
            "2018-01-02",
            "2018-01-09",
        ]
        helper.create_dataset_runs_for_run_id_values(
            api_utils,
            PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
            lookback_run_id_values,
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_key_nodate_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_NUM_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_nokey_date_nyse(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers":
                    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers":
                    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers":
                    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers":
                    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
            {
                "run_id": "2018-01-12",
                "expected_outliers":
                    PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET
        )

        helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD)

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"
            validate_outliers_findings(
                api_utils,
                PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_SF_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_nokey_nodate_aclaims_master(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_NUM_NOKEY_NODATE_ACLAIMS_MASTER_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_nokey_nodate_employees(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_PAYLOAD,
            job_response["runId"],
            PD_SF_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pushdown_snowflake_outliers_numerical_storage_limit(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_SF_OUTLIERS_NUM_STORAGE_LIMIT_DATASET
        )

        job_response = helper.run_pushdown_job(api_utils, PD_SF_OUTLIERS_NUM_STORAGE_LIMIT_PAYLOAD)
        params_dataset_runid = {
            "dataset": PD_SF_OUTLIERS_NUM_STORAGE_LIMIT_DATASET,
            "runId": job_response["runId"],
        }
        issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=params_dataset_runid)
        issue_count_outlier_count = issue_count_response["OUTLIER"]

        admin_config_response = api_utils.get(V2_GET_ADMIN_CONFIG)
        for config in admin_config_response:
            if config["colNm"] == "outlierlimit":
                expected_outlier_count = int(config["colValue"])
                break
        else:
            raise AssertionError("Unable to retrieve outlier limit setting")

        assert_that(
            expected_outlier_count,
            f"Limit for outlier storage is: {expected_outlier_count}  "
            f"Retrieved: {issue_count_outlier_count}",
        ).is_equal_to(issue_count_outlier_count)
