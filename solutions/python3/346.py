
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        初始化滑动平均值结构体。
        Initialize the moving average structure.
        :param size: 滑动窗口的大小
        """
        self.arr = deque(maxlen=size)

    def next(self, val: int) -> float:
        """
        添加一个新的数值到队列中，并返回当前窗口内的平均值。
        Add a new value to the queue and return the current window's average.
        :param val: 新的数值
        :return: 当前滑动窗口内的平均值
        """
        self.arr.append(val)
        return sum(self.arr) / len(self.arr)


# 你的 MovingAverage 对象将被实例化并调用如下：
# obj = MovingAverage(size)
# param_1 = obj.next(val)
