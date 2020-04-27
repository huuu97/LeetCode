class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        * 中序遍历
        时间复杂度 o(n) 最坏情况下（树为二叉搜索树或破坏条件的元素是最右叶结点）为O(N)
        空间复杂度 o(n) 存储q1

        """
        if not root:
            return True

        mid = -float("inf")
        q1 = []

        while root or q1:
            while root:
                q1.append(root)
                root = root.left

            node = q1.pop()
            # mid就是前一个节点的大小，理论上二叉搜索树的前一个点要小于后一个点，故不应该mid大于新的node
            if node.val <= mid:
                return False
            mid = node.val
            root = node.right

        return True

    def isValidBST_2(self, root):
        """
        * 递归
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        def helper(node, lower, upper):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.left, lower, val):
                return False

            if not helper(node.right, val, upper):
                return False

            return True

        return helper(root, -float("inf"), float("inf"))

    def isValidBST_3(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        if not root:
            return True
        q = [(root, -float("inf"), float("inf"))]
        while q:
            root, lower, upper = q.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            q.append((root.right, val, upper))
            q.append((root.left, lower, val))
        return True





solution = Solution()
a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(3)
p = solution.isValidBST(a)
print(p)
