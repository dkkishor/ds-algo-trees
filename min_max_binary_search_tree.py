'''
Find the min and max of a binary search tree
'''

from BST import BST
from BSTUtil import BSTUtil


def minmax(root):
    if root is None:
        return 'Tree is Empty.'

    curr = root
    while curr.get_left_node() is not None:
        curr = curr.get_left_node()

    min = curr.get_key()

    curr = root
    while curr.get_right_node() is not None:
        curr = curr.get_right_node()

    max = curr.get_key()

    return "Min: " + str(min) + ", Max: " + str(max)


if __name__ == "__main__":
    bst = BST()

    # Create sample data
    BSTUtil.create_tree_with_data(bst)

    print(minmax(bst._root))