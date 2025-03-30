import allure
import pytest

from data_test.pullup.data_outlier_day_by_day import EXPECTED_DATA_OUTLIERS_DAY_BY_DAY
from data_test.pullup.data_outlier_month_by_month import EXPECTED_DATA_OUTLIERS_MONTH_BY_MONTH
from data_test.pullup.data_outlier_test_jobs_outlier_minutes_hours_numbers_dates import (
    EXPECTED_DATA_HOUR_MIN,
)
from data_test.pullup.data_outlier_year_by_month import EXPECTED_OUTLIER_YEAR_BY_MONTH
from data_test.pullup.data_outliers_categorical_pull_up_athena import (
    OUTLIERS_CATEGORICAL_PULL_UP_ATHENA_EXPECTED_OUTLIERS,
)
from data_test.pullup.data_outliers_data_validation_postgres import (
    OUTLIERS_DATA_VALIDATION_EXPECTED_OUTLIERS,
)
from data_test.pullup.data_outliers_intraday_minutes_or_hours import (
    OUTLIERS_DAY_BY_HOUR_EXPECTED_OUTLIERS,
)
from data_test.pullup.data_outliers_no_dc_without_time_on_pull_up_athena import (
    OUTLIERS_NO_DC_EXPECTED_OUTLIERS,
)
from data_test.pullup.data_outliers_no_dl_key_on_pull_up_athena import NO_DL_KEY_EXPECTED_OUTLIERS
from data_test.pullup.data_pullup_outliers_cat_key_date_ms_trade import (
    PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
from data_test.pullup.data_pullup_outliers_cat_nokey_date_ms_trade import (
    PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
from data_test.pullup.data_pullup_outliers_num_key_date_ms_trade import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
)
from data_test.pullup.data_pullup_outliers_num_key_date_nyse import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
)
from data_test.pullup.data_pullup_outliers_num_key_date_union_lookback_nyse import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
    PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_RECORDS_FINDINGS,
)
from data_test.pullup.data_pullup_outliers_num_nokey_date_nyse import (
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
)
from data_test.pullup.data_outliers_downtrain_rerun_and_retrain import (
    EXPECTED_OUTLIER_BEFORE_DOWNTRAIN,
    EXPECTED_OUTLIER_AFTER_DOWNTRAIN,
)
from data_test.pullup.data_missing_endpoints_coverage import OUTLIER_OPT_RESPONSE
from endpoints.v2.controller_assignment_q import V2_INVALIDATE_ASSIGNMENT
from endpoints.v2.controller_hoot import V2_GET_OUTLIER
from endpoints.v2.controller_label import V2_RETRAIN
from endpoints.v2.controller_outlier_opt import V2_GET_OUTLIER_OPT
from payloads.pullup.pl_outlier_year_by_month import (
    DS_DEFS_OUTLIER_YEAR_BY_MONTH,
    RUN_DATE_OUTLIER_YEAR_BY_MONTH_FULL,
)
from payloads.pullup.pl_outliers_categorical_pull_up_athena import (
    OUTLIERS_CATEGORICAL_PULL_UP_ATHENA_PAYLOAD,
)
from payloads.pullup.pl_outliers_data_validation_postgres import OUTLIERS_DATA_VALIDATION_PAYLOAD
from payloads.pullup.pl_outliers_day_by_day import (
    DS_DEFS_OUTLIER_DAY_BY_DAY,
    DS_DEFS_OUTLIER_DAY_BY_DAY_RUN_ID_FULL,
)
from payloads.pullup.pl_outliers_intraday_minutes_or_hours import OUTLIERS_DAY_BY_HOUR_PAYLOAD
from payloads.pullup.pl_outliers_month_by_month import (
    DS_DEFS_OUTLIER_MONTH_BY_MONTH,
    DS_DEFS_OUTLIER_MONTH_BY_MONTH_RUN_ID_FULL,
)
from payloads.pullup.pl_outliers_no_dc_pull_up_athena import OUTLIERS_NO_DC_PAYLOAD
from payloads.pullup.pl_outliers_no_dl_key_athena import NO_DL_KEY_JOB_PAYLOAD
from payloads.pullup.pl_outliers_test_jobs_outlier_minutes_hours_numbers_dates import (
    DS_DEFS_HOUR_MIN,
    RUN_ID_HOUR_MIN_FULL,
)
from payloads.pullup.pl_pullup_outliers_cat_key_date_ms_trade import (
    PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
    PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pullup.pl_pullup_outliers_cat_nokey_date_ms_trade import (
    PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET,
    PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pullup.pl_pullup_outliers_num_key_date_ms_trade import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
    PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
)
from payloads.pullup.pl_pullup_outliers_num_key_date_nyse import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_DATASET,
    PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
)
from payloads.pullup.pl_pullup_outliers_num_key_date_union_lookback_nyse import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET,
    PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
)
from payloads.pullup.pl_pullup_outliers_num_nokey_date_nyse import (
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET,
    PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
)
from payloads.pullup.pl_outliers_downtrain_rerun_and_retrain import (
    OUTLIERS_DATASET,
    RUN_DATE_DOWNTRAIN_FULL,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import (
    compare_dicts_are_equal,
)
from utils.validator_observations import validate_records_findings
from utils.validator_outliers import (
    validate_outliers_findings_not_present,
    validate_outliers_findings,
)

helper = BaseHelper()


@pytest.mark.pullup
class TestPullUpOutliers:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def run_pullup_outlier_test(
        api_utils, dataset_defs, expected_outlier_findings, validate_details=True
    ):
        helper.delete_dataset_outlier_configurations(api_utils, dataset_defs["dataset"])
        job_output = helper.setup_dataset(api_utils, dataset_defs)

        validate_outliers_findings(
            api_utils,
            dataset_defs,
            job_output["runId"],
            expected_outlier_findings,
            validate_details=validate_details,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    @pytest.mark.smoke
    def test_categorical_outliers_on_pull_up_source_athena(self, api_utils):
        """Test Outliers - categorical outliers on Pull-up source ATHENA."""
        self.run_pullup_outlier_test(
            api_utils,
            OUTLIERS_CATEGORICAL_PULL_UP_ATHENA_PAYLOAD,
            OUTLIERS_CATEGORICAL_PULL_UP_ATHENA_EXPECTED_OUTLIERS,
            validate_details=False,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_no_dl_key_on_pull_up_source_athena(self, api_utils):
        """Test OUTLIERS - No dl-key, without key on pull-up source ATHENA."""
        self.run_pullup_outlier_test(
            api_utils,
            NO_DL_KEY_JOB_PAYLOAD,
            NO_DL_KEY_EXPECTED_OUTLIERS,
            validate_details=False,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_no_dc_without_time_on_pull_up_athena(self, api_utils):
        """Test OUTLIERS - No dc, without time on pull-up source ATHENA."""
        self.run_pullup_outlier_test(
            api_utils,
            OUTLIERS_NO_DC_PAYLOAD,
            OUTLIERS_NO_DC_EXPECTED_OUTLIERS,
            validate_details=False,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_data_validation_postgres(self, api_utils):
        """Test Outliers - Data Validation (Postgres)"""
        self.run_pullup_outlier_test(
            api_utils,
            OUTLIERS_DATA_VALIDATION_PAYLOAD,
            OUTLIERS_DATA_VALIDATION_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_intraday_minutes_or_hours(self, api_utils):
        """Test Outliers - Intraday Minutes or Hours"""
        self.run_pullup_outlier_test(
            api_utils,
            OUTLIERS_DAY_BY_HOUR_PAYLOAD,
            OUTLIERS_DAY_BY_HOUR_EXPECTED_OUTLIERS,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    @pytest.mark.flaky(retries=5, delay=5)
    def test_outliers_year_by_month(self, api_utils):
        """Test Outlier - Year by Month DEV-49590"""

        helper.delete_dataset_outlier_configurations(
            api_utils, DS_DEFS_OUTLIER_YEAR_BY_MONTH["dataset"]
        )

        helper.setup_dataset(api_utils, DS_DEFS_OUTLIER_YEAR_BY_MONTH)

        validate_outliers_findings(
            api_utils,
            DS_DEFS_OUTLIER_YEAR_BY_MONTH,
            RUN_DATE_OUTLIER_YEAR_BY_MONTH_FULL,
            EXPECTED_OUTLIER_YEAR_BY_MONTH,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_minutes_and_hours_with_numbers_and_dates(self, api_utils):
        """Test Outlier - Minutes and Hours with Numbers and Dates DEV-48968"""
        helper.delete_dataset_outlier_configurations(api_utils, DS_DEFS_HOUR_MIN["dataset"])

        helper.setup_dataset(api_utils, DS_DEFS_HOUR_MIN)

        validate_outliers_findings(
            api_utils, DS_DEFS_HOUR_MIN, RUN_ID_HOUR_MIN_FULL, EXPECTED_DATA_HOUR_MIN
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_outliers_day_by_day(self, api_utils):
        """Test Outlier - Day By Day (DEV-48961)"""
        helper.delete_dataset_outlier_configurations(
            api_utils, DS_DEFS_OUTLIER_DAY_BY_DAY["dataset"]
        )

        helper.setup_dataset(api_utils, DS_DEFS_OUTLIER_DAY_BY_DAY)

        validate_outliers_findings(
            api_utils,
            DS_DEFS_OUTLIER_DAY_BY_DAY,
            DS_DEFS_OUTLIER_DAY_BY_DAY_RUN_ID_FULL,
            EXPECTED_DATA_OUTLIERS_DAY_BY_DAY,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    @pytest.mark.flaky(retries=5, delay=5)
    def test_outliers_month_by_month(self, api_utils):
        """Test Outlier - Month by Month (DEV-48964)"""
        helper.delete_dataset_outlier_configurations(
            api_utils, DS_DEFS_OUTLIER_MONTH_BY_MONTH["dataset"]
        )

        helper.setup_dataset(api_utils, DS_DEFS_OUTLIER_MONTH_BY_MONTH)

        validate_outliers_findings(
            api_utils,
            DS_DEFS_OUTLIER_MONTH_BY_MONTH,
            DS_DEFS_OUTLIER_MONTH_BY_MONTH_RUN_ID_FULL,
            EXPECTED_DATA_OUTLIERS_MONTH_BY_MONTH,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_pullup_outliers_numerical_key_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-06",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET
        )

        helper.setup_dataset(api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-05T00:00:00.000+0000",
            PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_pullup_outliers_categorical_key_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET
        )

        helper.setup_dataset(api_utils, PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-10T00:00:00.000+0000",
            PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PULLUP_OUTLIERS_CAT_KEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_pullup_outliers_categorical_nokey_date_ms_trade(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET
        )

        helper.setup_dataset(api_utils, PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
            "2023-01-10T00:00:00.000+0000",
            PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
        )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PULLUP_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_pullup_outliers_numerical_key_date_nyse(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
            "2018-01-12",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers": PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers": PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers": PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers": PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_DATASET
        )

        helper.setup_dataset(api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD)

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"
            validate_outliers_findings(
                api_utils,
                PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PULLUP_OUTLIERS_NUM_KEY_DATE_NYSE_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers")
    def test_pullup_outliers_numerical_key_date_union_lookback_nyse(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET
        )

        helper.delete_dataset_if_exists(
            api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET
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
            PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
            lookback_run_id_values,
        )

        job_response = helper.setup_dataset(
            api_utils, PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_PAYLOAD,
            job_response["runId"],
            PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
        )

        validate_records_findings(
            api_utils,
            PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_DATASET,
            job_response["runId"],
            PULLUP_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_RECORDS_FINDINGS,
        )

    @allure.feature("Pullup")
    @allure.story("Outliers")
    def test_pullup_outliers_numerical_nokey_date_nyse(self, api_utils):
        # pylint: disable-msg=line-too-long
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers": PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers": PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers": PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers": PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
            {
                "run_id": "2018-01-12",
                "expected_outliers": PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_DATASET
        )

        response = helper.setup_dataset(api_utils, PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD)

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"
            validate_outliers_findings(
                api_utils,
                PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PULLUP_OUTLIERS_NUM_NOKEY_DATE_NYSE_PAYLOAD,
                run_id,
            )

        # Add coverage for /v2/outlier-opt/get endpoint, not test related.
        outlier_opt = api_utils.get(V2_GET_OUTLIER_OPT, params={"dataset": response["dataset"]})
        compare_dicts_are_equal(outlier_opt, OUTLIER_OPT_RESPONSE, "id")

    @allure.feature("Pullup")
    @allure.story("Outliers")
    @pytest.mark.skip(reason="Bug DEV-64471, DEV-64473, DEV-64474")
    def test_outliers_downtrain_rerun_and_retrain_operations(self, api_utils):
        """Test Outlier down trains properly, persist properly after re-run, retrain properly
        and score displays correctly DEV-48963"""

        # Precondition, delete all labels if they exist
        helper.delete_labels_if_exist(api_utils, OUTLIERS_DATASET)
        helper.delete_dataset_outlier_configurations(api_utils, OUTLIERS_DATASET["dataset"])

        job_response = helper.setup_dataset(api_utils, OUTLIERS_DATASET)

        params_dataset_runid = {
            "dataset": OUTLIERS_DATASET["dataset"],
            "runId": job_response["runId"],
        }
        # Expected 6 outliers
        validate_outliers_findings(
            api_utils, OUTLIERS_DATASET, RUN_DATE_DOWNTRAIN_FULL, EXPECTED_OUTLIER_BEFORE_DOWNTRAIN
        )

        outliers = api_utils.get(V2_GET_OUTLIER, params=params_dataset_runid)["data"]

        outlier_to_downtrain = {}
        for outlier in outliers:
            if (
                outlier["outColumn"] == "CLOSE"
                and outlier["outValue"] == "1800.0"
                and outlier["keyArr"] == ["JHD"]
            ):
                outlier_to_downtrain = outlier

        invalidate_outlier_params = {
            "id": outlier_to_downtrain["assignmentId"]["id"],
            "uuid": outlier_to_downtrain["assignmentId"]["uuid"],
            "annotation": "downtrain",
        }

        # Invalidate assignments and retrain model
        api_utils.post(V2_INVALIDATE_ASSIGNMENT, json=invalidate_outlier_params)
        retrain_params = {
            "dataset": OUTLIERS_DATASET["dataset"],
            "runId": job_response["runId"],
            "dqType": "OUTLIER",
        }
        api_utils.post(V2_RETRAIN, params=retrain_params)

        # Output should be 5 outliers
        validate_outliers_findings(
            api_utils, OUTLIERS_DATASET, RUN_DATE_DOWNTRAIN_FULL, EXPECTED_OUTLIER_AFTER_DOWNTRAIN
        )
        # Run the job, should be still 5 outliers after run
        helper.setup_dataset(api_utils, OUTLIERS_DATASET)

        validate_outliers_findings(
            api_utils, OUTLIERS_DATASET, RUN_DATE_DOWNTRAIN_FULL, EXPECTED_OUTLIER_AFTER_DOWNTRAIN
        )

        # Delete a label and validate findings, should be 6 outliers.
        helper.delete_labels_if_exist(api_utils, OUTLIERS_DATASET)
        api_utils.post(V2_RETRAIN, params=retrain_params)

        # Bug DEV-64474 - Range for the chart is return as null after delete of a label (lb, ub)
        validate_outliers_findings(
            api_utils, OUTLIERS_DATASET, RUN_DATE_DOWNTRAIN_FULL, EXPECTED_OUTLIER_BEFORE_DOWNTRAIN
        )
