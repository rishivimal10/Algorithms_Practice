from binary_trees.is_height_balanced import find_height, is_height_balanced_solution
from binary_trees.binary_tree_node import BinaryTreeNode

if __name__ == '__main__':
    root = BinaryTreeNode(data=1)
    root.left = BinaryTreeNode(data=2)
    root.right = BinaryTreeNode(data=3)
    root.left.left = BinaryTreeNode(data=4)
    root.left.right = BinaryTreeNode(data=5)
    root.left.left.left = BinaryTreeNode(data=6)

    print(is_height_balanced_solution(root))

