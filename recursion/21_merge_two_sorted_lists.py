class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists_2(self, l1, l2):
        """
        * 递归
        时间复杂度 o(n+m)
        空间复杂度 o(n+m)  每个元素都一定已经被遍历过了，所以 n + m 个栈帧会消耗 O(n + m)的空间。

        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists_2(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists_2(l1.next, l2)
            return l1



    def mergeTwoLists_1(self, l1, l2):
        """
        * 迭代
        时间复杂度 o(n+m)
        空间复杂度 o(1)

        """
        res = ListNode(0)
        p = res
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next

        if l1:
            p.next = l1

        if l2:
            p.next = l2

        return res.next
