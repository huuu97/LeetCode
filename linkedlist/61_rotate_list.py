class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        *先将链表闭合成环,找到相应的位置断开这个环，确定新的链表头和链表尾
        时间复杂度 o(n)
        空间复杂度 o(1)

        k < n : n-k-1
        k >= n: n - k % n - 1
        """
        if not head or not head.next:
            return head
        phead = head
        n = 1
        while phead.next:
            phead = phead.next
            n += 1
        phead.next = head

        ptail = head
        for i in range(n - k % n - 1):
            ptail = ptail.next

        result = ptail.next
        ptail.next = None
        return result
