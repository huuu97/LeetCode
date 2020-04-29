class Solution:
    def myAtoi(self, str: str) -> int:
        """
        *
        时间复杂度 o(n)
        空间复杂度 o(1)

        """
        # 先去掉空格确认符号
        i = 0
        size = len(str)
        sign = False
        for i in range(size):
            if str[i] == " ":
                continue
            else:
                if str[i] == "-":
                    sign = True
                    i += 1
                elif str[i] == "+":
                    i += 1
                break
        if i == size:
            return 0
        # 统计数字
        res = 0
        for j in range(i, size):
            if str[j] >= "0" and str[j] <= "9":
                res = res * 10 + int(str[j])
            else:
                break
        # 确认溢出
        if sign:
            res = -res
        if res >= 2 ** 31:
            res = 2 ** 31 - 1
        elif res <= -2 ** 31:
            res = -(2 ** 31)
        return res
