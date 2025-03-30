from payloads.pushdown.schema.pl_pd_athena_schema_sales import PD_ATHENA_SCHEMA_SALES_DATASET

PD_ATHENA_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS = [
    {
        "dataset": PD_ATHENA_SCHEMA_SALES_DATASET,
        "runId": "2022-05-04T00:00:00.000+0000",
        "obsType": "SCHEMA_EVOLUTION",
        "obs": "Column removed sales",
        "obsKey": "3b05eda8c27274cef692203b38e04481",
        "obsScore": None,
        "owlRank": 1,
        "linkId": "",
        "obsId": 3994,
        "assignmentId": {
            "id": 17127,
            "uuid": "9940ff23-2a27-4fc0-9bd2-aaf4349aeffa"
        },
        "obsSubType": None
    }
]
