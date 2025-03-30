import allure
import pytest
from assertpy import assert_that

from endpoints.v2.controller_cmd_line import V2_CMD_LINE
from endpoints.v2.controller_owl_check import V2_CMD_LINE2_JSON
from endpoints.v2.controller_owl_options import V2_OWL_OPTIONS_GET
from endpoints.v3.dataset_def_api import V3_DATASETDEFS
from payloads.pullup.pl_transform_and_column_and_expression import (
    PL_ADD_COLUMN_AND_EXPRESSION,
    PL_ADD_COLUMN_AND_EXPRESSION_QUERY,
    PL_ADD_TRANSFORM_DATE,
)
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


@pytest.mark.pullup
class TestTransform:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pullup")
    @allure.story("Transform")
    def test_transform_add_column_and_expression(self, api_utils):
        """Transform - Does it add a column and expression as expected."""
        helper.setup_dataset(api_utils, PL_ADD_COLUMN_AND_EXPRESSION)

        resp_dataset_defs = api_utils.get(
            V3_DATASETDEFS + "/" + PL_ADD_COLUMN_AND_EXPRESSION["dataset"]
        )

        assert_that(
            PL_ADD_COLUMN_AND_EXPRESSION["runId"], "Dataset Def Run ID unexpected"
        ).is_equal_to(resp_dataset_defs["runId"])
        assert_that(PL_ADD_COLUMN_AND_EXPRESSION_QUERY, "Dataset Def Query unexpected").is_equal_to(
            resp_dataset_defs["load"]["query"]
        )

        resp_cmd_line = api_utils.get(
            V2_CMD_LINE, params={"dataset": PL_ADD_COLUMN_AND_EXPRESSION["dataset"]}
        )
        pl_cmd = {"cmdline": resp_cmd_line["result"]}
        cmd_to_json_response = api_utils.get(V2_CMD_LINE2_JSON, params=pl_cmd)

        for i in cmd_to_json_response["args"]:
            if i == "-q":
                index_q = cmd_to_json_response["args"].index(i)
                assert_that(PL_ADD_COLUMN_AND_EXPRESSION_QUERY, "CMD Line -q failed").is_equal_to(
                    cmd_to_json_response["args"][index_q + 1]
                )
                break
        else:
            raise AssertionError('There is no argument "-q"')

        for i in cmd_to_json_response["args"]:
            if i == "-rd":
                index_rd = cmd_to_json_response["args"].index(i)
                assert_that(
                    PL_ADD_COLUMN_AND_EXPRESSION["runId"], "CMD Line -rd failed"
                ).is_equal_to(cmd_to_json_response["args"][index_rd + 1])
                break
        else:
            raise AssertionError('There is no argument "-rd"')

    @allure.feature("Pullup")
    @allure.story("Transform")
    def test_transform_param_command_line(self, api_utils):
        """Transform - Does it add transform tag to command line"""
        expression = "effectiveDate=TO_DATE(effectiveDate, 'yyyy-mm-dd') as effectiveDate"
        date_format = "'yyyy-mm-dd'"
        cmd = f'-transform "effectiveDate=TO_DATE(effectiveDate, {date_format}) as effectiveDate"'

        setup = helper.setup_dataset(api_utils, PL_ADD_TRANSFORM_DATE)
        assert_that(setup["status"]).is_equal_to("FINISHED")

        resp_cmd_line = api_utils.get(
            V3_DATASETDEFS + "/" + PL_ADD_TRANSFORM_DATE["dataset"] + "/cmdLine"
        )["cmdLine"]

        resp_ds_def = api_utils.get(V3_DATASETDEFS + "/" + PL_ADD_TRANSFORM_DATE["dataset"])

        resp_owl = api_utils.get(
            V2_OWL_OPTIONS_GET, params={"dataset": PL_ADD_TRANSFORM_DATE["dataset"]}
        )

        assert_that(resp_cmd_line, "Transform parameter in command line not found").contains(cmd)
        assert_that(
            resp_ds_def["load"]["expression"], "Transform expression not in dataset defs"
        ).contains(expression)
        assert_that(
            resp_owl["result"]["load"]["expression"], "Transform expression not in owl options"
        ).contains(expression)
