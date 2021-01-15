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


def approach_3(x: List[int], w: List[int]) -> int:
    """They say NumPy is fast!"""
    import numpy as np

    x, y = np.array(x), np.array(w)

    return np.dot(x, w)


import time

start_time = time.perf_counter()

total = 0

for _ in range(100_000_000):
    total += 1

elapsed_time = time.perf_counter() - start_time

print("It took {:0.1f} seconds.".format(elapsed_time))
