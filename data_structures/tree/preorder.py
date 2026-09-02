class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):

    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)

preorder(root)