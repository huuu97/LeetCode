class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        *将添加一个哑结点作为辅助，该结点位于列表头部。哑结点用来简化某些极端情况，例如列表中只含有一个结点，或需要删除列表的头部。
        *使用两个指针
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    def findnode(self, head, n):
        """
        找正着数的第三分之一的结点 四分之一 N分之一
        fast比slow多走三倍       四倍    N倍
        找倒着数的第三分之一的结点
        fast走三倍 slow走2倍

        *将添加一个哑结点作为辅助，该结点位于列表头部。哑结点用来简化某些极端情况，例如列表中只含有一个结点，或需要删除列表的头部。
        *使用两个指针
        时间复杂度 o(n)
        空间复杂度 o(1)
        fast-99
        slow-33
        fast-99
        slow-66
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast and fast.next and fast.next.next and fast.next.next.next:
            # fast.next = null 表示 fast 是链表的尾节点
            fast = fast.next.next.next
            slow = slow.next

        return ListNode(slow.val)
