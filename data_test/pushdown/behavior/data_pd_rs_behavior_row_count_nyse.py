from payloads.pushdown.behavior.pl_pd_rs_behavior_row_count_nyse import (
    PD_RS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
)

PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_TABLE_STATS = {
    "dataset": PD_RS_BEHAVIOR_ROW_COUNT_NYSE_DATASET,
    "runId": "2018-01-13 00:00:00",
    "runDate": "2018-01-13T00:00:00.000+0000",
    "rows": 0,
    "passFail": 0,
    "passFailLimit": 75,
    "peak": 1,
    "dayOfWeek": "Sat",
    "timeZone": "UTC",
    "avgRows": 0,
    "cols": 9,
    "activeRules": 0,
    "activeAlerts": 0,
    "runTime": "00:00:07",
    "dqItems": {
        "Row Count__ROW_COUNT": {
            "key": "Row Count__ROW_COUNT",
            "name": "Row Count",
            "stndDev": 0.0,
            "zscore": 6.0,
            "mean": 3105.0,
            "value": 0.0,
            "score": 30,
            "perChange": -100.0,
            "deltaPerChange": "NaN",
            "verbose": "Row Count deviation from observed range",
            "type": "ROW_COUNT",
            "linkId": "",
            "dqType": "ROW",
            "lbAbs": 2670.3,
            "ubAbs": 3539.7,
            "lbZscore": None,
            "ubZscore": None,
            "rangeChart": [
                0.0,
                2670.3,
                3539.7,
                3670.1099999999997
            ],
            "chartType": "ABSOLUTE",
            "chartHistory": None,
            "chartHistoryRange": None,
            "chartHistoryPassFail": None,
            "chartHistoryPassFailString": None,
            "chartHistoryMean": [],
            "passFail": 1,
            "isManual": False,
            "isRootCause": False,
            "status": "Breaking",
            "adaptiveTier": None,
            "assignmentId": {
                "id": 4504,
                "uuid": "3837af9e-5a1e-459a-b242-48300fb9b549"
            },
            "neverNegative": False
        }
    },
    "datashapes": [],
    "observations": [],
    "outliers": [],
    "validateSrc": [],
    "sources": [],
    "patterns": [],
    "rules": [],
    "alerts": [],
    "dupes": [],
    "shapeScore": 0,
    "dupeScore": 0,
    "patternScore": 0,
    "outlierScore": 0,
    "schemaScore": 0,
    "recordScore": 0,
    "ruleScore": 0,
    "sourceScore": 0,
    "behaviorScore": 30,
    "prettyPrint": True,
    "runDateStr": "2018-01-13 00:00:00",
    "score": 70
}

PD_RS_BEHAVIOR_ROW_COUNT_NYSE_EXPECTED_ROW_COUNT_DETAILS = {
    "key": "Row Count__ROW_COUNT",
    "name": "Row Count",
    "stndDev": 0.0,
    "zscore": 6.0,
    "mean": 3105.0,
    "value": 0.0,
    "score": 30,
    "perChange": -100.0,
    "deltaPerChange": "NaN",
    "verbose": "Row Count deviation from observed range",
    "type": "ROW_COUNT",
    "linkId": "",
    "dqType": "ROW",
    "lbAbs": 2670.0,
    "ubAbs": 3540.0,
    "lbZscore": None,
    "ubZscore": None,
    "rangeChart": [
        0.0,
        2670.0,
        3540.0,
        3670.5
    ],
    "chartType": "ABSOLUTE",
    "chartHistory": [
        [
            1515369600000,
            3106.0
        ],
        [
            1515456000000,
            3105.0
        ],
        [
            1515542400000,
            3107.0
        ],
        [
            1515628800000,
            3104.0
        ],
        [
            1515715200000,
            3100.0
        ],
        [
            1515801600000,
            0.0
        ]
    ],
    "chartHistoryRange": [
        [
            1515542400000,
            3079.0,
            3132.0
        ],
        [
            1515628800000,
            3102.0,
            3135.0
        ],
        [
            1515715200000,
            3100.0,
            3136.0
        ],
        [
            1515801600000,
            3100.0,
            3136.0
        ]
    ],
    "chartHistoryPassFail": [],
    "chartHistoryPassFailString": [
        [
            1515369600000,
            "P"
        ],
        [
            1515456000000,
            "P"
        ],
        [
            1515542400000,
            "P"
        ],
        [
            1515628800000,
            "P"
        ],
        [
            1515715200000,
            "P"
        ],
        [
            1515801600000,
            "F"
        ]
    ],
    "chartHistoryMean": [
        [
            1515369600000,
            None
        ],
        [
            1515456000000,
            None
        ],
        [
            1515542400000,
            None
        ],
        [
            1515628800000,
            None
        ],
        [
            1515715200000,
            None
        ],
        [
            1515801600000,
            3105.0
        ]
    ],
    "passFail": 0,
    "isManual": False,
    "isRootCause": False,
    "status": "Breaking",
    "adaptiveTier": None,
    "assignmentId": {
        "id": 4504,
        "uuid": "3837af9e-5a1e-459a-b242-48300fb9b549"
    },
    "neverNegative": False
}
