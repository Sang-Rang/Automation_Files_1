from payloads.pushdown.outliers.pl_pd_bq_outliers_cat_nokey_nodate_nyse_archive_breaks import (
    PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
)

PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 445,
            "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "DbkkTzfDkRYnz7ouHeR9nF3RpprCNq4GJUdv3hb7EB1dyvYG+X8ORliAGCEN6h+3",
            "outColumn": "SYMBOL",
            "outValue": "LBRT",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 2,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "NYSE~|LBRT~|2018-01-16",
            "linkIdArr": [
                "2018-01-16",
                "NYSE",
                "LBRT"
            ],
            "assignmentId": {
                "id": 2220,
                "uuid": "c434d86f-51a7-49bb-9739-c58326665906"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 444,
            "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "0HwPbsBKC2641E0qymGc4oIZGbIQH/56GtSVC2QFkIgHlu5z9HRisoqN9Q3BjlK5",
            "outColumn": "SYMBOL",
            "outValue": "SRE-A",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 3,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "NYSE~|SRE-A~|2018-01-15",
            "linkIdArr": [
                "2018-01-15",
                "NYSE",
                "SRE-A"
            ],
            "assignmentId": {
                "id": 2219,
                "uuid": "f0054747-ea7c-4eb7-b9cf-972a402e037a"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}

PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 5362654,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "LBRT",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 1,
        "link_id": "NYSE~|LBRT~|2018-01-12",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": True,
        "source_date": None,
        "frequency": 2,
        "percentile": 0.0
    },
    {
        "seqno": 5362656,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "SRE-A",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 1,
        "link_id": "NYSE~|SRE-A~|2018-01-12",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": True,
        "source_date": None,
        "frequency": 3,
        "percentile": 0.00031887755102040814
    },
    {
        "seqno": 5362657,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "SRE-A",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 1,
        "link_id": "NYSE~|SRE-A~|2018-01-16",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": True,
        "source_date": None,
        "frequency": 3,
        "percentile": 0.00031887755102040814
    },
    {
        "seqno": 5362660,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "AAN",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 34,
        "link_id": "",
        "is_outlier": False,
        "is_historical": False,
        "is_topn": True,
        "is_botn": False,
        "source_date": None,
        "frequency": 35,
        "percentile": 1.0
    },
    {
        "seqno": 5362658,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "SRE-A",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 1,
        "link_id": "NYSE~|SRE-A~|2018-01-15",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": True,
        "source_date": None,
        "frequency": 3,
        "percentile": 0.00031887755102040814
    },
    {
        "seqno": 5362655,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "LBRT",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 1,
        "link_id": "NYSE~|LBRT~|2018-01-16",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": True,
        "source_date": None,
        "frequency": 2,
        "percentile": 0.0
    },
    {
        "seqno": 5362659,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "ZX",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 33,
        "link_id": "",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": True,
        "is_botn": False,
        "source_date": None,
        "frequency": 33,
        "percentile": 0.021683673469387755
    },
    {
        "seqno": 5362664,
        "updts": "2023-10-05T14:41:33.590+0000",
        "job_uuid": "84daa4e4-5ec8-443e-8314-506d1d52da3f",
        "dataset": PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-10-05T00:00:00.000+0000",
        "id": 878,
        "key_column": None,
        "key_value": None,
        "value_column": "SYMBOL",
        "value": "ZYME",
        "date_value": None,
        "type": "CATEGORICAL",
        "median": "INVALID",
        "lb": None,
        "ub": None,
        "confidence": 0,
        "cnt": 33,
        "link_id": "",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": True,
        "is_botn": False,
        "source_date": None,
        "frequency": 33,
        "percentile": 0.021683673469387755
    }
]

PD_BQ_OUTLIERS_CAT_NOKEY_NODATE_NYSE_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "id": 878,
        "value_column": "SYMBOL",
        "EXCH": "NYSE",
        "SYMBOL": "LBRT",
        "TRADE_DATE": "2018-01-12",
        "OPEN": 21.2,
        "HIGH": 22.12,
        "LOW": 21.05,
        "CLOSE": 21.75,
        "VOLUME": 10448600,
        "PART_DATE_STR": "2018-01-12"
    },
    {
        "id": 878,
        "value_column": "SYMBOL",
        "EXCH": "NYSE",
        "SYMBOL": "SRE-A",
        "TRADE_DATE": "2018-01-12",
        "OPEN": 99.96,
        "HIGH": 100.62,
        "LOW": 99.96,
        "CLOSE": 100.28,
        "VOLUME": 543300,
        "PART_DATE_STR": "2018-01-12"
    },
    {
        "id": 878,
        "value_column": "SYMBOL",
        "EXCH": "NYSE",
        "SYMBOL": "SRE-A",
        "TRADE_DATE": "2018-01-15",
        "OPEN": 100.28,
        "HIGH": 100.28,
        "LOW": 100.28,
        "CLOSE": 100.28,
        "VOLUME": 0,
        "PART_DATE_STR": "2018-01-15"
    },
    {
        "id": 878,
        "value_column": "SYMBOL",
        "EXCH": "NYSE",
        "SYMBOL": "SRE-A",
        "TRADE_DATE": "2018-01-16",
        "OPEN": 100.3,
        "HIGH": 100.62,
        "LOW": 100.01,
        "CLOSE": 100.44,
        "VOLUME": 467600,
        "PART_DATE_STR": "2018-01-16"
    },
    {
        "id": 878,
        "value_column": "SYMBOL",
        "EXCH": "NYSE",
        "SYMBOL": "LBRT",
        "TRADE_DATE": "2018-01-16",
        "OPEN": 21.9,
        "HIGH": 22.09,
        "LOW": 21.36,
        "CLOSE": 21.82,
        "VOLUME": 1044100,
        "PART_DATE_STR": "2018-01-16"
    }
]
