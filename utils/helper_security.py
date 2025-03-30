import json

import pytest
from assertpy import assert_that

from endpoints.v2.controller_rule import V2_GET_RULES
from endpoints.v3.rule_api import V3_RULES
from utils.api_utils import APIUtils
from utils.constants import USER_PROFILES
from utils.helper import BaseHelper

helper = BaseHelper()


class SecurityHelper:
    """Security helper methods to use in tests."""

    report_only = False

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.fixture(scope="class")
    def api_utils_xml(self, base_url, get_auth_headers):
        get_auth_headers["X-Requested-With"] = "XMLHttpRequest"
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def get_pullup_job(api_utils):
        """Get data related to a pullup job for security tests that require a job"""
        # Note: Any job data will do, contents not important.
        run_id = "2021-06-03"
        ds_name = "ROLE_ACCESS_JOB"
        connection_name = "APPROVED_POSTGRES_UP"
        schema = "public"
        table = "aclaims_master"
        query = f"select * from {schema}.{table}"
        limit = "limit 5"
        columns = ["CM_BDOS"]  # Including but not limited to
        dataset_defs = helper.get_minimum_job_payload(
            api_utils,
            connection_name=connection_name,
            dataset_name=ds_name,
            query=f"{query} {limit}",
            run_id=run_id,
        )
        helper.run_pullup_job_if_dataset_does_not_exist(api_utils, dataset_defs, run_id)

        return {
            "dataset": ds_name,
            "runId": run_id,
            "connectionalias": connection_name,
            "query": query,
            "columns": columns,
            "schema": schema,
            "table": table,
        }

    @staticmethod
    def add_v3_rule_if_none(api_utils, dataset):
        """Add rule related to a pullup job for security tests"""
        # Note: Any functional rule data will do, contents not important.
        rule_count = api_utils.get(V2_GET_RULES, params={"dataset": dataset})
        if len(rule_count) > 0:
            return {"rule_name": rule_count[0]["ruleNm"]}
        rule_name = "if_CM_CLAIMANT_AGE_is_EMPTY"
        pl_rule = {
            "dataset": dataset,
            "ruleNm": rule_name,
            "ruleType": "EMPTYCHECK",
            "ruleValue": "CM_CLAIMANT_AGE",
            "points": 1,
            "ruleRepo": "",
            "perc": 1,
            "columnName": "CM_CLAIMANT_AGE",
            "businessCategory": "",
            "businessDesc": "",
            "dimId": None,
            "previewLimit": None,
            "runTimeLimit": None,
        }
        resp_rule = api_utils.post(V3_RULES, data=json.dumps(pl_rule), return_json=False)
        assert_that(resp_rule.status_code, "Added rule failed").is_equal_to(200)
        return {"rule_name": rule_name}

    @staticmethod
    def get_const_user_with_role(role):
        """Search the CONSTS file user profiles for a user that has the requested role"""
        found_user = None
        for user, properties in USER_PROFILES.items():
            if "roles" not in properties:
                continue  # Ignore users in CONSTs who don't have roles

            if role in properties["roles"]:
                found_user = user
                break

        if found_user is None:
            raise ValueError(f"No user found for role: {role}")
        return found_user

    def setup_user(self, get_auth_headers_multi_user, profile, payload=None):
        """Get the user by role, fetch their login info, setup header"""
        # To add the XMLHTTP header, add "xmlhttp" in the payload data.
        profile["user"] = self.get_const_user_with_role(profile["role"])
        if payload is not None:
            get_auth_headers_multi_user = self.check_xmlhttp(
                get_auth_headers_multi_user, payload, profile
            )
        user_login = get_auth_headers_multi_user[profile["user"]]
        return user_login

    def check_role_permissions(
        self, api_utils, get_auth_headers_multi_user, api, page_roles, payload=None
    ):
        """Call & Validate API access for every found user of given role using GET"""
        for profile in page_roles:
            user = self.setup_user(get_auth_headers_multi_user, profile, payload)
            response = api_utils.get(api, custom_headers=user, params=payload, return_json=False)
            self.report_results(profile, api, payload, response)

    def check_role_permissions_post(
        self, api_utils, get_auth_headers_multi_user, api, page_roles, payload=None
    ):
        """Call & Validate API access for every found user of given role, using POST and PARAMS"""
        for profile in page_roles:
            user = self.setup_user(get_auth_headers_multi_user, profile, payload)
            response = api_utils.post(api, custom_headers=user, params=payload, return_json=False)
            self.report_results(profile, api, payload, response)

    def check_role_permissions_post_data(
        self, api_utils, get_auth_headers_multi_user, api, page_roles, payload=None
    ):
        """Call & Validate API access for every found user of given role, using POST and DATA"""
        for profile in page_roles:
            user = self.setup_user(get_auth_headers_multi_user, profile, payload)
            response = api_utils.post(api, custom_headers=user, data=payload, return_json=False)
            self.report_results(profile, api, payload, response)

    def check_role_permissions_put_data(
        self, api_utils, get_auth_headers_multi_user, api, page_roles, payload=None
    ):
        """Call & Validate API access for every found user of given role, using PUT and DATA"""
        for profile in page_roles:
            user = self.setup_user(get_auth_headers_multi_user, profile, payload)
            response = api_utils.put(
                api, json.dumps(payload), custom_headers=user, return_json=False
            )
            self.report_results(profile, api, payload, response)

    @staticmethod
    def check_xmlhttp(get_auth_headers_multi_user, payload, profile):
        """Call the API with the given user and report or validate the response"""
        # Add XMLHTTP header if necessary, some APIs require it
        if payload is not None and "xmlhttp" in payload:
            get_auth_headers_multi_user[profile["user"]]["X-Requested-With"] = "XMLHttpRequest"
        return get_auth_headers_multi_user

    def report_results(self, profile, api, payload, response):
        # Write only to console if flag activated
        if self.report_only:
            print(f"{profile['user']}; {api}; Payload: {payload}; {response.status_code}; ")
            return

        # Validate the status code and (if given) message
        assert_that(
            response.status_code,
            f"{profile['user']}; {api}; Payload: {payload}; Unexpected status code.",
        ).is_equal_to(profile["code"])

        if profile["msg"] is not None:
            found_msg = response.json()
            for message in [found_msg, profile["msg"]]:
                if "timestamp" in message.keys():
                    del message["timestamp"]
            assert_that(
                found_msg,
                f"{profile['user']}; {api}; Payload: {payload}; Unexpected message.",
            ).is_equal_to(profile["msg"])
