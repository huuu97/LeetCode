class Solution:
    def generateParentheses(self, n):
        """
        *dfs
        时间复杂度 o((4^n)/(n^1/2))
        空间复杂度 O(n)，我们所需要的空间取决于递归栈的深度，每一层递归函数需要O(1)的空间，最多递归2n层。

        """
        def dfs(n, left, right, strings, result):
            if left == 0 and right == 0:
                result.append(strings[:])
                return result
            if left > right:
                return
            if left > 0:
                dfs(n, left-1, right, strings+"(", result)
            if right > 0:
                dfs(n, left, right-1, strings + ")", result)

        left = n
        right = n
        strings = ""
        result = []
        dfs(n, left, right, strings, result)
        return result
