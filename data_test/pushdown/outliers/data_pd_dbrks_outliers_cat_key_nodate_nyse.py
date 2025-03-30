from payloads.pushdown.outliers.pl_pd_dbrks_outliers_cat_key_nodate_nyse import (
    PD_DBRKS_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
)

PD_DBRKS_OUTLIERS_CAT_KEY_NODATE_NYSE_EXPECTED_OUTLIERS = {
    "data": [
        {
            "id": 51829,
            "dataset": PD_DBRKS_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "EXCH",
            "outKey":
                "lHPEZHCD6OrR7QNrpk2d/nd9XrzRn0AEMk0y2XxTvVVHjPnOINmcqBNPVfhH1Nne",
            "outColumn": "SYMBOL",
            "outValue": "LBRT",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 2,
            "keyArr": [
                "NYSE"
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
                "id": 299358,
                "uuid": "a3e18720-ce22-4414-8ff8-245490ee10d2"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        },
        {
            "id": 51828,
            "dataset": PD_DBRKS_OUTLIERS_CAT_KEY_NODATE_NYSE_DATASET,
            "runId": "2023-07-11T00:00:00.000+0000",
            "outKeyColumn": "EXCH",
            "outKey":
                "Zc60KPZt0KlQceYkMZmu3Ftl1851gBYlA/smLZ0kHvPULLKr2i1aj1PAfOwH0Aht",
            "outColumn": "SYMBOL",
            "outValue": "SRE-A",
            "obsSubType": "CATEGORICAL",
            "outMedian": "INVALID",
            "outCount": 3,
            "keyArr": [
                "NYSE"
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
                "id": 299357,
                "uuid": "1f47ceb2-02e0-447d-8c76-b1771318a3a1"
            },
            "obsType": "OUTLIER_CATEGORICAL"
        }
    ]
}
