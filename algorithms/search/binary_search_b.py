# Python3 Program for recursive binary search.
# Returns index of x in arr if present, else -1


def binary_search(arr, left, max_index, search_val):
    # Check base case
    if max_index >= left:

        mid = (
            left + (max_index - left) // 2
        )  # // only returns the integer ammount

        # If element is present at the middle itself
        if arr[mid] == search_val:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > search_val:
            return binary_search(arr, left, mid - 1, search_val)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(arr, mid + 1, max_index, search_val)

    else:
        # Element is not present in the array
        return -1


def main():
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    max_index = len(arr) - 1
    left = 10

    # Function call
    result = binary_search(arr, 0, max_index, left)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
