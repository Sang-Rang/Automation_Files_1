import copy
from datetime import datetime, timezone

import allure
import pytest
from assertpy import assert_that, soft_assertions

from data_test.general.data_local_jdbc_users import (
    PL_NEW_USER,
    MSG_UPDATE_USER,
    MSG_DEL_USER,
    PL_USER_UPDATE,
    MSG_NEW_USER,
    NOW,
    MODIFIED_USER,
    PASSWORD_USER,
    PL_CHANGE_PASSWORD,
    NEW_PW_USER_LOGIN,
    PL_RESTORE_PASSWORD,
    MSG_PWD_CHANGE,
)
from endpoints.v2.controller_security import (
    V2_CREATE_LOCAL_JDBC_USER,
    V2_GET_ALL_DB_USER_DETAILS,
    V2_UPDATE_LOCAL_JDBC_USER,
    V2_DELETE_USER,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
    V2_GET_DB_USER_LIST_BY_USER,
    V2_GET_PERSONA_LIST,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA,
    V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY,
    V2_USER_LOCAL_PASSWORD,
)
from endpoints.v2.controller_user_profile import V2_GET_USER_PROFILE_BY_USER
from tests.conftest import get_auth_token, construct_headers
from utils.api_utils import APIUtils
from utils.constants import BASE_CREDS, PROD_URL, USER_PROFILES


