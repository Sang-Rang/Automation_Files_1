from payloads.pullup.pl_outliers_downtrain_rerun_and_retrain import (
    OUTLIER_DS_NAME,
    RUN_DATE_DOWNTRAIN_FULL,
)

EXPECTED_OUTLIER_BEFORE_DOWNTRAIN = {
    "data": [
        {
            "id": 9571,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "Z0uyxjPBT8gbcUwKe2he1Xcz4NLtlePWXJWMeniO6CRivGU1PoSFkZrATzqZ0AMM",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "10.0",
            "outCount": 1,
            "keyArr": ["JHD"],
            "lb": 6.499999999999999,
            "ub": 13.5,
            "confidence": 0,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29341, "uuid": "9502b6dc-abbd-4060-8485-3c1522e125bd"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9572,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "O8NaQp7bO2/PeR9XePcm0CAW+N7Q9ho5O8DqE2TpEdacgvePjs1U8g07cqJZZK68",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "17.86",
            "outCount": 1,
            "keyArr": ["CS"],
            "lb": 11.608999999999998,
            "ub": 24.111,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29342, "uuid": "70b6fcfa-cc75-4e1b-9b2d-7dc97bac35de"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9573,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "AeIDsheZxAN6CDpGvPT1wkCS3p+F5hNjdDIeiu4x+H1NAN5e2OIq4lEAX83REtSv",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "33.29",
            "outCount": 1,
            "keyArr": ["HUN"],
            "lb": 21.638499999999997,
            "ub": 44.941500000000005,
            "confidence": 2,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29343, "uuid": "d1d2a48b-b8c5-48b6-a3b8-29b8f1f80ef6"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9574,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "XvaxMdb4r7B/K17ukhthyJuXpMOVV6J1iQOZjZHEiJrJgt/XQxhENDKBR4XLXeuC",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "89.15",
            "outCount": 1,
            "keyArr": ["HUBS"],
            "lb": 53.75000000000001,
            "ub": 120.35250000000002,
            "confidence": 6,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29344, "uuid": "8283bbbc-5f57-49da-aed1-4f7db490ce00"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9575,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "4gWqaMP/zcPpPpOt9a3Nk3Rrc2iZK2O2eY8vVKrzWTl+QPjH4z1vWAsAzh1WVRKG",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "135.17",
            "outCount": 1,
            "keyArr": ["HUBB"],
            "lb": 87.86049999999997,
            "ub": 182.4795,
            "confidence": 10,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29345, "uuid": "fab33fec-d4ff-4026-b9b8-a0f99c2ee523"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9576,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "XLV53G0131vEl2IWpzxHwjzrWeAg97R6hIoBYqtNCmZ9lC/gxZfsUYJgmmRm4CHn",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "253.34",
            "outCount": 1,
            "keyArr": ["HUM"],
            "lb": 164.671,
            "ub": 342.009,
            "confidence": 19,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29346, "uuid": "c596dd0f-a122-4a0f-b579-cfd92e678406"},
            "obsType": "OUTLIER_NUMERICAL",
        },
    ]
}

EXPECTED_OUTLIER_AFTER_DOWNTRAIN = {
    "data": [
        {
            "id": 9572,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "We/K1fvukXNUkLJ+PyvPnUbtoBV8GG7gnxNrOY5qTBAT9mbJImNYrnkxBUOelVNg",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "17.86",
            "outCount": 1,
            "keyArr": ["CS"],
            "lb": 11.608999999999998,
            "ub": 24.111,
            "confidence": 1,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29342, "uuid": "70b6fcfa-cc75-4e1b-9b2d-7dc97bac35de"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9573,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "F0HNKXNaWz8wWYPSo4YGTaZXODk4Cs+ug7pYl3RHmNYW2d6baX4m6+VUUMg28v1M",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "33.29",
            "outCount": 1,
            "keyArr": ["HUN"],
            "lb": 21.638499999999997,
            "ub": 44.941500000000005,
            "confidence": 2,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29343, "uuid": "d1d2a48b-b8c5-48b6-a3b8-29b8f1f80ef6"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9574,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "HyogpT63PZkaDqWfAABgqDrqnqGaCQdj8B52ag4zplQIhc1kbzkcO0a0+FIGImug",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "89.15",
            "outCount": 1,
            "keyArr": ["HUBS"],
            "lb": 53.75000000000001,
            "ub": 120.35250000000002,
            "confidence": 6,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29344, "uuid": "8283bbbc-5f57-49da-aed1-4f7db490ce00"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9575,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "pdqT4X278vM9+OBCMhNodKEGp50YpVxLbsXXjatHSSRHfil7W9VcZdF2jHG3el/N",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "135.17",
            "outCount": 1,
            "keyArr": ["HUBB"],
            "lb": 87.86049999999997,
            "ub": 182.4795,
            "confidence": 10,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29345, "uuid": "fab33fec-d4ff-4026-b9b8-a0f99c2ee523"},
            "obsType": "OUTLIER_NUMERICAL",
        },
        {
            "id": 9576,
            "dataset": OUTLIER_DS_NAME,
            "runId": RUN_DATE_DOWNTRAIN_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "5nz1YKhDeVr97r/mwLcDfQxasyTq+XhgyHAnVyqdCiC53UdvzibL+qUua2hcHqeg",
            "outColumn": "CLOSE",
            "outValue": "1800.0",
            "obsSubType": "NUMERICAL",
            "outMedian": "253.34",
            "outCount": 1,
            "keyArr": ["HUM"],
            "lb": 164.671,
            "ub": 342.009,
            "confidence": 19,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [""],
            "assignmentId": {"id": 29346, "uuid": "c596dd0f-a122-4a0f-b579-cfd92e678406"},
            "obsType": "OUTLIER_NUMERICAL",
        },
    ]
}
