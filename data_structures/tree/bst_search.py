class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print(search(root, 40))
print(search(root, 90))