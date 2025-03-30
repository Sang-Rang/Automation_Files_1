from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ADMIN_ONLY
from endpoints.v2.controller_email import V2_EMAIL_SERVER

ACCESS_MATRIX_EMAIL = {
    V2_EMAIL_SERVER: ACCESS_ADMIN_ONLY,
}
