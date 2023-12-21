import json
from Lesson_26_api.practice.pages.base_api import BaseApi


class PetPage(BaseApi):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.PET = "/pet"
        self.FIND_BY_STATUS = "/pet/findByStatus?status={}"
        self.PET_PET_ID = "/pet/{petId}"

    def get_pets_by_status(self, target_status):
        url = f"{self.FIND_BY_STATUS.format(target_status)}"
        response = self.get(url)
        return response

    def get_pet_id(self, pet_id):
        url = f"{self.PET_PET_ID.format(petId=pet_id)}"
        response = self.get(url)
        return response

    def add_new_pet(self, data):
        url = f"{self.PET}"
        response = self.post(url, data=json.dumps(data))
        return response

    def update_pet(self, data):
        url = f"{self.PET}"
        response = self.put(url, data=json.dumps(data))
        return response

    def delete_pet(self, pet_id):
        url = f"{self.PET_PET_ID.format(petId=pet_id)}"
        response = self.delete(url)
        return response
