from payloads.pushdown.schema.pl_pd_bq_schema_sales import PD_BQ_SCHEMA_SALES_DATASET

PD_BQ_SCHEMA_SALES_EXPECTED_SCHEMA_FINDINGS = [
    {
        "dataset": PD_BQ_SCHEMA_SALES_DATASET,
        "runId": "2022-05-04T00:00:00.000+0000",
        "obsType": "SCHEMA_EVOLUTION",
        "obs": "Column removed SALES",
        "obsKey": "dbdad56b1b93f7c48c4a9b373de78c5b",
        "obsScore": None,
        "owlRank": 1,
        "linkId": "",
        "obsId": 4026,
        "assignmentId": {
            "id": 17362,
            "uuid": "35767aae-65c8-476e-9250-68b6a33558df"
        },
        "obsSubType": None
    }
]
