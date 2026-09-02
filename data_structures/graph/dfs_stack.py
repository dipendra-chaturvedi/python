graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}


def dfs(start):

    visited = set()
    stack = [start]

    while stack:

        node = stack.pop()

        if node in visited:
            continue

        print(node)
        visited.add(node)

        for neighbor in reversed(graph[node]):
            stack.append(neighbor)


dfs("A")