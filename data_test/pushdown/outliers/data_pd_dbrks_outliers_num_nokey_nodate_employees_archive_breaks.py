# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_dbrks_outliers_num_nokey_nodate_employees_archive_breaks import (
    PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
)

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 91121,
            "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "vbYxGF0IoWHwXOTDhzVOlTl4a0V5D/QnICFq7tzE5/YwtNHenUXm3yWUcBqU2Q42",
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
            "linkId": "51~|abalsdon1e@eepurl.com",
            "linkIdArr": [
                "abalsdon1e@eepurl.com",
                "51"
            ],
            "assignmentId": {
                "id": 154489,
                "uuid": "709392b9-e023-4619-b24b-4955a97daa3e"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 91120,
            "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2023-09-10T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "L6sh7b+4ONs+LPdHhqyjEbo7QHMdNWUWuS+mJ+qN1qCDEBaE07Q/Dv7SKgqWQuyo",
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
                "id": 154488,
                "uuid": "50700238-f278-408e-a27d-5fdfefe96ae6"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 1392970,
        "updts": "2023-09-10T06:31:07.361+0000",
        "job_uuid": "009023d9-c062-4ae0-8539-bc9feca2098f",
        "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-09-10T00:00:00.000+0000",
        "id": 375,
        "key_column": None,
        "key_value": None,
        "value_column": "TIME_IN_SERVICE_YRS",
        "value": "110.91",
        "date_value": None,
        "type": "NUMERICAL",
        "median": "3.14",
        "lb": 0.0,
        "ub": 6.28,
        "confidence": 5,
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
        "seqno": 1392971,
        "updts": "2023-09-10T06:31:07.361+0000",
        "job_uuid": "009023d9-c062-4ae0-8539-bc9feca2098f",
        "dataset": PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2023-09-10T00:00:00.000+0000",
        "id": 375,
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

PD_DBRKS_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
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
