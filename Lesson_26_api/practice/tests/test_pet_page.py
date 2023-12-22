from Lesson_26_api.practice.pages.helpers import Helpers


class Status:
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class TestPetStore:
    def test_create_pet(self, a_pet):
        pass

    def test_read_pet_available(self, a_pet, pet_api, key_get_pet):
        response = pet_api.get_pets_by_status(Status.AVAILABLE)
        json_data = response.json()
        first_pet = json_data[0]
        key = list(first_pet.keys())

        Helpers.assert_key(key, key_get_pet)

    def test_update_pet(self, a_pet, pet_api, pet_info):
        # Arrange
        name_current = pet_info["name"]
        name_new = name_current.replace("TMS_", "SMS_")
        pet_info["name"] = name_new

        # Act
        response_put = pet_api.update_pet(pet_info)
        pet_id = response_put.json()["id"]
        response_get = pet_api.get_pet_id(pet_id)

        # Assert
        Helpers.check_name(response_get, name_new, "name")

    def test_delete_pet(self, a_pet):
        pass
