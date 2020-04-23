class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """
        *dp f[i] = cost[i] + min(f[i+1], f[i+2])
        时间复杂度 o(n)
        空间复杂度 o(1)
        """

        m = len(cost)
        f1 = 0
        f2 = 0

        for i in range(m - 1, -1, -1):
            f0 = cost[i] + min(f1, f2)
            f2 = f1
            f1 = f0
        return min(f1, f2)
