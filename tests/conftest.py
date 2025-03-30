import pytest
import requests
import urllib3

from endpoints.v2.controller_agent import V2_GET_AGENTS
from endpoints.v2.controller_explorer import V2_GET_REMOTE_HOST
from endpoints.v2.controller_health import V2_GET_ENVIRONMENT_DETAILS
from utils import constants
from utils.constants import BASE_CREDS, BASE_HEADER, PROD_URL, USER_PROFILES
from utils.dq_dgc_constants import DGC_BASE_URL
from utils.logger import Logger

# pylint: disable-msg=redefined-outer-name

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LOGGER = Logger.get_instance()


def construct_headers(token):
    """
    Construct the headers dictionary with the provided token.
    :param token: (str) The authentication token.
    :return: dict: The headers dictionary containing the authentication token.
    """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json, text/plain, application/octet-stream",
        "Authorization": "Bearer " + token,
    }
    return headers


def get_auth_token(base_url, base_creds, custom_iss=None, return_json=True):
    """
    Get the authentication token for the provided base URL and credentials.
    :param base_url: str, the base URL of the authentication endpoint.
    :param base_creds: dict, the production credentials dictionary.
    :param custom_iss: str, optional. Custom 'iss' parameter value. Default to None.
    :param return_json: bool, optional. Return json from output of /auth/signin. Default to True.
    :return: str, the authentication token.
    """
    if custom_iss:
        base_creds["iss"] = custom_iss
    base_ip = base_url + "/auth/signin"
    LOGGER.log_info(f"Starting getting the auth token, " f"the base URL is : " f"{base_ip}")
    prod_token = requests.post(
        base_ip,
        json=base_creds,
        headers=BASE_HEADER,
        verify=False,
        timeout=1200,
    )
    LOGGER.log_info(
        f"Received response for getting a token, " f"code: " f"{prod_token.status_code}"
    )
    if not return_json:
        return prod_token
    prod_token_json = prod_token.json()
    token = prod_token_json["token"]
    return token


@pytest.fixture(scope="class")
def get_auth_headers(base_url, base_creds, request):
    """
    Fixture that provides the authentication headers.
    :param base_url: str, the base URL of the authentication endpoint.
    :param base_creds: dict, the production credentials dictionary.
    :param request: (FixtureRequest): The pytest request fixture.
    :return: The authentication headers dictionary.
    """
    custom_iss = request.config.getoption("--iss")
    token = get_auth_token(base_url, base_creds, custom_iss)
    headers = construct_headers(token)
    return headers


@pytest.fixture(scope="class")
def get_auth_headers_multi_user(base_url, request):
    """
    Fixture that provides the authentication headers for multiple users.
    :param base_url: str, the base URL of the authentication endpoint.
    :param request: (FixtureRequest): The pytest request fixture.
    :return: A dictionary containing headers for each user.
    Usage:
    - add get_auth_headers_multi_user as a parameter to your test
    - create a var with header info, ex: user_1_headers = get_auth_headers_multi_user['user_auto']
    - request example: username = api_utils.get("/v2/username", custom_headers=user_1_headers)
    """
    custom_iss = request.config.getoption("--iss")
    headers = {}
    for user, creds in USER_PROFILES.items():
        token = get_auth_token(base_url, creds, custom_iss)
        user_headers = construct_headers(token)
        headers[user] = user_headers
    return headers


@pytest.fixture(scope="session")
def base_creds():
    """
    Creates a copy of credential object.
    :return:
    """
    return BASE_CREDS.copy()


@pytest.fixture(scope="session")
def agents_list(get_auth_headers, base_url):
    """
    Retrieves the list of agents from the production environment using the
    base_url and get_auth_headers fixtures.
    :param get_auth_headers:
    :param base_url:
    :return:
    """
    agents_url = base_url + V2_GET_AGENTS
    LOGGER.log_info(f"Getting the agents list for: {agents_url}")
    agents_list = requests.get(
        agents_url, headers=get_auth_headers, verify=False, timeout=1200
    ).json()
    LOGGER.log_info(f"Received response for agents list, code: {agents_list.status_code}")
    return agents_list


@pytest.fixture(scope="class", autouse=True)
def get_remote_host(get_auth_headers, base_url):
    """
    Retrieves the remote host from the base environment using the base_url
    and get_auth_headers fixtures.
    :param get_auth_headers:
    :param base_url:
    :return:
    """
    remote_host_url = base_url + V2_GET_REMOTE_HOST
    LOGGER.log_info(
        f"Retrieve the remote host from the base environment: {remote_host_url}"
    )
    remote_host = requests.get(
        remote_host_url, headers=get_auth_headers, verify=False, timeout=1200
    )
    remote_host_json = remote_host.json()
    LOGGER.log_info(
        f"Received response for retrieve the remote host, code: {remote_host.status_code}"
    )
    metastore_host = remote_host_json[0]["METASTORE_HOST"]
    host_details = {"host": metastore_host, "port": metastore_host[10: len(metastore_host)]}
    # Set the values in constants.py
    constants.PROD_HOST = host_details["host"]
    constants.PROD_PORT = host_details["port"]

    return host_details

@pytest.fixture(scope="class", autouse=True)
def get_env_details(get_auth_headers, base_url):
    env_details_url = base_url + V2_GET_ENVIRONMENT_DETAILS
    LOGGER.log_info(
        f"Retrieve the environment details from the base environment: {env_details_url}"
    )
    env_details = requests.get(
        env_details_url, headers=get_auth_headers, verify=False, timeout=1200
    )
    env_details_json = env_details.json()
    LOGGER.log_info(
        f"Received response for retrieve the environment details, code: {env_details.status_code}"
    )

    # Set the value in constants.py
    constants.APP_VERSION = env_details_json["version"]

    return env_details

def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        action="store",
        default=PROD_URL,
        help="Specify the environment IP address",
    )
    parser.addoption("--iss", action="store", default=None, help="Specify the iss value")
    parser.addoption("--dgc_base_url", action="store", default=DGC_BASE_URL,
                     help="Specify the url for DGC environment",
                     )


@pytest.fixture(scope="session")
def base_url(request):
    """
    Retrieves the base_url IP address
    :return:
    """
    return request.config.getoption("--base_url")
