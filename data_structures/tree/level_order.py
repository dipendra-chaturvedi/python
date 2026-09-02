from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

level_order(root)