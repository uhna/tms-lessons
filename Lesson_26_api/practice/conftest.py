from datetime import datetime
import pytest

from Lesson_26_api.practice.pages.helpers import Helpers
from Lesson_26_api.practice.pages.pet_page import PetPage
from Lesson_26_api.practice.config import Config
from Lesson_26_api.practice.pages.user_page import UserPage

PET_NAME = "TMS_dog_{}"
USERNAME = "TMS_class_{}"


@pytest.fixture(scope="session")
def host():
    return Config().HOST


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


@pytest.fixture
def key_get_user():
    data = [
        'id',
        'username',
        'firstName',
        'lastName',
        'email',
        'password',
        'phone',
        'userStatus'
    ]
    return data


@pytest.fixture
def key_get_pet():
    data = [
        'id',
        'category',
        'name',
        'photoUrls',
        'tags',
        'status',
    ]
    return data


@pytest.fixture(scope="session")
def pet_api(host):
    api = PetPage(host=host)
    return api


@pytest.fixture(scope="session")
def user_api(host):
    api = UserPage(host=host)
    return api


@pytest.fixture
def a_user(user_api, user_info):
    username = user_info["username"]
    user_api.add_user(user_info)
    yield user_info
    user_api.delete_user(username)
    response_get = user_api.get_user_by_username(username)
    json_data = response_get.json()
    assert json_data["message"] == "User not found", "User isn't deleted"


@pytest.fixture
def a_pet(pet_info, pet_api):
    response_add = pet_api.add_new_pet(pet_info)
    Helpers.check_name(response_add, pet_info["name"], "name")
    pet_id = response_add.json()["id"]
    yield pet_id
    response_del = pet_api.delete_pet(pet_id)
    Helpers.check_response(response_del)
    response_get_id = pet_api.get_pet_id(pet_id)
    json_get = response_get_id.json()
    assert json_get["message"] == "Pet not found", "Pet isn't deleted"

