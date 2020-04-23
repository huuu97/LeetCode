class Solution:
    def isMatch_1(self, s, p):
        if not p:
            return not s
        if len(p) > 1 and p[1] == '*':
            if s and (p[0] == '.' or s[0] == p[0]):
                # aa a*/.*
                # *匹配0个前面的，所以p往后跳2个 eg: aa a*a*    # *匹配1个前面的，所以s往后跳1个 eg: aa .*a
                return self.isMatch_1(s, p[2:]) or self.isMatch_1(s[1:], p)
            # aa c*
            # *匹配0个前面的，所以p往后跳2个 eg: aa c*a*
            return self.isMatch_1(s, p[2:])
        if s and (p[0] == '.' or s[0] == p[0]):
            # eg: aa .a, aa aa
            return self.isMatch_1(s[1:], p[1:])
        return False

    def isMatch(self, s: str, p: str) -> bool:
        ls, lp = len(s), len(p)
        dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
        dp[0][0] = True
        for j in range(2, lp + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                m, n = i - 1, j - 1
                if p[n] == '*':
                    if s[m] == p[n - 1] or p[n - 1] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                elif s[m] == p[n] or p[n] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]

solution = Solution()
a = solution.isMatch("aa", "c*a*")
print(a)