from payloads.pushdown.schema.pl_pd_mssql_schema_sales import PD_MSSQL_SCHEMA_SALES_DATASET

PD_MSSQL_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS = [
    {
        "dataset": PD_MSSQL_SCHEMA_SALES_DATASET,
        "runId": "2022-05-04T00:00:00.000+0000",
        "obsType": "SCHEMA_EVOLUTION",
        "obs": "Column removed sales",
        "obsKey": "d73b613f3b62ae20c1efd9a58bc44339",
        "obsScore": None,
        "owlRank": 1,
        "linkId": "",
        "obsId": 4041,
        "assignmentId": {
            "id": 17377,
            "uuid": "1e6c63fe-f460-439e-b49d-08f25457352e"
        },
        "obsSubType": None
    }
]
