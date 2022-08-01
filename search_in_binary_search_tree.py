'''

'''

from BSTUtil import BSTUtil
from BST import BST


def search(root, key):
    if root is None:
        return 'key: ' + str(key) + ' not found'

    curr = root

    while curr is not None:
        if key == curr.get_key():
            return 'key: ' + str(key) + ' found'
        elif key < curr.get_key():
            curr = curr.get_left_node()
        else:
            curr = curr.get_right_node()

    return 'key: ' + str(key) + ' not found'


if __name__ == "__main__":
    bst = BST()

    # Create sample data
    BSTUtil.create_tree_with_data(bst)

    print(search(bst._root, 0))
    print(search(bst._root, 8))
    print(search(bst._root, 93))
    print(search(bst._root, 80))
    print(search(bst._root, 125))

'''
OUTPUT:
key: 0 not found
key: 8 found
key: 93 found
key: 80 found
key: 125 not found
'''



