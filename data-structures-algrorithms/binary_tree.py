from queue import Queue
from binary_tree_printer import BinaryTreePrinter


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()

                if checking_node.left is None:
                    checking_node.left = TreeNode(value)
                    return

                elif checking_node.right is None:
                    checking_node.right = TreeNode(value)
                    return

                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

    def __str__(self):
        return BinaryTreePrinter().get_tree_string(self.root)


my_binary_tree = BinaryTree()

for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    my_binary_tree.insert(i)
    print(my_binary_tree)

# print(my_binary_tree.contains("F"))
