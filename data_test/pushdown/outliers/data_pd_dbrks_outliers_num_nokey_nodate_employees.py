from payloads.pushdown.outliers.pl_pd_dbrks_outliers_num_nokey_nodate_employees import (
    PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
)

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 91117,
            "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "eECAmp1MT6RTTTmj2zI3VrU8bPDii7EsTW7yHENi/D0Aq4bRvJAfGf+dCkvLDLpb",
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
            "confidence": 5,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 154485,
                "uuid": "b71e42fb-918a-4864-8806-00f359dc089a"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 91116,
            "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "1Q6iw1i/9Sdy2oW4NuVGILIiq3ThE5ACnRyHxlO+6pjX4SUj1jw+rK6RB2/0uqex",
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
                "id": 154484,
                "uuid": "6bc0efe6-d63c-486a-9e8f-73681d7aa232"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
