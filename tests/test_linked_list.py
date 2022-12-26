import pytest
from data_structures.linked_list import LinkedList, Node


@pytest.fixture
def test_list():
    new = LinkedList()
    new.add(20)
    new.add(30)
    new.add(88)
    new.add(89)
    return new


def test_size(test_list: LinkedList):
    """Test size method"""
    assert test_list.size() == 4


def test_add(test_list: LinkedList):
    """Test add method"""
    assert str(test_list) == "0:[89] -> 1:[88] -> 2:[30] -> 3:[20]"


def test_search(test_list: LinkedList):
    """Test search method"""
    result: Node | None = test_list.search(88)
    assert isinstance(result, Node) == True
    if result:
        assert result.data == 88
    if result and result.next_node:
        assert result.next_node.data == 30


def test_index(test_list: LinkedList):
    """Test index method"""
    # middle
    assert test_list.index(88) == 1
    # start
    assert test_list.index(89) == 0
    # end
    assert test_list.index(20) == 3
    # non-existent
    assert test_list.index(5000) is None


def test_insert(test_list: LinkedList):
    """Test insert method"""
    # middle
    test_list.insert(1001, 2)
    print(test_list)
    # start
    test_list.insert(1002, 0)
    print(test_list)
    # end
    test_list.insert(1003, 5)
    print(test_list)
    # assert
    assert (
        str(test_list)
        == "0:[1002] -> 1:[89] -> 2:[88] -> 3:[1001] -> 4:[30] -> 5:[1003] -> 6:[20]"
    )

    # non-existent
    with pytest.raises(IndexError):
        test_list.insert(1004, 1002)

    return test_list


def test_remove(test_list: LinkedList):
    """Test remove method"""
    # middle
    test_list.remove(88)
    print(test_list)
    # start
    test_list.remove(89)
    print(test_list)
    # end
    test_list.remove(20)
    print(test_list)
    # non-existent
    test_list.remove(4124)
    # assert
    assert str(test_list) == "0:[30]"


def test_delete(test_list: LinkedList):
    """Test delete method"""
    # middle
    test_list.delete(2)
    print(test_list)
    assert str(test_list) == "0:[89] -> 1:[88] -> 2:[20]"
    # start
    test_list.delete(0)
    print(test_list)
    assert str(test_list) == "0:[88] -> 1:[20]"
    # end
    test_list.delete(1)
    print(test_list)
    assert str(test_list) == "0:[88]"
    # non-existent
    test_list.delete(1)
    assert str(test_list) == "0:[88]"


def test_get_item(test_list: LinkedList):
    """Test __getitem__ method"""
    # middle
    assert test_list[2] == 30
    # end
    assert test_list[3] == 20
    # start
    assert test_list[0] == 89
    # non-existent
    with pytest.raises(IndexError):
        test_list[100]
