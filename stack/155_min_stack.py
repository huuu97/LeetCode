class MinStack:
    """
    * 栈
    时间复杂度 o(1)
    空间复杂度 o(n)

    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.assit = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.assit.append(x)
        else:
            self.stack.append(x)
            if self.assit[-1] >= x:
                self.assit.append(x)

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.assit[-1]:
            self.assit.pop()

    def top(self) -> int:
        if not self.stack:
            return
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.assit:
            return self.assit[-1]
        else:
            return

        # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()