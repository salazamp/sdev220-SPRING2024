# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:15:51 2024
created for sdev 220 fall 2024

@author: s.s.salama
"""

# 13.1) Write the current date as a string to the text file today.txt
import datetime
today = datetime.date.today()
file_ptr = open('today.txt', 'w')
file_ptr.write(str(today))
file_ptr.close()

# 13.2)Read the text file today.txt into the string today_string
file_ptr = open('today.txt', 'r')
today_date = file_ptr.read()
file_ptr.close()

# 13.3) Parse the date from today_string
today = datetime.datetime.strptime(today_date, '%Y-%m-%d').date()
print('Today is', today)

# 15.1 Use multiprocessing to create three separate processes.
import multiprocessing
from datetime import datetime
import time
import random


def print_time():
    now = datetime.now()
    print("Today's date and time is {}".format(now))
    time.sleep(random.random())


if __name__ == '__main__':
    proc1 = multiprocessing.Process(target=print_time())
    proc2 = multiprocessing.Process(target=print_time())
    proc3 = multiprocessing.Process(target=print_time())
    proc1.start()
    proc2.start()
    proc3.start()
    proc1.join()
    proc2.join()
    proc3.join()

    print('Completed')