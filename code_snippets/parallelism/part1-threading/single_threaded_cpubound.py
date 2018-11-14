#!/usr/bin/env python3

import threading
import time

COUNT = 50_000_000

def countdown(number):
    while number > 0:
        number -= 1

if __name__ == '__main__':
    print('Start of program.')

    start_time = time.time()

    countdown(COUNT)

    end_time = time.time()

    print('End of program.')

    print(f'Countdown took {int(end_time - start_time)} seconds')
