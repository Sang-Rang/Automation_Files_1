from payloads.pushdown.schema.pl_pd_trino_schema_sales import PD_TRINO_SCHEMA_SALES_DATASET

PD_TRINO_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS = [
    {
        "dataset": PD_TRINO_SCHEMA_SALES_DATASET,
        "runId": "2022-05-04T00:00:00.000+0000",
        "obsType": "SCHEMA_EVOLUTION",
        "obs": "Column removed sales",
        "obsKey": "60502816f88a3eab657bc8b8c3b94f50",
        "obsScore": None,
        "owlRank": 1,
        "linkId": "",
        "obsId": 4044,
        "assignmentId": {
            "id": 17380,
            "uuid": "f87719ba-46d2-4865-aacd-4956267424a3"
        },
        "obsSubType": None
    }
]
