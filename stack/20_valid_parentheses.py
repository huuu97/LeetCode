class Solution:
    def isValid(self, s: str) -> bool:
        """
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        if not s:
            return True
        if len(s) == 1:
            return False
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        stack = []
        idx = 0
        while len(s) > idx:
            if s[idx] in left:
                stack.append(s[idx])
                idx += 1
            else:
                if stack:
                    pre = stack.pop()
                    if right.index(s[idx]) != left.index(pre):
                        return False
                    else:
                        idx += 1
                else:
                    return False
        if not stack:
            return True
        else:
            return False

