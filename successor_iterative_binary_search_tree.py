'''
Find Successor of a node in Binary Search Tree using Iterative method
'''

from BST import BST
from BSTUtil import BSTUtil


def findNode(root, key):
    if root is None:
        return None

    curr = root
    while curr is not None:
        if key == curr.get_key():
            return curr
        elif key < curr.get_key():
            curr = curr.get_left_node()
        else:
            curr = curr.get_right_node()

    return None


def successor(root, key):
    # Find the node in the tree for the give key
    node = findNode(root, key)

    if node is None:
        return "key=" + str(key) + ", Successor=" + str(None)

    # Successor will be on the left most node starting with right side of the node
    if node.get_right_node() is not None:
        curr = node.get_right_node()
        while curr.get_left_node() is not None:
            curr = curr.get_left_node()

        return "key=" + str(key) + ", Successor=" + str(curr.get_key())

    # If there are no left nodes, then look for successor in the ancestor nodes
    ancestor = None
    curr = root
    while curr is not None and curr != node:
        if key < curr.get_key():
            ancestor = curr
            curr = curr.get_left_node()
        else:
            curr = curr.get_right_node()

    if ancestor is None:
        return "key=" + str(key) + ", Successor=" + str(None)

    return "key=" + str(key) + ", Successor=" + str(ancestor.get_key()) + "(ancestor)"


if __name__ == "__main__":
    bst = BST()
    BSTUtil.create_tree_with_data(bst)

    print(successor(bst._root, 65))
    print(successor(bst._root, 54))
    print(successor(bst._root, 82))
    print(successor(bst._root, 76))
    print(successor(bst._root, 80))
    print(successor(bst._root, 44))  # Root node
    print(successor(bst._root, 97))  # Max node
    print(successor(bst._root, 120))  # Non-existent node


'''
OUTPUT:
key=65, Successor=76
key=54, Successor=65(ancestor)
key=82, Successor=88(ancestor)
key=76, Successor=80
key=80, Successor=82(ancestor)
key=44, Successor=54
key=120, Successor=None
'''