class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        * 栈
        时间复杂度 o(n) 虽然外循环里面还有一个内循环，但内循环的次数受栈中剩余字符总数的限制，
        空间复杂度 o(n)

        "bcabc" -> "abc"
        "bcabac" ->  "abc"
        """
        size = len(s)

        last_appear_index = [0 for _ in range(26)]
        if_in_stack = [False for _ in range(26)]

        # 记录每个字符最后一次出现的索引
        for i in range(size):
            last_appear_index[ord(s[i]) - ord('a')] = i

        stack = []
        for i in range(size):
            # 如果读到的字符在栈中已经存在，舍弃这个字符；
            if if_in_stack[ord(s[i]) - ord('a')]:
                continue

            # 如果读到的ASCII值比栈顶元素小，看看栈顶元素在后面是否还会出现，
            # 如果还会出现，则舍弃栈顶元素，而选择后出现的那个字符，这样得到的字典序更小。
            while stack and ord(stack[-1]) > ord(s[i]) and last_appear_index[ord(stack[-1]) - ord('a')] >= i:
                top = stack.pop()
                if_in_stack[ord(top) - ord('a')] = False

            # 遍历字符串里的字符，如果读到的字符的ASCII值是升序，依次存到一个栈中；
            stack.append(s[i])
            if_in_stack[ord(s[i]) - ord('a')] = True

        return ''.join(stack)
