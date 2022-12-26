def split(unsplit_list: list[int]) -> tuple[list[int], list[int]]:
    """Splits a list in to two parts, taking

    Takes overall, O(log n) time
    """
    length = len(unsplit_list)
    half = length // 2
    left: list[int] = []
    right: list[int] = []
    i = 0
    while i < length:
        if i < half:
            left.append(unsplit_list[i])
        else:
            right.append(unsplit_list[i])
        i += 1

    return left, right


def merge_and_sort(left: list[int], right: list[int]) -> list[int]:
    """Merges two lists, sorting in the process
    Returns a new merged list

    Run's in overall linear O(n) time
    """
    li: list[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            li.append(left[i])
            i += 1
        else:
            li.append(right[j])
            j += 1

    while i < len(left):
        li.append(left[i])
        i += 1

    while j < len(right):
        li.append(right[j])
        j += 1

    return li


def merge_sort(unsorted_list: list[int]) -> list[int]:
    """Sorts a list in ascending order and return new sorted list

    Divide: Find the midpoint of list and divide into sublist
    Conquer: Recursively sort the sublists from previous step
    Combine: Merge the sorted sublists from previous

    Takes overall, O(n log n)
    """

    if len(unsorted_list) <= 1:
        return unsorted_list

    left_half, right_half = split(unsorted_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_and_sort(left, right)


def verify_sorted(li: list[int]) -> bool:
    """Returns True if input list is sorted, else False"""
    if len(li) <= 1:
        # empty list or list with one element is "naively" sorted
        return True
    return li[0] <= li[1] and verify_sorted(li[1:])
