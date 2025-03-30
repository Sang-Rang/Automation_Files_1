from datetime import datetime

# Multiple tests
TODAY = datetime.today()
TODAY_FORMAT = TODAY.strftime("%Y-%m-%d")
DATASET_DEMO_BLOCKS = "AUTO_SNOWFLAKE_SCH_JOB"
CONNECTION_DEMO_BLOCKS = "APPROVED_SNOWFLAKE_UP"
QUERY_DEMO_BLOCKS = "select * from PUBLIC.ACCOUNTS"
SCH_RES_HOUR_START = "07"
SCH_RES_HOUR_START_FULL = f"{SCH_RES_HOUR_START}:00:00.000+0000"
SCH_RES_HOUR_END = "08"
SCH_RES_HOUR_END_FULL = f"{SCH_RES_HOUR_END}:00:00.000+0000"
SCH_TYPE = "7"  # Sunday

# test_demo_blocks_schedule_job_save
SCH_DATA_DEMO_BLOCKS = {
    "agentId": 0,
    "dataset": DATASET_DEMO_BLOCKS,
    "scheduledRunTime": "04:00:00",
    "runDateFmt": "yyyy-MM-dd",
    "freq": "DAILY",
    "dom": "",
    "mon": 0,
    "tue": 0,
    "wed": 0,
    "thu": 0,
    "fri": 0,
    "sat": 1,
    "sun": 0,
    "active": 1,
}
EXP_SCH_DEMO_BLOCKS = {
    "alertWindowInMinutes": 30,
    "dataset": DATASET_DEMO_BLOCKS,
    "agentId": {"id": 0, "uuid": None},
    "updtTs": "2023-10-18T17:12:47.603+0000",
    "scheduledRunTime": SCH_DATA_DEMO_BLOCKS["scheduledRunTime"],
    "runDateFmt": SCH_DATA_DEMO_BLOCKS["runDateFmt"],
    "mon": SCH_DATA_DEMO_BLOCKS["mon"],
    "tue": SCH_DATA_DEMO_BLOCKS["tue"],
    "wed": SCH_DATA_DEMO_BLOCKS["wed"],
    "thu": SCH_DATA_DEMO_BLOCKS["thu"],
    "fri": SCH_DATA_DEMO_BLOCKS["fri"],
    "sat": SCH_DATA_DEMO_BLOCKS["sat"],
    "sun": SCH_DATA_DEMO_BLOCKS["sun"],
    "timeZone": "UTC",
    "active": SCH_DATA_DEMO_BLOCKS["active"],
    "runStatus": None,
    "freq": SCH_DATA_DEMO_BLOCKS["freq"],
    "dom": None,
    "qStart": None,
    "qMonth": None,
    "qDay": None,
    "runOffset": None,
    "late": True,
    "scheduledDays": [1],
}
EXP_SCH_DEMO_BLOCKS_RESET = {
    "alertWindowInMinutes": 30,
    "dataset": None,
    "agentId": None,
    "updtTs": None,
    "scheduledRunTime": "00:00:00",
    "runDateFmt": "yyyy-MM-dd",
    "mon": 1,
    "tue": 2,
    "wed": 3,
    "thu": 4,
    "fri": 5,
    "sat": 6,
    "sun": 7,
    "timeZone": "UTC",
    "active": 0,
    "runStatus": None,
    "freq": "DAILY",
    "dom": None,
    "qStart": None,
    "qMonth": None,
    "qDay": None,
    "runOffset": None,
    "late": True,
    "scheduledDays": [1, 2, 3, 4, 5, 6, 7],
}

