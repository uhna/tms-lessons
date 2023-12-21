from datetime import datetime
import pytest
from Lesson_26_api.practice.pages.pet_page import PetPage
from Lesson_26_api.practice.config import Config
from Lesson_26_api.practice.pages.user_page import UserPage

PET_NAME = "TMS_dog_{}"
USERNAME = "TMS_class_{}"


@pytest.fixture(scope="session")
def cfg():
    return Config()


@pytest.fixture(scope="session")
def host(cfg):
    return cfg.HOST


@pytest.fixture
def pet_info():
    current_timestamp = int(datetime.now().timestamp())
    data = {
        "id": 0,
        "category": {"id": 0, "name": "string"},
        "name": PET_NAME.format(current_timestamp),
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }
    return data


@pytest.fixture
def user_info():
    current_timestamp = int(datetime.now().timestamp())
    data = {
        "id": 0,
        "username": USERNAME.format(current_timestamp),
        "firstName": f"Tms_firstname_{current_timestamp}",
        "lastName": f"Tms_lastname_{current_timestamp}",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    return data


@pytest.fixture(scope="session")
def pet_api(host):
    api = PetPage(host=host)
    return api


@pytest.fixture(scope="session")
def user_api(host):
    api = UserPage(host=host)
    return api


@pytest.fixture(scope="session")
def response_200():
    def _assert(response):
        assert response.ok, f"{response.status_code = }"
    return _assert


@pytest.fixture(scope="session")
def check_name():
    def _check_name(response, expected_name, data):
        json_data = response.json()
        assert json_data[data] == expected_name, f"{json_data[data] = }"
    return _check_name


@pytest.fixture(scope="session")
def assert_key():
    def _assert_key(data, expected_keys):
        err_msg = f"There were unexpected keys, {data}"
        assert data == expected_keys, err_msg
    return _assert_key

