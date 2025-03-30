import pytest

PARAMS_PUSHDOWN_DQ_DATASET_WITH_METATAGS = [
    pytest.param(
        {
            "connection": "Snowflake",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_SNOWFLAKE",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SNOWFLAKE_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.snowflake,
    ),
    pytest.param(
        {
            "connection": "Oracle",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_ORACLE",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_ORACLE_PUSHDOWN",
            "source_query": "select * from OWLUSER.SALES",
        },
        marks=[pytest.mark.oracle,
               pytest.mark.skip("Skipped until DEV-116256 is deployed to 2025.05")]
    ),
    pytest.param(
        {
            "connection": "Bigquery",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_BIGQUERY",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_BIGQUERY_PUSHDOWN",
            "source_query": "select * from PUBLIC.SALES",
        },
        marks=pytest.mark.bigquery,
    ),
    pytest.param(
        {
            "connection": "Trino",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_TRINO",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_TRINO_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.trino,
    ),
    pytest.param(
        {
            "connection": "Saphana",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_SAPHANA",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_SAPHANA_PUSHDOWN",
            "source_query": "select * from TEST.SALES",
        },
        marks=pytest.mark.saphana,
    ),
    pytest.param(
        {
            "connection": "Redshift",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_REDSHIFT",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_REDSHIFT_PUSHDOWN",
            "source_query": "select * from public.sales2",
        },
        marks=pytest.mark.redshift,
    ),
    pytest.param(
        {
            "connection": "Databricks",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_DATABRICKS",
            "include_columns": ["NAME", "TRDATE", "SALES"],
            "connection_name": "APPROVED_DATABRICKS_PUSHDOWN",
            "source_query": "select * from public.sales",
        },
        marks=pytest.mark.databricks,
    ),
    pytest.param(
        {
            "connection": "Athena",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_ATHENA",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_ATHENA_PUSHDOWN",
            "source_query": "select * from default.sales",
        },
        marks=pytest.mark.athena,
    ),
    pytest.param(
        {
            "connection": "SQLServer",
            "dataset": "AUTO_PD_DATASET_WITH_METATAGS_SQLSERVER",
            "include_columns": ["name", "trdate", "sales"],
            "connection_name": "APPROVED_SQLSERVER_PUSHDOWN",
            "source_query": "select * from dbo.sales",
        },
        marks=pytest.mark.sqlserver,
    ),
]
