    
class MyCalendarTwo:
    """
    MyCalendarTwo 类用于管理两个重叠区间，实现日程安排功能。
    中文说明：MyCalendarTwo 类用于管理和处理双重预订的时间段，支持日程预约功能。
    """

    def __init__(self):
        """
        初始化时创建空的重叠区间列表和日程安排列表。
        中文说明：初始化对象时，创建一个空的重叠区间列表和一个空的日程安排列表。
        """
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        """
        预约一个新的日程，并检查是否有与现有日程冲突的部分，若有，则加入重叠区间列表中；
        如果没有冲突，则添加到日程安排列表中。
        中文说明：预约一个新时间段，并检查是否存在与其他已预订时间段的重叠。若存在重叠，
                  则将重叠部分添加到重叠区间列表中；否则将其添加到日程安排列表中。
        """
        for i, j in self.overlaps:
            if start < j and end > i:  # 检查是否有新的重叠
                return False

        for i, j in self.calendar:
            if start < j and end > i:  # 确认新预定是否与现有日程有冲突
                self.overlaps.append((max(start, i), min(end, j)))  # 记录重叠区间

        self.calendar.append((start, end))  # 添加新的日程安排
        return True
    