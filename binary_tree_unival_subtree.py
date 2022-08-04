'''
Given a binary tree, count the number of univalue subtrees.

NOTE:
    To install binarytree use following commannd
    python3 -m pip install binarytree
'''

from binarytree import build

univalCount = 0

def getUnivalCount(tree):
    global univalCount
    univalCount = 0

    if tree is None:
        return univalCount

    root = tree
    getUnivalCountHelper(root)
    print("Univalue Count=" + str(univalCount))
    return univalCount

def getUnivalCountHelper(root) -> bool:
    global univalCount

    # Base Case
    if root.left is None and root.right is None:
        univalCount += 1
        return True

    # Recursive Case
    isUnival = True
    if root.left is not None:
        isUnival = getUnivalCountHelper(root.left) and (root.value == root.left.value)
    if root.right is not None:
        isUnival = getUnivalCountHelper(root.right) and (root.value == root.right.value) and isUnival

    if isUnival:
        univalCount += 1

    return isUnival

if __name__ == "__main__":
    nodes = [5, 1, 5, 5, 5, None, 5]
    binary_tree = build(nodes)
    print(binary_tree)
    #print(binary_tree.value)
    getUnivalCount(binary_tree)

    nodes = [5, 5, 5, 5, 5, None, 5]
    binary_tree = build(nodes)
    print(binary_tree)
    # print(binary_tree.value)
    getUnivalCount(binary_tree)


'''
OUTPUT:
    __5
   /   \
  1     5
 / \     \
5   5     5

Univalue Count=4

    __5
   /   \
  5     5
 / \     \
5   5     5

Univalue Count=6
'''
