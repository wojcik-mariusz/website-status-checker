"""Services used to run main file"""
from typing import Any


class Website:
    def __init__(self, file_name: str):
        """file_name: file name with web names inside,
        required to read name of websites
        website_list: list contain dict of name of websites as key,
        and some information like status code as values
        """
        self.file_name = file_name
        self.website_list: list[dict[str, Any]] = []
        self.index = 0
        self.load_file(file_name)

    def load_file(self, file_name):
        """
        This function load file to memory, and create website list that
        contains website address with https, and index, status code.
        """
        with open(file=file_name, mode="r") as fh:
            data_list = fh.readlines()
            for v in data_list:
                v = "https://" + v.strip()
                data = {"Website": v, "status_code": -1}
                self.website_list.append(data)
                data["index"] = len(self.website_list) - 1

    def get_next_website_to_check(self):
        if self.index > len(self.website_list):
            return None

        data = self.website_list[self.index]
        self.index += 1
        return data

    def put_website_data(self):
        pass

    def save_report(self):
        pass
