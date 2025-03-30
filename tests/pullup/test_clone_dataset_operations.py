import copy
from datetime import datetime
import allure
import pytest
from payloads.pullup.pl_clone_dataset_operations import CLONE_DS_PAYLOAD
from data_test.pullup.data_clone_dataset_operations import EXPECTED_OUTLIERS
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator_outliers import validate_outliers_findings
from endpoints.v2.controller_owl_options import V2_OWL_OPTIONS_CLONE

helper = BaseHelper()


@pytest.mark.pullup
class TestCloneDataset:
    """Test Clone dataset operations."""

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        """Return instance of APIUtils class."""
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Clone Dataset")
    def test_clone_dataset_operations(self, api_utils):
        """Clone a dataset, go through Explorer > Run DQ Job."""
        helper.delete_dataset_outlier_configurations(api_utils, CLONE_DS_PAYLOAD["dataset"])
        job_response = helper.setup_dataset(api_utils, CLONE_DS_PAYLOAD)

        validate_outliers_findings(
            api_utils,
            CLONE_DS_PAYLOAD,
            job_response["runId"],
            EXPECTED_OUTLIERS,
            validate_details=False,
        )
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        temp_ds_name = f"temp_{now}_{CLONE_DS_PAYLOAD['dataset']}"

        clone_ds_params = {
            "sourceDataset": CLONE_DS_PAYLOAD["dataset"],
            "targetDataset": temp_ds_name,
        }
        cloned_job_response = api_utils.put(V2_OWL_OPTIONS_CLONE, params=clone_ds_params)
        helper.delete_dataset_outlier_configurations(
            api_utils, cloned_job_response["result"]["dataset"]
        )
        re_run_cloned_job_resp = helper.setup_dataset(api_utils, cloned_job_response["result"])

        # Modify the value of "dataset" key in the new dictionary
        new_expected_outliers = copy.deepcopy(EXPECTED_OUTLIERS)
        for outlier in new_expected_outliers["data"]:
            outlier["dataset"] = re_run_cloned_job_resp["dataset"]

        validate_outliers_findings(
            api_utils,
            cloned_job_response["result"],
            re_run_cloned_job_resp["runId"],
            new_expected_outliers,
            validate_details=False,
        )
