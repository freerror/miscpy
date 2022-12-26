def linear_search(list: list[int], target: int):
    """
    Returns the index position of the target if found, else None

    O(1) constant time
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
