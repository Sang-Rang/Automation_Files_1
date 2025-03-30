from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_date_ms_trade import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
)

PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 480415,
            "dataset": PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "trade_id",
            "outKey": "sE7a4nYjPgdo0fHsbk/c3eALKwgmi/boX2JFZouMczy0A9VTvqSlaPAQXVKriMY5",
            "outColumn": "trade_value",
            "outValue": "1200",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.00",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": -4.0,
            "ub": 20.0,
            "confidence": 2,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1479017,
                "uuid": "f9a8fcef-41ad-443e-aae6-c3019848c4dc"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
