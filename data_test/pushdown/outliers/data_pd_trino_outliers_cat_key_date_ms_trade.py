from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_date_ms_trade import (
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
)

PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10 = {
    "data": [
        {
            "id": 489463,
            "dataset": PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-10T00:00:00.000+0000",
            "outKeyColumn": "trade_id",
            "outKey": "UzuxWEsz918MDiiqnL81j6GCoNCJIJnkQBJrQjSChcpxdEam04jCcCEiQ4/qJP1a",
            "outColumn": "non_zero_computed",
            "outValue": "N",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 100,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1516785,
                "uuid": "7293fe07-f3a5-4693-ad66-2f6e26b325c8"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
