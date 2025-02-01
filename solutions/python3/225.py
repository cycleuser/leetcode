
class MyStack:

    def __init__(self):
        """
        初始化栈数据结构。
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        将元素x压入栈顶。
        :param x: 要添加的整数
        :return: 无返回值，仅为操作方法
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        移除并返回栈顶元素。
        :return: 栈顶元素
        """
        return self.data.pop()

    def top(self) -> int:
        """
        返回栈顶元素，不移除。
        :return: 栈顶元素
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        判断栈是否为空。
        :return: True 表示栈空，False 表示非空
        """
        return not bool(self.data)


# 你的 MyStack 对象将被实例化并调用如下：
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
