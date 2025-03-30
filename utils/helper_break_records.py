from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_job import V2_GET_JOB_STATUS_BY_DATASET

from utils.helper import BaseHelper


class BreakRecordsHelper:
    """Helper methods for break records"""

    @staticmethod
    def build_athena_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from Athena data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_rules where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Rules' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_bigquery_pushdown_archived_dupes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving dupes break records from BigQuery data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_DUPLICATES "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.COLLIBRA_DQ_BREAKS "
            f"where activity = 'Dupes' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_bigquery_pushdown_archived_outliers_break_record_sql(
            api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving outliers break records from Bigquery data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_OUTLIERS "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f'select query from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where activity = 'Outliers' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_bigquery_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from BigQuery data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_RULES where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.COLLIBRA_DQ_BREAKS "
            f"where activity = 'Rules' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_bigquery_pushdown_archived_shapes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving shapes break records from Databricks data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"SELECT * FROM {break_records_schema}.COLLIBRA_DQ_SHAPES WHERE job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"SELECT query from {break_records_schema}.COLLIBRA_DQ_BREAKS "
            f"WHERE activity = 'Shapes' AND job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_databricks_pushdown_archived_dupes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving dupes break records from Databricks data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_duplicates "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Dupes' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_databricks_pushdown_archived_outliers_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving outliers break records from Databricks data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_outliers "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Outliers' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_databricks_pushdown_archived_rules_break_record_sql_statements(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from Databricks data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_rules where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Rules' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_databricks_pushdown_archived_shapes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving shapes break records from Databricks data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_shapes where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Shapes' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_redshift_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from Redshift data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_rules where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Rules' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_saphana_pushdown_archived_outliers_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving outliers break records from SAP HANA data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_OUTLIERS "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Outliers' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_saphana_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving shapes break records from SAP HANA data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "TEST"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_SHAPES "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f"select \"query\" from {break_records_schema}.COLLIBRA_DQ_BREAKS "
            f"where \"activity\" = 'Shapes' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_saphana_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from SAP HANA data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_rules "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.collibra_dq_breaks '
            f"where \"activity\" = 'Rules' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_trino_pushdown_archived_dupes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving dupes break records from Trino data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_duplicates "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.collibra_dq_breaks '
            f"where activity = 'Dupes' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_trino_pushdown_archived_outliers_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving outliers break records from Trino data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_outliers "
            f"where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.collibra_dq_breaks "
            f"where activity = 'Outliers' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_trino_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from Trino data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_rules "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.collibra_dq_breaks '
            f"where \"activity\" = 'Rules' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_trino_pushdown_archived_shapes_break_record_sql(
            api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving shapes break records from Snowflake data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_SHAPES "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Shapes' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_saphana_pushdown_archived_dupes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving dupes break records from SAP HANA data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.collibra_dq_duplicates "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.collibra_dq_breaks '
            f"where \"activity\" = 'Dupes' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_snowflake_pushdown_archived_dupes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving dupes break records from Snowflake data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_DUPLICATES "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Dupes' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_snowflake_pushdown_archived_outliers_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving outliers break records from Snowflake data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_OUTLIERS "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Outliers' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_snowflake_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from Snowflake data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_RULES "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Rules' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_snowflake_pushdown_archived_shapes_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving shapes break records from Snowflake data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "PUBLIC"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_SHAPES "
            f"where \"job_uuid\" = '{job_uuid}'"
        )
        record_query = (
            f'select "query" from {break_records_schema}.COLLIBRA_DQ_BREAKS '
            f"where \"activity\" = 'Shapes' and \"job_uuid\" = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    @staticmethod
    def build_sqlserver_pushdown_archived_rules_break_record_sql(
        api_utils, connection, dataset, run_id
    ):
        """Build queries for retrieving rules break records from MSSQL data sources."""
        connection_details = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": connection})
        job_uuid = api_utils.get(
            V2_GET_JOB_STATUS_BY_DATASET, params={"dataset": dataset, "runId": run_id}
        )["jobId"]["uuid"]
        if connection_details["breakRecordsLocation"]:
            break_records_schema = connection_details["breakRecordsLocation"]
        else:
            break_records_schema = "public"
        data_query = (
            f"select * from {break_records_schema}.COLLIBRA_DQ_RULES where job_uuid = '{job_uuid}'"
        )
        record_query = (
            f"select query from {break_records_schema}.COLLIBRA_DQ_BREAKS "
            f"where activity = 'Rules' and job_uuid = '{job_uuid}'"
        )
        queries = {"dataQuery": data_query, "recordQuery": record_query}

        return queries

    def get_pushdown_archived_breaks(
        self, api_utils, connection_details, run_id, breaks_queries, write_sql_out=False
    ):
        connection_name = connection_details["aliasname"]
        limit_value = self.get_unlimited_query_limit_value(connection_details)

        # Write processed sql output to the console instead of validating
        # when adding new tests' expected results to the repo
        breaks = BaseHelper.run_query_and_extract_result(
            api_utils, breaks_queries["dataQuery"], connection_name, limit=limit_value
        )
        if write_sql_out:
            print(str(len(breaks)) + " break records found for runId " + run_id)
            print(breaks)
        break_query = BaseHelper.run_query_and_extract_result(
            api_utils, breaks_queries["recordQuery"], connection_name, limit=limit_value
        )
        break_query_sql = break_query[0]["query"]
        queried_break_records = BaseHelper.run_query_and_extract_result(
            api_utils, break_query_sql, connection_name, limit=limit_value
        )
        if write_sql_out:
            print(
                str(len(queried_break_records)) + " queried break records found for runId " + run_id
            )
            print(queried_break_records)

        return {"breaks": breaks, "queried_break_records": queried_break_records}

    @staticmethod
    def get_unlimited_query_limit_value(connection_details):
        """
        Most connections use -1 to represent an unlimited query return limit; however, some
        connection types require a non-negative limit value.  Return an appropriate value for
        effectively unlimited SQL results to be returned.
        :param connection_details: The details of a connection to be checked for an appropriate
        limit value
        :return:
        """

        # BigQuery connections require a nonnegative limit value.  All others use -1 for no limit.
        if connection_details["dbBrandName"] == "BIGQUERY":
            limit_value = 1000000
        else:
            limit_value = -1

        return limit_value
