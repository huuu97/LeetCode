class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height_1(self, root):
        """
        * 递归
        时间复杂度 o(n) 我们每个结点只访问一次
        空间复杂度 o(n+m)
        在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N次（树的高度），因此保持调用栈的存储将是O(N)。
        但在最好的情况下（树是完全平衡的），树的高度将是 log(N)。因此，在这种情况下的空间复杂度将是 O(log(N))。
        """
        if not root:
            return 0
        left = self.height_1(root.left)
        right = self.height_1(root.right)
        return 1 + max(left, right)

    def height_2(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        q = []
        if root is not None:
            q.append((1, root))

        depth = 0
        while q:
            current_depth, root = q.pop()
            if root is not None:
                depth = max(depth, current_depth)
                q.append((current_depth + 1, root.left))
                q.append((current_depth + 1, root.right))

        return depth
