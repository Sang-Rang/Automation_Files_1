from payloads.pushdown.outliers.pl_pd_saph_outliers_num_key_date_ms_trade_archive_breaks import (
    PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_05 = {
    "data": [
        {
            "id": 502081,
            "dataset": PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
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

PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_05 = [
    {
        "seqno": 4718727,
        "updts": "2023-09-11T21:09:53.278+0000",
        "job_uuid": "7d2ed51c-b664-4e58-9edd-67630f427a93",
        "dataset": PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-05T00:00:00.000+0000",
        "id": 527,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "TRADE_VALUE",
        "value": "1200.0",
        "date_value": "2023-01-05T00:00:00.000+0000",
        "type": "NUMERICAL",
        "median": "10",
        "lb": 0.1999999999999984,
        "ub": 17.000000000000004,
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

PD_SAPH_OUTLIERS_NUM_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_05 = [
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
