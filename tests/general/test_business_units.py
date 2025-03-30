from datetime import datetime
import allure
import pytest
from assertpy import assert_that
from endpoints.v2.controller_buisness_unit import V2_BUSINESS_UNIT
from utils.api_utils import APIUtils
from utils.helper import BaseHelper

helper = BaseHelper()


class TestBusinessUnits:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def create_business_unit(api_utils, bu_name, bu_sub_id=None):
        """Create business unit"""
        pl_bu = {"name": bu_name, "subId": bu_sub_id}

        # The return response for a business unit is a bit odd
        #   {'id': {id, name, subId}, result}

        resp_bu = api_utils.post(V2_BUSINESS_UNIT, params=pl_bu)
        assert_that(
            resp_bu, f"Unexpected return from creating business unit from data {pl_bu}"
        ).contains_key("id")
        new_bu = resp_bu["id"]

        assert_that(
            resp_bu["result"],
            f"Expect at least 1 business unit after creating a new one from data {pl_bu}",
        ).is_greater_than(0)
        assert_that(
            new_bu["id"], f"Invalid ID on new business unit from data {pl_bu}"
        ).is_greater_than(0)
        assert_that(
            new_bu["name"], f"Incorrect name returned for new business unit from data {pl_bu}"
        ).is_equal_to(bu_name)
        assert_that(
            new_bu["subId"], f"Incorrect subId on new business unit from data {pl_bu}"
        ).is_equal_to(bu_sub_id)
        return new_bu

    @staticmethod
    def update_business_unit(api_utils, bu_id, bu_name, bu_sub_id=None):
        """Update business unit"""
        pl_bu = {"name": bu_name, "id": bu_id, "subId": bu_sub_id}

        # The return response for a business unit is different from create
        #   {'result': {id, name, subId}}

        resp_bu = api_utils.put(V2_BUSINESS_UNIT, params=pl_bu)
        assert_that(
            resp_bu, f"Unexpected return from updating business unit from data {pl_bu}"
        ).contains_key("result")
        updated_bu = resp_bu["result"]

        assert_that(
            updated_bu["id"], f"Invalid ID on new business unit from data {pl_bu}"
        ).is_greater_than(0)
        assert_that(
            updated_bu["name"], f"Incorrect name returned for new business unit from data {pl_bu}"
        ).is_equal_to(bu_name)
        assert_that(
            updated_bu["subId"], f"Incorrect subId on new business unit from data {pl_bu}"
        ).is_equal_to(bu_sub_id)
        return updated_bu

    @staticmethod
    def delete_business_unit(api_utils, bu_id):
        """Delete business unit"""
        pl_bu = {"id": bu_id}

        # The return response for deleting a business unit is the remaining existing data,
        # nothing returned related to the business unit that was deleted

        resp_bu = api_utils.delete(V2_BUSINESS_UNIT, params=pl_bu, return_json=False)
        assert_that(
            resp_bu.status_code, f"Unexpected return from deleting business unit from data {pl_bu}"
        ).is_equal_to(200)

    @staticmethod
    def check_deleted_business_unit(api_utils, deleted_bu_id):
        existing_business_units = api_utils.get(V2_BUSINESS_UNIT)["result"]
        for business_unit in existing_business_units:
            assert_that(
                business_unit["id"], f"Failed to delete business unit {business_unit}"
            ).is_not_equal_to(deleted_bu_id)

    @staticmethod
    def get_and_check_business_unit(api_utils, bu_id, bu_name="", bu_sub_id=None):
        """Get and validate single business unit data if name provided"""
        resp_bu = api_utils.get(V2_BUSINESS_UNIT + "/" + str(bu_id))
        assert_that(
            resp_bu, f"Unexpected result getting business unit from id {bu_id}"
        ).contains_key("result")
        found_bu = resp_bu["result"]

        if bu_name != "":
            assert_that(
                found_bu["name"],
                f"Unexpected business unit name in GET from id {bu_id} & name {bu_name}",
            ).is_equal_to(bu_name)
            assert_that(
                found_bu["subId"],
                f"Unexpected business unit subId from id {bu_id} & name {bu_name}",
            ).is_equal_to(bu_sub_id)

        return found_bu

    @allure.feature("Admin")
    @allure.story("Business Units")
    def test_add_update_delete_business_unit(self, api_utils):
        """Test Business Unit - Add, Update, and Delete"""
        bu_name = "AUTO_BU_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
        bu_name_edit = bu_name + "_edit"

        new_bu = self.create_business_unit(api_utils, bu_name=bu_name)
        self.update_business_unit(api_utils, new_bu["id"], bu_name_edit)
        self.get_and_check_business_unit(api_utils, new_bu["id"], bu_name_edit)
        self.delete_business_unit(api_utils, new_bu["id"])
        self.check_deleted_business_unit(api_utils, str(new_bu["id"]))

    @allure.feature("Admin")
    @allure.story("Business Units")
    def test_add_update_delete_business_unit_with_multiple_children(self, api_utils):
        """Test Business Unit - Add, Update, and Delete With Multiple Children"""

        # Intended data structure for this test:
        #   Parent
        #       - Level 1 (no children)
        #       - Level 2 (2 children)
        #           - Child 1
        #           - Child 2

        bu_parent_name = "AUTO_BU_PARENT_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
        bu_level1_name = "AUTO_BU_LEVEL1_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
        bu_level2_name = "AUTO_BU_LEVEL2_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
        bu_level2_child1_name = "AUTO_BU_LEVEL2_CHILD1_" + str(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )
        bu_level2_child2_name = "AUTO_BU_LEVEL2_CHILD2_" + str(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )

        bu_parent = self.create_business_unit(api_utils, bu_name=bu_parent_name)
        bu_level1 = self.create_business_unit(
            api_utils, bu_name=bu_level1_name, bu_sub_id=bu_parent["id"]
        )
        bu_level2 = self.create_business_unit(
            api_utils, bu_name=bu_level2_name, bu_sub_id=bu_parent["id"]
        )
        bu_level2_child1 = self.create_business_unit(
            api_utils, bu_name=bu_level2_child1_name, bu_sub_id=bu_level2["id"]
        )
        bu_level2_child2 = self.create_business_unit(
            api_utils, bu_name=bu_level2_child2_name, bu_sub_id=bu_level2["id"]
        )

        # Check everything is assigned the expected parent/child relationships
        self.get_and_check_business_unit(api_utils, bu_parent["id"], bu_parent_name)
        self.get_and_check_business_unit(
            api_utils, bu_level1["id"], bu_level1_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2["id"], bu_level2_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2_child1["id"], bu_level2_child1_name, bu_level2["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2_child2["id"], bu_level2_child2_name, bu_level2["id"]
        )

        # Rename the child and move it under the level 1 which has no children
        bu_level2_child1_rename = bu_level2_child1_name + "_edit"
        self.update_business_unit(
            api_utils, bu_level2_child1["id"], bu_level2_child1_rename, bu_level1["id"]
        )

        # Recheck all parent/child relationships
        self.get_and_check_business_unit(api_utils, bu_parent["id"], bu_parent_name)
        self.get_and_check_business_unit(
            api_utils, bu_level1["id"], bu_level1_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2["id"], bu_level2_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2_child1["id"], bu_level2_child1_rename, bu_level1["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2_child2["id"], bu_level2_child2_name, bu_level2["id"]
        )

        # Validate one child can be deleted and does not modify any other data
        self.delete_business_unit(api_utils, bu_level2_child2["id"])
        self.check_deleted_business_unit(api_utils, bu_level2_child2["id"])

        # Recheck all remaining parent/child relationships
        self.get_and_check_business_unit(api_utils, bu_parent["id"], bu_parent_name)
        self.get_and_check_business_unit(
            api_utils, bu_level1["id"], bu_level1_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2["id"], bu_level2_name, bu_parent["id"]
        )
        self.get_and_check_business_unit(
            api_utils, bu_level2_child1["id"], bu_level2_child1_rename, bu_level1["id"]
        )

        # Validate the parent is deleted with all children
        self.delete_business_unit(api_utils, bu_parent["id"])
        self.check_deleted_business_unit(api_utils, bu_level1["id"])
        self.check_deleted_business_unit(api_utils, bu_level2["id"])
        self.check_deleted_business_unit(api_utils, bu_level2_child1["id"])
