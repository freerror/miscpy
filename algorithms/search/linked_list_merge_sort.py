from data_structures.linked_list import LinkedList


def merge_sort(linked_list: LinkedList):
    """Sorts a linked list in ascending order
    - Recursively divide linked list in to sublists containing a single node
    - Repeatedly merge the sublists and sort until one remains

    Returns a sorted LinkedList.
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left: LinkedList = merge_sort(left_half)
    right: LinkedList = merge_sort(right_half)

    return merge_and_sort(left, right)


def split(linked_list: LinkedList) -> tuple[LinkedList, LinkedList]:
    """Divide the unsorted list at midpoint into sublists then return
    Takes O(k log n), k being the number of steps to the split (due to get_node_by_index)
    """

    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.get_node_by_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

    return left_half, right_half  # type: ignore


def merge_and_sort(left: LinkedList, right: LinkedList):
    """Merges two linked lists, sorting by data in the nodes
    Returns a new, merged list
    """

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # Add fake head that is discarded later
    merged.add(0)

    # Set current to head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from the right to merged linked list
        if left_head is None and right_head and current:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the  the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None and left_head and current:
            current.next_node = left_head
            # call next on left to set loop condition to False
            left_head = left_head.next_node
        elif left_head and right_head:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if (
                (left_data and right_data)
                and left_data < right_data
                and current
            ):
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            elif (
                (left_data and right_data)
                and left_data > right_data
                and current
            ):
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node if current else None

    # Discard fake head and set first merged node as head
    head = merged.head.next_node if merged.head else None
    merged.head = head
    return merged
