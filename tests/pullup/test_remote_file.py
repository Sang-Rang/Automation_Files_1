import allure
import pytest
from assertpy import assert_that

from data_test.pullup.data_pullup_remotefiles import EXPECTED_PARQUET_FILE_FORMATTED_VIEW_DATA
from endpoints.v2.controller_cmd_line import V2_OPTIONS_CMD_LINE
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_explorer import V2_GET_READ_REMOTE_FILE_SYSTEMS
from endpoints.v2.controller_owl_options import (
    V2_OWL_OPTIONS_GENERATE_TEMPORARY_DATASET_NAME,
    V2_UPSERT_OWL_OPTIONS,
    V2_UPSERT_LOAD_OPT,
    V2_DELETE_OWL_OPTIONS,
)
from utils.analyze_estimate_filergram import AnalyzeEstimateFiltergram
from utils.api_utils import APIUtils
from utils.constants import PROD_RUN_ID
from utils.helper import BaseHelper

helper = BaseHelper()
aef = AnalyzeEstimateFiltergram()


@pytest.mark.pullup
class TestRemoteFile:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Remote Files")
    @allure.story("CMD")
    def test_remote_file_cmd_date_format(self, api_utils):
        """Test the given date format appears in the CMD line for loading a remote file"""

        # Note: This reflects the GUI process to generate this data.
        connection = "APPROVED_GCS"
        date_format = "dd-MMM-yy"
        exp_rd = f'-rd "{PROD_RUN_ID}"'
        exp_format = f'-df "{date_format}"'
        connection_config = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})

        # While the user is creating the job, a temporary dataset name is generated to save config
        resp_temp_name = api_utils.get(
            V2_OWL_OPTIONS_GENERATE_TEMPORARY_DATASET_NAME, params={"connectionAlias": connection}
        )
        temp_name = resp_temp_name["result"]
        pl_ds_run_id = {"dataset": temp_name, "runId": PROD_RUN_ID}
        pl_upsert_load = {
            "dataset": temp_name,
            "fullFile": True,
            "fileType": "csv",
            "dateFormat": date_format,
            "filePath": f"{connection_config['hostname']}/nyse.csv",
            "delimiter": ",",
            "unionLookBack": False,
            "connectionName": connection,
            "fileCharSet": "UTF-8",
            "addDateColumn": False,
        }

        # When the user builds the model, two upserts are performed that generate the ds defs
        upsert_owl = api_utils.put(V2_UPSERT_OWL_OPTIONS, params=pl_ds_run_id, return_json=False)
        assert_that(upsert_owl.status_code, "Upsert Owl Options call failed").is_equal_to(200)

        upsert_load = api_utils.put(V2_UPSERT_LOAD_OPT, params=pl_upsert_load, return_json=False)
        assert_that(upsert_load.status_code, "Upsert load opt call failed").is_equal_to(200)

        # The command line can then be populated before running the job
        cmd_line = api_utils.get(V2_OPTIONS_CMD_LINE, params=pl_ds_run_id, return_json=False)
        assert_that(cmd_line.status_code, "Generating the command line failed").is_equal_to(200)
        cmd_line_content = cmd_line.text

        assert_that(cmd_line_content, "Run date not found in command line").contains(exp_rd)
        assert_that(cmd_line_content, "Date format missing in command line").contains(exp_format)

        # When the user navigates away, the temp dataset is deleted.
        resp_delete = api_utils.delete(
            V2_DELETE_OWL_OPTIONS, params={"dataset": temp_name}, return_json=False
        )
        assert_that(
            resp_delete.status_code, f"Deleting owl options failed for dataset: {temp_name}"
        ).is_equal_to(200)

    @allure.feature("Remote Files")
    @allure.story("Jobs")
    def test_remote_parquet_file_formatted_view(self, api_utils):
        """This test ensures that the formatted view is returned correctly by
        v2/getreadremotefilesystems API when the user is creating a CDQ scan
        on the parquet file."""
        params = {
            "connectionalias": "APPROVED_S3_KEY",
            "path": "holidays_v1.parquet",
            "type": "parquet",
            "delimiter": ",",
            "header": "",
            "charset": "UTF-8",
            "dtfmt": "",
            "resetcache": True,
            "skiplines": 0,
            "hasheaders": True,
            "flatten": False,
            "multiline": False,
        }
        file_formatted_view_response = api_utils.get(V2_GET_READ_REMOTE_FILE_SYSTEMS, params=params)

        assert_that(file_formatted_view_response, "The formatted data is incorrect").is_equal_to(
            EXPECTED_PARQUET_FILE_FORMATTED_VIEW_DATA
        )
