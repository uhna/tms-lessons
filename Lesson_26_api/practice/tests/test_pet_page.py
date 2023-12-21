class Status:
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class TestPetStore:
    def test_create_pet(self, pet_api, pet_info, response_200, check_name):
        response = pet_api.add_new_pet(pet_info)

        response_200(response)
        check_name(response, pet_info["name"], "name")

        pet_id = response.json()["id"]
        pet_api.delete_pet(pet_id)

    def test_read_pet_available(self, pet_api, response_200, assert_key):
        response = pet_api.get_pets_by_status(Status.AVAILABLE)

        # Assert
        response_200(response)
        json_data = response.json()
        first_pet = json_data[0]
        expected_keys = [
            'id',
            'category',
            'name',
            'photoUrls',
            'tags',
            'status',
        ]
        assert_key(list(first_pet.keys()), expected_keys)

    def test_update_pet(self, pet_api, pet_info, response_200, check_name):
        # Arrange
        response_post = pet_api.add_new_pet(pet_info)
        json_data = response_post.json()
        pet_id = json_data["id"]
        name_current = json_data["name"]
        name_new = name_current.replace("TMS_", "SMS_")
        json_data["name"] = name_new

        # Act
        response_put = pet_api.update_pet(json_data)
        response_get = pet_api.get_pet_id(pet_id)

        # Assert
        response_200(response_put)
        check_name(response_get, name_new, "name")

        pet_api.delete_pet(pet_id)

    def test_delete_pet(self, pet_api, pet_info, response_200):
        # Arrange
        response_post = pet_api.add_new_pet(pet_info)
        json_data = response_post.json()
        pet_id = json_data["id"]

        # Act
        response_del = pet_api.delete_pet(pet_id)
        response_get_id = pet_api.get_pet_id(pet_id)
        json_get = response_get_id.json()

        # Assert
        response_200(response_del)
        assert json_get["message"] == "Pet not found", "Pet isn't deleted"