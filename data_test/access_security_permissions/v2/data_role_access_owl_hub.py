from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ADMIN_ONLY
from endpoints.v2.controller_owl_hub import V2_GET_CLEAN_DB_DEFAULTS

ACCESS_MATRIX_OWL_HUB = {
    V2_GET_CLEAN_DB_DEFAULTS: ACCESS_ADMIN_ONLY,
}
