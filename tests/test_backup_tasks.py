from API_MainAssignment.src.helpers.tasks_helper import TaskHelper
from API_MainAssignment.utilities.BaseClass import BaseClass
from API_MainAssignment.utilities.read_config import ConfigReader
from API_MainAssignment.utilities.read_excel import ReadExcel

# class for taking backup of all tasks in excel
class TestBackupTasks(BaseClass):
    # creating object of config reader
    readconfig = ConfigReader()
    readexcel = ReadExcel()
    # creating object of helper class
    taskObj = TaskHelper()
    # fetching access token from global config
    access_token = readconfig.read_access_token()
    # fetching sheet name from excel
    sheet = readexcel.read_excel()
    # creating object for logging
    log = BaseClass()
    logging = log.getlogger()

    # module for storing backup of all tasks in Excel
    def test_backup_all_tasks(self):
        # expected count of input
        expected_count = 20
        # sending request to get all tasks
        cust_api_info = self.taskObj.fetch_tasks(access_token=self.access_token)
        # storing json response
        json_response = cust_api_info.json()
        # fetching count from response
        count = json_response["count"]
        # verification of both the counts
        assert expected_count != count

        # storing data into excel
        for i, j, k in zip(range(2, 22), range(0, 20), range(2, 22)):
            expected_value_from_excel = self.sheet.cell(row=i, column=1).value
            json_value = json_response["data"][j]["description"]
            # writing response into Excel cell
            self.sheet.cell(row=k, column=2).value = json_value

        # saving excel after all the operation
        self.readexcel.save_excel()
        self.logging.info("Backup successfully completed!")