# test_schedule_restrictions
SCH_RES_UPDATE_HOUR_START = "08:00:00.000+0000"  # Include leading zeros
SCH_RES_UPDATE_HOUR_END = "09:00:00.000+0000"
PL_SCH_RES_CREATE = {
    "type": SCH_TYPE,
    "startvalue": f"{TODAY_FORMAT} {SCH_RES_HOUR_START}:00:00 GMT",  # Today for audit, weird design
    "endvalue": f"{TODAY_FORMAT} {SCH_RES_HOUR_END}:00:00 GMT",
}
PL_SCH_RES_CREATE_UPDATE = {
    "id": 0,
    "type": SCH_TYPE,
    "startvalue": f"{TODAY_FORMAT} {SCH_RES_UPDATE_HOUR_START}:00:00 GMT",  # Today for audit
    "endvalue": f"{TODAY_FORMAT} {SCH_RES_UPDATE_HOUR_END}:00:00 GMT",
}

# test_schedule_restrictions_job_refused
MSG_RES_REFUSED = (
    "Invalid timeslot selected, check restrictions: java.lang.Exception: "
    "This timeslot is restricted on Sunday"
)
PL_CREATE_RES_REFUSED = {
    "type": SCH_TYPE,
    "startvalue": f"{TODAY_FORMAT} {SCH_RES_HOUR_START}:00:00 GMT",  # Today for audit, weird design
    "endvalue": f"{TODAY_FORMAT} {SCH_RES_HOUR_END}:00:00 GMT",
}
SCH_DATA_RES_REFUSED = {
    "agentId": 0,
    "dataset": DATASET_DEMO_BLOCKS,
    "scheduledRunTime": f"{SCH_RES_HOUR_START}:00:00",
    "runDateFmt": "yyyy-MM-dd",
    "freq": "DAILY",
    "dom": "",
    "mon": 0,
    "tue": 0,
    "wed": 0,
    "thu": 0,
    "fri": 0,
    "sat": 0,
    "sun": 7,
    "active": 0,
}

# test_job_schedule_restrictions_multi_one_day
PL_SCH_RES_CREATE_MULTI = [
    {
        "type": SCH_TYPE,
        "startvalue": f"{TODAY_FORMAT} 07:00:00 GMT",
        "endvalue": f"{TODAY_FORMAT} 08:00:00 GMT",
    },
    {
        "type": SCH_TYPE,
        "startvalue": f"{TODAY_FORMAT} 08:00:00 GMT",
        "endvalue": f"{TODAY_FORMAT} 09:00:00 GMT",
    },
    {
        "type": SCH_TYPE,
        "startvalue": f"{TODAY_FORMAT} 10:00:00 GMT",
        "endvalue": f"{TODAY_FORMAT} 11:00:00 GMT",
    },
    {
        "type": SCH_TYPE,
        "startvalue": f"{TODAY_FORMAT} 13:00:00 GMT",
        "endvalue": f"{TODAY_FORMAT} 14:00:00 GMT",
    },
    {
        "type": SCH_TYPE,
        "startvalue": f"{TODAY_FORMAT} 16:00:00 GMT",
        "endvalue": f"{TODAY_FORMAT} 18:00:00 GMT",
    },
]
EXP_SCH_RES_MULTI = [
    {
        "id": 0,
        "type": SCH_TYPE,
        "start_value": f"{TODAY_FORMAT}T07:00:00.000+0000",
        "end_value": f"{TODAY_FORMAT}T08:00:00.000+0000",
    },
    {
        "id": 0,
        "type": SCH_TYPE,
        "start_value": f"{TODAY_FORMAT}T08:00:00.000+0000",
        "end_value": f"{TODAY_FORMAT}T09:00:00.000+0000",
    },
    {
        "id": 0,
        "type": SCH_TYPE,
        "start_value": f"{TODAY_FORMAT}T10:00:00.000+0000",
        "end_value": f"{TODAY_FORMAT}T11:00:00.000+0000",
    },
    {
        "id": 0,
        "type": SCH_TYPE,
        "start_value": f"{TODAY_FORMAT}T13:00:00.000+0000",
        "end_value": f"{TODAY_FORMAT}T14:00:00.000+0000",
    },
    {
        "id": 0,
        "type": SCH_TYPE,
        "start_value": f"{TODAY_FORMAT}T16:00:00.000+0000",
        "end_value": f"{TODAY_FORMAT}T18:00:00.000+0000",
    },
]
