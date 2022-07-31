'''
Creates Binary Search Tree (BST) structure with sample data
'''

from Node import Node

class BST:
    def __init__(self):
        self._root = None

    def add_node(self, key):
        newnode = Node(key, key)

        if self._root is None:
            self._root = newnode
            return

        curr = self._root
        prev = None
        while curr is not None:
            prev = curr
            if key == curr.get_key():
                raise Exception("Key already exists")
            elif key < curr.get_key():
                curr = curr.get_left_node()
            else:
                curr = curr.get_right_node()

        if key < prev.get_key():
            prev.set_left_node(newnode)
        else:
            prev.set_right_node(newnode)

    def print_tree_preorder(self, node, level):
        if node is None:
            return

        print(str(node.get_key()).rjust(level*4, ' '))
        self.print_tree_preorder(node.get_left_node(), level + 1)
        self.print_tree_preorder(node.get_right_node(), level + 1)

        return

    def print_tree_inorder(self, node, level):
        if node is None:
            return

        self.print_tree_inorder(node.get_left_node(), level + 1)
        print(str(node.get_key()), end=' ')
        self.print_tree_inorder(node.get_right_node(), level + 1)

        return

    def print_tree_postorder(self, node, level):
        if node is None:
            return

        self.print_tree_inorder(node.get_left_node(), level + 1)
        self.print_tree_inorder(node.get_right_node(), level + 1)
        print(str(node.get_key()), end=' ')

        return
