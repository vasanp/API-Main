import pytest

from API_MainAssignment.src.helpers.tasks_helper import TaskHelper
from API_MainAssignment.src.helpers.user_helper import UserHelper
from API_MainAssignment.utilities.BaseClass import BaseClass
from API_MainAssignment.utilities.read_config import ConfigReader

# class for creating account and adding task

class TestAddTask():
    # creating objects of classes
    readconfig = ConfigReader()
    # creating object of helper classes
    userObj = UserHelper()
    taskObj = TaskHelper()
    # creating object for logging
    log = BaseClass()
    logging = log.getlogger()
    # fetching access token from global config file
    access_token = readconfig.read_access_token()

    # module for creating new user
    def test_create_user(self):
        cust_api_info = self.userObj.create_user()

    # module for login user
    def test_login_user(self):
        cust_api_info = self.userObj.login_user()

    # module for adding a new single task
    def test_add_single_task(self):
        # fetching user task details from global config file
        user_task_details = self.readconfig.read_user_task_details()
        # sending request to add a task
        cust_api_info = self.taskObj.add_a_task(user_task_details, access_token=self.access_token)
        # storing json response
        json_response = cust_api_info.json()

        # assertion for verification of request
        expected_task = user_task_details["description"]
        new_task_added = json_response["data"]["description"]
        assert expected_task == new_task_added
        self.logging.info("One task successfully added!")
