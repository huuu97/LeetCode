class Solution(object):
    def partitionLabels(self, S):
        """
        * 贪心 对于遇到的每一个字母，去找这个字母最后一次出现的位置，用来更新当前的最小区间。
        时间复杂度 O(n)，  N 为 S 的长度
        空间复杂度 o(n)    存储每个字符的位置

        """
        last = {}
        # 来表示字符 char 最后一次出现的下标
        for idx, c in enumerate(S):
            last[c] = idx
        # anchor 和 j 来表示当前区间的首尾
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            # 遍历到了当前区间的末尾
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


