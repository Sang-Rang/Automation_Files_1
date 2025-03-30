from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_alert import V2_GET_ACTIVE_ALERTS_COUNT

ACCESS_MATRIX_ALERT = {
    V2_GET_ACTIVE_ALERTS_COUNT: ACCESS_ALL,
}
