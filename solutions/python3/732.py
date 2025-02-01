
class MyCalendarThree:

    def __init__(self):
        """
        初始化日历对象。
        Initialize the calendar object.
        """
        self.times = []

    def book(self, start: int, end: int) -> int:
        """
        为给定的 'start' 和 'end' 添加一个预订。
        Add a booking for given 'start' and 'end'.
        
        :param start: 预订开始时间
        :param end: 预订结束时间
        :return: 返回当前最大重叠次数
        """
        bisect.insort(self.times, (start, 1))  # 插入开始时间，权重为1（表示增加一个活动）
        bisect.insort(self.times, (end, -1))   # 插入结束时间，权重为-1（表示减少一个活动）

        res = cur = 0
        for _, x in self.times:
            cur += x               # 累加当前活动数
            res = max(res, cur)    # 更新最大重叠次数

        return res
