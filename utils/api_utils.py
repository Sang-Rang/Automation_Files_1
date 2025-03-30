import requests
import curlify
from utils.logger import Logger


class APIUtils:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.logger = Logger.get_instance()

    def json_return_check(self, response):
        # If the response does not have content-type of application/json in
        # the header, then the response is invalid json.
        if "application/json" in str(response.headers):
            return response.json()

        # Also print to the console so the user sees the issue immediately.
        print("=====================================")
        print(f"ERROR: The API response provided no json output: {response}")
        print("=====================================")

        self.logger.log_exception("=====================================")
        self.logger.log_exception(f"ERROR: The API response provided no json output {response}")
        self.logger.log_exception("=====================================")
        return response

    def get(self, endpoint, params=None, return_json=True, custom_headers=None, **kwargs):
        """
        Get request wrapper method
        :param endpoint: str
        :param params: dict
        :param return_json: bool, returns a JSON by default
        :param custom_headers: dict, provide a custom headers for request
        :param kwargs: optional, any additional parameters, like timeout,
        proxies, etc.
        :return:

        Example of using kwargs in tests:
        kwargs = {"timeout:5", "proxies": {"http:" "proxy.example.com"}}
        response = get(endpoint, params, **kwargs)
        """
        # pylint: disable-msg=missing-timeout, no-else-return
        url = self.base_url + endpoint
        self.logger.log_info(f"Sending GET request to: {url}")
        headers = custom_headers if custom_headers is not None else self.headers
        response = requests.get(url, params=params, headers=headers, verify=False, **kwargs)
        curl_command = curlify.to_curl(response.request)
        self.logger.log_info("=====================================")
        self.logger.log_info(f"CURL request command: {curl_command}")
        self.logger.log_info("=====================================")

        self.logger.log_info(f"Received response: {response.status_code}")
        if return_json:
            return self.json_return_check(response)
        else:
            return response

    def post(
        self, endpoint, params=None, data=None, return_json=True, custom_headers=None, **kwargs
    ):
        """
        Post request wrapper method
        :param endpoint: str
        :param params: dict
        :param data: None
        :param return_json: bool, returns a JSON by default
        :param custom_headers: dict, provide a custom headers for request
        :param kwargs: optional, any additional parameters, like timeout,
        proxies, etc.
        :return: response in json format
        Example of using kwargs in tests:
        kwargs = {"timeout:5", "proxies": {"http:" "proxy.example.com"}}
        response = post(endpoint, params, **kwargs)
        """
        # pylint: disable-msg=missing-timeout, no-else-return
        url = self.base_url + endpoint
        self.logger.log_info(f"Sending POST request to: {url}")

        # Copy existing headers into custom headers
        headers = self.headers.copy()
        if custom_headers:
            headers.update(custom_headers)
        self.logger.log_info(f"Using headers: {headers}")
        try:
            response = requests.post(
                url,
                params=params,
                data=data,
                headers=headers,
                verify=False,
                **kwargs,
            )
            curl_command = curlify.to_curl(response.request)
            self.logger.log_info("=====================================")
            self.logger.log_info(f"CURL request command: {curl_command}")
            self.logger.log_info("=====================================")
            self.logger.log_info(f"Received response: {response.status_code}")
            if return_json:
                return self.json_return_check(response)
            else:
                return response

        except requests.exceptions.RequestException as error:
            self.logger.log_error(f"POST request failed: {error}")
            raise

    def put(self, endpoint, json=None, return_json=True, custom_headers=None, **kwargs):
        """
        Put request wrapper method
        :param endpoint: str
        :param json: json
        :param return_json: bool, returns a JSON by default
        :param custom_headers: dict, provide a custom headers for request
        :param kwargs: optional, any additional parameters, like timeout,
        proxies, etc.
        :return: response in json format
        """
        # pylint: disable-msg=missing-timeout, no-else-return
        url = self.base_url + endpoint
        self.logger.log_info(f"Sending PUT request to: {url}")
        headers = custom_headers if custom_headers is not None else self.headers
        response = requests.put(url, json, headers=headers, verify=False, **kwargs)
        curl_command = curlify.to_curl(response.request)
        self.logger.log_info("=====================================")
        self.logger.log_info(f"CURL request command: {curl_command}")
        self.logger.log_info("=====================================")

        self.logger.log_info(f"Received response: {response.status_code}")
        if return_json:
            return self.json_return_check(response)
        else:
            return response

    def delete(self, endpoint, json=None, return_json=True, custom_headers=None, **kwargs):
        """
        Delete request wrapper method
        :param endpoint: str
        :param json: json
        :param return_json: bool, returns a JSON by default
        :param custom_headers: dict, provide a custom headers for request
        :param kwargs: optional, any additional parameters, like timeout,
        proxies, etc.
        :return: response in json format
        """
        # pylint: disable-msg=missing-timeout, no-else-return
        url = self.base_url + endpoint
        self.logger.log_info(f"Sending DELETE request to: {url}")
        headers = custom_headers if custom_headers is not None else self.headers
        response = requests.delete(url, headers=headers, json=json, verify=False, **kwargs)
        curl_command = curlify.to_curl(response.request)
        self.logger.log_info("=====================================")
        self.logger.log_info(f"CURL request command: {curl_command}")
        self.logger.log_info("=====================================")

        self.logger.log_info(f"Received response: {response.status_code}")
        if return_json:
            return self.json_return_check(response)
        else:
            return response

    def patch(self, endpoint, data=None, return_json=True, custom_headers=None, **kwargs):
        """
        Patch request wrapper method
        :param endpoint: str
        :param parameters: any
        :param data: any
        :param return_json: bool, returns a JSON by default
        :param custom_headers: dict, provide a custom headers for request
        :param kwargs: optional, any additional parameters, like timeout,
        proxies, etc.
        :return: response in json format
        """
        # pylint: disable-msg=missing-timeout, no-else-return
        url = self.base_url + endpoint
        self.logger.log_info(f"Sending PATCH request to: {url}")
        headers = custom_headers if custom_headers is not None else self.headers
        response = requests.patch(url, headers=headers, data=data, verify=False, **kwargs)
        curl_command = curlify.to_curl(response.request)
        self.logger.log_info("=====================================")
        self.logger.log_info(f"CURL request command: {curl_command}")
        self.logger.log_info("=====================================")

        self.logger.log_info(f"Received response: {response.status_code}")
        if return_json:
            return self.json_return_check(response)
        else:
            return response