class TestLocalJdbcUsers:
    # These users for password & lock tests must exist out of the USER_PROFILES to prevent failure
    # to login from impacting other tests cases, should something go wrong during execution.
    # These user payloads include parameters for multiple API calls

    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def setup_modified_user_if_does_not_exist(api_utils, credentials):
        """If the modified user does not exist, create it and enable & give roles"""
        pl_update = copy.deepcopy(credentials)
        pl_update["locked"] = False

        all_users = api_utils.get(V2_GET_ALL_DB_USER_DETAILS)

        if credentials["username"] not in all_users:
            api_utils.post(V2_CREATE_LOCAL_JDBC_USER, params=pl_update, return_json=False)

            # Create call does not include roles, which is required for access.
            api_utils.post(V2_UPDATE_LOCAL_JDBC_USER, params=pl_update, return_json=False)

        all_users = api_utils.get(V2_GET_ALL_DB_USER_DETAILS)
        found_user = next(item for item in all_users if item["username"] == credentials["username"])

        return found_user

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_add_update_delete(self, api_utils):
        """Test create, update, delete for a new local jdbc user"""

        # Create
        new_user = api_utils.post(V2_CREATE_LOCAL_JDBC_USER, params=PL_NEW_USER)
        with soft_assertions():
            assert_that(MSG_NEW_USER, "New user unexpected response").is_equal_to(new_user)

        # Search
        all_users = api_utils.get(V2_GET_ALL_DB_USER_DETAILS)
        found_user = next(item for item in all_users if item["username"] == PL_NEW_USER["username"])

        # Validate default expected data
        with soft_assertions():
            assert_that(found_user["authoritiesList"], "New user authoritiesList").is_equal_to(
                [{"authority": None, "owlRolesToDatasets": None}]
            )
            assert_that(found_user["email"], "New user email").is_equal_to(PL_NEW_USER["email"])
            assert_that(found_user["enabled"], "New user should be disabled").is_equal_to(False)
            assert_that(found_user["firstName"], "New user first name").is_equal_to(
                PL_NEW_USER["firstname"]
            )
            assert_that(found_user["lastName"], "New user last name").is_equal_to(
                PL_NEW_USER["lastname"]
            )
            assert_that(found_user["locked"], "New user should be unlocked").is_equal_to(False)
            assert_that(found_user["username"], "New user username").is_equal_to(
                PL_NEW_USER["username"]
            )

        # Update to enable user & add role
        updated_user = api_utils.post(V2_UPDATE_LOCAL_JDBC_USER, params=PL_USER_UPDATE)
        with soft_assertions():
            assert_that(updated_user, "Updated user unexpected response").is_equal_to(
                MSG_UPDATE_USER
            )

        # Check the new user can log in (now that role added & enabled)
        token = get_auth_token(PROD_URL, MODIFIED_USER, BASE_CREDS["iss"], return_json=False)
        assert_that(token.status_code, "Initial setup failed").is_equal_to(200)

        # Delete
        del_user = api_utils.post(V2_DELETE_USER, params={"username": PL_NEW_USER["username"]})
        with soft_assertions():
            assert_that(del_user, "Deleted user unexpected response").is_equal_to(MSG_DEL_USER)
        all_users = api_utils.get(V2_GET_ALL_DB_USER_DETAILS)
        assert_that(all_users, "Deleted user was still found.").does_not_contain(
            PL_NEW_USER["username"]
        )

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_locked(self, api_utils):
        """Test local JDBC user loses access when locked out"""
        self.setup_modified_user_if_does_not_exist(api_utils, MODIFIED_USER)
        creds = {
            "username": MODIFIED_USER["username"],
            "password": MODIFIED_USER["password"],
            "iss": MODIFIED_USER["iss"],  # Used for login
        }
        # Set the status to unlocked
        token = get_auth_token(
            base_url=PROD_URL, base_creds=creds, custom_iss=creds["iss"], return_json=False
        )
        assert_that(token.status_code, "Initial setup failed").is_equal_to(200)

        # Update the status to locked and validate refusal
        MODIFIED_USER["locked"] = True
        api_utils.post(V2_UPDATE_LOCAL_JDBC_USER, params=MODIFIED_USER, return_json=False)

        token = get_auth_token(PROD_URL, creds, return_json=False)
        assert_that(token.status_code, "Failed to lock user").is_equal_to(401)

        # Reset the status and validate success
        MODIFIED_USER["locked"] = False
        api_utils.post(V2_UPDATE_LOCAL_JDBC_USER, params=MODIFIED_USER, return_json=False)

        token = get_auth_token(PROD_URL, creds, return_json=False)
        assert_that(token.status_code, "Failed to reset user's lock status").is_equal_to(200)

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_profile(self, api_utils, get_auth_headers_multi_user):
        """Test a local jdbc user can update their name and email on user profile"""
        # Note: These API calls modify a currently logged-in user.
        user_profile = "user_view_data"
        user = USER_PROFILES[user_profile]
        user_login = get_auth_headers_multi_user[user_profile]

        current_db_user = api_utils.get(V2_GET_DB_USER_LIST_BY_USER, custom_headers=user_login)[0]
        profile = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user_login)

        # Validate some basic data.
        found_date = current_db_user["created"]
        convert_date = datetime.strptime(found_date, "%Y-%m-%dT%H:%M:%S.%f%z")
        assert_that(convert_date, "Unexpected created date").is_before(datetime.now(timezone.utc))
        assert_that(current_db_user["enabled"], "User was not enabled").is_true()
        assert_that(current_db_user["accountNonLocked"], "User was not unlocked").is_true()
        assert_that(current_db_user["username"], "Unexpected dbuser username").is_equal_to(
            user["username"]
        )
        assert_that(profile["email"], "No email found").is_not_empty()
        assert_that(profile["username"], "Unexpected profile username").is_equal_to(
            user["username"]
        )
        assert_that(profile["firstName"], "No first name found").is_not_empty()
        assert_that(profile["lastName"], "No last name found").is_not_empty()

        save_first = profile["firstName"]
        save_last = profile["lastName"]
        save_email = profile["email"]

        pl_update_profile = {
            "username": profile["username"],
            "firstname": profile["firstName"] + str(NOW),
            "lastname": profile["lastName"] + str(NOW),
            "email": f"email{NOW}@NotARealAddress.com",
        }

        update = api_utils.post(
            V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
            custom_headers=user_login,
            params=pl_update_profile,
            return_json=False,
        )
        assert_that(update.status_code, "Update user profile failed").is_equal_to(200)

        # Validate the update call
        profile_updated = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user_login)

        assert_that(profile_updated["email"], "Email failed to update").is_equal_to(
            pl_update_profile["email"]
        )
        assert_that(profile_updated["firstName"], "First name failed to update").is_equal_to(
            pl_update_profile["firstname"]
        )
        assert_that(profile_updated["lastName"], "Last name failed to update").is_equal_to(
            pl_update_profile["lastname"]
        )

        # Restore old settings
        pl_update_profile["firstname"] = save_first
        pl_update_profile["lastname"] = save_last
        pl_update_profile["email"] = save_email
        update_restore = api_utils.post(
            V2_UPDATE_LOCAL_JDBC_USER_PROFILE,
            custom_headers=user_login,
            params=pl_update_profile,
            return_json=False,
        )
        assert_that(update_restore.status_code, "Failed to restore old profile data").is_equal_to(
            200
        )

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_persona(self, api_utils, get_auth_headers_multi_user):
        """Test updating persona for local jdbc user"""
        user_profile = "user_view_data"
        user = USER_PROFILES[user_profile]["username"]
        user_login = get_auth_headers_multi_user[user_profile]
        set_persona = 1

        persona_list = api_utils.get(V2_GET_PERSONA_LIST, custom_headers=user_login)
        assert_that(len(persona_list), "No persona options found.").is_greater_than(1)

        profile = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user_login)
        current_persona = profile["persona"]

        if current_persona == 1:
            set_persona = 2

        pl_persona = {"username": profile["username"], "persona": set_persona}
        update_persona = api_utils.post(
            V2_UPDATE_LOCAL_JDBC_USER_PROFILE_PERSONA, custom_headers=user_login, params=pl_persona
        )
        assert_that(update_persona, "Unexpected persona update response").is_equal_to(
            {"message": f"Update for user {user} was successful!"}
        )

        profile_updated = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user_login)
        assert_that(profile_updated["persona"]).is_equal_to(set_persona)

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_story(self, api_utils, get_auth_headers_multi_user):
        """Test updating user story for local jdbc user"""
        user_profile = "user_view_data"
        user = USER_PROFILES[user_profile]["username"]
        user_login = get_auth_headers_multi_user[user_profile]
        msg = {"message": f"Update for user {user} was successful!"}

        # Update the user story data
        pl_story = {"username": user, "title": f"title{NOW}", "description": f"desc{NOW}"}
        update_story = api_utils.post(
            V2_UPDATE_LOCAL_JDBC_USER_PROFILE_STORY, custom_headers=user_login, params=pl_story
        )
        assert_that(update_story, "Unexpected update profile story message").is_equal_to(msg)

        # Validate changes applied
        current_story = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=user_login)
        assert_that(pl_story["title"], "Title did not update correctly").is_equal_to(
            current_story["title"]
        )
        assert_that(pl_story["description"], "Description did not update correctly").is_equal_to(
            current_story["description"]
        )

    @allure.feature("Users")
    @allure.story("Local JDBC Users")
    def test_local_jdbc_user_change_password(self, api_utils):
        """Test local JDBC user can change password and login"""
        # Note: These API calls modify a currently logged-in user, so token generation required.

        # Setup the test to login as the password user
        self.setup_modified_user_if_does_not_exist(api_utils, PASSWORD_USER)
        token_setup = get_auth_token(PROD_URL, PASSWORD_USER, BASE_CREDS["iss"])
        headers = construct_headers(token_setup)

        # Safety check: Ensure this is logged into the correct user to change password on
        user_profile = api_utils.get(V2_GET_USER_PROFILE_BY_USER, custom_headers=headers)
        assert_that(user_profile["firstName"], "Unexpected first name").is_equal_to(
            PASSWORD_USER["firstname"]
        )
        assert_that(user_profile["lastName"], "Unexpected last name").is_equal_to(
            PASSWORD_USER["lastname"]
        )

        # Change user's password
        change_password = api_utils.post(
            V2_USER_LOCAL_PASSWORD, params=PL_CHANGE_PASSWORD, custom_headers=headers
        )
        assert_that(change_password, "Unexpected password change response").is_equal_to(
            MSG_PWD_CHANGE
        )

        # Check the last password no longer works
        token_old_pw = get_auth_token(PROD_URL, PASSWORD_USER, BASE_CREDS["iss"], return_json=False)
        assert_that(token_old_pw.status_code, "Could still login with old password").is_equal_to(
            401
        )

        # Check the current password does work
        token_new_pw = get_auth_token(PROD_URL, NEW_PW_USER_LOGIN, BASE_CREDS["iss"])
        assert_that(token_new_pw).is_not_empty()
        headers = construct_headers(token_new_pw)

        # Restore the old password (using log in with new password)
        restore_password = api_utils.post(
            V2_USER_LOCAL_PASSWORD,
            params=PL_RESTORE_PASSWORD,
            custom_headers=headers,
            return_json=False,
        )
        assert_that(restore_password.status_code, "Failed to restore old password").is_equal_to(200)

        # Confirm old password works again
        token_restore = get_auth_token(
            PROD_URL, PASSWORD_USER, BASE_CREDS["iss"], return_json=False
        )
        assert_that(
            token_restore.status_code, "Could not login with restored password"
        ).is_equal_to(200)
