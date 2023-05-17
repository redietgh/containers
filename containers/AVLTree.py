'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the
BinaryTree and BST files,,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):

    def __init__(self, xs=None):
        super().__init__()

    def balance_factor(self):
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        if node is None:
            return True
        ret = True
        if node.left:
            if AVLTree._balance_factor(node) >= -1 \
                    and AVLTree._balance_factor(node) <= 1:
                ret &= AVLTree._is_avl_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if AVLTree._balance_factor(node) >= -1 \
                    and AVLTree._balance_factor(node) <= 1:
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        if node is None or node.right is None:
            return node
        newroot = Node(node.right.value)
        newroot.right = node.right.right

        newleft = Node(node.value)
        newleft.left = node.left
        newleft.right = node.right.left

        newroot.left = newleft
        return newroot

    @staticmethod
    def _right_rotate(node):
        if node is None or node.left is None:
            return node
        newroot = Node(node.left.value)
        newroot.left = node.left.left

        newright = Node(node.value)
        newright.right = node.right
        newright.left = node.left.right

        newroot.right = newright
        return newroot

    def insert(self, value):
        super().insert(value)
        self.root = AVLTree._insertv(self.root)
        print("self.root=", self.root)
        return self.root

    @staticmethod
    def _insertv(node):
        if node is None:
            return node
        if AVLTree._balance_factor(node) < -1 \
                or AVLTree._balance_factor(node) > 1:
            node = AVLTree._rebalance(node)
        if node.left:
            node.left = AVLTree._insertv(node.left)
        if node.right:
            node.right = AVLTree._insertv(node.right)
        print("node=", node)
        return node

    @staticmethod
    def _rebalance(node):
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
        return node

    def insert_list(self, xs):
        for x in xs:
            AVLTree.insert(self, value=x)
