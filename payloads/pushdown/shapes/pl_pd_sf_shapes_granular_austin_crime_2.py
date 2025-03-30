from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET = "AUTO_PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2"

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": PROD_HOST,
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": True,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shapeSensitivity": 0.007,
        "shapeMaxPerCol": 46,
        "shapeMaxColSize": 43,
        "shape": True,
        "shapeGranular": True,
        "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
        "pushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ],
        "profilePushDown": [
            "count",
            "distinct",
            "mean",
            "minmax",
            "quality"
        ]
    },
    "alertEmail": "",
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "pushdown": {
        "connectionName": "APPROVED_SNOWFLAKE_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.AUSTIN_CRIME_UNIQUE_KEY",
        "backRuns": 0,
        "backRunBin": "DAY",
        "threads": 2,
        "key": ""
    },
    "user": BASE_CREDS["username"]
}

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS = {
    "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
    "dataShapeSensitivity": 0.007,
    "dataShapeMaxPerCol": 46,
    "dataShapeMaxColSize": 43,
    "dataShapeColInclusion[unique_key]": 1,
    "dataShapeColType[unique_key]": "NUMBER",
    "dataShapeColInclusion[address]": 1,
    "dataShapeColType[address]": "VARCHAR",
    "dataShapeColInclusion[census_tract]": 1,
    "dataShapeColType[census_tract]": "DOUBLE",
    "dataShapeColInclusion[clearance_date]": 1,
    "dataShapeColType[clearance_date]": "Date",
    "dataShapeColInclusion[clearance_status]": 1,
    "dataShapeColType[clearance_status]": "VARCHAR",
    "dataShapeColInclusion[council_district_code]": 1,
    "dataShapeColType[council_district_code]": "NUMBER",
    "dataShapeColInclusion[description]": 1,
    "dataShapeColType[description]": "VARCHAR",
    "dataShapeColInclusion[district]": 1,
    "dataShapeColType[district]": "VARCHAR",
    "dataShapeColInclusion[latitude]": 1,
    "dataShapeColType[latitude]": "DOUBLE",
    "dataShapeColInclusion[longitude]": 1,
    "dataShapeColType[longitude]": "DOUBLE",
    "dataShapeColInclusion[location]": 1,
    "dataShapeColType[location]": "VARCHAR",
    "dataShapeColInclusion[location_description]": 1,
    "dataShapeColType[location_description]": "VARCHAR",
    "dataShapeColInclusion[primary_type]": 1,
    "dataShapeColType[primary_type]": "VARCHAR",
    "dataShapeColInclusion[timestamp]": 1,
    "dataShapeColType[timestamp]": "Date",
    "dataShapeColInclusion[x_coordinate]": 1,
    "dataShapeColType[x_coordinate]": "NUMBER",
    "dataShapeColInclusion[y_coordinate]": 1,
    "dataShapeColType[y_coordinate]": "NUMBER",
    "dataShapeColInclusion[year]": 1,
    "dataShapeColType[year]": "NUMBER",
    "dataShapeColInclusion[zipcode]": 1,
    "dataShapeColType[zipcode]": "VARCHAR"
}
