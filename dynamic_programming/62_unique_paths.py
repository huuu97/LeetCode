class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        *dp
        时间复杂度 o(m*n)
        空间复杂度 o(m*n)
        """
        dp = [[1]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[n][m]
