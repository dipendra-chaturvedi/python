class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):

        current = self.head

        while current:
            print(current.data)
            current = current.next


linked_list = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

linked_list.head = node1
node1.next = node2
node2.next = node3

linked_list.display()