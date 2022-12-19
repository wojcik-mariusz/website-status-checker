"""Main file."""
import os
import time
from threading import Thread

from websites import Website

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

website = Website("websites.txt")


class Client(Thread):
    def __init__(self, thread_name, websites, sleep_time: float = 0.0):
        Thread.__init__(self)
        self.thread_name = thread_name
        self.websites = websites
        self.sleep_time = sleep_time

    def run(self) -> None:
        while True:
            websites_to_check = self.websites.get_next_website_to_check()
            if websites_to_check is None:
                break
            print(websites_to_check)
            time.sleep(self.sleep_time)
        print(self.thread_name + " ended.")
