class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_1(self, head):
        """
        *哈希表
        时间复杂度 o(n)
        空间复杂度 o(n)
        """
        visited = {}
        if not head or not head.next:
            return False
        while head:
            if head not in visited:
                visited[head] = head.val
            else:
                return True
            head = head.next
        return False

    def hasCycle_2(self, head):
        """
        *快慢指针
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        if not head or not head.next:
            return False
        fast = head
        slow = head
        while fast and fast.next:  # and fast.next!!!!!!
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
