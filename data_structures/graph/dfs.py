graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}


def dfs(node, visited):

    if node in visited:
        return

    print(node)
    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor, visited)


visited = set()

dfs("A", visited)