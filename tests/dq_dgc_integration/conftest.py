import base64

import pytest
import urllib3

from utils.dq_dgc_constants import DGC_BASE_CREDS

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def construct_headers_dgc(creds):
    """
    Construct the headers dictionary with base dgc credentials.
    :param creds: (dict) The authentication credentials.
    :return: dict: The headers dictionary containing the encoded auth credentials.
    """
    credentials = f"{creds['username']}:{creds['password']}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json, text/plain",
        "Authorization": "Basic " + encoded_credentials,
    }
    return headers


@pytest.fixture(scope="class")
def get_auth_headers_dgc(dgc_base_creds):  # pylint: disable=redefined-outer-name
    """
    Fixture that provides the authentication headers.
    :param dgc_base_creds: (dict) DGC authentication credentials.
    :return: dict: The headers dictionary containing the encoded auth credentials.
    """
    return construct_headers_dgc(dgc_base_creds)


@pytest.fixture(scope="session")
def dgc_base_creds():
    """
    Creates a copy of DGC credential object.
    :return:
    """
    return DGC_BASE_CREDS.copy()


@pytest.fixture(scope="session")
def dgc_base_url(request):
    """
    Retrieves DGC base_url
    :return:
    """
    return request.config.getoption("--dgc_base_url")
