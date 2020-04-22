class Solution:
    def isMatch_1(self, s, p):
        if not p:
            return not s
        if len(p) > 1 and p[1] == '*':
            if s and (p[0] == '.' or s[0] == p[0]):
                # *匹配0个前面的，所以p往后跳2个         # *匹配1个前面的，所以s往后跳1个
                return self.isMatch_1(s, p[2:]) or self.isMatch_1(s[1:], p)
            # *匹配0个前面的，所以p往后跳2个
            return self.isMatch_1(s, p[2:])
        if s and (p[0] == '.' or s[0] == p[0]):
            return self.isMatch_1(s[1:], p[1:])
        return False

