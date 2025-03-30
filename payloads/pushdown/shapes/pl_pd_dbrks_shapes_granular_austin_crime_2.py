from utils.constants import PROD_RUN_ID

PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET = "AUTO_PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2"

PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_PAYLOAD = {
    "runId": PROD_RUN_ID,
    "dataset": PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
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
        "dataset": PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
        "correlation": False,
        "histogram": False,
        "shapeGranular": True,
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
        "connectionName": "APPROVED_DATABRICKS_PUSHDOWN",
        "maxConnections": 10,
        "sourceQuery": "select * from public.austin_crime_unique_key",
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
    "user": "gaberosenadmin"
}

PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_SHAPES_SETTINGS = {
    "dataset": PD_DBRKS_SHAPES_GRANULAR_AUSTIN_CRIME_2_DATASET,
    "dataShapeSensitivity": 0.007,
    "dataShapeMaxPerCol": 46,
    "dataShapeMaxColSize": 43,
    "dataShapeColInclusion[unique_key]": 1,
    "dataShapeColType[unique_key]": "DECIMAL",
    "dataShapeColInclusion[address]": 1,
    "dataShapeColType[address]": "STRING",
    "dataShapeColInclusion[census_tract]": 1,
    "dataShapeColType[census_tract]": "DOUBLE",
    "dataShapeColInclusion[clearance_date]": 1,
    "dataShapeColType[clearance_date]": "Date",
    "dataShapeColInclusion[clearance_status]": 1,
    "dataShapeColType[clearance_status]": "STRING",
    "dataShapeColInclusion[council_district_code]": 1,
    "dataShapeColType[council_district_code]": "DECIMAL",
    "dataShapeColInclusion[description]": 1,
    "dataShapeColType[description]": "STRING",
    "dataShapeColInclusion[district]": 1,
    "dataShapeColType[district]": "STRING",
    "dataShapeColInclusion[latitude]": 1,
    "dataShapeColType[latitude]": "DOUBLE",
    "dataShapeColInclusion[longitude]": 1,
    "dataShapeColType[longitude]": "DOUBLE",
    "dataShapeColInclusion[location]": 1,
    "dataShapeColType[location]": "STRING",
    "dataShapeColInclusion[location_description]": 1,
    "dataShapeColType[location_description]": "STRING",
    "dataShapeColInclusion[primary_type]": 1,
    "dataShapeColType[primary_type]": "STRING",
    "dataShapeColInclusion[timestamp]": 1,
    "dataShapeColType[timestamp]": "Date",
    "dataShapeColInclusion[x_coordinate]": 1,
    "dataShapeColType[x_coordinate]": "DECIMAL",
    "dataShapeColInclusion[y_coordinate]": 1,
    "dataShapeColType[y_coordinate]": "DECIMAL",
    "dataShapeColInclusion[year]": 1,
    "dataShapeColType[year]": "DECIMAL",
    "dataShapeColInclusion[zipcode]": 1,
    "dataShapeColType[zipcode]": "STRING"
}
