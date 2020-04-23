class Solution:
    def generate(self, numRows: int):
        """
        *dp
        时间复杂度 o(n*n)
        空间复杂度 o(1)
        """
        res = []
        for i in range(1,numRows+1):
            row = [1]*i
            if i > 2:
                for j in range(1,i-1):
                    row[j] = res[-1][j-1] + res[-1][j]
            res.append(row)

        return res
