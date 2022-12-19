"""Services used to run main file"""
from typing import Any


class Website:
    def __init__(self, file_name: str):
        """f
        ile_name: file name with web names inside,
        required to read name of websites
        website_list: list contain dict of name of websites as key,
        and some informations like status code as values
        """
        self.file_name = file_name
        self.website_list: list[dict[str, Any]] = []
        self.index = 0

    def load_file(self):
        pass

    def get_next_website_to_check(self):
        pass

    def put_website_data(self):
        pass

    def save_report(self):
        pass
