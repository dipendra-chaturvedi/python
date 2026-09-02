class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)

inorder(root)