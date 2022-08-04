'''
Given a binary tree and a sum, find if the tree has root-to-leaf path of
adding of all the values equals sum

NOTE:
    To install binarytree use following commannd
    python3 -m pip install binarytree
'''

from binarytree import build

psflag = False

def hasPathSum(tree, sum):
    global psflag
    psflag = False

    root = tree
    hasPathSumHelper(root, sum)
    print("For sum=" + str(sum) + ",hasPathSum=" + str(psflag))
    return psflag

def hasPathSumHelper(root, sum):
    global psflag

    # Backtracking Case
    if psflag: return

    # Base Case
    if root.left is None and root.right is None:
        if sum == root.value:
            psflag = True
        return

    # Recursive Case
    sum -= root.value
    if root.left is not None:
        hasPathSumHelper(root.left, sum)
    if root.right is not None:
        hasPathSumHelper(root.right, sum)

    return

if __name__ == "__main__":
    nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    binary_tree = build(nodes)
    print(binary_tree)
    #print(binary_tree.value)
    hasPathSum(binary_tree, 22)
    hasPathSum(binary_tree, 26)
    hasPathSum(binary_tree, 27)
    hasPathSum(binary_tree, 18)
    hasPathSum(binary_tree, 19)
    hasPathSum(binary_tree, 23)
    hasPathSum(binary_tree, 24)
    hasPathSum(binary_tree, 25)

'''
OUTPUT:
         5___
        /    \
    ___4     _8__
   /        /    \
  11       13     4
 /  \            / \
7    2          5   1

For sum=22,hasPathSum=True
For sum=26,hasPathSum=True
For sum=27,hasPathSum=True
For sum=18,hasPathSum=True
For sum=19,hasPathSum=False
For sum=23,hasPathSum=False
For sum=24,hasPathSum=False
For sum=25,hasPathSum=False
'''