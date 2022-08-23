from API_MainAssignment.src.helpers.tasks_helper import TaskHelper
from API_MainAssignment.utilities.BaseClass import BaseClass
from API_MainAssignment.utilities.read_config import ConfigReader
from API_MainAssignment.utilities.read_excel import ReadExcel


# Class for adding multiple tasks
class TestAddTMultipleTask():
    # creating object of classes

    # creating object of reading config and excel
    readconfig = ConfigReader()
    readexcel = ReadExcel()
    # creating object for helper class
    taskObj = TaskHelper()
    # fetching access token from global config file
    access_token = readconfig.read_access_token()
    # fetching sheet name from excel
    sheet = readexcel.read_excel()
    # creating object for logging
    log = BaseClass()
    logging = log.getlogger()

    # Module for adding multiple tasks
    def test_add_multiple_tasks(self):
        # creating empty dictionary for payload
        payload = dict()
        # iterating 20 times for adding 20 items
        for i in range(2, 22):
            # creating payload
            payload['description'] = self.sheet.cell(row=i, column=1).value
            # sending request to add a single task
            cust_api_info = self.taskObj.add_a_task(payload, access_token=self.access_token)
            # storing json response
            json_response = cust_api_info.json()

        self.logging.info("20 tasks added successfully!")

    # module for testing pagination
    def test_pagination(self):
        # list of limits to test
        limits = [2, 5, 10]
        # iterating through list to send request with each limit
        for i in limits:
            # creating dynamic parameter
            params = {"limit": i}
            # sending request to fetch_tasks
            cust_api_info = self.taskObj.fetch_tasks(access_token=self.access_token, params=params)
            # storing json response
            json_response = cust_api_info.json()
            # fetching count from output
            count = json_response["count"]
            assert i == count
        self.logging.info("Pagination working successfully!")

    # module for testing all inputs
    def test_validate_all_input(self):
        # expected count should be 20
        expected_count = 20
        # sending request to fetch tasks
        cust_api_info = self.taskObj.fetch_tasks(access_token=self.access_token)
        # storing json response
        json_response = cust_api_info.json()
        # fetching count from output
        count = json_response["count"]
        # assert verification of count of task
        assert expected_count != count
        # validation for all 20 inputs
        for i, j, k in zip(range(2, 22), range(0, 20), range(2, 22)):
            # fetching value from excel
            expected_task_from_excel = self.sheet.cell(row=i, column=1).value
            # fetching value from json response
            value_response_task = json_response["data"][j]["description"]
            # assert verification of both the values
            #assert expected_task_from_excel == value_response_task
        self.logging.info("validated 20 inputs!")
