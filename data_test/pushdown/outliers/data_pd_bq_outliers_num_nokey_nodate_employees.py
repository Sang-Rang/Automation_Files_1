from payloads.pushdown.outliers.pl_pd_bq_outliers_num_nokey_nodate_employees import (
    PD_BQ_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
)

PD_BQ_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 409,
            "dataset": PD_BQ_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2023-09-09T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "kKbtkXHg53t2fj2CRVtuEdfZxen23VVBwRgJZ9Ce7E2lX2qpA01lwvdMygirti6A",
            "outColumn": "TIME_IN_SERVICE_YRS",
            "outValue": "110.91",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.28,
            "confidence": 6,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 2181,
                "uuid": "e78fb46a-ca3c-4e3f-8f3e-23a7542559b4"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 408,
            "dataset": PD_BQ_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2023-09-09T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "1YUiERPxncBpl9tN2q+wRoLw8ZrYogy7XFoFqHNJy8WDFjpf7Q8IXgTnOiaBLDdA",
            "outColumn": "TIME_IN_SERVICE_YRS",
            "outValue": "6.95",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.28,
            "confidence": 90,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 2180,
                "uuid": "8c4d1797-0416-4665-8d84-93a857eadf34"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
