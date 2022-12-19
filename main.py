"""Main file."""
import os
import time
from threading import Lock
from threading import Thread

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
            print(websites_to_check)
            time.sleep(self.sleep_time)
        print(self.thread_name + " ended.")


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
