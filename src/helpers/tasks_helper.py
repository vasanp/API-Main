from API_MainAssignment.utilities.genericUtilities import GenericUtilities

# Helper class for users
class TaskHelper:
    # creating constructor for generic utilities class
    def __init__(self):
        self.generic_utilities = GenericUtilities()

    # logic for adding a task
    def add_a_task(self, data, access_token):
        # creating payload
        payload = data
        # endpoint for request
        endpoint = "/task"
        # expected status code
        expected_status_code = 201
        # creating header with access token
        headers = {"Authorization": "Bearer {}".format(access_token), "Content-Type": "application/json"}
        # hitting the request and returning response
        response = self.generic_utilities.post(endpoint, payload=payload, headers=headers,
                                               expected_status_code=expected_status_code)
        return response

    # logic for fetching task details
    def fetch_tasks(self, access_token, params=None):
        # creating params
        params = params
        # endpoint for request
        endpoint = "/task"
        # expected status code
        expected_status_code = 200
        # creating headers for request
        headers = {"Authorization": "Bearer {}".format(access_token), "Content-Type": "application/json"}
        # hitting request and returning response
        response = self.generic_utilities.get(endpoint, params=params, headers=headers,
                                              expected_status_code=expected_status_code)
        return response
