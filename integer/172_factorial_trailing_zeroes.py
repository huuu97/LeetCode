class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        * 找规律 每9个一轮
        时间复杂度 o(logn)
        空间复杂度 o(1)
        规律是每隔 5 个数，出现一个 5，每隔 25 个数，出现 2 个 5，每隔 125 个数，出现 3 个 5...
        5 的个数就是 n / 5 + n / 25 + n / 125 ...
        """
        if n < 5:
            return 0
        x = 5
        y = 0
        while x <= n:
            y += n // x
            x *= 5
        return y
