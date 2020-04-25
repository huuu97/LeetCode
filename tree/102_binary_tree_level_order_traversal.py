class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder_1(self, root: TreeNode):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []
        q1 = []
        q2 = []
        res = []
        q1.append(root)
        while q1:
            n = len(q1)
            for _ in range(n):
                node = q1.pop(0)
                q2.append(node.val)
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            res.append(q2)
            q2 = []

        return res

    def levelOrder_2(self, root: TreeNode):
        """
        * 递归
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []
        levels = []

        def helper(node, level, levels):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level+1, levels)
            if node.right:
                helper(node.right, level+1, levels)
            return levels

        helper(root, 0, levels)
        return levels

