from payloads.pushdown.outliers.pl_pd_dbrks_outliers_num_key_date_ms_trade import (
    PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
)

PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 56674,
            "dataset": PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "FjjlvcARMm74J/fpiBv/vwBMYC7e6otcTEBMlTpjfi7eyF3mmf3zwBGh6C731H25",
            "outColumn": "TRADE_VALUE",
            "outValue": "1200",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.00",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": 0.20000000000000107,
            "ub": 17.0,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 90418,
                "uuid": "e266b935-27ba-4480-936c-d4c75a45392a"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
