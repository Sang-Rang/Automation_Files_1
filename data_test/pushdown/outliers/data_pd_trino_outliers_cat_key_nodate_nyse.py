from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_nodate_nyse import (
    PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
)

PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 491742,
            "dataset": PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "exch",
            "outKey": "epKMpIJxtYDbxs4kBwYkEUfomENvYhWr6Cq/IXAH3+yhip+DNQBFu28wre17pNlo",
            "outColumn": "symbol",
            "outValue": "LBRT",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 2,
            "keyArr": [
                "NYSE"
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
                "id": 1522850,
                "uuid": "90113ea3-b791-4010-b5b2-48b3ef73698b"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 491741,
            "dataset": PD_TRINO_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "exch",
            "outKey": "Rs7x7MfkVqgjQNFJP33TLnZA6stkFl6Ocjnp7E3DTmnAnlCpK5ncCacKfPdet5bv",
            "outColumn": "symbol",
            "outValue": "SRE-A",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 3,
            "keyArr": [
                "NYSE"
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
                "id": 1522849,
                "uuid": "52db38fd-87b9-47eb-881e-5d543d960671"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
