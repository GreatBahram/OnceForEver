#!/usr/bin/env python3
from multiprocessing import Pool

jobs = [
        (1, 'Mat', 'Fraser'),
        (2, 'Rich', 'Froning'),
        (3, 'Brooke', 'Ence'),
        (4, 'Tia', 'Toomey'),
        ]


def simple_func(args):
    number, fname, lname = args
    return (number, fname)


def main():
    # map method example
    with Pool() as pool:
        results = pool.map(simple_func, jobs)
    for result in results:
        print(result[0], result[1])

    # imap method example
    with Pool() as pool:
        for result in pool.imap(simple_func, jobs):
            print(result[0], result[1])


    # imap_unordered method example
    with Pool() as pool:
        for result in pool.imap_unordered(simple_func, jobs):
            print(result[0], result[1])

    # starmap method example, take note there is no need to unpack the arguments
    def custom_func(number, fname, lname):
        return (number, fname)

    with Pool() as pool:
        results = pool.starmap(custom_func, jobs)
        for result in results:
            print(result[0], result[1])

if __name__ == '__main__':
    main()

