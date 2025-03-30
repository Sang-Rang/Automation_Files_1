from data_test.access_security_permissions.data_user_role_access_common import (
    ACCESS_DENIED_MSG_403, ACCESS_ALL,
)
from endpoints.v2.controller_dataset import V2_RENAME_DATASET

ACCESS_ROLE_ACCESS_DATASET = [
    {"role": "ROLE_ADMIN", "code": 200, "msg": None},
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
]

ACCESS_MATRIX_DATASET = {
    V2_RENAME_DATASET: ACCESS_ALL,
}
