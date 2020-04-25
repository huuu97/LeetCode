class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        """
        * 递归
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []
        if root:
            self.res.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)

        return self.res


class Solution_2:
    def preorderTraversal(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []
        q1 = []
        q2 = []
        while root or q1:
            if root:
                q1.append(root)
                q2.append(root.val)
                root = root.left
            else:
                node = q1.pop()
                root = node.right
        return q2
