from utils.constants import PROD_RUN_ID

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_CONNECTION = "APPROVED_SNOWFLAKE_PUSHDOWN"
PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET = (
    "AUTO_PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS"
)

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET,
    "colMatch": {},
    "transforms": [],
    "jobId": {
        "id": -1
    },
    "host": "10.64.2.3:5432/rc202309?currentSchema=validation",
    "hootOnly": False,
    "logLevel": "INFO",
    "outliers": [],
    "patterns": [],
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": False,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": False,
        "behaviorEmptyCheck": False,
        "behaviorUniqueCheck": False,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shape": True,
        "shapeSensitivity": 0.007,
        "shapeMaxPerCol": 46,
        "shapeMaxColSize": 43,
        "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET,
        "shapeGranular": True,
        "correlation": False,
        "histogram": False,
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
    "pushdown": {
        "connectionName": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_CONNECTION,
        "maxConnections": 10,
        "sourceQuery": "select * from PUBLIC.AUSTIN_CRIME_UNIQUE_KEY",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": True,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "linkId": [
        "unique_key"
    ],
    "user": "gaberosenadmin"
}

PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_SHAPES_SETTINGS = {
    "dataset": PD_SF_SHAPES_GRANULAR_AUSTIN_CRIME_2_ARCHIVE_BREAKS_DATASET,
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
