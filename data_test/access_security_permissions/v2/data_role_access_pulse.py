from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_pulse import V2_GET_PULSE_BY_DATASET, V2_GET_PULSE

ACCESS_MATRIX_PULSE = {V2_GET_PULSE_BY_DATASET: ACCESS_ALL, V2_GET_PULSE: ACCESS_ALL}
