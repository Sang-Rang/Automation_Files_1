from data_test.access_security_permissions.data_user_role_access_common import ACCESS_ALL
from endpoints.v2.controller_page import V2_GET_PAGES, V2_ADD_PAGE

ACCESS_MATRIX_PAGE = {
    V2_GET_PAGES: ACCESS_ALL,
    V2_ADD_PAGE: ACCESS_ALL  # Used with V2_DELETE_PAGE
}
