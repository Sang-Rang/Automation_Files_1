from utils.constants import BASE_CREDS, PROD_HOST, PROD_RUN_ID

PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_DATASET = "AUTO_PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME"

PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_DATASET,
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
    "agentId": {
        "id": 0,
        "uuid": ""
    },
    "profile": {
        "on": True,
        "only": False,
        "behaviorScoreOff": False,
        "behaviorRowCheck": True,
        "behaviorTimeCheck": False,
        "behaviorMinValueCheck": False,
        "behaviorMaxValueCheck": False,
        "behaviorMeanValueCheck": False,
        "behaviorNullCheck": True,
        "behaviorEmptyCheck": True,
        "behaviorUniqueCheck": True,
        "behaviorLookback": 10,
        "behaviorMinSupport": 4,
        "profileStringLength": False,
        "shape": True,
        "shapeSensitivity": 3.506,
        "shapeMaxPerCol": 46,
        "shapeMaxColSize": 43,
        "shapeGranular": True,
        "dataset": PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_DATASET,
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
        "connectionName": "APPROVED_BIGQUERY_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from samples.austin_crime",
        "backRuns": 0,
        "backRunBin": "DAY",
        "sourceBreakDupes": False,
        "sourceBreakOutliers": False,
        "sourceBreakRules": False,
        "sourceBreakShapes": False,
        "threads": 2,
        "key": "",
        "sqlLoggingToggle": False
    },
    "user": BASE_CREDS["username"]
}

PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_SHAPES_SETTINGS = {
    "dataset": PD_BQ_SHAPES_GRANULAR_AUSTIN_CRIME_DATASET,
    "dataShapeSensitivity": 3.506,
    "dataShapeMaxPerCol": 46,
    "dataShapeMaxColSize": 43,
    "dataShapeColInclusion[unique_key]": 1,
    "dataShapeColType[unique_key]": "INT64",
    "dataShapeColInclusion[address]": 1,
    "dataShapeColType[address]": "STRING",
    "dataShapeColInclusion[census_tract]": 1,
    "dataShapeColType[census_tract]": "FLOAT64",
    "dataShapeColInclusion[clearance_date]": 1,
    "dataShapeColType[clearance_date]": "Date",
    "dataShapeColInclusion[clearance_status]": 1,
    "dataShapeColType[clearance_status]": "STRING",
    "dataShapeColInclusion[council_district_code]": 1,
    "dataShapeColType[council_district_code]": "INT64",
    "dataShapeColInclusion[description]": 1,
    "dataShapeColType[description]": "STRING",
    "dataShapeColInclusion[district]": 1,
    "dataShapeColType[district]": "STRING",
    "dataShapeColInclusion[latitude]": 1,
    "dataShapeColType[latitude]": "FLOAT64",
    "dataShapeColInclusion[longitude]": 1,
    "dataShapeColType[longitude]": "FLOAT64",
    "dataShapeColInclusion[location]": 1,
    "dataShapeColType[location]": "STRING",
    "dataShapeColInclusion[location_description]": 1,
    "dataShapeColType[location_description]": "STRING",
    "dataShapeColInclusion[primary_type]": 1,
    "dataShapeColType[primary_type]": "STRING",
    "dataShapeColInclusion[timestamp]": 1,
    "dataShapeColType[timestamp]": "Date",
    "dataShapeColInclusion[x_coordinate]": 1,
    "dataShapeColType[x_coordinate]": "INT64",
    "dataShapeColInclusion[y_coordinate]": 1,
    "dataShapeColType[y_coordinate]": "INT64",
    "dataShapeColInclusion[year]": 1,
    "dataShapeColType[year]": "INT64",
    "dataShapeColInclusion[zipcode]": 1,
    "dataShapeColType[zipcode]": "STRING"
}
