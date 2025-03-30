from datetime import datetime, timedelta
# pylint: disable-msg=import-error
from utils.constants import PROD_AGENT_ID

CONNECTION = "APPROVED_ATHENA_UP"
DATASET = "AUTO_ATHENA_PULSESCHEDULE"
QUERY = "select * from default.aclaims_master"

# Additional Filter options and category names
NM_BUSINESS_UNIT = "bizUnit"
NM_SERIES = "series"
NM_SCHEDULED = "scheduled"

# Data
DATA_LOOK_BACK = [
    {
        "timeRange": 9,
        "time": (datetime.now() - timedelta(9)).strftime("%Y-%m-%d"),
    },
    {
        "timeRange": 14,
        "time": (datetime.now() - timedelta(14)).strftime("%Y-%m-%d"),
    },
    {
        "timeRange": 30,
        "time": (datetime.now() - timedelta(30)).strftime("%Y-%m-%d"),
    },
    {
        "timeRange": 60,
        "time": (datetime.now() - timedelta(60)).strftime("%Y-%m-%d"),
    },
]

DATA_MODE = ["DRAFT", "PUBLISHED"]

DATA_SCHEDULED = [
    {NM_SCHEDULED: "DAILY", "msg": "FREQ: DAILY"},
    {NM_SCHEDULED: "MONTHLY", "msg": "FREQ: MONTHLY"},
]

# These filters are always required
DATA_DEFAULT_FILTER = {
    "lookback": DATA_LOOK_BACK[0]["timeRange"],
    "lb_time": DATA_LOOK_BACK[0]["time"],
    "runMode": "ALL",
    NM_SCHEDULED: "ALL",
    "showFailed": False,
}

# Hard data
EPOCH_DIVIDE_VALUE = 1000
DATETIME_CONVERT_FORMAT = "%Y-%m-%d"
SEARCH_Y_CAT_STRING = ".*<label class='white'>(.*)</label>.*"
SEARCH_Y_CAT_GROUP = 1

DATA_JOB_SCH_QUERY_ALL = {
    "dataset": DATASET,
    "agentId": PROD_AGENT_ID,
    "scheduledRunTime": "00:00:00",
    "runDateFmt": "yyyy-MM-dd",
    "active": 1,
    "offset": 0,
}

DATA_JOB_SCH_QUERY_DAILY = DATA_JOB_SCH_QUERY_ALL.copy()
DATA_JOB_SCH_QUERY_DAILY.update(
    {
        "dom": 0,
        "mon": 0,
        "tue": 0,
        "wed": 0,
        "thu": 0,
        "fri": 0,
        "sat": 0,
        "sun": 7,
        "freq": "DAILY",
        "qDay": 0,
    }
)

DATA_JOB_SCH_QUERY_MONTHLY = DATA_JOB_SCH_QUERY_ALL.copy()
DATA_JOB_SCH_QUERY_MONTHLY.update(
    {
        "dom": 1,
        "mon": 0,
        "tue": 0,
        "wed": 0,
        "thu": 0,
        "fri": 0,
        "sat": 0,
        "sun": 0,
        "offset": "",
        "freq": "MONTHLY",
        "qDay": 0,
    }
)
