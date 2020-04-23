class Solution:
    def countSquares(self, matrix):
        """
        *dp
        时间复杂度 o(n*n)
        空间复杂度 o(n*n)
        dp[i][j]表示 matrix[i][j] 这个点可以往左上构造的最大正方形的边长

        0 1 1 1      0 1 1 1
        1 1 1 1  ->  1 1 2 2
        0 1 1 1      0 1 2 3
        """
        if len(matrix) < 1:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i == 0 and matrix[i][j] == 1:
                        dp[i][j] = 1
                    elif j == 0 and matrix[i][j] == 1:
                        dp[i][j] = 1
                    elif i != 0 and j != 0 and matrix[i][j] == 1:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    res += dp[i][j]

        return res

