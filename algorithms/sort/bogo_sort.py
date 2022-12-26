import random


numbers = [8, 1, 18, 55, 1, 5, 98, 7, 3, 5500, 5501, 520, 21, 8]


def is_sorted(values: list[int]):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values: list[int]):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    print(attempts)
    return values


print(bogo_sort(numbers))
