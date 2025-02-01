
class SummaryRanges:

    def __init__(self):
        """
        初始化数据结构，用于存储区间起始和结束点以及使用过的数字。
        
        English: Initialize the data structure to store interval starts, ends, and used numbers.
        """
        self.starts, self.ends, self.used = [-float("inf"), float("inf")], [-float("inf"), float("inf")], set()

    def addNum(self, val):
        """
        添加一个数字到区间中，并更新区间状态。
        
        English: Add a number to the intervals and update interval states.
        :param val: int - 要添加的数字
        """
        if val not in self.used:
            self.used.add(val)
            i = bisect.bisect_left(self.starts, val) - 1
            # 如果val正好位于两个区间的间隙处，则合并这两个区间
            if self.ends[i] + 1 == val and val + 1 == self.starts[i + 1]:
                del self.starts[i + 1]
                del self.ends[i]
            # 如果val紧邻当前区间的结束点
            elif self.ends[i] + 1 == val:
                self.ends[i] += 1
            # 如果val紧邻下一个区间的起始点
            elif self.starts[i + 1] == val + 1:
                self.starts[i + 1] -= 1
            # 如果val独立于当前区间和下一个区间
            elif val > self.ends[i]:
                self.starts.insert(i + 1, val)
                self.ends.insert(i + 1, val)

    def getIntervals(self):
        """
        获取所有有效区间的列表。
        
        English: Get the list of all valid intervals.
        :return: List[List[int]] - 区间列表
        """
        return [[s, e] for s, e in zip(self.starts[1:-1], self.ends[1:-1])]  # exclude infinity
