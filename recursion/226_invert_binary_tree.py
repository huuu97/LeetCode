class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        * 递归
        时间复杂度 o(n) 我们每个结点只访问一次
        空间复杂度 o(n) 递归将会被调用 N次（树的高度），因此保持调用栈的存储将是O(N)。

        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root

    def invertTree_2(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return
        q = []
        q.append(root)
        while q:
            node = q.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
