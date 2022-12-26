from typing import Union


class Node:
    """Object for storing a single node of linked list.
    Models two attributes - data and the link ot the next node in the list"""

    data: int | None = None
    next_node: Union["Node", None] = None

    def __init__(self, data: int):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data} next_node: {self.next_node}>"


class LinkedList:
    """Singly linked list"""

    head: Node | None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """Returns count of nodes in list in O(n) (linear) time"""
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def add(self, data: int):
        """Add new node to head of list, linked to the previous head
        This is a O(1) / "constant time" operation"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, search: int):
        """Return the node matching the search or None
        Takes linear time aka O(n)"""
        current = self.head
        while current:
            if current.data == search:
                return current
            else:
                current = current.next_node
        return None

    def index(self, search: int):
        """Return the index of the node matching the search or None Takes
        linear time aka O(n)"""
        current = self.head
        index = 0
        while current:
            if current.data == search:
                return index
            else:
                current = current.next_node
                index += 1
        return None

    def insert(self, data: int, index: int):
        """Insert new node with data at index. Inserting is in constant time
        0(1) but finding the insertion point takes linear 0(n) time"""
        if index == 0:
            self.add(data)
        elif index > 0:
            to_be_inserted_node = Node(data)
            current = self.head
            pos = index
            while pos > 1:
                current = current.next_node if current else None
                pos -= 1
            if current:
                to_be_inserted_node.next_node = current.next_node
                current.next_node = to_be_inserted_node
            else:
                raise IndexError("Index not part of list")

    def remove(self, search: int):
        """Search for the value and remove the corresponding node. Takes linear
        time 0(n)"""
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == search:
                found = True
                if not previous:
                    self.head = current.next_node
                    return current
                else:
                    previous.next_node = current.next_node
                    return current
            else:
                previous = current
                current = current.next_node
        return None

    def delete(self, index: int):
        """Remove node at index. Ultimately linear time 0(n) as we traverse the
        list to find the index to remove"""
        current = self.head
        pos = index
        while pos > 1:
            current = current.next_node if current else None
            pos -= 1
        if current:
            if index == 0:
                self.head = current.next_node
                return
            node_to_remove = current.next_node
            current.next_node = (
                node_to_remove.next_node if node_to_remove else None
            )
        else:
            raise IndexError("Index not part of list")

    def get_node_by_index(self, key: int):
        """Get node by index in linear time O(n)"""
        current = self.head
        pos = 0
        while True:
            if not current:
                raise IndexError()
            elif pos == key:
                return current
            current = current.next_node
            pos += 1

    def __getitem__(self, key: int):
        """Get item method in linear time O(n)"""
        current = self.head
        pos = 0
        while True:
            if not current:
                raise IndexError()
            elif pos == key:
                return current.data
            current = current.next_node
            pos += 1

    def __repr__(self):
        """Return a str representation of the list
        Takes O(n) linear time"""
        nodes: list[str] = []
        current = self.head
        idx = 0
        while current:
            nodes.append(f"{idx}:[{current.data}]")
            idx += 1

            current = current.next_node
        return " -> ".join(nodes)


def main():
    l = LinkedList()
    l.add(20)
    l.add(30)
    l.add(88)
    l.add(89)
    print("size:", l.size())
    print(l)
    print("search for 88 result:", l.search(88))
    print("inserting 42 at index 2")
    l.insert(42, 2)
    print(l)
    print("inserting 16 at 5")
    l.insert(16, 5)
    print(l)
    print("inserting 77 at 0")
    l.insert(77, 0)
    print(l)
    print("inserting 24 at impossible 20")
    try:
        l.insert(24, 20)
    except IndexError as e:
        print(e.__class__, e.args)
    print("removing node 4")
    l.delete(4)
    print(l)
    print("removing node 5")
    l.delete(5)
    print(l)
    print("removing node 0")
    l.delete(0)
    print(l)
    print("removing impossible node 20")
    try:
        l.delete(20)
    except IndexError as e:
        print(e.__class__, e.args)
    print(l)
    print("Get the index of 42:", l.index(42))
    print("Get the index of 89:", l.index(89))
    print("Get the index of 20:", l.index(20))
    print("Get the index of impossible 1000:", l.index(1000))
    print("Remove value 20")
    l.remove(20)
    print(l)
    print("Remove value 88")
    l.remove(88)
    print(l)
    print("Remove value 89")
    l.remove(89)
    print(l)
    print("Remove impossible value 89")
    l.remove(89)
    print(l)


if __name__ == "__main__":
    main()
