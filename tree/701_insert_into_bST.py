# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉搜索树的巨大优势就是：在平均情况下，能够在 O(logN) 的时间内完成搜索和插入元素。


class Solution:
    def insertIntoBST_1(self, root: TreeNode, val: int) -> TreeNode:
        """
        * 递归

        时间复杂度 height, 平均情况logn
        空间复杂度 height 在递归过程中堆栈使用的空间

        注意：二叉搜索树，保持左>中>右

        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

    def insertIntoBST_2(self, root: TreeNode, val: int) -> TreeNode:
        """
        * 迭代

        时间复杂度 height, 平均情况logn
        空间复杂度 1

        """
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left

        return TreeNode(val)
