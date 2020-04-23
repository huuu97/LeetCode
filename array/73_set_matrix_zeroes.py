class Solution:
    def setZeroes_1(self, matrix):
        """
        时间复杂度 o(m*n)
        空间复杂度 o(m+n)
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in range(m):
            for j in range(n):
                if i in row:
                    matrix[i][j] = 0
                if j in col:
                    matrix[i][j] = 0

        return matrix

    def setZeroes_2(self, matrix):
        """
        时间复杂度 o(m*n)
        空间复杂度 o(1)
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        row = False
        col = False
        for i in range(m):
            if matrix[i][0] == 0:
                col = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                row = True
                break
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row:
            for i in range(n):
                matrix[0][i] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0

