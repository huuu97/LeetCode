class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        * 递归
        时间复杂度 o(n) 我们每个结点只访问一次
        空间复杂度 o(n)  递归调用的次数受树的高度限制。在最糟糕情况下，树是线性的，其高度为O(n)。
        """
        return self.mirror(root, root)

    def mirror(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return r1.val == r2.val and self.mirror(r1.left, r2.right) and self.mirror(r1.right, r2.left)

    def isSymmetric_2(self, root):
        """
        * 迭代
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        q = []
        q.append((root, root))

        while q:
            node1, node2 = q.pop()
            if not node1 and not node2:
                continue
            if not node2 or not node1:
                return False
            if node1.val != node2.val:
                return False
            q.append((node1.left, node2.right))
            q.append((node1.right, node2.left))

        return True


