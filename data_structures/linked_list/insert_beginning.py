class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)

node1.next = node2

head = node1

new_node = Node(5)

new_node.next = head
head = new_node

current = head

while current:
    print(current.data)
    current = current.next

# Before insertion
# head
#  ↓
# [10] → [20] → None


# After insertion
# head
#  ↓
# [5] → [10] → [20] → None