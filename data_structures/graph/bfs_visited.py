from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}


def bfs(start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node)

            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)


bfs("A")