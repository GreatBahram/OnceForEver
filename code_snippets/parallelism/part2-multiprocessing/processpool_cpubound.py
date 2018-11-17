#!/usr/bin/env python3
import time
from multiprocessing import Pool, cpu_count

COUNT = 85_000_000

def countdown(number):
    while number > 0:
        number -= 1

if __name__ == '__main__':
    print('Start of program.')

    start_time = time.time()
    num_of_process = cpu_count()
    
    jobs = [COUNT//2, COUNT//2]

    with Pool(processes=num_of_process) as pool:
        pool.map(countdown, jobs)

    end_time = time.time()

    print('End of program.')

    print(f'Countdown took {int(end_time - start_time)} seconds')
