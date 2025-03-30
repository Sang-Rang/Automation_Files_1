from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT
from endpoints.v2.controller_business_unit_to_dataset import (
    V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET,
    V2_BUSINESS_UNIT_TO_DS,
)

ACCESS_MATRIX_BUSINESS_UNIT_TO_DATASET = {
    V2_BUSINESS_UNIT_TO_DS_GET_BY_DATASET: ACCESS_ALL,
    V2_BUSINESS_UNIT_TO_DS: ACCESS_ALL,
    V2_BUSINESS_UNIT: ACCESS_ALL,
}
