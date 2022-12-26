import pytest
import time

from algorithms.search.binary_search import binary_search
from algorithms.search.binary_search import recursive_binary_search
from algorithms.search.linear_search import linear_search


@pytest.fixture
def medium_list():
    return [i for i in range(0, 900_001)]


@pytest.fixture
def short_list():
    return [i for i in range(0, 1001)]


def test_var_assignment():
    spec_var = 32
    copy_var = spec_var
    spec_var = 33
    assert copy_var == 32


def test_binary_search_found(short_list: list[int], medium_list: list[int]):
    for i in range(0, 900_000):
        result = binary_search(medium_list, i)
        assert result == i


def test_binary_search_not_found(
    short_list: list[int], medium_list: list[int]
):
    for i in range(-1, -3, -1):
        result = binary_search(short_list, i)
        print(result, end=", ")
        assert result is None


def test_linear_slower_than_binary(medium_list: list[int]):
    """As linear is O(1) it is slower than O(log n) confirm expected result"""
    start_time = time.perf_counter_ns()
    result = linear_search(medium_list, 100000)
    linear_total_time = time.perf_counter_ns() - start_time
    print(f"Found result:{result} in {linear_total_time}")
    start_time = time.perf_counter_ns()
    result = binary_search(medium_list, 100000)
    binary_total_time = time.perf_counter_ns() - start_time
    print(f"Found result:{result} in {binary_total_time}")
    assert binary_total_time < linear_total_time


def test_recursive_binary_search_found(short_list: list[int]):
    for i in range(0, len(short_list)):
        result = recursive_binary_search(short_list, i)
        print(result, end=", ")
        # assert result is True
