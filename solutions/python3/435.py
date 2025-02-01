
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # 优化：通过按结束时间排序来减少重叠区间
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.end)  # 按照区间结束时间进行升序排序
        
        res = 0  # 记录需要移除的重叠区间数量
        curr = -float("inf")  # 初始化当前选择区间的终点为负无穷，确保第一个区间能被选中

        for i in intervals:
            if curr > i.start:  # 当前选择的区间和下一个区间有重叠
                res += 1  # 增加需要移除的数量
            else:  # 如果没有重叠
                curr = i.end  # 更新当前选择区间的终点为下一个区间的结束时间
        
        return res  # 返回需要移除的重叠区间数量
