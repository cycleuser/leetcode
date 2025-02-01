
# Definition for an interval.
class Interval:
    # 初始化区间对象，包含开始和结束时间
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    """
    检查会议是否可以参加。
    
    参数：
    intervals : List[Interval] - 一个表示区间的列表
    
    返回值：
    bool - 如果所有区间不重叠，则返回 True，否则返回 False
    """
    def canAttendMeetings(self, intervals):
        # 根据区间的结束时间进行排序
        intervals.sort(key=lambda x: x.end)
        
        # 检查相邻两个区间的开始时间和前一个区间的结束时间是否冲突
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        # 如果循环未返回 False，则所有区间不重叠
        return True
