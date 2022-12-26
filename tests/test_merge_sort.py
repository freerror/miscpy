import pytest
from algorithms.sort.merge_sort import (
    split,
    merge_and_sort,
    merge_sort,
    verify_sorted,
)


@pytest.fixture
def uneven_list():
    return [12, 30, 44, 55, 66]


@pytest.fixture
def even_list():
    return [12, 30, 44, 55, 66, 77]


def test_split(uneven_list: list[int], even_list: list[int]):
    left, right = split(uneven_list)
    assert left == [12, 30]
    assert right == [44, 55, 66]
    left, right = split(even_list)
    assert left == [12, 30, 44]
    assert right == [55, 66, 77]


def test_merge_and_sort(even_list: list[int], uneven_list: list[int]):
    merged_list = merge_and_sort(even_list, uneven_list)
    assert isinstance(merged_list, list)


def test_merge_sort_and_verify():
    result = merge_sort([4, 3, 4, 2, 30, 1, 0])
    assert result == [0, 1, 2, 3, 4, 4, 30]
    assert verify_sorted(result) == True
