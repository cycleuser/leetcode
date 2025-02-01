
class MyQueue:

    def __init__(self):
        """
        初始化队列数据结构。
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        将元素x添加到队列末尾。
        :param x: 待添加的整数
        :return: 无返回值
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        移除并返回队列前端的元素。
        :return: 前端元素，类型为int
        """
        front = self.data[0]
        self.data = self.data[1:]
        return front

    def peek(self) -> int:
        """
        返回队列前端的元素，不移除它。
        :return: 前端元素，类型为int
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        检查队列是否为空。
        :return: 如果队列为空返回True，否则返回False
        """
        return not bool(self.data)


# 对象将被实例化并调用如下：
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
