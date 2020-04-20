class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList_1(self, head):
        """
        *递归
        时间复杂度 o(n)
        空间复杂度 o(n) 由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层。
        """
        if not head or not head.next:
            return head
        else:
            result = self.reverseList_1(head.next)
            head.next.next = head
            head.next = None
            return result

    def reverseList_2(self, head):
        """
        *迭代
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        if not head or not head.next:
            return head

        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre
