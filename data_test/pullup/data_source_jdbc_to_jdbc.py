SOURCE_COUNT_EXPECTED = {
    "targetRowCount": 10,
    "sourceRowCount": 7,
    "targetColCount": 5,
    "sourceColCount": 5,
    "data": [
        {
            "countType": "Dataset Row Count",
            "targetCount": 10,
            "sourceCount": 7,
            "change": 3,
            "percChange": 42.86,
            "assignmentId": {"id": "", "uuid": ""},
            "description": "The row size does not match. Source has 7 rows. Target has 10 rows. "
            "Source-to-target difference: 3 (+42.86%)",
        }
    ],
}

SOURCE_SCHEMA_EXPECTED = {
    "colOrderPassing": True,
    "percMatching": 80,
    "percPassing": 80,
    "checkType": True,
    "checkCase": False,
    "checkColOrder": False,
    "targetToSourceMap": "email=email_address|last_name=last_namez|first_name=first_namez",
    "colOrderAssignmentId": None,
    "colOrderTarget": "id=0|first_name=1|last_name=2|gender=3|email=4",
    "colOrderSource": "id=0|first_namez=1|last_namez=2|email_address=3|GENDER=4",
    "data": [
        {
            "targetColNm": "id",
            "targetColType": "integer",
            "targetColOrder": "1",
            "sourceColNm": "id",
            "sourceColType": "integer",
            "sourceColOrder": "1",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False,
        },
        {
            "targetColNm": "first_name",
            "targetColType": "string",
            "targetColOrder": "2",
            "sourceColNm": "first_namez",
            "sourceColType": "string",
            "sourceColOrder": "2",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False,
        },
        {
            "targetColNm": "last_name",
            "targetColType": "string",
            "targetColOrder": "3",
            "sourceColNm": "last_namez",
            "sourceColType": "string",
            "sourceColOrder": "3",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False,
        },
        {
            "targetColNm": "gender",
            "targetColType": "string",
            "targetColOrder": "4",
            "sourceColNm": "GENDER",
            "sourceColType": "integer",
            "sourceColOrder": "5",
            "matchLevel": 4,
            "itemLabel": "Failing",
            "passStatus": 4,
            "assignmentId": {"id": "", "uuid": ""},
            "description": "The target column [gender] (type: string) does not match source column "
            "[GENDER] (type: integer)",
            "obsSubType": "SCHEMA_TYPE",
            "inferredTargetColNm": False,
        },
        {
            "targetColNm": "email",
            "targetColType": "string",
            "targetColOrder": "5",
            "sourceColNm": "email_address",
            "sourceColType": "string",
            "sourceColOrder": "4",
            "matchLevel": 2,
            "itemLabel": "Passing",
            "passStatus": 2,
            "assignmentId": None,
            "description": "",
            "obsSubType": "",
            "inferredTargetColNm": False,
        },
    ],
}

