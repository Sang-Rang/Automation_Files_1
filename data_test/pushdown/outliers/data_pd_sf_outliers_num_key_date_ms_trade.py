from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_date_ms_trade import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
)

PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 176731,
            "dataset": PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "Yrr2aC/r5azcufYabDapXnHNzSwwngSj+Z4DK6muq/0bpFSc/BkUXw05ust43MLK",
            "outColumn": "TRADE_VALUE",
            "outValue": "1200",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.00",
            "outCount": 1,
            "keyArr": [
                "X1"
            ],
            "lb": 0.2,
            "ub": 17.0,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 501283,
                "uuid": "c403741b-aa01-4ef0-9759-21058acb5315"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
