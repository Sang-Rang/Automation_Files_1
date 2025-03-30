import allure
import pytest
from assertpy import assert_that

from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


class TestDataPreviewSqlSecurity:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    expected_select_exception = (
        "Execution error. Only SELECT SQL statements are allowed to be executed."
    )
    expected_multi_query_exception = "Execution error. More than 1 query found."
    snowflake_pullup_connection = "APPROVED_SNOWFLAKE_UP"
    snowflake_pushdown_connection = "APPROVED_SNOWFLAKE_PUSHDOWN"
    target_schema = "PUBLIC"
    target_table = "SECURITY_TARGET_TABLE_001"

    def validate_table_state(self, api_utils, connection):
        """Verify target table is in expected state.  If the table needs to be recreated, use:
        CREATE TABLE PUBLIC.SECURITY_TARGET_TABLE_002
        (ID NUMERIC AUTOINCREMENT START 1 INCREMENT 1, TEXT001 VARCHAR)
        INSERT INTO PUBLIC.SECURITY_TARGET_TABLE_002 (TEXT001)
        VALUES ('Table for security tests')"""
        expected_text_value = "Table for security tests"
        schema = self.target_schema
        table = self.target_table

        select_result = helper.run_query_and_extract_result(
            api_utils, f"select * from {schema}.{table}", connection
        )

        # Verify that the expected row and only the expected row is returned
        assert_that(len(select_result), "Unexpected row count found.").is_equal_to(1)
        assert_that(select_result[0]["ID"], "Unexpected ID value found.").is_equal_to(1)
        assert_that(select_result[0]["TEXT001"], "Unexpected text found").is_equal_to(
            expected_text_value
        )

    @staticmethod
    def verify_sql_exception(sql_result, expected_exception):
        sql_result_exception = sql_result["exception"]
        assert_that(
            sql_result["exception"],
            f"Expected exception to be {expected_exception} in "
            f"{sql_result} but found {sql_result_exception}",
        ).is_equal_to(expected_exception)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_select(self, api_utils):
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_drop_table(self, api_utils):
        sql = f"DROP TABLE {self.target_schema}.{self.target_table}"
        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_update_table(self, api_utils):
        sql = (
            f"UPDATE TABLE {self.target_schema}.{self.target_table} "
            "SET TEXT001 = 'UpdatedByPullUpUpdateTest'"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_delete_from_table(self, api_utils):
        sql = f"DELETE FROM TABLE {self.target_schema}.{self.target_table} WHERE ID = 1"
        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_describe_table(self, api_utils):
        sql = f"DESCRIBE TABLE {self.target_schema}.{self.target_table}"

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_alter_table(self, api_utils):
        sql = (
            f"ALTER TABLE {self.target_schema}.{self.target_table} "
            f"RENAME TO {self.target_table}_RENAMED_BY_PULLUP_ALTER_TEST"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pullup_snowflake_connection_drop_after_select(self, api_utils):
        sql = (
            f"SELECT * FROM {self.target_schema}.{self.target_table}; "
            f"DROP TABLE {self.target_schema}.{self.target_table}"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pullup_connection)

        self.verify_sql_exception(sql_result, self.expected_multi_query_exception)
        self.validate_table_state(api_utils, self.snowflake_pullup_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_select(self, api_utils):
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_drop_table(self, api_utils):
        sql = f"DROP TABLE {self.target_schema}.{self.target_table}"

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_update_table(self, api_utils):
        sql = (
            f"UPDATE TABLE {self.target_schema}.{self.target_table} "
            "SET TEXT001 = 'UpdatedByPushdownUpdateTest'"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_delete_from_table(self, api_utils):
        sql = f"DELETE FROM TABLE {self.target_schema}.{self.target_table} WHERE ID = 1"

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_describe_table(self, api_utils):
        sql = f"DESCRIBE TABLE {self.target_schema}.{self.target_table}"

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_alter_table(self, api_utils):
        sql = (
            f"ALTER TABLE {self.target_schema}.{self.target_table} "
            f"RENAME TO {self.target_table}_RENAMED_BY_PULLUP_ALTER_TEST"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_select_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)

    @allure.feature("Security")
    @allure.story("Data preview SQL security")
    def test_pushdown_snowflake_connection_drop_after_select(self, api_utils):
        sql = (
            f"SELECT * FROM {self.target_schema}.{self.target_table}; "
            f"DROP TABLE {self.target_schema}.{self.target_table}"
        )

        sql_result = helper.run_sql(api_utils, sql, self.snowflake_pushdown_connection)

        self.verify_sql_exception(sql_result, self.expected_multi_query_exception)
        self.validate_table_state(api_utils, self.snowflake_pushdown_connection)
