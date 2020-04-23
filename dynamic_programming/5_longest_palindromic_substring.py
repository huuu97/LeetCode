class Solution:
    def longestPalindrome_1(self, s):
        """
        *dp
        时间复杂度 o(n*n)
        空间复杂度 o(n*n)
        """
        if not s:
            return None
        m = len(s)
        dp = [[0]*m for _ in range(m)]
        res = ""
        max_len = -float("inf")

        for i in range(m):
            for j in range(i+1):
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                if dp[j][i] == 1 and max_len < i+1-j:
                    max_len = i+1-j
                    res = s[j:i+1]
        return res

    def longestPalindrome_2(self, s):
        """
        *中心扩展
        时间复杂度 o(n*n)
        空间复杂度 o(1)
        """
        if not s or len(s) == 1:
            return s
        res = ""
        m = len(s)

        for i in range(1, m):
            left = i - 1
            right = i
            while left >= 0 and right < m and s[left] == s[right]:
                left -= 1
                right += 1
            sub_l = left + 1
            sub_r = right - 1
            if sub_r + 1 - sub_l > len(res):
                res = s[sub_l:sub_r + 1]

            left = i - 1
            right = i + 1
            while left >= 0 and right < m and s[left] == s[right]:
                left -= 1
                right += 1
            sub_l = left + 1
            sub_r = right - 1
            if sub_r + 1 - sub_l > len(res):
                res = s[sub_l:sub_r + 1]

        return res
