class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        * 自顶向下(递归)
        时间复杂度 o(nlogn)
        空间复杂度 o(n)    如果树完全倾斜，递归栈可能包含所有节点。

        """
        if not root:
            return True

        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced_2(self, root: TreeNode) -> bool:
        """
        * 自底向上(递归)  首先判断子树是否平衡，然后比较子树高度判断父节点是否平衡
        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        self.res = True

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)+1
            right = helper(root.right)+1
            if abs(left-right) > 1:
                self.res = False
            return max(left, right)

        helper(root)
        return self.res
