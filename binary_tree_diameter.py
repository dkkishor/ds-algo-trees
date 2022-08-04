'''
Given a binary tree, find the length of the logest path between any 2 nodes.
This path may or may not pass through the root.

NOTE:
    To install binarytree use following commannd
    python3 -m pip install binarytree
'''

from binarytree import build

maxDiameter = 0

def getTreeDiameter(tree):
    global maxDiameter
    maxDiameter = 0

    root = tree
    getTreeDiameterHelper(root)
    print("Diameter=" + str(maxDiameter))
    return maxDiameter

def getTreeDiameterHelper(root):
    global maxDiameter

    # Base Case
    if root.left is None and root.right is None:
        return 0

    # Recursive Case
    lHeight = 0
    rHeight = 0
    if root.left is not None:
        lHeight = getTreeDiameterHelper(root.left) + 1
    if root.right is not None:
        rHeight = getTreeDiameterHelper(root.right) + 1

    # Post Order
    maxDiameter = maxDiameter if maxDiameter > (lHeight + rHeight) else (lHeight + rHeight)
    # print(maxDiameter, lHeight, rHeight)

    return lHeight if lHeight > rHeight else rHeight

if __name__ == "__main__":
    nodes = [5, 4, 8, 11, 7, 13, 4, 2, None, None, None, None, None, None, None]
    binary_tree = build(nodes)
    print(binary_tree)
    #print(binary_tree.value)
    getTreeDiameter(binary_tree)

    nodes = [5, 4, 8, 11, 7, None, None, 2, None, None, 5, None, None, None, None, 12, None, None, None, None, None, None, 6]
    binary_tree = build(nodes)
    print(binary_tree)
    # print(binary_tree.value)
    getTreeDiameter(binary_tree)

'''
OUTPUT:
       __5___
      /      \
    _4       _8
   /  \     /  \
  11   7   13   4
 /
2

Diameter=5

          ______5
         /       \
       _4         8
      /  \
     11   7
    /      \
  _2        5
 /           \
12            6

Diameter=6
'''
