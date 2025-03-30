import allure
import pytest

from data_test.pushdown.shapes.data_pd_bq_shapes_granular_austin_crime_2 import (
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES,
)
from data_test.pushdown.shapes.data_pd_bq_shapes_granular_austin_crime_2_archive_breaks import (
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_DATA,
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_SHAPES,
)
from endpoints.v2.controller_hoot import V2_POST_UPDATE_SHAPE_SETTINGS
from payloads.pushdown.shapes.pl_pd_bq_shapes_granular_austin_crime_2_archive_breaks import (
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_CONNECTION,
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET,
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_PAYLOAD,
    PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_SHAPES_SETTINGS,
)

from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_shapes import (
    validate_shapes_findings,
    validate_pushdown_shapes_archived_break_records,
)

helper = BaseHelper()


@pytest.mark.pushdown
@pytest.mark.bigquery
class TestPushdownShapesBigQueryArchiveBreaks:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Shapes - Archive Break Records")
    def test_pushdown_bigquery_shapes_granular_austin_crime_2_archive_breaks(self, api_utils):
        api_utils.post(
            V2_POST_UPDATE_SHAPE_SETTINGS,
            params=PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_SHAPES_SETTINGS,
        )
        job_response = helper.run_pushdown_job(
            api_utils, PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_PAYLOAD
        )

        validate_shapes_findings(
            api_utils,
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_SHAPES,
        )

        validate_shapes_findings(
            api_utils,
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_PAYLOAD,
            job_response["runId"],
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_EXPECTED_SHAPES,
            compare_link_ds_to_nolink_ds=True,
        )

        validate_pushdown_shapes_archived_break_records(
            api_utils,
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_CONNECTION,
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET,
            job_response["runId"],
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_DATA,
            PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT,
        )
