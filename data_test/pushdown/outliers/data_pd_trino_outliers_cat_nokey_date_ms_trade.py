from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_nokey_date_ms_trade import (
    PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET,
)

PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10 = {
    "data": [
        {
            "id": 491754,
            "dataset": PD_TRINO_OUTLIERS_CAT_NOKEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "fzuVv8K0AccNMwFUvI7uPC2ag0q0z6fcVMZrnHVPjU8DFU1GJe58bW91+v+effb2",
            "outColumn": "non_zero_computed",
            "outValue": "N",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 33,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1522863,
                "uuid": "4633f7c5-a27f-4d51-8934-76e4da0a6a48"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
