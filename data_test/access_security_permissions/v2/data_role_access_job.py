from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_job import (
    V2_GET_IS_PUSHDOWN,
    V2_GET_JOB_STATUS_BY_DATASET,
    V2_JOB_CHART_SERIES, V2_GET_OWL_CHECK_Q,
)

ACCESS_MATRIX_JOB = {
    V2_GET_IS_PUSHDOWN: ACCESS_ALL,
    V2_GET_JOB_STATUS_BY_DATASET: ACCESS_ALL,
    V2_JOB_CHART_SERIES: ACCESS_ALL,
    V2_GET_OWL_CHECK_Q: ACCESS_ALL,
}
