import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_security import V2_GET_SECURITY_SETTINGS_BY_TYPE
from utils.api_utils import APIUtils


class TestConnectionSecuritySettings:
    """Test Connection Security Settings."""

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        """Return instance of APIUtils class."""
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Security")
    @allure.story("Dataset Connection Security Settings")
    def test_verify_dataset_and_connection_security_settings(self, api_utils):
        """Verify the dataset and connection security settings are not enabled."""
        dataset_security_setting = None
        connection_security_setting = None

        security_settings = api_utils.get(V2_GET_SECURITY_SETTINGS_BY_TYPE, params={"type": "DB"})

        for setting in security_settings:
            col_nm = setting["colNm"]
            col_value = setting["colValue"]

            if col_nm == "DATASET_SECURITY":
                dataset_security_setting = col_value
            elif col_nm == "CONNECTION_SECURITY":
                connection_security_setting = col_value

            if dataset_security_setting and connection_security_setting:
                break

        assert_that(
            dataset_security_setting,
            f"Expected dataset security setting to be FALSE.  "
            f"Value returned was: {dataset_security_setting}.  "
            f"Check dataset security setting which may be impacting tests.",
        ).is_equal_to("FALSE")
        assert_that(
            connection_security_setting,
            f"Expected connection security setting to be FALSE or null.  "
            f"Value returned was: {connection_security_setting}.  "
            f"Check connection security setting which may be impacting tests.",
        ).is_in("FALSE", None)
