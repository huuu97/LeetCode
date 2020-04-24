class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        * 栈
        时间复杂度 o(n)
        空间复杂度 o(n)

        * 也可以暴力 每次计算s[i,j],判断是不是valid，然后记录最长的j-i
        时间复杂度 o(n*n)
        空间复杂度 o(n)
        """
        if not s or len(s) < 2:
            return 0
        mlen = 0
        stack = []

        # 防止 )()
        stack.append(-1)
        for i in range(len(s)):
            tmp = s[i]
            if tmp == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mlen = max(mlen, i - stack[-1])

        return mlen
