import json


def test_son_file():
    with open("HW_Files.txt", "r") as file:
        lines = file.read().splitlines()

    some_dict = {}
    for line in lines:
        name, surname = line.strip().split(',')
        some_dict[name] = surname

    sorted_data = dict(sorted(some_dict.items()))

    with open('new_file.json', 'w') as json_file:
        json.dump(sorted_data, json_file, ensure_ascii=False, indent=4,
                  sort_keys=True)
