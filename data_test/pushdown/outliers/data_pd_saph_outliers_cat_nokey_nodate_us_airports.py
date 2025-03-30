from payloads.pushdown.outliers.pl_pd_saph_outliers_cat_nokey_nodate_us_airports import (
    PD_SAPH_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
)

PD_SAPH_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 16730,
            "dataset": PD_SAPH_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2023-06-24T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "X3YEeESVUsceVY4CKhs324Js11tuhGsY/qD1Nnn6ZA7/HmGVhZuBZC7DpeBBNLT5",
            "outColumn": "AIRPORT_TYPE",
            "outValue": "Balloonport",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 14,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 72850,
                "uuid": "df93ef59-9bcd-43ff-bb31-9f5c1f8246dc"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 16729,
            "dataset": PD_SAPH_OUTLIERS_CAT_NOKEY_NODATE_US_AIRPORTS_DATASET,
            "runId": "2023-06-24T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "MU37eAZ2XTQzCxNQcORkRIdRTKOV2v6SED74JRwd/SvYzB/YwjwCzEIO85HJWgHU",
            "outColumn": "AIRPORT_TYPE",
            "outValue": "Gliderport",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 35,
            "keyArr": [
                ""
            ],
            "lb": 0.0,
            "ub": 0.0,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 72849,
                "uuid": "a3249e1e-4a4a-4269-8220-1266929be8d5"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
