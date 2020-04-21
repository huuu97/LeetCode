class Solution:
    def permute_1(self, nums):
        """
        *dfs
        时间复杂度 o(N*N!)   树形 N!个叶结点，每叶节点构成的树高为N
        空间复杂度 o(n!)     解的个数
        """
        def dfs(nums, used, n, path, result):
            if len(path) == n:
                result.append(path[:])
                return result
            for j in range(n):
                if used[j] == 0:
                    path.append(nums[j])
                    used[j] = 1
                    dfs(nums, used, n, path, result)
                    used[j] = 0
                    path.pop()

        used = [0]*len(nums)
        result, path = [], []
        dfs(nums, used, len(nums), path, result)
        return result

