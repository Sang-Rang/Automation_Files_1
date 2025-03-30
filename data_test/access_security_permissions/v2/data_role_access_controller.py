from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller import (
    V2_GET_DATASET_HISTORY_RUN_ID,
    V2_DEPLOYMENT_TYPE,
    V2_GET_COUNT_IN_TRAINING,
    V2_GET_UI_TIMEOUT,
    V2_GET_RECENT_RUNS,
)
from endpoints.v2.controller_dq_inbox import V2_GET_DQ_INBOX

ACCESS_MATRIX_CONTROLLER = {
    V2_GET_DATASET_HISTORY_RUN_ID: ACCESS_ALL,
    V2_DEPLOYMENT_TYPE: ACCESS_ALL,
    V2_GET_COUNT_IN_TRAINING: ACCESS_ALL,
    V2_GET_UI_TIMEOUT: ACCESS_ALL,
    V2_GET_RECENT_RUNS: ACCESS_ALL,
    V2_GET_DQ_INBOX: ACCESS_ALL,
}
