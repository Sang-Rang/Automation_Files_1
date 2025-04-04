from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from data_test.access_security_permissions.data_user_role_access_common import (
    ACCESS_DENIED_MSG_403,
    ACCESS_ADMIN_ONLY,
)
from endpoints.v2.controller_security import (
    V2_GET_CURRENT_USER_OWL_ROLES,
    V2_GET_ACTIVITY_AUDIT,
    V2_GET_LOCAL_DB_ROLES,
    V2_GET_LIST_ROLES_BY_DISTNCT_DATASETS,
    V2_GET_LOCAL_DB_ROLES_WITH_DATASETS_AND_USERS,
    V2_GET_SECURITY_SETTINGS_BY_TYPE,
    V2_GET_SECURITY_SETTINGS_BY_COL_TYPE,
    V2_GET_ALL_DB_USER_DETAILS,
    V2_SQL_EDITOR_ACCESS,
    V2_GLOBAL_RULES_ACCESS,
    V2_USERNAME_ACCESS_BY_DATASET,
    V2_USERNAME_RULES_ACCESS_BY_DATASET,
    V2_GET_DB_USER_LIST_BY_USER,
    V2_GET_PERSONAL_LIST,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY,
    V2_USERNAME,
)

SQL_EDITOR_400_MSG = {
    "message": "Error: Only users with ROLE_ADMIN or ROLE_VIEW_DATA can use the SQL Editor"
}

ACCESS_MATRIX_SECURITY = {
    V2_GET_CURRENT_USER_OWL_ROLES: ACCESS_ALL,
    V2_GET_ACTIVITY_AUDIT: ACCESS_ADMIN_ONLY,
    V2_GET_LOCAL_DB_ROLES_WITH_DATASETS_AND_USERS: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
    V2_GLOBAL_RULES_ACCESS: ACCESS_ALL,
    V2_USERNAME_ACCESS_BY_DATASET: ACCESS_ALL,
    V2_USERNAME_RULES_ACCESS_BY_DATASET: ACCESS_ALL,
    V2_GET_DB_USER_LIST_BY_USER: ACCESS_ALL,
    V2_GET_PERSONAL_LIST: ACCESS_ALL,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE: ACCESS_ALL,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA: ACCESS_ALL,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY: ACCESS_ALL,
    V2_USERNAME: ACCESS_ALL,
    V2_GET_ALL_DB_USER_DETAILS: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
    V2_SQL_EDITOR_ACCESS: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_DATA_PREVIEW", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_DATASET_MANAGER", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_DATASET_RULES", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_DATASET_TRAIN", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_OWL_CHECK", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_PUBLIC", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_SETUP", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_USER_MANAGER", "code": 400, "msg": SQL_EDITOR_400_MSG},
        {"role": "ROLE_VIEW_DATA", "code": 200, "msg": None},
    ],
    V2_GET_SECURITY_SETTINGS_BY_COL_TYPE: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
    V2_GET_SECURITY_SETTINGS_BY_TYPE: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
    V2_GET_LIST_ROLES_BY_DISTNCT_DATASETS: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
    V2_GET_LOCAL_DB_ROLES: [
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        # {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},  # DEV-69524
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    ],
}
