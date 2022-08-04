'''
Given a binary search tree and a sum, find if the tree has root-to-leaf path of
adding of all the values equals sum
'''

from BST import BST
from BSTUtil import BSTUtil

psFlag = False

def hasPathSum(root, sum):
    global psFlag
    psFlag = False
    if root is None:
        return False

    hasPathSumHelper(root, sum)
    print("For sum=" + str(sum) + ",hasPathSum=" + str(psFlag))
    return psFlag

def hasPathSumHelper(root, sum):
    global psFlag

    # Backtracking
    if psFlag:
        return

    # Base condition
    if root.get_left_node() is None and root.get_right_node() is None:
        if sum == root.get_key():
            psFlag = True

        return

    # Recursive condition
    sum -= root.get_key()
    if root.get_left_node() is not None:
        hasPathSumHelper(root.get_left_node(), sum)
    if root.get_right_node() is not None:
        hasPathSumHelper(root.get_right_node(), sum)

if __name__ == "__main__":
    bst = BST()
    BSTUtil.create_tree_with_data(bst)
    hasPathSum(bst._root, 69)
    hasPathSum(bst._root, 70)
    hasPathSum(bst._root, 1)
    hasPathSum(bst._root, 150)
    hasPathSum(bst._root, 121)


'''
OUTPUT:
For sum=69,hasPathSum=True
For sum=70,hasPathSum=False
For sum=1,hasPathSum=False
For sum=150,hasPathSum=True
For sum=121,hasPathSum=False
'''