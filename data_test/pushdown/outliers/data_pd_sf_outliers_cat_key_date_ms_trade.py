from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_key_date_ms_trade import (
    PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
)

PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_EXPECTED_OUTLIERS_2023_01_10 = {
    "data": [
        {
            "id": 59138,
            "dataset": PD_SF_OUTLIERS_CAT_KEY_DATE_MS_TRADE_DATASET,
            "runId": "2023-01-10T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "GnG4LNmZJptuA+zII6wK6JdrAybsyJcGceWcf28QKTur6zfNCMYtNFEzMQo15JyW",
            "outColumn": "NON_ZERO_COMPUTED",
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
                "id": 98832,
                "uuid": "cf14fd68-8a22-47dc-95c7-46de935ebaeb"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
