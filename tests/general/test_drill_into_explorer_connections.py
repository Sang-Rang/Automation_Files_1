import time

import allure
import pytest
from assertpy import soft_assertions, assert_that
from utils.api_utils import APIUtils
from endpoints.v2.controller_explorer import (
    V2_GET_EXPLORER_SEARCH,
    V2_POST_EXPLORER_TABLE_SEARCH,
)


# pylint: disable-next = too-many-public-methods
class TestDrillIntoExplorerConnections:
    """Test Drill Into Explorer."""

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        """Return instance of APIUtils class."""
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    # Define the common params and data as class variables
    params = {
        "catalogsearch": "",
        "schemasearch": "",
        "tablesearch": "",
        "showstats": "0",
        "showviews": "0",
        "eagerfetch": "0",
    }
    data = {
        "schema": "default",
        "tables": "-",
        "showstats": "0",
        "showviews": "0",
        "eagerfetch": "0",
    }

    @staticmethod
    # pylint: disable-next = too-many-arguments
    def get_schemas_and_tables_count(
        api_utils,
        connection,
        params,
        min_schema_count,
        data,
        min_table_count,
    ):
         # Add re-try logic for databricks
        max_retries = 50
        timeout = 3
        attempts = 0

        # Get schemas and tables count for provided connection
        # If connection is databricks, use re-try logic
        if connection == "APPROVED_CDATA_DATABRICKS_UP":
            while attempts < max_retries:
                schemas = api_utils.get(V2_GET_EXPLORER_SEARCH, params=params, return_json=False)

                if schemas.status_code == 200:
                    break

                time.sleep(timeout)
                attempts += 1
        else:
            schemas = api_utils.get(V2_GET_EXPLORER_SEARCH, params=params, return_json=False)
        # Validate the connection is up
        assert_that(
            schemas.status_code, f"Connection problem detected. Result: {schemas}"
        ).is_equal_to(200)
        schemas_count = len(schemas.json())

        # Check the schema data
        with soft_assertions():
            assert_that(schemas_count, "Schema List").is_greater_than_or_equal_to(min_schema_count)

        data["alias"] = connection
        tables = api_utils.post(V2_POST_EXPLORER_TABLE_SEARCH, params=data)
        assert_that(tables, f"Expected data not found. Data: {tables}").contains_key("tableMaps")
        tables_count = len(tables["tableMaps"])
        assert_that(tables_count, "Table Drill-in List").is_greater_than_or_equal_to(
            min_table_count
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_athena_pushdown(self, api_utils):
        """Explorer - Athena Pushdown."""
        connection = "APPROVED_ATHENA_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 150
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.smoke
    def test_athena_up(self, api_utils):
        """Explorer - Athena Up."""
        connection = "APPROVED_ATHENA_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 150
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_bigquery_key_sensitive_props(self, api_utils):
        """Explorer - Bigquery key sensitive props."""
        connection = "APPROVED_BIGQUERY_KEY_SENSITIVE_PROPERTIES"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "nyc_taxi_trips"
        min_table_count = 10
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.smoke
    def test_bigquery_key(self, api_utils):
        """Explorer - BigQuery Key."""
        connection = "APPROVED_BIGQUERY_KEY"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "nyc_taxi_trips"
        min_table_count = 10
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_bigquery_pushdown(self, api_utils):
        """Explorer - BigQuery Pushdown."""
        connection = "APPROVED_BIGQUERY_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "nyc_taxi_trips"
        min_table_count = 10
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_cdata_athena_up(self, api_utils):
        """Explorer - Approved cdata athena up."""
        connection = "APPROVED_CDATA_ATHENA_UP"
        params = self.params.copy()
        params["alias"] = connection
        params["showviews"] = "1"
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        data["showviews"] = "1"
        min_table_count = 150
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_cdata_bigquery_key(self, api_utils):
        """Explorer - Approved cdata bigquery key."""
        connection = "APPROVED_CDATA_BIGQUERY_KEY"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "nyc_taxi_trips"
        min_table_count = 10
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.connection_warmup
    def test_approved_cdata_databricks_up(self, api_utils):
        """Explorer - Approved cdata databricks up."""
        connection = "APPROVED_CDATA_DATABRICKS_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.skip(
        reason="Mongo has shards that are brought up and down.  "
        "Connection string must be updated dynamically for this test to be reliable."
    )
    def test_approved_cdata_mongo_up(self, api_utils):
        """Explorer - Approved cdata mongo up."""
        connection = "APPROVED_CDATA_MONGO_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "sample_training"
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.connection_warmup
    def test_approved_databricks_cluster_endpoint(self, api_utils):
        """Explorer - Approved databricks cluster endpoint."""
        connection = "APPROVED_DATABRICKS_CLUSTER_ENDPOINT"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "data"
        min_table_count = 4
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_databricks_pushdown(self, api_utils):
        """Explorer - Approved databricks pushdown."""
        connection = "APPROVED_DATABRICKS_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 4

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 15
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_databricks_sql_endpoint(self, api_utils):
        """Explorer - Approved databricks sql endpoint."""
        connection = "APPROVED_DATABRICKS_SQL_ENDPOINT"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 4

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 15
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_databricks_sql_hive(self, api_utils):
        """Explorer - Approved databricks sql hive."""
        connection = "APPROVED_DATABRICKS_SQL_HIVE"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 25
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_databricks_sql_unity_catalog(self, api_utils):
        """Explorer - Approved databricks sql unity catalog."""
        connection = "APPROVED_DATABRICKS_SQL_UNITY_CATALOG"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 4

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 15
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_db2_up(self, api_utils):
        """Explorer - Approved DB2 up."""
        connection = "APPROVED_DB2_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "OWLDB2"
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_dremio_up(self, api_utils):
        """Explorer - Approved Dremio Up."""
        connection = "APPROVED_DREMIO_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "pgsql.public"
        min_table_count = 30
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_hive_kp(self, api_utils):
        """Explorer - Approved Hive kp."""
        connection = "APPROVED_HIVE_KP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 3

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 1
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.skip(reason="Connection is down.  Enable when the connection is available.")
    def test_approved_hive_up(self, api_utils):
        """Explorer - Approved Hive Up."""
        connection = "APPROVED_HIVE_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        min_table_count = 4
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.smoke
    def test_approved_mysql_up(self, api_utils):
        """Explorer - Approved mysql up."""
        connection = "APPROVED_MYSQL_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 5

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "lake"
        min_table_count = 15
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.flaky(retries=12, delay=5)
    @pytest.mark.connection_warmup
    @pytest.mark.skip(reason="Needs refactoring to make less flaky, DEV-75187")
    def test_approved_oracle_kkt(self, api_utils):
        """Explorer - Approved oracle kkt."""
        connection = "APPROVED_ORACLE_KKT"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 35

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "OWLUSER"
        min_table_count = 1
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_oracle_up(self, api_utils):
        """Explorer - Approved oracle up."""
        connection = "APPROVED_ORACLE_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 20

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "OWLUSER"
        min_table_count = 25
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_postgres_pwdmgr(self, api_utils):
        """Explorer - Approved Postgres pwdmgr."""
        connection = "APPROVED_POSTGRES_PWDMGR"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "samples"
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_postgres_up(self, api_utils):
        """Explorer - Approved postgres up."""
        connection = "APPROVED_POSTGRES_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "samples"
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_postgres_up_sensitive_props(self, api_utils):
        """Explorer - Approved Postgres up Sensitive props."""
        connection = "APPROVED_POSTGRES_UP_SENSITIVE_PROPS"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 1

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "samples"
        min_table_count = 5
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_redshift_pushdown(self, api_utils):
        """Explorer - Approved Redshift Pushdown"""
        connection = "APPROVED_REDSHIFT_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "public"
        min_table_count = 20
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_redshift_up(self, api_utils):
        """Explorer - Approved Redshift Up."""
        connection = "APPROVED_REDSHIFT_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 15

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "public"
        min_table_count = 20
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_snowflake_pushdown(self, api_utils):
        """Explorer - Approved Snowflake pushdown."""
        connection = "APPROVED_SNOWFLAKE_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 3

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "PUBLIC"
        min_table_count = 100
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.smoke
    def test_approved_snowflake_up(self, api_utils):
        """Explorer - Approved Snowflake up."""
        connection = "APPROVED_SNOWFLAKE_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "PUBLIC"
        min_table_count = 100
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_sqlserver_up(self, api_utils):
        """Explorer - Approved Sqlserver up."""
        connection = "APPROVED_SQLSERVER_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 10

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "dbo"
        min_table_count = 50
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    @pytest.mark.skip(reason="TechVedika hosted instance is down.  Enable when connection is up.")
    def test_approved_sybase_up(self, api_utils):
        """Explorer - Approved Sybase Up."""
        connection = "APPROVED_SYBASE_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 20

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "dbo"
        min_table_count = 100
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_trino_pushdown(self, api_utils):
        """Explorer - Approved Trino Pushdown."""
        connection = "APPROVED_TRINO_PUSHDOWN"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 1

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "public"
        min_table_count = 100
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )

    @allure.feature("Explorer")
    @allure.story("Drill In")
    def test_approved_trino_up(self, api_utils):
        """Explorer - Approved Trino Up."""
        connection = "APPROVED_TRINO_UP"
        params = self.params.copy()
        params["alias"] = connection
        min_schema_count = 1

        data = self.data.copy()
        data["alias"] = connection
        data["schema"] = "public"
        min_table_count = 100
        self.get_schemas_and_tables_count(
            api_utils,
            connection,
            params,
            min_schema_count,
            data,
            min_table_count,
        )
