'''
Convert sorted array to balanced binary search tree
'''

from binarytree import Node

def arrayToBST(arrList):
    global root
    root = None

    if len(arrList) == 0:
        return None

    arrayToBSTHelper(arrList, 0, len(arrList) - 1)
    return

def arrayToBSTHelper(arrList, start, end):
    global root

    # Base Case
    if start > end:
        return None

    # Recursive Case
    mid = start + ( (end - start) // 2 )

    node = Node(arrList[mid])
    if root is None:
        root = node
    node.left = arrayToBSTHelper(arrList, start, mid - 1)
    node.right = arrayToBSTHelper(arrList, mid + 1, end)

    return node

if __name__ == "__main__":
    arrayToBST([-10, -3, 0, 5, 9])
    print(root)

'''
OUTPUT:
   ____0
  /     \
-10      5
   \      \
    -3     9
'''
