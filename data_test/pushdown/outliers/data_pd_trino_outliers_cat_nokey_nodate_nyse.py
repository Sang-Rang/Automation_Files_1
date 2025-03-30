from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_nodate_nyse import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
)

PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 491757,
            "dataset": PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "3HT3znHUzWMPe0N801Qfbm7CmlAbvuWsatW7Cv68hBVQoHOx6s1JMSptU6NGgTGR",
            "outColumn": "symbol",
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
                "id": 1522866,
                "uuid": "77c5929b-42ce-4303-893a-9c64a5e340fa"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 491756,
            "dataset": PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "bxdC9XfWaAFKdFE0xWCeywzgxUPVdQaBMz8EP4LkZ6b2a8jnIomtudFDSJN1g+rr",
            "outColumn": "symbol",
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
                "id": 1522865,
                "uuid": "ed99e971-c47f-40c0-8804-721afebdd95b"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
