from payloads.pushdown.outliers.pl_pd_dbrks_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 533,
            "dataset": PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-01-05T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "FZBYWR4yErFj/mMw8GfkLUkKYfwJBmkgSi6FaLWq+utnN+LUZBODV59TbYZdYZ5B",
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
            "linkId": "X1~|2023-01-05",
            "linkIdArr": [
                "2023-01-05",
                "X1"
            ],
            "assignmentId": {
                "id": 2338,
                "uuid": "5228cfcc-2dd2-47c3-bcb2-143e5fd17b98"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05 = [
    {
        "seqno": 2092905,
        "updts": "2023-09-12T04:51:57.371+0000",
        "job_uuid": "6ca99d54-d6d7-476d-a040-aeafaadeeb7a",
        "dataset": PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-05T00:00:00.000+0000",
        "id": 534,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "TRADE_VALUE",
        "value": "1200.0",
        "date_value": "2023-01-05T00:00:00.000+0000",
        "type": "NUMERICAL",
        "median": "10.0",
        "lb": 0.20000000000000107,
        "ub": 17.0,
        "confidence": 1,
        "cnt": 1,
        "link_id": "X1~|2023-01-05",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": False,
        "source_date": None,
        "frequency": None,
        "percentile": None
    }
]

PD_DBRKS_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05 = [
    {
        "id": 534,
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
