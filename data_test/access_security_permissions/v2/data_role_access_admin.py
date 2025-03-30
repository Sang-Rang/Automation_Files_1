from data_test.access_security_permissions.data_user_role_access_common import (
    ACCESS_ALL,
    ACCESS_ADMIN_ONLY,
)
from endpoints.v2.controller_admin import (
    V2_GET_ADMIN_CONFIG,
    V2_GET_TOTAL_BYTES,
    V2_GET_APP_CONFIG,
    V2_GET_CLI_OPTIONS,
)

ACCESS_MATRIX_ADMIN = {
    V2_GET_ADMIN_CONFIG: ACCESS_ALL,
    V2_GET_TOTAL_BYTES: ACCESS_ADMIN_ONLY,
    V2_GET_APP_CONFIG: ACCESS_ALL,
    V2_GET_CLI_OPTIONS: ACCESS_ALL,
}
