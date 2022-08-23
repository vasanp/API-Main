from API_MainAssignment.src.helpers.user_helper import UserHelper
from API_MainAssignment.utilities.BaseClass import BaseClass
from API_MainAssignment.utilities.read_config import ConfigReader

# class for testing negative scenarios
class TestNegativeScenarios(BaseClass):
    # creating object of config file reader
    readconfig = ConfigReader()
    # creating object user helper class
    userObj = UserHelper()
    # creating object for logging
    log = BaseClass()
    logging = log.getlogger()

    # module for testing existing user account creation
    def test_validate_create_existing_user(self):
        # fetching user details from global config file
        user_details_exist = self.readconfig.read_negative_scenarios_creation_details()
        # sending request to create user
        cust_api_info = self.userObj.create_user(user_details=user_details_exist)


    # module for testing user login without account creation
    def test_validate_login_user_without_account_creation(self):
        user_credentials_not_exist = self.readconfig.read_negative_scenarios_login_details()
        # sending request
        cust_api_info = self.userObj.login_user(user_credentials=user_credentials_not_exist)
