class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        *

        时间复杂度 o(n)
        空间复杂度 o(1)

        """
        res = 0
        bit = 1
        a = int(num1)

        for i in num2[::-1]:
            res += int(i) * a * bit
            bit *= 10
        return str(res)
