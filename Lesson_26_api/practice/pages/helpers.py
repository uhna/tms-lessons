class Helpers:
    @classmethod
    def check_response(cls, response):
        assert response.ok, f"{response.status_code = }"

    @classmethod
    def check_name(cls, response, expected_name, name):
        json_data = response.json()
        assert json_data[name] == expected_name, f"{json_data[name] = }"

    @classmethod
    def assert_key(cls, data, expected_keys):
        err_msg = f"There were unexpected keys, {data}"
        assert data == expected_keys, err_msg
