from payloads.pushdown.outliers.pl_pd_saph_outliers_num_key_date_ms_trade import (
    PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
)

PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 502081,
            "dataset": PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "HmDRW+BgkfoNbLVgdmxeoOym1b2RL1dpbcyXSuSnJlLzP/7t6LSrk8VyWKoMfjS9",
            "outColumn": "TRADE_VALUE",
            "outValue": "1200",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.00",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": 0.1999999999999984,
            "ub": 17.000000000000004,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1580561,
                "uuid": "ce772303-ff66-43d9-8f2b-fed4bf3b4dcf"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
