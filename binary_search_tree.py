class Node:

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):

        if value < current_node.value:

            if current_node.left_child is None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)

        elif value > current_node.value:

            if current_node.right_child is None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node

            else:
                self._insert(value, current_node.right_child)

        else:
            print('This Value is already in the tree ')

    def print_tree(self):

        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):

        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):

        if current_node is None:
            return current_height

        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)

        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):

        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search(value, current_node.right_child)
        return False

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child is not None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._find(value, current_node.right_child)
        return False

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0

            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        # get parent of node to be deleted
        node_parent = node.parent

        node_children_amount = num_children(node)

        # break the operation into diffrent cases based on the
        # structure of the tree & node to be deleted

        # Case 1: node has no children
        if node_children_amount == 0:

            # remove refrence to the node from the parent
            if node_parent.left_child == node:
                node_parent.left_child = None

            else:
                node_parent.right_child = None

        # Case 2: single child
        if node_children_amount == 1:

            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the noe to be delted with its child
            if node.parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        #  Case 3: two children
        if node_children_amount == 2:

            successor = min_value_node(node.right_child)
            node.value = successor.value
            self.delete_node(successor)
            pass


def fill_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        current_element = randint(0,max_int)
        tree.insert(current_element)
    return tree


tree = BinarySearchTree()
# tree = fill_tree(tree)

# tree.print_tree()
# print('Tree height is {}'.format(tree.height()))
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.print_tree()
print('\n')
# print('Tree height is {}'.format(tree.height()))
# print(tree.search(10))
# print(tree.search(30))
tree.delete_value(10)
tree.print_tree()






















