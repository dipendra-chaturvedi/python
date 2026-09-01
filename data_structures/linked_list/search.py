class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

search_value = 20

current = node1
found = False

while current:

    if current.data == search_value:
        found = True
        break

    current = current.next


if found:
    print("Value found")
else:
    print("Value not found")