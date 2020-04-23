class Solution:
    def spiralOrder(self, matrix):
        """
        n是输入矩阵所有元素的个数。
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        if not matrix:
            return []

        res = []
        while matrix:
            if [] in matrix:
                break
            # top
            if matrix:
                for e in matrix[0]:
                    res.append(e)
                matrix.pop(0)

            if [] in matrix:
                break
            # right
            if matrix:
                for i in range(len(matrix)):
                    res.append(matrix[i][-1])
                    matrix[i].pop()

            if [] in matrix:
                break
            # bottom
            if matrix:
                for e in matrix[-1][::-1]:
                    res.append(e)
                matrix.pop()

            if [] in matrix:
                break
            # left
            if matrix:
                for i in range(len(matrix)-1, -1, -1):
                    res.append(matrix[i][0])
                    matrix[i].pop(0)

        return res

solution = Solution()
a = solution.spiralOrder([[3],[6],[9]])
print(a)