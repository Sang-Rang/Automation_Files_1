from payloads.pushdown.outliers.pl_pd_trino_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 480714,
            "dataset": PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "trade_id",
            "outKey": "RngZjYV39ecjOpHkaz03yGiWhUCoUh+u9s64nz0p3a4BlOkCMrlSDBEIIyrALrh/",
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
                "id": 1480108,
                "uuid": "168cd0ff-7ca3-47b3-8591-61b6a128118c"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05 = [
    {
        "seqno": 9911240,
        "updts": "2024-08-31T19:48:25.484+0000",
        "job_uuid": "fb055e9c-bc82-4536-8f37-284e592d353b",
        "dataset": PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-05T00:00:00.000+0000",
        "id": 1617,
        "key_column": "trade_id",
        "key_value": "X1",
        "value_column": "trade_value",
        "value": "1200.0000",
        "date_value": "2023-01-05T00:00:00.000+0000",
        "type": "NUMERICAL",
        "median": "10.0000",
        "lb": -4.0,
        "ub": 20.0,
        "confidence": 2,
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

PD_TRINO_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05 = [
    {
        "id": 1617,
        "value_column": "trade_value",
        "trade_date": "2023-01-05",
        "end_date": "2023-01-10",
        "trade_id": "X1",
        "trade_value": 1200.0,
        "notional": 1000,
        "exposure": 2000,
        "non_zero_computed": "Y",
        "delta_days_computed": 5,
        "variance_bucket_computed": "100-1000",
        "test_reason": "Catch This - Numerical Outlier"
    }
]
