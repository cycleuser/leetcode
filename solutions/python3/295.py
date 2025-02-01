
class MedianFinder:

    # 初始化数据结构，用于存储左右两部分和中间值
    def __init__(self):
        import heapq  # 引入堆模块
        self.l = []   # 左侧小顶堆
        self.r = []   # 右侧大顶堆
        self.m = []   # 中间值列表

    def addNum(self, num):
        # 如果中间值为空，直接加入第一个数
        if not self.m:
            self.m = [num]
        elif len(self.m) == 1:  # 如果中间值只有一个元素
            m = self.m[0]
            if num >= m:
                # 新数字大于等于当前中间值，左右两堆分别加入
                self.m = [m, heapq.heappushpop(self.r, num)]
            else:
                # 新数字小于当前中间值，调整堆并更新中间值
                self.m = [-heapq.heappushpop(self.l, -num), m]
        else:  # 如果中间值有两个元素
            m1, m2 = self.m
            if num >= m2:
                # 新数字大于等于第二个中间值
                heapq.heappush(self.r, num)
                heapq.heappush(self.l, -m1)
                self.m = [m2]
            elif num <= m1:
                # 新数字小于第一个中间值
                heapq.heappush(self.l, -num)
                heapq.heappush(self.r, m2)
                self.m = [m1]
            else:
                # 新数字在两个中间值之间，调整堆并更新中间值
                heapq.heappush(self.l, -m1)
                heapq.heappush(self.r, m2)
                self.m = [num]

    def findMedian(self):
        # 计算当前所有中间值的平均数作为中位数
        return sum(self.m) / len(self.m)
