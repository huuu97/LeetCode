class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        * 递归
        时间复杂度 o(n) 我们每个结点只访问一次
        空间复杂度 o(n) 递归将会被调用 N次（树的高度），因此保持调用栈的存储将是O(N)。

        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # //左子树上能找到，但是右子树上找不到，此时就应当直接返回左子树的查找结果
        if left and not right:
            return left
        # //右子树上能找到，但是左子树上找不到，此时就应当直接返回右子树的查找结果
        if not left:
            return right
        # // 左右子树上均能找到，说明此时的p结点和q结点分居root结点两侧，此时就应当直接返回root结点
        return root


class Solution2:
    answer = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        * 递归
        时间复杂度 o(n) 我们每个结点只访问一次
        空间复杂度 o(n) 递归将会被调用 N次（树的高度），因此保持调用栈的存储将是O(N)。

        """
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            mid = False
            if node == p or node == q:
                mid = True
            if mid + left + right >= 2:
                self.answer = node
            return mid or left or right

        dfs(root)
        return self.answer
