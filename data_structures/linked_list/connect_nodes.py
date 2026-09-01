class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)

node1.next = node2

print(node1)
print(node1.data)
print(node1.next)
print(node1.next.data)