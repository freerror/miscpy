from data_structures.linked_list import LinkedList
from algorithms.search.linked_list_merge_sort import merge_sort


def test_merge_sort():
    li = LinkedList()
    li.add(10)
    li.add(2)
    li.add(44)
    li.add(15)
    li.add(200)
    print(li)
    sorted_linked_list = merge_sort(li)
    print(sorted_linked_list)
