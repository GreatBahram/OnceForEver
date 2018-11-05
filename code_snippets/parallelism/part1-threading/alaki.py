#!/usr/bin/env python3

import threading
import time


def long_function(name):
    """ just wasting time"""
    time.sleep(5)
    print(name)

def main():

    print('Start of the program.')
    
    # instanciate the Thread class
    thread = threading.Thread(target=long_function, args=('bahram', ))

    # run the thread
    thread.run()

    # wait until the thread is finished
    thread.join()

    print('End of the program.')

if __name__ == '__main__':
    main()
