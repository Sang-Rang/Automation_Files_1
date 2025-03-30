from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_owl_options import (
    V2_OWL_OPTIONS_GET,
    V2_OWL_OPTIONS_DISTINCT_USERNAMES,
)

ACCESS_MATRIX_OWL_OPTIONS = {
    V2_OWL_OPTIONS_GET: ACCESS_ALL,
    V2_OWL_OPTIONS_DISTINCT_USERNAMES: ACCESS_ALL,
}
