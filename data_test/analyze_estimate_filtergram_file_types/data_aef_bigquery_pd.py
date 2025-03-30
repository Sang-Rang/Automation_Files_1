WHERE_DATE = "2018-01-06"
TABLE_NAME = "samples.311_service_requests"
COL_NAME = "created_date"
ROW_COUNT = 50
DATASET_NAME = "AUTO_CXN_BQ_PD"
QUERY = f"select * from {TABLE_NAME} where {COL_NAME} > '{WHERE_DATE}' limit {ROW_COUNT}"
CONN_NAME = "APPROVED_BIGQUERY_PUSHDOWN"


PL_DS_RUN_ID = {"dataset": DATASET_NAME, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET_NAME, "runId": WHERE_DATE, "sense": 3}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}
EXP_DAYS_WITH = [
    {"rowcount": 1427, "day_owl_str": "2018-01-06", "day": "2018-01-06"},
    {"rowcount": 1355, "day_owl_str": "2018-01-07", "day": "2018-01-07"},
    {"rowcount": 1485, "day_owl_str": "2018-01-08", "day": "2018-01-08"},
    {"rowcount": 2094, "day_owl_str": "2018-01-09", "day": "2018-01-09"},
    {"rowcount": 1804, "day_owl_str": "2018-01-10", "day": "2018-01-10"},
    {"rowcount": 1760, "day_owl_str": "2018-01-11", "day": "2018-01-11"},
    {"rowcount": 1652, "day_owl_str": "2018-01-12", "day": "2018-01-12"},
    {"rowcount": 1200, "day_owl_str": "2018-01-13", "day": "2018-01-13"},
    {"rowcount": 1244, "day_owl_str": "2018-01-14", "day": "2018-01-14"},
    {"rowcount": 1401, "day_owl_str": "2018-01-15", "day": "2018-01-15"},
    {"rowcount": 1991, "day_owl_str": "2018-01-16", "day": "2018-01-16"},
    {"rowcount": 1857, "day_owl_str": "2018-01-17", "day": "2018-01-17"},
    {"rowcount": 1450, "day_owl_str": "2018-01-18", "day": "2018-01-18"},
    {"rowcount": 1632, "day_owl_str": "2018-01-19", "day": "2018-01-19"},
    {"rowcount": 1173, "day_owl_str": "2018-01-20", "day": "2018-01-20"},
    {"rowcount": 1076, "day_owl_str": "2018-01-21", "day": "2018-01-21"},
    {"rowcount": 1895, "day_owl_str": "2018-01-22", "day": "2018-01-22"},
    {"rowcount": 1843, "day_owl_str": "2018-01-23", "day": "2018-01-23"},
    {"rowcount": 1558, "day_owl_str": "2018-01-24", "day": "2018-01-24"},
    {"rowcount": 4, "day_owl_str": "2018-01-25", "day": "2018-01-25"},
]
EXP_DS_SCAN = {
    "score": 100,
    "rc": ROW_COUNT,
    "passFail": 1,
    "peak": 1,
    "scoreDupe": 0,
    "scoreSource": 0,
    "scoreDatashape": 0,
    "scoreSchema": 0,
    "scoreRecord": 0,
    "scoreOutlier": 0,
    "scorePattern": 0,
    "scoreRule": 0,
    "scoreBehavior": 0,
    "passFailAvg": 0,
    "physicalName": None,
    "userLabel": None,
    "rcSrc": None,
    "passFailRc": 1,
    "pushDownOptions": None,
    "daysWithoutData": 0,
    "runsWithoutData": 0,
    "daysSinceLastRun": 0,
}
EXP_DS_SCORE = {
    "failScore": 75,
    "datashapeScore": 1,
    "dupeScore": 1,
    "schemaScore": 1,
    "recordScore": 1,
    "outlierScore": 1,
    "fpgScore": 1,
    "validateSrcScore": 1,
    "behaviorScore": 1,
    "rulesTotalScore": 0,
    "validateSrcTotalScore": 0,
    "dupeTotalScore": 0,
    "fpgTotalScore": 0,
    "behaviorTotalScore": 0,
    "outlierTotalScore": 0,
    "schemaTotalScore": 0,
    "recordTotalScore": 0,
    "datashapeTotalScore": 0,
    "datashapeMaxPerCol": 20,
    "datashapeMaxColSize": 12,
    "datashapeSensitivity": 0,
    "behaviorScoreOff": False,
    "lbAbsRowCnt": None,
    "ubAbsRowCnt": None,
    "lbZscoreRowCnt": None,
    "ubZscoreRowCnt": None,
}

