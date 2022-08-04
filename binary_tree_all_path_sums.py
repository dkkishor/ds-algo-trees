'''
Given a binary tree and a sum, find if the tree has root-to-leaf path of
adding of all the values equals sum

NOTE:
    To install binarytree use following commannd
    python3 -m pip install binarytree
'''

from binarytree import build

def getSumPaths(tree, sum):
    root = tree
    slate, result = [], []
    getSumPathsHelper(root, sum, slate, result)
    print("For sum=" + str(sum) + ",result=" + str(result))
    return result

def getSumPathsHelper(root, sum, slate, result):

    # Base Case
    if root.left is None and root.right is None:
        if sum == root.value:
            slate.append(root.value)
            result.append(slate.copy())
            slate.pop()
        return

    # Recursive Case
    sum -= root.value
    slate.append(root.value)
    if root.left is not None:
        getSumPathsHelper(root.left, sum, slate, result)
    if root.right is not None:
        getSumPathsHelper(root.right, sum, slate, result)

    # Backtracking
    slate.pop()
    return

if __name__ == "__main__":
    nodes = [5, 4, 8, 11, None, 13, 4, 2, 7, None, None, None, None, 5, 1]
    binary_tree = build(nodes)
    print(binary_tree)
    #print(binary_tree.value)
    getSumPaths(binary_tree, 22)
    getSumPaths(binary_tree, 26)
    getSumPaths(binary_tree, 27)
    getSumPaths(binary_tree, 18)
    getSumPaths(binary_tree, 19)
    getSumPaths(binary_tree, 23)
    getSumPaths(binary_tree, 24)
    getSumPaths(binary_tree, 25)

'''
OUTPUT:
         5___
        /    \
    ___4     _8__
   /        /    \
  11       13     4
 /  \            / \
2    7          5   1

For sum=22,result=[[5, 4, 11, 2], [5, 8, 4, 5]]
For sum=26,result=[[5, 8, 13]]
For sum=27,result=[[5, 4, 11, 7]]
For sum=18,result=[[5, 8, 4, 1]]
For sum=19,result=[]
For sum=23,result=[]
For sum=24,result=[]
For sum=25,result=[]
'''
