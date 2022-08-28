from stack import Stack
from binary_tree_printer import BinaryTreePrinter


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None:
            return
        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            self.__insert_value(node.right, value)

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)

        else:
            self.__insert_value(self.root, value)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val, end=" ")
        self.__in_order(node.right)

    def in_order_traversal(self):
        self.__in_order(self.root)

    # Depth First Search(DFS):
    def contains(self, value):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.is_empty():
            node = nodes.pop()
            if node.val == value:
                return True
            elif value < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)
        return False

    def __str__(self):
        return BinaryTreePrinter().get_tree_string(self.root)


my_binary_search_tree = BinarySearchTree()

for i in [10, 5, 17, 3, 7, 12, 19, 1, 4]:
    my_binary_search_tree.insert(i)
    print(my_binary_search_tree)

print("In order traversal:", end=" ")
my_binary_search_tree.in_order_traversal()

print("\n Is contains 7:", my_binary_search_tree.contains(7))
