from data_test.access_security_permissions.data_user_role_access_common import (
    ACCESS_ALL,
    ACCESS_DENIED_MSG_403,
)
from endpoints.v2.controller_catalog import (
    V2_GET_DATA_ASSET,
    V2_GET_CATALOG_BY_DATASET,
    V2_UPDATE_CATALOG_OBJ,
    V2_DELETE_DATASET_LIST,
    V2_GET_CATALOG_FREQUENT_RUNS,
    V2_GET_CATALOG_RECENT_RUNS,
    V2_SEARCH_DETAILS,
)

ACCESS_MATRIX_CATALOG = {
    V2_GET_DATA_ASSET: ACCESS_ALL,
    V2_GET_CATALOG_BY_DATASET: ACCESS_ALL,
    V2_GET_CATALOG_FREQUENT_RUNS: ACCESS_ALL,
    V2_GET_CATALOG_RECENT_RUNS: ACCESS_ALL,
    V2_SEARCH_DETAILS: ACCESS_ALL,
    V2_UPDATE_CATALOG_OBJ: [
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
    ],
    V2_DELETE_DATASET_LIST: [
        # Tip: Those who have access should be last in the list so only 1 job is run instead of 2.
        {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_MANAGER", "code": 200, "msg": None},
        {"role": "ROLE_DATASET_RULES", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_CHECK", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_OWL_ROLE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_PUBLIC", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_SETUP", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_USER_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_VIEW_DATA", "code": 403, "msg": ACCESS_DENIED_MSG_403},
        {"role": "ROLE_ADMIN", "code": 200, "msg": None},
    ],
}
