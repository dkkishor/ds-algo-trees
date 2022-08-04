'''
Prints the right side view of the tree printing right most element of any given tree.
'''

from collections import deque
from BST import BST
from BSTUtil import BSTUtil


def getRightSideView(root) -> list[int]:
    result = []

    if root is None:
        return result

    q = deque()
    q.append(root)

    while q:
        count = len(q)

        for i in range(count):
            rnode = q.popleft()

            if rnode.get_left_node() is not None:
                q.append(rnode.get_left_node())

            if rnode.get_right_node() is not None:
                q.append(rnode.get_right_node())

        result.append(rnode.get_key())

    print(result)


if __name__ == "__main__":
    bst = BST()
    BSTUtil.create_tree_with_data(bst)
    getRightSideView(bst._root)


'''
OUTPUT:
[[44], [17, 88], [8, 32, 65, 97], [28, 54, 82, 93], [29, 76], [80]]
'''