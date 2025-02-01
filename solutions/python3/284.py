
# 以下是Iterator接口的定义，已经为您实现。
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         初始化一个迭代器对象到列表的开始位置。
#         :param nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         返回迭代中是否还有更多元素。
#         :return: bool
#         """
#
#     def next(self):
#         """
#         返回下一个元素在迭代中的值。
#         :return: int
#         """

class PeekingIterator:
    # 初始化时，先检查是否有下一项，并记录当前项
    def __init__(self, iterator):
        self.it = iterator
        self.bool = self.it.hasNext()  # 检查是否还有下一个元素
        self.num = self.it.next() if self.bool else None  # 获取下一个元素，如果没有则为None

    # 查看但不移除队首元素
    def peek(self):
        return self.num

    # 移除并返回当前项（即peek之后的下一项）
    def next(self):
        n = self.num
        self.bool = self.it.hasNext()  # 更新是否有下一个元素的状态
        if self.bool:
            self.num = self.it.next()  # 获取下一个元素
        return n

    # 检查是否还有未处理的元素
    def hasNext(self):
        return self.bool
