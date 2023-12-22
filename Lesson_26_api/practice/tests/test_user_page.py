from Lesson_26_api.practice.pages.helpers import Helpers


class TestUser:
    def test_add_get_user(self, a_user, key_get_user, user_info, user_api):
        username = user_info["username"]
        response_get = user_api.get_user_by_username(username)
        key = list(response_get.json().keys())

        Helpers.check_response(response_get)
        Helpers.check_name(response_get, username, "username")
        Helpers.assert_key(key, key_get_user)

    def test_update_user(self, a_user, user_api, user_info):
        username = user_info["username"]
        firstname = user_info["firstName"]
        new_firstname = firstname.replace("TMS_", "NEW_")
        user_info["firstName"] = new_firstname

        user_api.put_user(username, user_info)
        response_get = user_api.get_user_by_username(username)

        Helpers.check_response(response_get)
        Helpers.check_name(response_get, new_firstname, "firstName")

    def test_delete_user(self, a_user):
        pass
