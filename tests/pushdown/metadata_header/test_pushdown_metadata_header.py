import allure
import pytest

from endpoints.v2.controller_explorer import V2_GET_TABLE_INFORMATION
from utils.api_utils import APIUtils
from utils.helper import BaseHelper
from utils.validator import compare_dicts_are_equal

helper = BaseHelper()


@pytest.mark.pushdown
class TestPushdownMetadataHeaders:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.athena
    def test_pushdown_athena_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "10",
            "size": None,
            "clusteredColumn": None,
            "numberOfRows": None,
            "lastModified": None,
            "creationDate": None,
        }
        table_info_params = {
            "schema": "default",
            "table": "nyse",
            "aliasname": "APPROVED_ATHENA_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.athena
    def test_pushdown_bigquery_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "6928978",
            "clusteredColumn": None,
            "numberOfRows": "102817",
            "lastModified": "2023-07-03 19:43:09.188000",
            "creationDate": "2023-07-03 19:43:09.188000",
        }
        table_info_params = {
            "schema": "PUBLIC",
            "table": "NYSE",
            "aliasname": "APPROVED_BIGQUERY_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.databricks
    def test_pushdown_databricks_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "N/A",
            "clusteredColumn": "N/A",
            "numberOfRows": "102817",
            "lastModified": "2023-06-07 13:26:30.614000000",
            "creationDate": "2023-06-07 13:26:30.614000000",
        }
        table_info_params = {
            "schema": "public",
            "table": "nyse",
            "aliasname": "APPROVED_DATABRICKS_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @pytest.mark.skip(reason="Skipped until DEV-116255 is deployed to 2025.05")
    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.oracle
    def test_pushdown_oracle_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "N/A",
            "clusteredColumn": "N/A",
            "numberOfRows": "103706",
            "lastModified": "2023-09-18 12:54:57",
            "creationDate": "2019-10-02 13:34:16",
        }
        table_info_params = {
            "schema": "OWLUSER",
            "table": "NYSE",
            "aliasname": "APPROVED_ORACLE_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.redshift
    def test_pushdown_redshift_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": None,
            "clusteredColumn": None,
            "numberOfRows": None,
            "lastModified": None,
            "creationDate": None,
        }
        table_info_params = {
            "schema": "public",
            "table": "nyse",
            "aliasname": "APPROVED_REDSHIFT_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.saphana
    def test_pushdown_saphana_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "N/A",
            "clusteredColumn": "N/A",
            "numberOfRows": "102817",
            "lastModified": None,
            "creationDate": "2024-02-13 04:17:07.679000000"
        }
        table_info_params = {
            "schema": "TEST",
            "table": "NYSE",
            "aliasname": "APPROVED_SAPHANA_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.snowflake
    def test_pushdown_snowflake_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "2278400",
            "clusteredColumn": None,
            "numberOfRows": "102817",
            "lastModified": "2024-12-19 14:52:56.635 -0800",
            "creationDate": "2020-06-03 07:37:43.667 -0700",
        }
        table_info_params = {
            "schema": "PUBLIC",
            "table": "NYSE",
            "aliasname": "APPROVED_SNOWFLAKE_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)

    @allure.feature("Pushdown")
    @allure.story("Pushdown - Metadata header")
    @pytest.mark.sqlserver
    def test_pushdown_sqlserver_metadata_header_nyse(self, api_utils):
        expected_header_information = {
            "numberOfColumns": "9",
            "size": "659",
            "numberOfRows": "102817",
            "lastModified": "2023-11-20 19:55:46.147",
            "creationDate": "2023-11-20 19:55:46.147",
        }
        table_info_params = {
            "schema": "dbo",
            "table": "NYSE",
            "aliasname": "APPROVED_SQLSERVER_PUSHDOWN",
            "failOnError": False,
        }
        header_information = api_utils.post(V2_GET_TABLE_INFORMATION, params=table_info_params)

        compare_dicts_are_equal(expected_header_information, header_information)
