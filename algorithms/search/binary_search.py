def binary_search(list: list[int], target: int):
    search_start = 0
    search_end = len(list) - 1
    while search_start <= search_end:
        search_mid = (search_start + search_end) // 2
        if (to_check := list[search_mid]) == target:
            return search_mid
        elif target < to_check:
            search_end = search_mid - 1
        else:
            search_start = search_mid + 1
    return None


def recursive_binary_search(list: list[int], target: int) -> int | None:
    if len(list) == 0:
        return False
    else:
        mid = (len(list)) // 2

        if list[mid] == target:
            return mid
        else:
            if target > list[mid]:
                new_list = list[mid + 1 :]
                removed = len(list[: mid + 1])
            else:
                new_list = list[:mid]
                removed = 0
            result = recursive_binary_search(new_list, target)
            return (result or 0) + removed
