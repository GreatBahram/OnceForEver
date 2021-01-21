from typing import List


large_a = list(range(1000))
large_b = list(range(1000))


def approach_1(x: List[int], w: List[int]) -> int:
    """Generate index; access items; add them."""
    z = 0.0
    for i in range(len(x)):
        z += x[i] * w[i]
    return z


def approach_2(x: List[int], w: List[int]) -> int:
    """Using functional operators."""
    import operator

    return sum(map(operator.mul, x, w))


import numpy as np
large_a, large_b = np.arange(1000), np.arange(1000)

def approach_3(x: List[int], w: List[int]) -> int:
    """They say NumPy is fast!"""

    return np.dot(x, w)


########################################################

import time

start_time = time.perf_counter()

total = 0

for _ in range(100_000_000):
    total += 1

elapsed_time = time.perf_counter() - start_time

print("It took {:0.1f} seconds.".format(elapsed_time))

########################################################

import timeit
setup = "import numpy as np"
stmt = "np.sum(np.arange(1000))"
timeit.timeit(stmt=stmt, setup=setup, number=1_000)
timeit.timeit(stmt=stmt, setup=setup, number=10_000)
# the return value is in seconds.

########################################################

topic = "timing and profiling"
timeit.timeit("print(topic)", number=1)

# Fix the problem using globals
timeit.timeit("print(topic)", number=1, globals=globals())

# Fix the problem using import statment
timeit.timeit("print(topic)", setup="from __main__ import topic", number=1)

########################################################

import timeit 

timeit.timeit("approach_1(large_a, large_b)", globals=globals(), number=10_000)
timeit.timeit("approach_2(large_a, large_b)", globals=globals(), number=10_000)

setup = """
import numpy as np

large_a, large_b = np.arange(1000), np.arange(1000)

from __main__ import approach_3
"""

timeit.timeit("approach_3(large_a, large_b)", setup=setup, number=10_000)

########################################################

%timeit approach_1(large_a, large_b)

%timeit approach_2(large_a, large_b)

import numpy as np

large_a, large_b = np.arange(1000), np.arange(1000)


def approach_3(x: List[int], w: List[int]) -> int:
    """They say NumPy is fast!"""
    return np.dot(x, w)

%timeit approach_3(large_a, large_b)

########################################################

import time


def an_expensive_function(times: int):
    time.sleep(times)


def main():
    print("Start")
    an_expensive_function(1)
    an_expensive_function(3)
    an_expensive_function(1)
    print("End")


if __name__ == "__main__":
    main()


python3 -m cProfile -o output.prof profile_this.py

pip install snakeviz

snakeviz output.prof

