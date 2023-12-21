from Lesson_26_api.practice.pages.base_api import BaseApi
import json


class UserPage(BaseApi):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.USER = "/user"
        self.USER_NAME = "/user/{}"

    def get_user_by_username(self, username):
        url = f"{self.USER_NAME.format(username)}"
        response = self.get(url)
        return response

    def add_user(self, data):
        url = f"{self.USER}"
        response = self.post(url, data=json.dumps(data))
        return response

    def put_user(self, username, data):
        url = f"{self.USER_NAME.format(username)}"
        response = self.put(url, data=json.dumps(data))
        return response

    def delete_user(self, username):
        url = f"{self.USER_NAME.format(username)}"
        response = self.delete(url)
        return response
