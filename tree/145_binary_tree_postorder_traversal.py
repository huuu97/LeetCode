class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root):
        """
        * 递归
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []

        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        if root:
            self.res.append(root.val)

        return self.res


class Solution_2:
    def postorderTraversal(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []
        q1 = []
        q2 = []
        q1.append(root)
        while q1:
            node = q1.pop()
            q2.insert(0, node.val)
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)

        return q2
