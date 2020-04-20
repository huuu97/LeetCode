class Solution:
    def twosum_1(self, array, target):
        """
        *暴力法
        时间复杂度 o(n^2)
        空间复杂度 o(1)
        """
        n = len(array)
        result = [0]*2
        for i in range(n):
            for j in range(i+1, n):
                if array[i] + array[j] == target:
                    result[0] = i
                    result[1] = j
                    return result
        return None

    def twosum_2(self, array, target):
        """
        *一遍hash
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        map = {}
        for idx, val in array:
            if target - val in map:
                return [map[target-val], idx]
            else:
                map[target-val] = idx
        return None
