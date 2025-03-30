from payloads.pushdown.outliers.pl_pd_sf_outliers_cat_nokey_nodate_nyse import (
    PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
)

PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 51823,
            "dataset": PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "Wz8aimCzaip8thJ+n651g4IHTiywpNe5EPqmrmo9EcVzgsayip17g24yHw35zY7X",
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
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 299352,
                "uuid": "997037c4-a811-4a4f-bd8e-f4fda1907876"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 51822,
            "dataset": PD_SF_OUTLIERS_CAT_NOKEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "",
            "outKey":
                "LW6Ubr/NVyUEAER4G8+KFDwOcouSr+rS8lb8Rb8IVs24da+dtM4GAQ0y8nNRQgRz",
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
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 299351,
                "uuid": "ad5dfe82-665b-48ab-b182-0edd069cdbfc"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
