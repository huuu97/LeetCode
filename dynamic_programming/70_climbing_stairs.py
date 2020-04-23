class Solution:
    def climbStairs(self, n: int) -> int:
        """
        *dp
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        if n < 4:
            return n
        a = [0, 1, 2, 3]
        for i in range(4, n+1):
            a.append(a[i-1] + a[i-2])
        return a[-1]
