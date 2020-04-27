class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.array = []

    def inorderTraversal(self, root):
        """
        * 递归
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return []

        if root.left:
            self.inorderTraversal(root.left)

        self.array.append(root.val)

        if root.right:
            self.inorderTraversal(root.right)

        return self.array


class Solution_2:
    def inorderTraversal(self, root):
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
            while root:
                q1.append(root)
                root = root.left

            node = q1.pop()
            q2.append(node.val)
            root = node.right

        return q2
