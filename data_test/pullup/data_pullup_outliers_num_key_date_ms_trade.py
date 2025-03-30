from payloads.pullup.pl_pullup_outliers_num_key_date_ms_trade import (
    PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
)

PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 73547,
            "dataset": PULLUP_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "+mISylAKZccU/b/Kwg3DMv6LXVD7tatJtLFnCdx60lh8E02yKVbsys7tonwk57sz",
            "outColumn": "TRADE_VALUE",
            "outValue": "1200.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.0",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": -4.0,
            "ub": 20.0,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 117936,
                "uuid": "30e615bb-aea2-41f9-8d1d-8fad2a146709"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
