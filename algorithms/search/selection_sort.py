numbers = [8, 1, 18, 55, 1, 5, 98, 7, 3, 5500, 5501, 520, 21, 8]


def is_sorted(values: list[int]):
    """Iterates over list values comparing to next value
    Returns True if the list is sorted ascending.
    Runs in constant time O(1)
    """
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def idx_of_min(values: list[int]):
    """From a list, returns the value with the lowest value
    Runs in constant time O(1)
    """
    min_idx = 0
    for idx in range(len(values[1:])):
        if values[idx] < values[min_idx]:
            min_idx = idx
    return min_idx


def selection_sort(values: list[int]):
    """Sort via finding the lowest value for each item in list
    Exactly as it seems, worse case is O(n^2), quite inefficient
    """
    sorted_list: list[int] = []
    queue = values[:]
    for _ in values:
        sorted_list.append(queue.pop(idx_of_min(queue)))
    return sorted_list


print(selection_sort(numbers))
