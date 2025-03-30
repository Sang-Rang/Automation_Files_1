import allure
import pytest

from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_date_ms_trade import (
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10,
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10,
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_nodate_nyse import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_nodate_us_airports import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_key_nodate_us_airports_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_date_ms_trade import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10,
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10,
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_nodate_nyse import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_nodate_us_airports import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_cat_nokey_nodate_us_airports_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_ms_trade import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
)
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_nyse import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_11,
)
# from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_union_lookback_nyse import (
#     PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
# )
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_date_union_lookback_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
# from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_nodate_nyse import (
#     PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
# )
from data_test.pushdown.outliers.data_pd_trino_outliers_num_key_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_num_nokey_date_nyse import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
)
from data_test.pushdown.outliers.data_pd_trino_outliers_num_nokey_date_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_12,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_12,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_08,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_09,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_10,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_11,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_12,
)
# from data_test.pushdown.outliers.data_pd_trino_outliers_num_nokey_nodate_employees import (
#     PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS,
# )
# pylint: disable-next=line-too-long
from data_test.pushdown.outliers.data_pd_trino_outliers_num_nokey_nodate_employees_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_nodate_us_airports_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_nodate_us_airports_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_date_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_date_union_lookback_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_nodate_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_nokey_date_nyse_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
)
# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_nokey_nodate_employees_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION,
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_outliers import (
    validate_outliers_findings,
    validate_outliers_findings_not_present,
    validate_pushdown_outliers_archived_break_records,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.trino
class TestPushdownOutliersTrinoArchiveBreaks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_key_date_ms_trade_archive_breaks(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2023-01-10",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10,
                "expected_data":
                    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET
        )

        helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD
        )

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"

            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )
            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["no_linkId_dataset_expected_outliers"],
                compare_link_ds_to_nolink_ds=True,
            )

            validate_pushdown_outliers_archived_break_records(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
                PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
                run_id_string,
                run["expected_data"],
                run["expected_query_result"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_key_nodate_nyse_archive_breaks(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_key_nodate_us_airports_archive_breaks(
        self, api_utils
    ):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
            compare_link_ds_to_nolink_ds=True
        )

        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_CAT_KEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_nokey_date_ms_trade_archive_breaks(
        self, api_utils
    ):
        run_ids_with_no_expected_outliers = [
            "2023-01-05",
            "2023-01-06",
            "2023-01-07",
            "2023-01-08",
            "2023-01-09",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2023-01-10",
                "expected_outliers":
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10,
                "expected_data":
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10,
                "expected_query_result":
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10,
                "no_linkId_dataset_expected_outliers":
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET
        )

        helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD
        )

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"

            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )
            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["no_linkId_dataset_expected_outliers"],
                compare_link_ds_to_nolink_ds=True,
            )

            validate_pushdown_outliers_archived_break_records(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
                run_id_string,
                run["expected_data"],
                run["expected_query_result"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_nokey_nodate_nyse_archive_breaks(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_categorical_nokey_nodate_us_airports_archive_breaks(
        self, api_utils
    ):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS,
            compare_link_ds_to_nolink_ds=True
        )

        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_key_date_ms_trade_archive_breaks(
        self, api_utils,
    ):
        run_ids_with_no_expected_outliers = [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-06",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2023-01-05",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET
        )

        helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD
        )

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"

            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )
            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["no_linkId_dataset_expected_outliers"],
                compare_link_ds_to_nolink_ds=True,
            )

            validate_pushdown_outliers_archived_break_records(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_CONNECTION,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
                run_id_string,
                run["expected_data"],
                run["expected_query_result"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_key_date_nyse_archive_breaks(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
            "2018-01-12",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_08,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_08,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_08,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_09,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_09,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_09,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_10,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_10,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_10,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_11,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_11,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_11,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET
        )

        helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"

            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )
            # This section of the code is commented out and will be uncommented
            # once DEV-117955 is fixed.
            # validate_outliers_findings(
            #     api_utils,
            #     PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            #     run_id_string,
            #     run["no_linkId_dataset_expected_outliers"],
            #     compare_link_ds_to_nolink_ds=True,
            # )
            #
            validate_pushdown_outliers_archived_break_records(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET,
                run_id_string,
                run["expected_data"],
                run["expected_query_result"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_KEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_key_date_nyse_union_lookback_archive_breaks(
        self, api_utils
    ):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_DATASET
        )

        helper.delete_dataset_if_exists(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_DATASET
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
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            lookback_run_id_values,
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        # This section of the code is commented out and will be uncommented
        # once DEV-117955 is fixed.
        # validate_outliers_findings(
        #     api_utils,
        #     PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_PAYLOAD,
        #     job_response["runId"],
        #     PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_EXPECTED_OUTLIERS,
        #     compare_link_ds_to_nolink_ds=True,
        # )
        #
        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_NUM_KEY_DATE_UNION_LOOKBACK_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_key_nodate_nyse_archive_breaks(self, api_utils):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        # This section of the code is commented out and will be uncommented
        # once DEV-117955 is fixed.
        # validate_outliers_findings(
        #     api_utils,
        #     PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
        #     job_response["runId"],
        #     PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_EXPECTED_OUTLIERS,
        #     compare_link_ds_to_nolink_ds=True,
        # )
        #
        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_NUM_KEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_nokey_date_nyse_archive_breaks(self, api_utils):
        run_ids_with_no_expected_outliers = [
            "2018-01-07",
        ]
        run_ids_with_expected_outliers = [
            {
                "run_id": "2018-01-08",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_08,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_08,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_08,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_08,
            },
            {
                "run_id": "2018-01-09",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_09,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_09,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_09,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_09,
            },
            {
                "run_id": "2018-01-10",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_10,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_10,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_10,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_10,
            },
            {
                "run_id": "2018-01-11",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_11,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_11,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_11,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_11,
            },
            {
                "run_id": "2018-01-12",
                "expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_OUTLIERS_2018_01_12,
                "expected_data":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_DATA_2018_01_12,
                "expected_query_result":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2018_01_12,
                "no_linkId_dataset_expected_outliers":
                    PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_EXPECTED_OUTLIERS_2018_01_12,
            },
        ]
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET
        )

        helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD
        )

        for run in run_ids_with_expected_outliers:
            run_id_string = run["run_id"] + "T00:00:00.000+0000"

            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["expected_outliers"],
            )
            validate_outliers_findings(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
                run_id_string,
                run["no_linkId_dataset_expected_outliers"],
                compare_link_ds_to_nolink_ds=True,
            )

            validate_pushdown_outliers_archived_break_records(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_CONNECTION,
                PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_DATASET,
                run_id_string,
                run["expected_data"],
                run["expected_query_result"],
            )

        for run_id in run_ids_with_no_expected_outliers:
            validate_outliers_findings_not_present(
                api_utils,
                PD_TRINO_OUTLIERS_NUM_NOKEY_DATE_NYSE_ARCHIVE_BREAKS_PAYLOAD,
                run_id,
            )

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Outliers - Archive Break Records")
    def test_pushdown_trino_outliers_numerical_nokey_nodate_employees_archive_breaks(
        self, api_utils
    ):
        helper.delete_dataset_outlier_configurations(
            api_utils, PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET
        )

        job_response = helper.run_pushdown_job(
            api_utils, PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_outliers_findings(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_OUTLIERS,
        )
        # This section of the code is commented out and will be uncommented
        # once DEV-117955 is fixed.
        # validate_outliers_findings(
        #     api_utils,
        #     PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_PAYLOAD,
        #     job_response["runId"],
        #     PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS,
        #     compare_link_ds_to_nolink_ds=True,
        # )
        #
        validate_pushdown_outliers_archived_break_records(
            api_utils,
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_CONNECTION,
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )
