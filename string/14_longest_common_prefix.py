class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        * 垂直扫描
        时间复杂度 O(S)，S 是所有字符串中字符数量的总和。
        空间复杂度 o(1)

        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]

        return strs[0]
