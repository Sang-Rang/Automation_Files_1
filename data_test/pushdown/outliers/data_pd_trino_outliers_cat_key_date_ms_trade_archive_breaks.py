from payloads.pushdown.outliers.pl_pd_trino_outliers_cat_key_date_ms_trade_archive_breaks import (
    PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
)

PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_OUTLIERS_2023_01_10 = {
    "data": [
        {
            "id": 185939,
            "dataset": PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-01-10T00:00:00.000+0000",
            "outKeyColumn": "trade_id",
            "outKey": "xpQPO7J7srqAd7FUL7mygCh7EmU6AIAwWU+ljI9qL/ZLMeYqbdzVQ3Cg4zY8eDqq",
            "outColumn": "non_zero_computed",
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
                "id": 596456,
                "uuid": "c141089e-c345-42c5-a171-20709a6e4273"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}

PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_DATA_2023_01_10 = [
    {
        "seqno": 10827465,
        "updts": "2024-10-01T14:14:22.394+0000",
        "job_uuid": "1558c2e2-6503-4138-9026-89f7ad8e872e",
        "dataset": PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 2069,
        "key_column": "trade_id",
        "key_value": "X1",
        "value_column": "non_zero_computed",
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
        "percentile": 0
    },
    {
        "seqno": 10827466,
        "updts": "2024-10-01T14:14:22.394+0000",
        "job_uuid": "1558c2e2-6503-4138-9026-89f7ad8e872e",
        "dataset": PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 2069,
        "key_column": "trade_id",
        "key_value": "X1",
        "value_column": "non_zero_computed",
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
        "percentile": 0
    },
    {
        "seqno": 10827467,
        "updts": "2024-10-01T14:14:22.394+0000",
        "job_uuid": "1558c2e2-6503-4138-9026-89f7ad8e872e",
        "dataset": PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-01-10T00:00:00.000+0000",
        "id": 2069,
        "key_column": "trade_id",
        "key_value": "X1",
        "value_column": "non_zero_computed",
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
        "percentile": 0
    }
]

PD_TRINO_OUTLIERS_CAT_KEY_DATE_MS_TRADE_ARCHIVE_BREAKS_EXP_QUERY_OUT_2023_01_10 = [
  {
    "id": 2069,
    "value_column": "non_zero_computed",
    "trade_date": "2023-01-10",
    "end_date": "2023-01-10",
    "trade_id": "X1",
    "trade_value": 0,
    "notional": 1000,
    "exposure": 2000,
    "non_zero_computed": "N",
    "delta_days_computed": 0,
    "variance_bucket_computed": "0",
    "test_reason": "Catch this - Trade Value in acceptable range but goes to 0.  "
                   "Must use categorical"
  }
]
