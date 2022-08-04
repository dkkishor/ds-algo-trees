'''
Traverses the tree in Level Order and returns all elements in a level as a list
Add the elements in reverse order for every odd level, treating root as zero level
Final output is list of lists
'''

from collections import deque
from BST import BST
from BSTUtil import BSTUtil


def getLevelOrder(root) -> list[list[int]]:
    result = []
    q = deque()
    q.append(root)
    reverse = False

    while q:
        levelList = []
        count = len(q)

        for i in range(count):
            curr = q.popleft()
            levelList.append(curr.get_key())

            if curr.get_left_node() is not None:
                q.append(curr.get_left_node())

            if curr.get_right_node() is not None:
                q.append(curr.get_right_node())

        if reverse:
            levelList.reverse()
        result.append(levelList)
        reverse = not reverse

    print(result)


if __name__ == "__main__":
    bst = BST()
    BSTUtil.create_tree_with_data(bst)
    getLevelOrder(bst._root)


'''
OUTPUT:
[[44], [88, 17], [8, 32, 65, 97], [93, 82, 54, 28], [29, 76], [80]]
'''