class Solution:
    def minIncrementForUnique(self, A) -> int:
        """
        时间复杂度 o(nlogn)
        空间复杂度 o(1)
        3 2 1 2 1 7
        sort:1 1 2 2 3 7
        new: 1 2 3 4 5 7
        """
        if not A:
            return 0
        A.sort()
        rs = 0
        t = A[0]
        for i in range(1, len(A)):
            if A[i] <= t:
                rs = rs + t + 1 - A[i]
                A[i] = t + 1

            t = A[i]

        return rs
