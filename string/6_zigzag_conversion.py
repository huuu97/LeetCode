class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        *
        时间复杂度 o(n)  遍历一遍字符串 s；
        空间复杂度 o(n)  各行字符串共占用 O(N) 额外空间。

        """
        if numRows < 2:
            return s
        res = [""]*numRows
        i, flag = 0, -1
        for c in s:
            # 把每个字符 c 填入对应行
            res[i] += c
            if i == 0 or i == numRows - 1:
                #  在达到 Z 字形转折点时，执行反向。
                flag = -flag
            #  更新当前字符 c 对应的行索引；
            i += flag

        return "".join(res)
