import pytest
from endpoints.v2.controller_security import (
    V2_CREATE_LOCAL_JDBC_USER_ADMIN,
    V2_DELETE_USER,
    V2_CREATE_LOCAL_JDBC_USER,
    V2_UPDATE_LOCAL_JDBC_USER,
)
from tests.a_setup_and_configure.helper_setup import SetupEnvHelper
from utils.api_utils import APIUtils
from utils.constants import USER_PROFILES, BASE_CREDS
from utils.helper import BaseHelper
from utils.helper_connections import ConnectionsHelper

helper = BaseHelper()
connections_helper = ConnectionsHelper()
setup_env_helper = SetupEnvHelper()


class TestSetupUsers:
    # CONFIGURATION OPTIONS
    # -----------------------------------------------------

    # Used for testing purposes only
    create_user = True
    add_roles = True
    delete_user = False  # Be careful!
    prefix_user_name = ""
    use_base_creds_tenant = True  # Overwrites iss/tenant.

    # -----------------------------------------------------

    # Notes
    # - Creates Admin user if profile name includes "admin", otherwise standard user
    # - Usernames/passwords come from CONST
    # - BASE_CREDS ISS must match the new user's ISS to add roles to users

    # -----------------------------------------------------

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @pytest.mark.skip(reason="Setup users is a one-time manual execution for new RC envs.")
    def test_setup_users(self, api_utils):
        # Create a user for every profile in the const list
        for profile, user in USER_PROFILES.items():
            user_name = f"{self.prefix_user_name}{user['username']}"  # Useful for testing
            user_email = f"{self.prefix_user_name}{user['username']}@NotRealAddress.com"

            pl_create_user = {
                "firstname": "Automation",
                "lastname": "User",
                "username": user_name,
                "email": user_email,
                "password": user["password"],
                "confirmPassword": user["password"],
                "adduser": "Add User",
                "enabled": True,
            }

            if self.create_user:
                # The type of user has different input parameters & APIs
                if profile.find("admin") > -1:
                    pl_create_user["enabled"] = True
                    post_user = api_utils.post(
                        V2_CREATE_LOCAL_JDBC_USER_ADMIN, params=pl_create_user, return_json=False
                    )
                else:
                    # Tenant requires all lower case
                    if self.use_base_creds_tenant:
                        pl_create_user["tenant"] = BASE_CREDS["iss"].lower()
                    else:
                        pl_create_user["tenant"] = user["iss"].lower()
                    post_user = api_utils.post(
                        V2_CREATE_LOCAL_JDBC_USER, params=pl_create_user, return_json=False
                    )

                if post_user.status_code != 200:
                    print(
                        f"Create user failed: {pl_create_user}, "
                        f"status {post_user.status_code}, msg: {post_user.text}"
                    )

            if self.add_roles:
                self.add_user_roles(api_utils, pl_create_user, user)

            if self.delete_user:
                self.del_user(api_utils, user_name)

    @staticmethod
    def add_user_roles(api_utils, pl_user, const_user):
        # roles = ROLES
        role_list = ",".join(const_user["roles"])
        pl_update = {
            "firstname": pl_user["firstname"],
            "lastname": pl_user["lastname"],
            "username": pl_user["username"],
            "email": pl_user["email"],
            "locked": False,
            "enabled": True,
            "roles": role_list,
        }

        update = api_utils.post(V2_UPDATE_LOCAL_JDBC_USER, params=pl_update, return_json=False)
        if update.status_code != 200:
            print(
                f"Update user failed: {pl_update}, status {update.status_code}, msg: {update.text}"
            )

    @staticmethod
    def del_user(api_utils, username):
        delete = api_utils.post(V2_DELETE_USER, params={"username": username}, return_json=False)
        if delete.status_code != 200:
            print(
                f"Create user failed for {username}, "
                f"status {delete.status_code}, msg: {delete.text}"
            )
