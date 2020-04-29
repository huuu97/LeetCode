class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        * 转成string

        时间复杂度 o(logn)
        空间复杂度 o(1)

        """
        if x < 0:
            return False
        s = str(x)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
