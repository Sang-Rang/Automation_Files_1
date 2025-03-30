from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ADMIN_ONLY
from endpoints.v2.controller_audit_trail import (
    V2_GET_DATASETS_AUDIT_TRAIL_ITEMS,
    V2_GET_AUDIT_TRAIL_ITEMS,
)

ACCESS_MATRIX_AUDIT_TRAIL = {
    V2_GET_DATASETS_AUDIT_TRAIL_ITEMS: ACCESS_ADMIN_ONLY,
    V2_GET_AUDIT_TRAIL_ITEMS: ACCESS_ADMIN_ONLY,
}
