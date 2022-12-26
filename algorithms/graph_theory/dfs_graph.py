"""Iterative DFS"""

# Simple
# GRAPH = [[3, 2, 1], [3, 0], [3, 0], [4, 2, 1, 0], [3]]

# More Complex
# GRAPH = [
#     [1, 2],
#     [0, 2, 3, 4],
#     [0, 1],
#     [1, 5],
#     [1],
#     [3, 6, 7, 8],
#     [5],
#     [5, 8],
#     [5, 7, 9],
#     [8],
# ]
GRAPH = [
    [2, 1],
    [4, 3, 2, 0],
    [1, 0],
    [5, 1],
    [1],
    [8, 7, 6, 3],
    [5],
    [8, 5],
    [9, 7, 5],
    [8],
]


def visit(vertex: int):
    print(vertex)


def dfs(graph: list[list[int]], start: int):
    marked: set[int] = set()
    stack: list[int] = [start]
    while stack:
        v = stack.pop()
        if v in marked:
            continue
        visit(v)
        marked.add(v)
        for neighbor in graph[v]:
            if neighbor in marked:
                continue
            stack.append(neighbor)


def next_neighbor(vertex: int, graph: list[list[int]], res: list[int]):
    for neighbor in graph[vertex]:
        if neighbor not in res:
            return neighbor


def dfs_post_order_recursive(
    graph: list[list[int]], start: int, visited: set[int]
):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_post_order_recursive(graph, neighbor, visited)
    visit(start)


def dfs_pre_order_recursive(
    graph: list[list[int]], start: int, visited: set[int]
):
    visit(start)
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_pre_order_recursive(graph, neighbor, visited)


def main():
    print("DFS (pre-order)")
    dfs(GRAPH, 0)
    print("DFS (post-order) recursive")
    dfs_post_order_recursive(GRAPH, 0, set())
    print("DFS (pre-order) recursive")
    dfs_pre_order_recursive(GRAPH, 0, set())


if __name__ == "__main__":
    main()
