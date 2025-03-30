from payloads.pushdown.outliers.pl_pd_trino_outliers_num_nokey_nodate_employees import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
)

PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 480630,
            "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2024-08-31T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "QEteI2Pkdh7pVRIqhG0v82gVHPqVva/OzknI2FqiKZRGqpZbYcFk2204RsVovjXE",
            "outColumn": "time_in_service_yrs",
            "outValue": "110.91",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.289479176433818,
            "confidence": 6,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1479379,
                "uuid": "a955609b-c28a-4bf4-9db6-47df6d890b39"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 480629,
            "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2024-08-31T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "EMO4PBBa41ymco61UXpqlfXrGvu/FukcyUZvb8kbSH+pBHlEDcEaYykMV+qQvsuU",
            "outColumn": "time_in_service_yrs",
            "outValue": "6.95",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.289479176433818,
            "confidence": 90,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 1479378,
                "uuid": "f4e0cd85-7dfa-4cfa-8455-89d122560198"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
