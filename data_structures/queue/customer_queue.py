queue = []

queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")

print("Queue:", queue)

customer = queue.pop(0)

print("Served:", customer)
print("Remaining:", queue)