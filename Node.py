'''
Creates a single node of a tree
'''
class Node:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = None;
        self._right = None;

    def set_left_node(self, node):
        self._left = node

    def set_right_node(self, node):
        self._right = node

    def get_key(self):
        return self._key

    def get_left_node(self):
        return self._left

    def get_right_node(self):
        return self._right
