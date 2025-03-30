from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_nodate_us_airports import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
)

PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 491763,
            "dataset": PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "0uxTIp+VoOh37319xgOtXU13PRvRA4grTZoqIHRbE8qjP52CLWu6DoTpe1Wen1bf",
            "outColumn": "airport_type",
            "outValue": "Balloonport",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 14,
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
                "id": 1522876,
                "uuid": "ee93d9cd-b949-4ee6-a403-6e082e199502"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 491762,
            "dataset": PD_TRINO_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2024-09-19T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "S32TeszA9Y18JLmwL70MBpCqkdfl1iFl+7GOef+HBWWdZIXLT+ZoQpYxwCqDrow6",
            "outColumn": "airport_type",
            "outValue": "Gliderport",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 35,
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
                "id": 1522875,
                "uuid": "d1cd68ae-a43d-4687-9d9a-4ee254ebe4b3"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
