import json
import os
from abc import ABC
from json import JSONDecodeError


class Helper(ABC):

    @staticmethod
    def get_root_directory() -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        while not os.path.basename(current_dir) == 'src':
            current_dir = os.path.dirname(current_dir)
        return os.path.dirname(current_dir)

    @staticmethod
    def get_storage(storage_name) -> str:
        root_dir = Helper.get_root_directory()
        storage_path = os.path.join(root_dir, 'storage', storage_name)
        return storage_path

    @staticmethod
    def get_storage_details(storage_name: str) -> dict:
        storage_path = Helper.get_storage(storage_name)
        storage_details_path = os.path.join(storage_path, "storage_details.json")
        try:
            with open(storage_details_path, "r") as jsonFile:
                return json.load(jsonFile)
        except JSONDecodeError:
            return {}

    @staticmethod
    def update_storage_details(storage_name, details: dict) -> None:
        storage_path = Helper.get_storage(storage_name)
        storage_details_path = os.path.join(storage_path, "storage_details.json")
        with open(storage_details_path, "w") as jsonFile:
            # noinspection PyTypeChecker
            json.dump(details, jsonFile)



if __name__ == '__main__':
    mock_storage_name = "cot_report"
    mock_details = {
        "as_of": "2024-10-29",
        "storage": "10yr_cot_report.csv"
    }
    print(Helper.get_root_directory())
    print(Helper.get_storage(mock_storage_name))
    print(Helper.get_storage_details(mock_storage_name))
    Helper.update_storage_details(mock_storage_name, mock_details)