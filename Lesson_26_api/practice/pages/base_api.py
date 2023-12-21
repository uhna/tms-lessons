import requests


class BaseApi:
    def __init__(self, host):
        self.host = host

    def get(self, path):
        response = requests.get(self.host + path)
        return response

    def post(self, path, data=None):
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.host + path, data=data, headers=headers)
        return response

    def put(self, path, data=None):
        headers = {"Content-Type": "application/json"}
        response = requests.put(self.host + path, data=data, headers=headers)
        return response

    def delete(self, path):
        response = requests.delete(self.host + path)
        return response
