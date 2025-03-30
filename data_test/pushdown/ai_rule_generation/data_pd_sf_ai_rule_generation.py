from payloads.pushdown.ai_rule_generation.pl_pd_sf_ai_rule_generation import (
    PD_SF_AI_RULE_SALES_DATASET,
)

PD_SF_AI_RULE_SALES_AI_PROMPT_PAYLOAD = {
    "prompt": f"Given this table name:@{PD_SF_AI_RULE_SALES_DATASET} With the following columns: "
              f"[name,sales,trdate] Write a valid SQL query to find all rows with 0 sales",
    "max_tokens": 1024,
    "dataset": PD_SF_AI_RULE_SALES_DATASET,
    "page": "/dq/rule",
}

PD_SF_AI_RULE_SALES_RULE_DEFINITION = {
    "dataset": PD_SF_AI_RULE_SALES_DATASET,
    "ruleNm": "test1",
    "ruleType": "SQLF",
    "ruleValue": "",
    "filterQuery": "",
    "points": 1,
    "ruleRepo": "",
    "perc": 1,
    "columnName": "SALES",
    "businessCategory": "",
    "businessDesc": "",
    "dimId": None,
    "scoringScheme": 0,
    "tolerance": 0,
}
