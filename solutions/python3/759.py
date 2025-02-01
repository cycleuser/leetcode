
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # 初始化员工的时间段列表，按开始时间排序
    def employeeFreeTime(self, schedule):
        # 将所有时间段按开始时间排序
        intervals = sorted(((intr.start, intr.end) for emp in schedule for intr in emp), key=lambda x: x[0])
        
        # 结果列表和栈的初始化
        res, stack = [], []

        # 遍历排序后的所有时间段
        for s, e in intervals:
            if not stack:
                # 如果栈为空，直接将当前时间段加入栈
                stack.append((s, e))
            elif s <= stack[-1][-1]:
                # 当前时间段与栈顶时间段重叠或相邻，合并它们
                stack.append((s, max(e, stack.pop()[1])))
            else:
                # 找到一个空闲时段，记录并更新栈
                res.append([stack[-1][1], s])
                stack.append((s, e))
        
        return res
