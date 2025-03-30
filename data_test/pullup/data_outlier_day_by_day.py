# pylint: disable-msg=import-error
from payloads.pullup.pl_outliers_day_by_day import (
    DS_DEFS_OUTLIER_DAY_BY_DAY,
    DS_DEFS_OUTLIER_DAY_BY_DAY_RUN_ID_FULL,
)

EXPECTED_DATA_OUTLIERS_DAY_BY_DAY = {
    "data": [
        {
            "id": 1614,
            "dataset": DS_DEFS_OUTLIER_DAY_BY_DAY["dataset"],
            "runId": DS_DEFS_OUTLIER_DAY_BY_DAY_RUN_ID_FULL,
            "outKeyColumn": "SYMBOL",
            "outKey": "TbAzQX5mB4lJ0xMDy5YbNZT5/yVyNVTR2ClcG0lp35mCbhUo/nCftlBqf+BCP1oZ",
            "outColumn": "CLOSE",
            "outValue": "0.68",
            "obsSubType": "NUMERICAL",
            "outMedian": "1.12",
            "outCount": 1,
            "keyArr": [
                "KOD.W"
            ],
            "lb": 0.728,
            "ub": 1.5120000000000002,
            "confidence": 93,
            "owlRank": 0,
            "linkId": "",
            "linkIdArr": [
                ""
            ],
            "assignmentId": {
                "id": 5073,
                "uuid": "f25675c9-4309-4339-a975-073d8332a404"
            },
            "obsType": "OUTLIER_NUMERICAL"
        }
    ]
}
