from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    idx: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def build_tree():
    r""" Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    return root


def visit(node: Node):
    print(node.idx)


def dfs_postorder_iterative(root: Node):
    if root is None:
        return
    stack = [root]
    out: list[int] = []

    while stack:
        curr = stack.pop()
        out.append(curr.idx)

        for child in curr.left, curr.right:
            if child:
                stack.append(child)
    while out:
        print(out.pop())


def dfs_postorder_recursive(root: Node):
    """Recursive algorithm with postorder ordering"""
    if not root:
        return
    for child in root.left, root.right:
        if child:
            dfs_postorder_recursive(child)
    visit(root)


def dfs_preorder_recursive(root: Node):
    """Recursive algorithm with preorder ordering"""
    if not root:
        return
    visit(root)
    for child in root.left, root.right:
        if child:
            dfs_postorder_recursive(child)


def main():
    root = build_tree()
    print("Preorder Recursive")
    dfs_preorder_recursive(root)
    print("Postorder Recursive")
    dfs_postorder_recursive(root)
    print("Postorder Iterative")
    dfs_postorder_iterative(root)


if __name__ == "__main__":
    main()
