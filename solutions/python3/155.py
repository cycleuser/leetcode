
class MinStack:

    def __init__(self):
        """
        初始化最小栈结构。
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        将元素 x 压入栈中。如果 x 小于当前栈顶的最小值，则将 x 作为新的最小值压入栈中。
        """
        if not self.data or x < self.data[-1][1]:
            self.data.append([x, x])
        else:
            self.data.append([x, self.data[-1][1]])

    def pop(self):
        """
        :rtype: void
        弹出栈顶元素。
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        获取当前栈顶的值，但不弹出它。
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        返回当前栈中的最小值。
        """
        return self.data[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
