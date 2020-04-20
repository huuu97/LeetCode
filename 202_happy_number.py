class Solution:
    def isHappy_1(self, n):
        # 如果不是快乐数 最终会出现1, 4 16 37 58 89 145 42 20循环
        """
        *使用set
        检查数字是否在哈希集中需要O(1)的时间，而对于其他数据结构，则需要O(n)的时间。选择正确的数据结构是解决这些问题的关键部分。
        时间复杂度 o(logn)
        空间复杂度 o(logn)
        """
        seen = set()
        num = list(str(n))
        sum = 0
        while True:
            for i in num:
                sum += int(i) ** 2
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)

            num = list(str(sum))
            sum = 0

    def isHappy_2(self, n):
        """
        *使用两个指针
        时间复杂度 o(logn)
        空间复杂度 o(1)
        """
        def get_next(n):
            sum = 0
            num = list(str(n))
            for i in num:
                sum += int(i) ** 2
            return sum

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
