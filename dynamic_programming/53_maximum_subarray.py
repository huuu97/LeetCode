class Solution:
    def maxSubArray(self, nums) -> int:
        """
        *dp
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        if not nums:
            return 0
        m = len(nums)
        maximum = nums[0]
        for i in range(1, m):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            if nums[i] > maximum:
                maximum = nums[i]
        return maximum
