class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        *使用两个指针
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
