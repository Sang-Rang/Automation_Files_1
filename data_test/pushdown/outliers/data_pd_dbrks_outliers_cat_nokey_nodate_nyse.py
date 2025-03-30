from payloads.pushdown.outliers.pl_pd_dbrks_outliers_cat_nokey_nodate_nyse import (
    PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
)

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 51825,
            "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "4OmywZWKk3Aqxw5ZIxGKH2eXOqeqhrjQFejawWJTRGx0r9bomDUer5DMxsR5IuzD",
            "outColumn": "SYMBOL",
            "outValue": "LBRT",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 2,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 299354,
                "uuid": "b0887cd5-8e18-4db3-8033-ea89f4796f85"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 51824,
            "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "tjTUvwLOlcCH/rtUWsjH+8LkXEXsf8M2kqnkRC5Gj2KOUo3aKjTbunScjWJGtAv9",
            "outColumn": "SYMBOL",
            "outValue": "SRE-A",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 3,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 299353,
                "uuid": "9a46a2d3-2970-4d7e-911a-26964c988ebc"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
