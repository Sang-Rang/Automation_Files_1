from payloads.pushdown.outliers.pl_pd_bq_outliers_cat_key_nodate_nyse import (
    PD_BQ_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
)

PD_BQ_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 51827,
            "dataset": PD_BQ_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "EXCH",
            "outKey":
                "vBd9K69C8pzWCsWc1A4aL72McoMQWZzJy2mte4BcUJHugRslDnIBkrMe/cx/P0AT",
            "outColumn": "SYMBOL",
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
                "id": 299356,
                "uuid": "f8c8b43d-5c5e-484a-991a-386853f69bfd"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 51826,
            "dataset": PD_BQ_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "EXCH",
            "outKey":
                "HXJ+NZ2IcgayuR9y7heLcbq89slnSzSuRY6bXO3+e9Exl/Ic/mj2ND3iBVvHrp8C",
            "outColumn": "SYMBOL",
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
                "id": 299355,
                "uuid": "5a24f897-0f35-4cd5-b1e0-4f22e4feb180"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
