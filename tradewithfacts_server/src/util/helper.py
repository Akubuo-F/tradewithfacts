import os
from abc import ABC


class Helper(ABC):

    @staticmethod
    def get_root_directory() -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        while not os.path.basename(current_dir) == 'src':
            current_dir = os.path.dirname(current_dir)
        return os.path.dirname(current_dir)

    @staticmethod
    def get_storage(filename: str):
        root_dir = Helper.get_root_directory()
        storage_path = os.path.join(root_dir, 'storage', filename)
        return storage_path


if __name__ == '__main__':
    print(Helper.get_root_directory())
    print(Helper.get_storage('10yr_cot_report.csv'))