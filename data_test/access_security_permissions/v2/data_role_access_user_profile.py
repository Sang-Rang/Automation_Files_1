from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_user_profile import (
    V2_GET_USER_PROFILES_USER_LIST,
    V2_GET_USER_PROFILE_BY_USER,
    V2_GET_LIST_DATASETS_BY_ROLE,
)

ACCESS_MATRIX_USER_PROFILE = {
    V2_GET_USER_PROFILES_USER_LIST: ACCESS_ALL,
    V2_GET_USER_PROFILE_BY_USER: ACCESS_ALL,
    V2_GET_LIST_DATASETS_BY_ROLE: ACCESS_ALL,
}
