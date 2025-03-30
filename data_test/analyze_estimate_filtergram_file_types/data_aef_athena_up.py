WHERE_DATE = "2021-07-06"
TABLE_NAME = "default.aclaims_master"
COL_NAME = "cm_bdos"
DATASET = "AUTO_CXN_ATHENA_POST_RUN"
QUERY = (
    (
        "select CAST(cm_bdos as TIMESTAMP) as cm_bdos, cm_claim_status, cm_claimant_age, "
        "CAST(cm_claimant_bdate as TIMESTAMP) as cm_claimant_bdate, cm_claimant_sex, "
        "CAST(cm_conversion_date as TIMESTAMP) as cm_conversion_date, "
        "CAST(cm_date_claim_paid as TIMESTAMP) as cm_date_claim_paid, "
        "CAST(cm_date_received as TIMESTAMP) as cm_date_received, cm_denied_reason1, "
        "cm_denied_reason2, cm_diagnosis_code, cm_disab_days, cm_doc_origin_dsc, "
        "CAST(cm_edos as TIMESTAMP) as cm_edos, CAST(cm_eff_date_family as TIMESTAMP) "
        "as cm_eff_date_family, CAST(cm_end_treatmn_dte as TIMESTAMP) as cm_end_treatmn_dte,"
        "CAST(cm_fica_date as TIMESTAMP) as cm_fica_date, cm_group_number, cm_hospital_days, "
        "cm_lob, cm_medicare_number, cm_pending_flag1, cm_pending_flag2, cm_pending_flag3, "
        "cm_pending_flag4, CAST(cm_proof_loss_dt as TIMESTAMP) as cm_proof_loss_dt, "
        "cm_relationship, cm_state_of_issue, cm_state_of_res, cm_tax_status from "
    )
    + TABLE_NAME
    + " where "
    + COL_NAME
    + " >= '${rd}' limit 3"
)
CONN_NAME = "APPROVED_ATHENA_UP"
ROW_COUNT = 3
FILTERGRAM_COL = COL_NAME

PL_DS_GEN = {"dataset": DATASET, "runId": WHERE_DATE}
PL_DS_STATS = {"dataset": DATASET, "runId": WHERE_DATE, "sense": 3}
PL_FILTERGRAM_MULTIPLE = {
    "dataset": DATASET,
    "column": FILTERGRAM_COL,
    "runid": f"{WHERE_DATE}T00:00:00.000 0000",
    "datevalue": f"{WHERE_DATE} 00:00:00 00",
    "limit": 500,
}
PL_FILTERGRAM_SINGLE = {
    "dataset": DATASET,
    "column": "cm_hospital_days",
    "runid": f"{WHERE_DATE}T00:00:00.000 0000",
    "datevalue": f"{WHERE_DATE} 00:00:00 00",
    "limit": 500,
}
PL_DAYS_WITH_DATA = {
    "cxn": CONN_NAME,
    "schemaAndTableNm": TABLE_NAME,
    "colNm": COL_NAME,
    "groupBy": "day",
}
PL_JOB_EST = {
    "drivername": "",
    "aliasname": CONN_NAME,
    "hostname": "",
    "cols": "cm_bdos,cm_claim_status,cm_claimant_age,cm_claimant_bdate,"
    "cm_claimant_sex,cm_conversion_date,cm_date_claim_paid,"
    "cm_date_received, cm_denied_reason1,cm_denied_reason2,"
    "cm_diagnosis_code,cm_disab_days,cm_doc_origin_dsc,cm_edos,"
    "cm_eff_date_family,cm_end_treatmn_dte, cm_fica_date,"
    "cm_group_number,cm_hospital_days,cm_lob,cm_medicare_number,"
    "cm_pending_flag1,cm_pending_flag2,cm_pending_flag3,"
    "cm_pending_flag4, cm_proof_loss_dt,cm_relationship,"
    "cm_state_of_issue,cm_state_of_res,cm_tax_status",
    "table": TABLE_NAME,
    "where": f"{COL_NAME} >= '{WHERE_DATE}'",
    "query": QUERY.replace("${rd}", str(WHERE_DATE)),
}

EXP_FILTERGRAM_MULTIPLE = {
    "2021-07-18 00:00:00.000": 1,
    "2021-07-06 00:00:00.000": 1,
    "2021-11-29 00:00:00.000": 1,
}
EXP_FILTERGRAM_SINGLE = {"0": 3}
EXP_JOB_EST = {"rowCount": 3, "colCount": 30}
EXP_DAYS_WITH = [
    {"rowcount": 6, "day_owl_str": "2021-07-06", "day": "2021-07-06"},
    {"rowcount": 1, "day_owl_str": "2021-07-07", "day": "2021-07-07"},
    {"rowcount": 1, "day_owl_str": "2021-07-08", "day": "2021-07-08"},
    {"rowcount": 1, "day_owl_str": "2021-07-09", "day": "2021-07-09"},
    {"rowcount": 1, "day_owl_str": "2021-07-10", "day": "2021-07-10"},
    {"rowcount": 2, "day_owl_str": "2021-07-12", "day": "2021-07-12"},
    {"rowcount": 2, "day_owl_str": "2021-07-13", "day": "2021-07-13"},
    {"rowcount": 2, "day_owl_str": "2021-07-14", "day": "2021-07-14"},
    {"rowcount": 1, "day_owl_str": "2021-07-15", "day": "2021-07-15"},
    {"rowcount": 1, "day_owl_str": "2021-07-16", "day": "2021-07-16"},
    {"rowcount": 2, "day_owl_str": "2021-07-18", "day": "2021-07-18"},
    {"rowcount": 2, "day_owl_str": "2021-07-20", "day": "2021-07-20"},
    {"rowcount": 1, "day_owl_str": "2021-07-25", "day": "2021-07-25"},
    {"rowcount": 1, "day_owl_str": "2021-07-26", "day": "2021-07-26"},
    {"rowcount": 3, "day_owl_str": "2021-07-27", "day": "2021-07-27"},
    {"rowcount": 2, "day_owl_str": "2021-07-28", "day": "2021-07-28"},
    {"rowcount": 1, "day_owl_str": "2021-08-11", "day": "2021-08-11"},
    {"rowcount": 1, "day_owl_str": "2021-11-02", "day": "2021-11-02"},
    {"rowcount": 1, "day_owl_str": "2021-11-29", "day": "2021-11-29"},
    {"rowcount": 1, "day_owl_str": "2025-05-19", "day": "2025-05-19"},
]
EXP_DS_SCAN = {
    "runId": f"{WHERE_DATE}T00:00:00.000+0000",
    "dataset": DATASET,
    "score": 100,
    "rc": 3,
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
    "passFailAvg": 0.0,
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
    "dataset": DATASET,
    "failScore": 75,
    "datashapeScore": 1.0,
    "dupeScore": 1.0,
    "schemaScore": 1.0,
    "recordScore": 1.0,
    "outlierScore": 1.0,
    "fpgScore": 1.0,
    "validateSrcScore": 1.0,
    "behaviorScore": 1.0,
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
    "datashapeSensitivity": 0.0,
    "behaviorScoreOff": False,
    "lbAbsRowCnt": None,
    "ubAbsRowCnt": None,
    "lbZscoreRowCnt": None,
    "ubZscoreRowCnt": None,
}
