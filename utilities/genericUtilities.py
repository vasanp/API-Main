import requests
import json

from API_MainAssignment.utilities.read_config import ConfigReader


class GenericUtilities:

    def __init__(self):
        # creating object for global config file reader
        self.objconfig = ConfigReader()
        # fetching base url from config file
        self.base_url = self.objconfig.read_request_details()

    # post method
    def post(self, endpoint, payload, headers=None, expected_status_code=None):
        # if headers not available , assign default headers
        if not headers:
            headers = {"Content-Type": "application/json"}

        # if expected status code not available , assign default status code
        if not expected_status_code:
            expected_status_code = 200

        # constructing url
        url = self.base_url + endpoint
        # hitting request
        response = requests.post(url=url, data=json.dumps(payload), headers=headers)
        # assertion of status code
        #assert expected_status_code == int(response.status_code)
        # returning response
        return response

    # Get Method
    def get(self, endpoint, params=None, headers=None, expected_status_code=None):
        # if headers not available , assign default headers
        if not headers:
            headers = {"Content-Type": "application/json"}

        # if expected status code not available , assign default status code
        if not expected_status_code:
            expected_status_code = 200

        # constructing url
        url = self.base_url + endpoint
        # hitting request
        response = requests.get(url=url, params=params, headers=headers)
        # assertion of status code
        #assert expected_status_code == int(response.status_code)
        # returning response
        return response
