graph = {
    "A": [("B", 5), ("C", 10)],
    "B": [("A", 5), ("C", 3)],
    "C": [("A", 10), ("B", 3)]
}

print(graph)
print(graph["A"])