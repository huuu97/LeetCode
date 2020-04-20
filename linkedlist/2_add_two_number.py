class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers_1(self, head1, head2):
        """
        *用一个数组来存储加和的结果
        时间复杂度 o(max(m,n))
        空间复杂度 o(max(m,n))+1
        """
        dummy1 = head1
        dummy2 = head2
        add = 0
        re = []
        while dummy1 and dummy2:
            value = dummy1.val + dummy2.val + add
            if value >= 10:
                re.append(value-10)
                add = 1
            else:
                re.append(value)
                add = 0
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        while dummy1:
            value = dummy1.val + add
            if value >= 10:
                re.append(value-10)
                add = 1
            else:
                re.append(value)
                add = 0
            dummy1 = dummy1.next

        while dummy2:
            value = dummy2.val + add
            if value >= 10:
                re.append(value-10)
                add = 1
            else:
                re.append(value)
                add = 0
            dummy2 = dummy2.next

        if add == 1:
            re.append(1)

        head = ListNode(0)
        du = head
        for i in re:
            head.next = ListNode(i)
            head = head.next
        return du.next

    def addTwoNumbers_2(self, head1, head2):
        """
        *直接得到新的结点
        时间复杂度 o(max(m,n))
        空间复杂度 o(max(m,n))+1
        """
        dummy1 = head1
        dummy2 = head2
        add = 0
        re = ListNode(0)
        dummy = re
        while dummy1 and dummy2:
            value = dummy1.val + dummy2.val + add
            if value >= 10:
                dummy.next = ListNode(value-10)
                add = 1
            else:
                dummy.next = ListNode(value)
                add = 0
            dummy1 = dummy1.next
            dummy2 = dummy2.next
            dummy = dummy.next

        while dummy1:
            value = dummy1.val + add
            if value >= 10:
                dummy.next = ListNode(value-10)
                add = 1
            else:
                dummy.next = ListNode(value)
                add = 0
            dummy1 = dummy1.next
            dummy = dummy.next

        while dummy2:
            value = dummy2.val + add
            if value >= 10:
                dummy.next = ListNode(value-10)
                add = 1
            else:
                dummy.next = ListNode(value)
                add = 0
            dummy2 = dummy2.next
            dummy = dummy.next

        if add == 1:
            dummy.next = ListNode(1)

        return re.next
