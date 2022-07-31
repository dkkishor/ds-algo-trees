'''
Create & Print Binary Search Tree
'''

from BST import BST

def create_tree_with_data(bst):
    # Root Node
    bst.add_node(44)

    # Add Left Nodes
    bst.add_node(17)
    bst.add_node(8)
    bst.add_node(32)
    bst.add_node(28)
    bst.add_node(29)

    # Add Right nodes
    bst.add_node(88)
    bst.add_node(65)
    bst.add_node(97)
    bst.add_node(54)
    bst.add_node(82)
    bst.add_node(93)
    bst.add_node(76)
    bst.add_node(80)


if __name__ == "__main__":
    bst = BST()
    create_tree_with_data(bst)
    print("****** PRINTING IN PREORDER ******")
    bst.print_tree_preorder(bst._root, 0)
    print("----------------------------------")
    print("****** PRINTING IN INORDER ******")
    bst.print_tree_inorder(bst._root, 0)
    print("")
    print("----------------------------------")
    print("****** PRINTING IN POSTORDER ******")
    bst.print_tree_postorder(bst._root, 0)


'''
OUTPUT:
****** PRINTING IN PREORDER ******
44
  17
       8
      32
          28
              29
  88
      65
          54
          82
              76
                  80
      97
          93
----------------------------------
****** PRINTING IN INORDER ******
8 17 28 29 32 44 54 65 76 80 82 88 93 97 
----------------------------------
****** PRINTING IN POSTORDER ******
8 17 28 29 32 54 65 76 80 82 88 93 97 44 
'''
