from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_web_log import V2_GET_LIMITED_WEB_LOGS, V2_GET_ALL_WEB_LOGS

ACCESS_MATRIX_WEB_LOG = {
    V2_GET_LIMITED_WEB_LOGS: ACCESS_ALL,
    V2_GET_ALL_WEB_LOGS: ACCESS_ALL,
}
