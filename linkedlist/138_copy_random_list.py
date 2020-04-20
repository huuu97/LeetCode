class ListNode:
    def __init__(self, x, next, random):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList_1(self, head):
        """
        *回溯
        *此方法中，我们只需要遍历整个图并拷贝它。
        拷贝的意思是每当遇到一个新的未访问过的节点，你都需要创造一个新的节点。遍历按照深度优先进行。
        我们需要在回溯的过程中记录已经访问过的节点，否则因为随机指针的存在我们可能会产生死循环。
        时间复杂度 o(n)
        空间复杂度 o(n) 维护一个已访问字典
        """
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = ListNode(head.val, None, None)
        self.visited[head] = node

        node.next = self.copyRandomList_1(head.next)
        node.random = self.copyRandomList_1(head.random)

        return node

    def copyRandomList_2(self, head):
        """
        *O(1) 空间的迭代
        *并将每个拷贝节点都放在原来对应节点的旁边。这种旧节点和新节点交错的方法让我们可以在不需要额外空间的情况下解决这个问题。
        时间复杂度 o(n)
        空间复杂度 o(1)
        """
        if not head:
            return head
        dummy = head
        while dummy:
            # 1->1'->2->2'->...
            # =左边就是->的左边结点，=右边就是->的右边节点
            node = ListNode(dummy.val, None, None) # 1->2  1'
            node.next = dummy.next                 # 1->2<- 1'
            dummy.next = node                      # 1 -> 1' -> 2
            dummy = node.next                      # 移动到2

        dummy = head
        while dummy:
            if dummy.random:
                dummy.next.random = dummy.random.next
            else:
                dummy.next.random = None
            dummy = dummy.next.next

        old = head
        new = head.next
        re = head.next
        # 1->1'->2->2'->3->3'->None
        # 1->2->3->None    1'->2'->3'->None
        while old:
            old.next = old.next.next
            if new.next:
                new.next = new.next.next
            else:
                new.next = None
            old = old.next
            new = new.next

        return re
