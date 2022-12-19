"""Services used to run main file"""
from typing import Any


class Website:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.website_list: list[dict[str, Any]] = []
        self.index = 0
