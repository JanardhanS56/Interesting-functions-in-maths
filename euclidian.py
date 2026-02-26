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
