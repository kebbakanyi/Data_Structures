import sys


class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


def validate_bst(root, minimum=-sys.maxsize, maximum=sys.maxsize):

    if root is None:
        return True
    #     min < root.value < max
    if (minimum < root.value < maximum and
            validate_bst(root.left_child, minimum, root.value) and
            validate_bst(root.right_child, root.value, maximum)):
            return True
    else:
        return False


root = Node(5)
l1 = Node(4)
r1 = Node(6)
r2 = Node(10)

r1.right_child = r2

root.left_child = l1
root.right_child = r1

print(validate_bst(root))
