from payloads.pushdown.schema.pl_pd_dbrks_schema_sales import PD_DBRKS_SCHEMA_SALES_DATASET

PD_DBRKS_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS = [
    {
        "dataset": PD_DBRKS_SCHEMA_SALES_DATASET,
        "runId": "2022-05-04T00:00:00.000+0000",
        "obsType": "SCHEMA_EVOLUTION",
        "obs": "Column removed SALES",
        "obsKey": "87df00cda67c15fef10e39cf611a5c8c",
        "obsScore": None,
        "owlRank": 1,
        "linkId": "",
        "obsId": 4028,
        "assignmentId": {
            "id": 17364,
            "uuid": "e4bc6c82-d0b0-41cb-8a16-f92f30b374c4"
        },
        "obsSubType": None
    }
]