SOURCE_VALUE_EXPECTED = {
    "checkValues": True,
    "validateValuesTrim": False,
    "validateValuesShowMissingKeys": False,
    "countRowMismatch": 10,
    "countRowTotal": 10,
    "percRowMatch": 0,
    "countColumnShift": 1,
    "colIssueCountMap": "gender=10",
    "data": [
        {
            "id": 0,
            "obsSubType": "VALUE_EXACT",
            "system": "Target (Mysql)",
            "key": ["8"],
            "column": "first_name",
            "value": ["Cyril"],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None,
        },
        {
            "id": 0,
            "obsSubType": "VALUE_EXACT",
            "system": "Source (Postgres)",
            "key": ["8"],
            "column": "first_namez",
            "value": ["null"],
            "passStatus": 1,
            "assignmentId": {"id": 109684, "uuid": "ca8caea1-b3da-4b96-b176-eada80d5c74b"},
            "description": "target column [first_name] value does not match source column "
            "[first_namez] value: [Cyril] vs [null]",
            "count": 1,
        },
        {
            "id": 1,
            "obsSubType": "VALUE_EXACT",
            "system": "Target (Mysql)",
            "key": ["9"],
            "column": "email",
            "value": ["ecosgriff8@bloglines.com"],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None,
        },
        {
            "id": 1,
            "obsSubType": "VALUE_EXACT",
            "system": "Source (Postgres)",
            "key": ["9"],
            "column": "email_address",
            "value": ["null"],
            "passStatus": 1,
            "assignmentId": {"id": 109685, "uuid": "ece71189-2b73-43d6-a1b3-2cab9d959ac4"},
            "description": "target column [email] value does not match source column "
            "[email_address] value: [ecosgriff8@bloglines.com] vs [null]",
            "count": 1,
        },
        {
            "id": 2,
            "obsSubType": "VALUE_EXACT",
            "system": "Target (Mysql)",
            "key": ["10"],
            "column": "first_name",
            "value": ["Zeke"],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None,
        },
        {
            "id": 2,
            "obsSubType": "VALUE_EXACT",
            "system": "Source (Postgres)",
            "key": ["10"],
            "column": "first_namez",
            "value": ["null"],
            "passStatus": 1,
            "assignmentId": {"id": 109686, "uuid": "7d3717e6-2bdb-4cfc-a1e6-8a7ccefe4a90"},
            "description": "target column [first_name] value does not match source column "
            "[first_namez] value: [Zeke] vs [null]",
            "count": 1,
        },
        {
            "id": 3,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Target (Mysql)",
            "key": ["6"],
            "column": "gender",
            "value": ["Non-binary"],
            "passStatus": 4,
            "assignmentId": None,
            "description": "",
            "count": None,
        },
        {
            "id": 3,
            "obsSubType": "VALUE_THRESHOLD",
            "system": "Source (Postgres)",
            "key": ["6"],
            "column": "GENDER",
            "value": ["4"],
            "passStatus": 1,
            "assignmentId": {"id": 109687, "uuid": "c5ca292f-e756-431c-8032-35845fc1fd53"},
            "description": "More than 90% of target column [gender] values do not match source "
            "column [GENDER] value. For example: [Non-binary] vs [4]",
            "count": 1,
        },
    ],
    "dataOld": {
        "columns": [
            {"title": "id", "name": "id", "data": "id"},
            {"title": "system", "name": "system", "data": "system"},
            {"title": "key", "name": "key", "data": "key"},
            {"title": "column", "name": "column", "data": "column"},
            {"title": "value", "name": "value", "data": "value"},
            {"title": "passStatus", "name": "passStatus", "data": "passStatus"},
            {"title": "assignmentId", "name": "assignmentId", "data": "assignmentId"},
        ],
        "data": [
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Source (Postgres)",
                "passStatus": 1,
                "column": "first_namez",
                "count": 1,
                "description": "target column [first_name] value does not match source column "
                "[first_namez] value: [Cyril] vs [null]",
                "id": 0,
                "value": ["null"],
                "assignmentId": {"id": 109684, "uuid": "ca8caea1-b3da-4b96-b176-eada80d5c74b"},
                "key": ["8"],
            },
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Target (Mysql)",
                "passStatus": 4,
                "column": "first_name",
                "count": None,
                "description": "",
                "id": 0,
                "value": ["Cyril"],
                "assignmentId": None,
                "key": ["8"],
            },
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Source (Postgres)",
                "passStatus": 1,
                "column": "email_address",
                "count": 1,
                "description": "target column [email] value does not match source column "
                "[email_address] value: [ecosgriff8@bloglines.com] vs [null]",
                "id": 1,
                "value": ["null"],
                "assignmentId": {"id": 109685, "uuid": "ece71189-2b73-43d6-a1b3-2cab9d959ac4"},
                "key": ["9"],
            },
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Target (Mysql)",
                "passStatus": 4,
                "column": "email",
                "count": None,
                "description": "",
                "id": 1,
                "value": ["ecosgriff8@bloglines.com"],
                "assignmentId": None,
                "key": ["9"],
            },
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Source (Postgres)",
                "passStatus": 1,
                "column": "first_namez",
                "count": 1,
                "description": "target column [first_name] value does not match source column "
                "[first_namez] value: [Zeke] vs [null]",
                "id": 2,
                "value": ["null"],
                "assignmentId": {"id": 109686, "uuid": "7d3717e6-2bdb-4cfc-a1e6-8a7ccefe4a90"},
                "key": ["10"],
            },
            {
                "obsSubType": "VALUE_EXACT",
                "system": "Target (Mysql)",
                "passStatus": 4,
                "column": "first_name",
                "count": None,
                "description": "",
                "id": 2,
                "value": ["Zeke"],
                "assignmentId": None,
                "key": ["10"],
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Source (Postgres)",
                "passStatus": 1,
                "column": "GENDER",
                "count": 1,
                "description": "More than 90% of target column [gender] values do not match "
                "source column [GENDER] value. For example: [Non-binary] vs [4]",
                "id": 3,
                "value": ["4"],
                "assignmentId": {"id": 109687, "uuid": "c5ca292f-e756-431c-8032-35845fc1fd53"},
                "key": ["6"],
            },
            {
                "obsSubType": "VALUE_THRESHOLD",
                "system": "Target (Mysql)",
                "passStatus": 4,
                "column": "gender",
                "count": None,
                "description": "",
                "id": 3,
                "value": ["Non-binary"],
                "assignmentId": None,
                "key": ["6"],
            },
        ],
    },
}
