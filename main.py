"""Main file."""
import os
import time
from threading import Lock
from threading import Thread

import validators
from requests import get  # type: ignore

from websites import Website

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

website = Website("websites.txt")

data_lock = Lock()


class Client(Thread):
    def __init__(self, thread_name, websites, sleep_time: float = 0.0):
        Thread.__init__(self)
        self.thread_name = thread_name
        self.websites = websites
        self.sleep_time = sleep_time

    def run(self) -> None:
        while True:
            data_lock.acquire()
            websites_to_check = self.websites.get_next_website_to_check()
            data_lock.release()
            if websites_to_check is None:
                break
            self.check_url(websites_to_check)
            time.sleep(self.sleep_time)
        print(self.thread_name + " ended.")

    def check_url(self, data):
        try:
            valid_url_flag = validators.url(data["Website"])
            if valid_url_flag:
                data["valid_url_flag"] = True
                response = get(url=data["Website"], allow_redirects=True)
                data["status_code"] = response.status_code
            else:
                data["valid_url_flag"] = False
        except Exception as e:
            data["exception"] = e
        data_lock.acquire()
        self.websites.put_website_data(data)
        data_lock.release()


num_threads = 5
thread_list = []
num = 0

while num < num_threads:
    client = Client("T" + str(num), website, 0.2)
    thread_list.append(client)
    client.start()
    num += 1

for thread in thread_list:
    thread.join()

website.save_report()
print("Job done")
