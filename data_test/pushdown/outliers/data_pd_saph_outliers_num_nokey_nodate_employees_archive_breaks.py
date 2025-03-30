# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_saph_outliers_num_nokey_nodate_employees_archive_breaks import (
    PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET
)

PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 411,
            "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-09T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "393ObE1ukdAlyNBStkvDTAicdolRm7ReNCIux04CCgNQMzdJHsX8D7fG6/bL9259",
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
            "linkId": "51~|abalsdon1e@eepurl.com",
            "linkIdArr": [
                "abalsdon1e@eepurl.com",
                "51"
            ],
            "assignmentId": {
                "id": 2183,
                "uuid": "84792381-706a-43af-8b8e-2ad63534194c"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 410,
            "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-09T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "s0AelArS6HdeSLr+XR5BUjQaA684VqdLSvTuNlcShim27Qhj6yn0wuqTgC8t+1yW",
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
            "linkId": "8~|ckrollman7@geocities.jp",
            "linkIdArr": [
                "8",
                "ckrollman7@geocities.jp"
            ],
            "assignmentId": {
                "id": 2182,
                "uuid": "3e51d2bb-ccd1-4ac8-b036-447a2f694ef5"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 4145990,
        "updts": "2023-09-09T21:59:52.391+0000",
        "job_uuid": "dddb64ea-00ef-45cc-94df-380243401e57",
        "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-09-09T00:00:00.000+0000",
        "id": 365,
        "key_column": None,
        "key_value": None,
        "value_column": "TIME_IN_SERVICE_YRS",
        "value": "110.91",
        "date_value": None,
        "type": "NUMERICAL",
        "median": "3.14",
        "lb": 0.0,
        "ub": 6.28,
        "confidence": 6,
        "cnt": 1,
        "link_id": "51~|abalsdon1e@eepurl.com",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": False,
        "source_date": None,
        "frequency": None,
        "percentile": None
    },
    {
        "seqno": 4145991,
        "updts": "2023-09-09T21:59:52.391+0000",
        "job_uuid": "dddb64ea-00ef-45cc-94df-380243401e57",
        "dataset": PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-09-09T00:00:00.000+0000",
        "id": 365,
        "key_column": None,
        "key_value": None,
        "value_column": "TIME_IN_SERVICE_YRS",
        "value": "6.95",
        "date_value": None,
        "type": "NUMERICAL",
        "median": "3.14",
        "lb": 0.0,
        "ub": 6.28,
        "confidence": 90,
        "cnt": 1,
        "link_id": "8~|ckrollman7@geocities.jp",
        "is_outlier": True,
        "is_historical": False,
        "is_topn": False,
        "is_botn": False,
        "source_date": None,
        "frequency": None,
        "percentile": None
    }
]

PD_SAPH_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "id": 365,
        "value_column": "TIME_IN_SERVICE_YRS",
        "EMPLOYEE_ID": "51",
        "FIRST_NAME": "Anne",
        "LAST_NAME": "Balsdon",
        "EMAIL": "abalsdon1e@eepurl.com",
        "GENDER": "Male",
        "CITY": "Charlotte",
        "DEPARTMENT": "Product Management",
        "LATITUDE": "35.26",
        "LONGITUDE": "-80.8042",
        "HOME_PHONE": "704-414-0164",
        "POSTAL_CODE": "28225",
        "STATE": "NC",
        "STREET_ADDRESS": "4 Tomscot Junction",
        "DATE_OF_HIRE": "12/23/1910",
        "TIME_IN_SERVICE_YRS": 110.91
    },
    {
        "id": 365,
        "value_column": "TIME_IN_SERVICE_YRS",
        "EMPLOYEE_ID": "8",
        "FIRST_NAME": "Christa",
        "LAST_NAME": "Krollman",
        "EMAIL": "ckrollman7@geocities.jp",
        "GENDER": "Female",
        "CITY": "Columbia",
        "DEPARTMENT": "Research and Development",
        "LATITUDE": "34.0635",
        "LONGITUDE": "-81.0265",
        "HOME_PHONE": "803-188-7333",
        "POSTAL_CODE": "29203",
        "STATE": "SC",
        "STREET_ADDRESS": "766 Mosinee Lane",
        "DATE_OF_HIRE": "11/11/2014",
        "TIME_IN_SERVICE_YRS": 6.95
    }
]
