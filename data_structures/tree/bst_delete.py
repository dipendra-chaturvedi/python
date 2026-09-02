class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delete(root, target):

    if root is None:
        return None

    if target < root.data:
        root.left = delete(root.left, target)

    elif target > root.data:
        root.right = delete(root.right, target)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = root.right

        while successor.left:
            successor = successor.left

        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

root = delete(root, 30)

inorder(root)