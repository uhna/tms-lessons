class TestUser:
    def test_add_user(self, user_api, user_info, response_200, ):
        response = user_api.add_user(user_info)

        response_200(response)
        username = user_info["username"]
        user_api.delete_user(username)

    def test_get_user_username(self, user_api, user_info, response_200,
                               assert_key):
        user_api.add_user(user_info)
        username = user_info["username"]
        response = user_api.get_user_by_username(username)
        json_data = response.json()
        expected_key = [
            'id',
            'username',
            'firstName',
            'lastName',
            'email',
            'password',
            'phone',
            'userStatus'
        ]
        assert_key(list(json_data.keys()), expected_key)
        user_api.delete_user(username)

    def test_update_user(self, user_api, user_info, response_200, check_name):
        user_api.add_user(user_info)
        username = user_info["username"]
        firstname = user_info["firstName"]
        new_firstname = firstname.replace("TMS_", "NEW_")
        user_info["firstName"] = new_firstname

        response = user_api.put_user(username, user_info)
        response_get = user_api.get_user_by_username(username)

        response_200(response)
        check_name(response_get, new_firstname, "firstName")

        user_api.delete_user(username)

    def test_delete_user(self, user_api, user_info, response_200):
        user_api.add_user(user_info)
        username = user_info["username"]

        response_del = user_api.delete_user(username)
        response_get = user_api.get_user_by_username(username)
        json_data = response_get.json()

        response_200(response_del)
        assert json_data["message"] == "User not found", "User isn't deleted"
