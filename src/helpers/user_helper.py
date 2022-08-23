from API_MainAssignment.utilities.BaseClass import BaseClass
from API_MainAssignment.utilities.genericUtilities import GenericUtilities
from API_MainAssignment.utilities.read_config import ConfigReader

# Helper class for users
class UserHelper:
    # creating constructor for generic utilities class
    def __init__(self):
        self.generic_utilities = GenericUtilities()
        self.readconfig = ConfigReader()

    # creating object of logging class
    log = BaseClass()
    logging = log.getlogger()

    # logic for create user module
    def create_user(self, user_details=None, expected_status_code=None):
        # if user details not available, assign default
        if not user_details:
            user_details = self.readconfig.read_create_user_details()

        # if expected status code not available, assign default
        if not expected_status_code:
            expected_status_code = 201

        # expected email from response
        expected_email = user_details["email"]
        # attaching user details to payload
        payload = user_details
        # endpoint for request
        endpoint = "/user/register"
        # expected status code
        expected_status_code = expected_status_code
        # hitting request
        response = self.generic_utilities.post(endpoint, payload=payload, expected_status_code=expected_status_code)
        # storing response in json
        response_status_code = response.status_code
        json_response = response.json()
        # email from response
        # verification of both the emails
        if response_status_code == 201:
            output_email = json_response["user"]["email"]
        else:
            self.logging.info("user already exists")
            return False

        if expected_email == output_email:
            self.logging.info("user Created")
            return True
        else:
            return False

    # logic for login user module
    def login_user(self, user_credentials=None, expected_status_code=None):
        global access_token
        # if user credentials not available, assign default
        if not user_credentials:
            user_credentials = self.readconfig.read_create_user_details()

        # if expected status code not available, assign default
        if not expected_status_code:
            expected_status_code = 200

        # attaching user creds to payload
        payload = user_credentials
        # endpoint for request
        endpoint = "/user/login"
        expected_status_code = expected_status_code
        # expected status code
        response = self.generic_utilities.post(endpoint, payload=payload, expected_status_code=expected_status_code)
        # storing response in json
        response_status_code = response.status_code
        json_response = response.json()
        # fetching access token to write in Global Config file
        if response_status_code == 200:
            access_token = json_response["token"]
            self.readconfig.write_config_file(access_token=access_token)
        else:
            self.logging.info("unable to login, please create account")
            return False

        # expected email from response
        expected_email = user_credentials["email"]
        output_email = json_response["user"]["email"]
        # verification of both the emails
        if expected_email == output_email:
            self.logging.info("user validated")
            return True
        else:
            return False
