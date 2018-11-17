#!/usr/bin/env python3
import multiprocessing
import time

COUNT = 85_000_000

def countdown(number):
    while number > 0:
        number -= 1

if __name__ == '__main__':
    print('Start of program.')

    start_time = time.time()

    process1 = multiprocessing.Process(target=countdown, args=(COUNT//2,))
    process2 = multiprocessing.Process(target=countdown, args=(COUNT//2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()

    print('End of program.')

    print(f'Countdown took {int(end_time - start_time)} seconds')
