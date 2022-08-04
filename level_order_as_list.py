'''
Traverses the tree in Level Order and returns all elements as a list
'''

from collections import deque
from BST import BST
from BSTUtil import BSTUtil


def getLevelOrder(root) -> list[int]:
    q = deque()

    q.append(root)
    result = []

    while q:
        curr = q.popleft()
        result.append(curr.get_key())

        if curr.get_left_node() is not None:
            q.append(curr.get_left_node())

        if curr.get_right_node() is not None:
            q.append(curr.get_right_node())

    print(result)


if __name__ == "__main__":
    bst = BST()
    BSTUtil.create_tree_with_data(bst)
    getLevelOrder(bst._root)


'''
OUTPUT:
[44, 17, 88, 8, 32, 65, 97, 28, 54, 82, 93, 29, 76, 80]
'''