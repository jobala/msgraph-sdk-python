from network.ABCRequests import ABCRequests
import requests


class Requests(ABCRequests):
    def get(self, path, token):
        headers = {'Authorization': 'Bearer {}'.format(token)}
        result = requests.get(path, headers=headers)
        return result.json()

