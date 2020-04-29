class Solution:
    def reverse_1(self, x: int) -> int:
        """
        * 转成string

        时间复杂度 o(n)
        空间复杂度 o(1)

        """
        sign = False
        if x < 0:
            sign = True
            x = abs(x)

        new = str(x)
        res = int(new[::-1])
        if res > 2**31:
            return 0
        if sign:
            res = -res
        return res

    def reverse_2(self, x: int) -> int:
        """
        * 求余

        时间复杂度 o(logn)   x 中大约有log 10(x) 位数字。
        空间复杂度 o(1)

        """
        sign = False
        if x < 0:
            sign = True
            x = abs(x)
        res = 0
        while x/10 > 0:
            y = x%10
            res = res*10 + y
            x = x //10

        if res > 2**31:
            return 0
        if sign:
            res = -res
        return res
