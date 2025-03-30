from data_test.access_security_permissions.data_user_role_access_common import (
    DGC_ACCESS_ADMIN_ONLY,
    ACCESS_ALL,
)
from endpoints.dgc_integration.dq.dgc_connection_api import (
    DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS
)
from endpoints.dgc_integration.dq.integration_api import (
    DGC_INTEGRATIONS_STATUS,
)

ACCESS_MATRIX_DGC = {
    DGC_INTEGRATIONS_CONNECTIONS_CREDENTIALS: DGC_ACCESS_ADMIN_ONLY,
    DGC_INTEGRATIONS_STATUS: ACCESS_ALL,
}
