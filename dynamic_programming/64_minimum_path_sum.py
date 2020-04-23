class Solution:
    def minPathSum(self, grid) -> int:
        """
        *dp
        时间复杂度 o(m*n)
        空间复杂度 o(1)
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0 and i != 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
