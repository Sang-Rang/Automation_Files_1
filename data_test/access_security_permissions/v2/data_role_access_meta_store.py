from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ADMIN_ONLY
from endpoints.v2.controller_meta_store import (
    V2_LICENSES,
    V2_GET_MULTI_TENANT_MODE,
    V2_LICENSES_LICENSE_EXPIRATION_COUNTDOWN,
)

ACCESS_MATRIX_META_STORE = {
    V2_LICENSES: ACCESS_ADMIN_ONLY,
    V2_GET_MULTI_TENANT_MODE: ACCESS_ALL,
    V2_LICENSES_LICENSE_EXPIRATION_COUNTDOWN: ACCESS_ALL,
}