AEF_BQ_PD_PAYLOAD = {
	"dataset": DATASET_NAME,
	"runId": WHERE_DATE,
	"runIdEnd": "",
	"runState": "DRAFT",
	"passFail": 1,
	"passFailLimit": 75,
	"jobDescription": "",
	"jobId": {
		"id": -1,
		"uuid": None
	},
	"coreMaxActiveConnections": None,
	"linkId": None,
	"licenseKey": "",
	"logFile": "",
	"logLevel": "INFO",
	"hootOnly": False,
	"prettyPrint": True,
	"useTemplate": False,
	"parallel": False,
	"plan": False,
	"dataPreviewOff": False,
	"datasetSafeOff": False,
	"obslimit": 300,
	"pgUser": "",
	"pgPassword": "",
	"host": "10.64.2.3:5432/dqqa?currentSchema=automation",
	"port": None,
	"user": "anonymous : use -owluser",
	"alertEmail": "",
	"scheduleTime": None,
	"schemaScore": 1,
	"optionAppend": "",
	"keyDelimiter": "~~",
	"agentId": {
		"id": 0,
		"uuid": None
	},
	"load": {
		"readonly": False,
		"passwordManager": None,
		"alias": "",
		"query": "",
		"queryHistory": "",
		"key": "",
		"expression": "",
		"addDateColumn": False,
		"zeroFillNull": False,
		"replaceNulls": "",
		"stringMode": False,
		"operator": None,
		"dateColumn": None,
		"transform": None,
		"filter": "",
		"filterNot": "",
		"sample": 1,
		"backRun": 0,
		"backRunBin": "DAY",
		"unionLookBack": False,
		"unionLookBackMinRow": 0,
		"cache": True,
		"dateFormat": "yyyy-MM-dd",
		"timeFormat": "HH:mm:ss.SSS",
		"timestamp": False,
		"filePath": "",
		"fileQuery": "",
		"fullFile": False,
		"fileHeader": None,
		"inferSchema": True,
		"fileType": None,
		"delimiter": ",",
		"fileCharSet": "UTF-8",
		"skipLines": 0,
		"avroSchema": "",
		"xmlRowTag": "",
		"flatten": False,
		"handleMaps": False,
		"handleMixedJson": False,
		"multiLine": False,
		"lib": "",
		"additionalLib": "",
		"driverName": None,
		"connectionName": "",
		"connectionUrl": "",
		"userName": "",
		"password": "",
		"connectionProperties": {},
		"hiveNative": None,
		"hiveNativeHWC": False,
		"useSql": True,
		"columnName": None,
		"lowerBound": None,
		"upperBound": None,
		"numPartitions": 0,
		"partitionNumber": 0,
		"escapeWithBackTick": False,
		"escapeWithSingleQuote": False,
		"escapeWithDoubleQuote": False,
		"escapeCharacter": "",
		"checkHeader": True,
		"archiveConnection": "",
		"coreFetchMode": False,
		"archiveBreaks": False,
		"ruleSerial": False
	},
	"pushdown": {
		"dataset": DATASET_NAME,
		"connectionName": CONN_NAME,
		"maxConnections": 10,
		"sourceQuery": QUERY,
		"backRuns": 0,
		"backRunBin": "DAY",
		"dateFormatType": "DATE",
		"threads": 2,
		"manualSourceQuery": False,
		"key": "",
		"sourceOutputSchema": "",
		"sourceBreakRules": False,
		"sourceBreakOutliers": False,
		"sourceBreakDupes": False,
		"sourceBreakShapes": False,
		"sourceBreakResults": False,
		"sqlLoggingToggle": False,
		"unionLookback": False,
		"unionLookbackMin": 0
	},
	"outliers": [],
	"patterns": [],
	"dupe": {
		"on": False,
		"only": False,
		"include": None,
		"exclude": None,
		"depth": 0,
		"lowerBound": 99,
		"upperBound": 100,
		"approximate": 1,
		"limitPerDupe": 15,
		"checkHeader": True,
		"filter": None,
		"ignoreCase": True,
		"score": 1,
		"limit": 300
	},
	"profile": {
		"on": True,
		"only": False,
		"include": [
			"unique_key",
			"created_date",
			"closed_date",
			"resolution_action_updated_date",
			"status",
			"status_notes",
			"agency_name",
			"category",
			"complaint_type",
			"descriptor",
			"incident_address",
			"supervisor_district",
			"neighborhood",
			"location",
			"source",
			"media_url",
			"latitude",
			"longitude",
			"police_district"
		],
		"exclude": [],
		"correlation": None,
		"histogram": None,
		"semantic": None,
		"dataConceptId": 300,
		"limit": 300,
		"histogramLimit": 0,
		"score": 1,
		"shape": False,
		"shapeTotalScore": 0,
		"shapeSensitivity": 0,
		"shapeMaxPerCol": 20,
		"shapeMaxColSize": 12,
		"shapeGranular": None,
		"behavioralDimension": "",
		"behavioralDimensionGroup": "",
		"behavioralValueColumn": "",
		"behaviorScoreOff": False,
		"behaviorLookback": 10,
		"behaviorMinSupport": 4,
		"profilePushDown": [
			"count",
			"distinct",
			"mean",
			"minmax",
			"quality"
		],
		"behaviorRowCheck": True,
		"behaviorTimeCheck": False,
		"behaviorMinValueCheck": False,
		"behaviorMaxValueCheck": False,
		"behaviorMeanValueCheck": False,
		"behaviorNullCheck": True,
		"behaviorEmptyCheck": True,
		"behaviorUniqueCheck": True,
		"profileStringLength": False,
		"detectStringNumerics": False,
		"detectTopnBotn": False,
		"detectScalePrecision": False,
		"adaptiveTier": None,
		"advancedTier": False,
		"filter": ""
	},
	"source": {
		"on": False,
		"only": False,
		"validateValues": False,
		"key": None,
		"include": None,
		"exclude": None,
		"includeSrc": None,
		"excludeSrc": None,
		"map": None,
		"score": 1,
		"limit": 30,
		"sourcePushDownCount": False,
		"checkType": True,
		"checkCase": False,
		"validateSchemaOrder": False,
		"matches": False,
		"validateValuesThreshold": 0.9,
		"validateValuesThresholdStrictDownScore": False,
		"validateValuesShowAll": False,
		"validateValuesIgnoreNull": False,
		"validateValuesIgnoreEmpty": False,
		"validateValuesIgnorePrecision": False,
		"validateValuesTrim": False,
		"validateValuesShowMissingKeys": False,
		"validateSrcJoinOnly": False,
		"validateValuesFilter": "",
		"dataset": "",
		"driverName": "",
		"user": "",
		"password": "",
		"passwordManager": "",
		"connectionName": "",
		"connectionUrl": "",
		"query": "",
		"lib": "",
		"connectionProperties": {},
		"filePath": "",
		"fileQuery": "",
		"fullFile": False,
		"header": None,
		"skipLines": 0,
		"inferSchema": True,
		"fileType": None,
		"delimiter": ",",
		"fileCharSet": "UTF-8",
		"avroSchema": "",
		"xmlRowTag": "",
		"flatten": False,
		"handleMaps": False,
		"handleMixedJson": False,
		"multiLine": False,
		"filterCols": None
	},
	"rule": {
		"on": True,
		"only": False,
		"lib": None,
		"name": "",
		"absoluteScoring": False,
		"ruleBreakPreviewLimit": 6
	},
	"colMatch": {
		"colMatchParallelProcesses": 3,
		"colMatchDurationMins": 20,
		"colMatchBatchSize": 2,
		"level": "exact",
		"fuzzyDistance": 1,
		"connectionList": []
	},
	"spark": {
		"numExecutors": 3,
		"driverMemory": "",
		"executorMemory": "",
		"executorCores": 1,
		"conf": "",
		"queue": "",
		"master": "local[*]",
		"principal": "",
		"keyTab": "",
		"deployMode": "",
		"jars": None,
		"packages": None,
		"files": None
	},
	"env": {
		"dataset": DATASET_NAME,
		"jdbcPrincipal": "",
		"jdbcKeyTab": ""
	},
	"record": {
		"on": False,
		"in": "",
		"notIn": "",
		"include": None,
		"percDeltaLimit": 0.1,
		"score": 1,
		"dataset": None,
		"dateColumn": None,
		"keyColumn": None,
		"timeBin": "DAY",
		"by": None
	},
	"stream": None,
	"pipeline": [],
	"metaTags": None,
	"outlierConfiguration": None,
	"shape": {
		"enabled": False,
		"totalScore": 0,
		"sensitivity": 0,
		"maxPerCol": 20,
		"maxColSize": 12,
		"granular": None,
		"columnSettings": []
	},
	"jobSchedule": None,
	"connectionType": "PUSHDOWN"
}
