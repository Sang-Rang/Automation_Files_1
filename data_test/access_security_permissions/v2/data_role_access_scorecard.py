from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_scorecard import V2_GET_HEATMAP_BY_DATASET, V2_PUT_SCORECARD

ACCESS_MATRIX_SCORECARD = {
    V2_GET_HEATMAP_BY_DATASET: ACCESS_ALL,
    V2_PUT_SCORECARD: ACCESS_ALL,  # Also used for V2_GET_HEATMAP_BY_PAGE & update & delete
}
