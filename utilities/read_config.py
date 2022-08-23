import json
from configparser import ConfigParser
from pathlib import Path


# class for reading config file
class ConfigReader:
    # fetching config file
    file = Path(
        '/Users/vasanp/PycharmProjects/pythonProject/API_MainAssignment/utilities/Config.ini')
    config = ConfigParser()
    config.read(file)
    config.read('{0} in {1}'.format(file, 'Config.ini'))

    # reading data from config files for request details
    def read_request_details(self):
        request_details = self.config['request details']['url']
        return request_details

    # reading data from config files for user details
    def read_create_user_details(self):
        user_details = json.loads(self.config.get('account creation details', 'user_details'))
        return user_details

    # reading data from config files for login user details
    def read_login_user_details(self):
        user_credentials = json.loads(self.config.get('credentials', 'user_credentials'))
        return user_credentials

    # reading data from config files for task details
    def read_user_task_details(self):
        user_task_details = json.loads(self.config.get('Task details', 'task_details'))
        return user_task_details

    # reading data from config files for negative scenarios user details
    def read_negative_scenarios_creation_details(self):
        user_details_existing = json.loads(self.config.get('negative scenarios details', 'user_details_exist'))
        return user_details_existing

    # reading data from config files for negative scenarios user login details
    def read_negative_scenarios_login_details(self):
        user_credentials_not_exist = json.loads(
            self.config.get('negative scenarios details', 'user_credentials_not_exist'))
        return user_credentials_not_exist

    # writing data into config files for access token
    def write_config_file(self, access_token):
        self.config.set('Access token', 'token', access_token)  # Writing new entry
        self.config.write(self.file.open("w"))

    # reading data from config files for access token
    def read_access_token(self):
        user_access_token = self.config['Access token']['token']
        return user_access_token
