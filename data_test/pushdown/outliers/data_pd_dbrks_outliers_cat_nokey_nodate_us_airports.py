from payloads.pushdown.outliers.pl_pd_dbrks_outliers_cat_nokey_nodate_us_airports import (
    PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
)

PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 5599,
            "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "Gh1BuyOlHW/H/mo9F0wXKgWXZPeUPG9zBCpUT1eA/1AbrwLzZ4XlM8qaBnQK8qHa",
            "outColumn": "AIRPORT_TYPE",
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
                "id": 61067,
                "uuid": "37e74c82-8ca9-4a4a-a42b-fd55d4ea3e6e"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 5598,
            "dataset": PD_DBRKS_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "0W3bU3oestGRCIbJMRujOZBtjlqdQJRy5F3awpw3EcW/VYWjrDpqZ35l5h6FT5wc",
            "outColumn": "AIRPORT_TYPE",
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
                "id": 61066,
                "uuid": "149f2f05-86c0-4fc3-abd6-2b8661583ccb"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
