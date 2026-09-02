from collections import deque


graph = {
    "A": [("B", 5), ("C", 10)],
    "B": [("D", 3)],
    "C": [("E", 2)],
    "D": [],
    "E": []
}


def bfs(start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node in visited:
            continue

        print(node)
        visited.add(node)

        for neighbor, weight in graph[node]:
            print("  →", neighbor, "weight:", weight)
            queue.append(neighbor)


bfs("A")