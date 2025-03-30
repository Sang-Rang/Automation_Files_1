from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_label import (
    V2_VIEW_ITEM_LABELS,
    V2_INVALID_RUN,
    V2_REMOVE_DATASET_RUN,
    V2_OFF_PEAK_RUN,
    V2_IGNORE_RUN,
    V2_RETRAIN,
)

ACCESS_MATRIX_LABEL = {
    V2_VIEW_ITEM_LABELS: ACCESS_ALL,
    V2_RETRAIN: ACCESS_ALL,
    V2_IGNORE_RUN: ACCESS_ALL,
    V2_OFF_PEAK_RUN: ACCESS_ALL,
    V2_INVALID_RUN: ACCESS_ALL,
    V2_REMOVE_DATASET_RUN: ACCESS_ALL,
}
