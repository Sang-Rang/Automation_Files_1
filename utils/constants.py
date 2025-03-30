#  Keep all the constants here
import datetime

APP_VERSION = ""
PROD_AGENT_ID = None
PROD_AGENT_NAME = None
PROD_AGENT_UUID = ""
PROD_HOST = ""
PROD_PORT = ""
PROD_RUN_ID = datetime.date.today().strftime("%Y-%m-%d")
PROD_URL = "https://dq-qa.dq.cp.collibra.dev"

BASE_CREDS = {
    "username": "autoadmin01@cdq-ad.dq.cp.collibra.dev",
    "password": "Password123!",
    "iss": "automation",
}

USER_PROFILES = {
    "user_auto_admin": {
        "username": "autoadmin01",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_ADMIN"]
    },
    "user_auto": {
        "username": "auto_user",
        "password": "Password123!",
        "iss": "automation",
        "roles":  ["ROLE_USER"]
    },
    "user_conn_mgr": {
        "username": "auto_conn_mgr",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_CONNECTION_MANAGER"]
    },
    "user_data_gov_mgr": {
        "username": "auto_data_gov_mgr",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_DATA_GOVERNANCE_MANAGER"]
    },
    "user_data_preview": {
        "username": "auto_data_preview",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_DATA_PREVIEW"]
    },
    "user_ds_mgr": {
        "username": "auto_ds_mgr",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_DATASET_MANAGER"]
    },
    "user_ds_rules": {
        "username": "auto_ds_rules",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_DATASET_RULES"]
    },
    "user_ds_train": {
        "username": "auto_ds_train",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_DATASET_TRAIN"]
    },
    "user_owl_check": {
        "username": "auto_owl_check",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_OWL_CHECK"]
    },
    "user_owl_role_mgr": {
        "username": "auto_owl_role_mgr",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_OWL_ROLE_MANAGER"]
    },
    "user_public": {
        "username": "auto_public",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_PUBLIC"]
    },
    "user_setup": {
        "username": "auto_setup",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_SETUP"]
    },
    "user_user_mgr": {
        "username": "auto_user_mgr",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_USER_MANAGER"]
    },
    "user_view_data": {
        "username": "auto_view_data",
        "password": "Password123!",
        "iss": "automation",
        "roles": ["ROLE_VIEW_DATA"]
    }
}

BASE_HEADER = {"Content-Type": "application/json"}
