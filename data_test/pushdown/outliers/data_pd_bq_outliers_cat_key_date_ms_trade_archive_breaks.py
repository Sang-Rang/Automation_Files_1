from payloads.pushdown.outliers.pl_pd_bq_outliers_cat_key_date_ms_trade_archive_breaks import (
    PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10 = {
    "data": [
        {
            "id": 1086,
            "dataset": PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-01-10T00:00:00.000+0000",
            "outKeyColumn": "TRADE_ID",
            "outKey": "CXlgF7RS5jo4jImYHXtv4RhjX8pqvNW/1+XA61J6DOwXukeT5RttZ3rliyiKTaNT",
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
            "linkId": "2023-01-10~|X1",
            "linkIdArr": [
                "2023-01-10",
                "X1"
            ],
            "assignmentId": {
                "id": 3602,
                "uuid": "6292c726-e41e-4cce-934f-d2370aa89991"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}

PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10 = [
    {
        "seqno": 5087725,
        "updts": "2023-09-12T19:10:47.185+0000",
        "job_uuid": "72694591-1325-4fc4-a87c-9e8ee6515bc7",
        "dataset": PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 640,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "NON_ZERO_COMPUTED",
        "value": "N",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 100,
        "cnt": 1,
        "link_id": "2023-01-10~|X1",
        "is_outlier": False,
        "is_historical": False,
        "is_topn": True,
        "is_botn": True,
        "source_date": "2023-01-10",
        "frequency": 1,
        "percentile": 0.0
    },
    {
        "seqno": 5087726,
        "updts": "2023-09-12T19:10:47.185+0000",
        "job_uuid": "72694591-1325-4fc4-a87c-9e8ee6515bc7",
        "dataset": PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 640,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "NON_ZERO_COMPUTED",
        "value": "Y",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 100,
        "cnt": 5,
        "link_id": "",
        "is_outlier": False,
        "is_historical": True,
        "is_topn": True,
        "is_botn": True,
        "source_date": "2023-01-05 - 2023-01-10 (historical)",
        "frequency": 5,
        "percentile": 0.0
    },
    {
        "seqno": 5087727,
        "updts": "2023-09-12T19:10:47.185+0000",
        "job_uuid": "72694591-1325-4fc4-a87c-9e8ee6515bc7",
        "dataset": PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 640,
        "key_column": "TRADE_ID",
        "key_value": "X1",
        "value_column": "NON_ZERO_COMPUTED",
        "value": "N",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 100,
        "cnt": 1,
        "link_id": "2023-01-10~|X1",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": True,
        "is_botn": True,
        "source_date": "2023-01-10",
        "frequency": 1,
        "percentile": 0.0
    }
]

PD_BQ_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10 = [
    {
        "id": 640,
        "value_column": "NON_ZERO_COMPUTED",
        "TRADE_DATE": "2023-01-10",
        "END_DATE": "2023-01-10",
        "TRADE_ID": "X1",
        "TRADE_VALUE": 0.0,
        "NOTIONAL": 1000,
        "EXPOSURE": 2000,
        "NON_ZERO_COMPUTED": "N",
        "DELTA_DAYS_COMPUTED": 0,
        "VARIANCE_BUCKET_COMPUTED": "0",
        "TEST_REASON": "Catch this - Trade Value in acceptable range but goes to 0.  "
                       "Must use categorical"
    }
]
