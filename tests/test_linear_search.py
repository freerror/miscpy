import time
from algorithms.search.linear_search import linear_search
import pytest


@pytest.fixture
def example_list():
    return [i for i in range(0, 100001)]


def test_linear_search_found(example_list: list[int]):
    start_time = time.perf_counter_ns()
    result = linear_search(example_list, 100000)
    total_time = time.perf_counter_ns() - start_time
    print(total_time)
    assert result == 100000


def test_linear_search_not_found(example_list: list[int]):
    start_time = time.perf_counter_ns()
    result = linear_search(example_list, -1)
    total_time = time.perf_counter_ns() - start_time
    print(total_time)
    assert result is None
