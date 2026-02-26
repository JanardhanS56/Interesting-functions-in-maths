#Implements a stochastic integer transformation process on the set {1, …, 1000}. At each step, two random elements are selected, replaced by their absolute difference, and the process repeats until one value remains.

#Despite the randomness, the final result is deterministic due to invariance of the set’s greatest common divisor (gcd). This demonstrates a multiset extension of the Euclidean algorithm and highlights how algebraic invariants govern seemingly random discrete systems.

import numpy as np

numbers = np.arange(1, 1001)

while len(numbers) > 1:
    i, j = np.random.choice(len(numbers), 2, replace=False)

    m = numbers[i]
    n = numbers[j]

    d = abs(m - n)

    # remove larger index first to avoid shifting issues
    for index in sorted([i, j], reverse=True):
        numbers = np.delete(numbers, index)

    numbers = np.append(numbers, d)

print(numbers)
