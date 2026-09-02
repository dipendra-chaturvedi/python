class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_max(root):

    current = root

    while current.right:
        current = current.right

    return current.data


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print(find_max(root))