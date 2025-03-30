DGC_ACCESS_DENIED_MSG_403 = {
    "errorCode": "requestValidationError",
    "helpMessage": "Please ensure you have the appropriate DQ role.",
    "statusCode": 403,
    "titleMessage": "Access Denied",
    "userMessage": "You don't have sufficient permissions to access this endpoint.",
}
ACCESS_DENIED_MSG_403 = {"message": "Access Denied"}
ACCESS_DENIED_MSG_400 = {"message": "Error Occured With Message:  Access Denied"}

ACCESS_ALL = [  # All users have access
    {"role": "ROLE_ADMIN", "code": 200, "msg": None},
    {"role": "ROLE_USER", "code": 200, "msg": None},
    {"role": "ROLE_CONNECTION_MANAGER", "code": 200, "msg": None},
    {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 200, "msg": None},
    {"role": "ROLE_DATA_PREVIEW", "code": 200, "msg": None},
    {"role": "ROLE_DATASET_MANAGER", "code": 200, "msg": None},
    {"role": "ROLE_DATASET_RULES", "code": 200, "msg": None},
    {"role": "ROLE_DATASET_TRAIN", "code": 200, "msg": None},
    {"role": "ROLE_OWL_CHECK", "code": 200, "msg": None},
    {"role": "ROLE_OWL_ROLE_MANAGER", "code": 200, "msg": None},
    {"role": "ROLE_PUBLIC", "code": 200, "msg": None},
    {"role": "ROLE_SETUP", "code": 200, "msg": None},
    {"role": "ROLE_USER_MANAGER", "code": 200, "msg": None},
    {"role": "ROLE_VIEW_DATA", "code": 200, "msg": None},
]

ACCESS_ADMIN_ONLY = [  # Only the admin user has access
    {"role": "ROLE_ADMIN", "code": 200, "msg": None},
    {"role": "ROLE_USER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": ACCESS_DENIED_MSG_403},
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
]

DGC_ACCESS_ADMIN_ONLY = [  # Only the admin user has access
    {"role": "ROLE_ADMIN", "code": 200, "msg": None},
    {"role": "ROLE_USER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_CONNECTION_MANAGER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATA_GOVERNANCE_MANAGER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATA_PREVIEW", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATASET_MANAGER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATASET_RULES", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_DATASET_TRAIN", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_OWL_CHECK", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_OWL_ROLE_MANAGER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_PUBLIC", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_SETUP", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_USER_MANAGER", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
    {"role": "ROLE_VIEW_DATA", "code": 403, "msg": DGC_ACCESS_DENIED_MSG_403},
]
