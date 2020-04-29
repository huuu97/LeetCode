class Solution:
    def addDigits(self, num: int) -> int:
        """
        * 找规律 每9个一轮
        时间复杂度 o(1)
        空间复杂度 o(1)

        0 -> 9
        """
        if num % 9 == 0 and num != 0:
            num = 9
        else:
            num %= 9

        return num
