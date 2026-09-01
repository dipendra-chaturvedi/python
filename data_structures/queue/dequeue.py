queue = []

queue.append("A")
queue.append("B")
queue.append("C")

print("Before dequeue:", queue)

item = queue.pop(0)

# It is wrong because first will remove the first.
# item = queue.pop(1)

print("Removed:", item)
print("After dequeue:", queue)