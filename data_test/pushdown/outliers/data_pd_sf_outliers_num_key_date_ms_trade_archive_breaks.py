from payloads.pushdown.outliers.pl_pd_sf_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 531,
            "dataset": PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "RMB3QOOkbG4V1S0T7YfXsyoSIaxZMB5f9LD51bQdUIeEQdflqqH6SjWGTWrUliAh",
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
            "linkId": "2023-01-05~|X1",
            "linkIdArr": [
                "2023-01-05",
                "X1"
            ],
            "assignmentId": {
                "id": 2336,
                "uuid": "c5708097-437f-49b1-986f-ba76c38e98ce"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05 = [
    {
        "seqno": 4718727,
        "updts": "2023-09-11T21:09:53.278+0000",
        "job_uuid": "7d2ed51c-b664-4e58-9edd-67630f427a93",
        "dataset": PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-05T00:00:00.000+0000",
        "id": 527,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "TRADE_VALUE",
        "value": "1200.0",
        "date_value": "2023-01-05T00:00:00.000+0000",
        "type": "NUMERICAL",
        "median": "10",
        "lb": 0.2,
        "ub": 17.0,
        "confidence": 1,
        "cnt": 1,
        "link_id": "2023-01-05~|X1",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": False,
        "source_date": None,
        "frequency": None,
        "percentile": None
    }
]

PD_SF_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05 = [
    {
        "id": 527,
        "value_column": "TRADE_VALUE",
        "TRADE_DATE": "2023-01-05",
        "END_DATE": "2023-01-10",
        "TRADE_ID": "X1",
        "TRADE_VALUE": 1200.0,
        "NOTIONAL": 1000,
        "EXPOSURE": 2000,
        "NON_ZERO_COMPUTED": "Y",
        "DELTA_DAYS_COMPUTED": 5,
        "VARIANCE_BUCKET_COMPUTED": "100-1000",
        "TEST_REASON": "Catch This - Numerical Outlier"
    }
]
