# pylint: disable-next=line-too-long
from payloads.pushdown.outliers.pl_pd_trino_outliers_num_nokey_nodate_employees_archive_breaks import (
    PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
)

PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 222090,
            "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2025-01-12T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "xilAkwDB810+Nml1rKl6Esx2atppog9Cf9LuHHdFRWuyidiawoLGZPPiy0ag5tFQ",
            "outColumn": "time_in_service_yrs",
            "outValue": "110.91",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.289479176,
            "confidence": 6,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 764039,
                "uuid": "85c1bd00-dac4-4383-a541-4acbb653eb35"
            },
            "obsType": "OUTLIER_NUMERICAL"
        },
        {
            "id": 222091,
            "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
            "runId": "2025-01-12T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey": "TIixwf7bWSOfvO3YZsi1+6Wtr7zAIHfXHHp9KQ4NAX7MD5yY3mV/jX+Dt/vFVT8R",
            "outColumn": "time_in_service_yrs",
            "outValue": "6.95",
            "obsSubType": "NUMERICAL",
            "outMedian": "3.14",
            "outCount": 1,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 6.289479176,
            "confidence": 90,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 764040,
                "uuid": "4b13b2c0-73c0-4f1b-99c1-f5b4ed36443d"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}

PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_DATA = [
    {
        "seqno": 9912410,
        "updts": "2024-09-01T13:23:39.870+0000",
        "job_uuid": "f4908e6b-a6fe-41ad-bd48-f572e38482e7",
        "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-09-01T00:00:00.000+0000",
        "id": 1637,
        "key_column": None,
        "key_value": None,
        "value_column": "time_in_service_yrs",
        "value": "110.9100",
        "date_value": None,
        "type": "NUMERICAL",
        "median": "3.1447",
        "lb": 0.0,
        "ub": 6.289479176,
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
        "seqno": 9912411,
        "updts": "2024-09-01T13:23:39.870+0000",
        "job_uuid": "f4908e6b-a6fe-41ad-bd48-f572e38482e7",
        "dataset": PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_DATASET,
        "run_id": "2024-09-01T00:00:00.000+0000",
        "id": 1637,
        "key_column": None,
        "key_value": None,
        "value_column": "time_in_service_yrs",
        "value": "6.9500",
        "date_value": None,
        "type": "NUMERICAL",
        "median": "3.1447",
        "lb": 0.0,
        "ub": 6.289479176,
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

PD_TRINO_OUTLIERS_NUM_NOKEY_NODATE_EMPLOYEES_ARCHIVE_BREAKS_EXPECTED_QUERY_RESULT = [
    {
        "id": 1637,
        "value_column": "time_in_service_yrs",
        "employee_id": "51",
        "first_name": "Anne",
        "last_name": "Balsdon",
        "email": "abalsdon1e@eepurl.com",
        "gender": "Male",
        "city": "Charlotte",
        "department": "Product Management",
        "latitude": "35.26",
        "longitude": "-80.8042",
        "home_phone": "704-414-0164",
        "postal_code": "28225",
        "state": "NC",
        "street_address": "4 Tomscot Junction",
        "date_of_hire": "12/23/1910",
        "time_in_service_yrs": 110.91
    },
    {
        "id": 1637,
        "value_column": "time_in_service_yrs",
        "employee_id": "8",
        "first_name": "Christa",
        "last_name": "Krollman",
        "email": "ckrollman7@geocities.jp",
        "gender": "Female",
        "city": "Columbia",
        "department": "Research and Development",
        "latitude": "34.0635",
        "longitude": "-81.0265",
        "home_phone": "803-188-7333",
        "postal_code": "29203",
        "state": "SC",
        "street_address": "766 Mosinee Lane",
        "date_of_hire": "11/11/2014",
        "time_in_service_yrs": 6.95
    }
]
