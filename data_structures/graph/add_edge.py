graph = {
    "A": ["B"],
    "B": ["A"],
    "C": []
}

graph["A"].append("C")
graph["C"].append("A")

print(graph)