
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        将新的区间插入到已存在的区间列表中，并调整重叠的区间。

        中文注释：
        - 初始化一个新的空列表 `new` 用于存储合并后的结果
        - 遍历所有现有区间，决定如何处理新插入的区间
            - 如果新区间完全在当前区间的右侧，则直接插入当前区间到 `new`
            - 否则，更新新区间以与当前区间重叠的部分

        英文注释：
        - Initialize an empty list `new` to store the merged intervals.
        - Iterate through all existing intervals and decide how to handle the new interval:
            - If the new interval is completely to the right of the current interval, directly append the current interval to `new`.
            - Otherwise, update the new interval to merge with the overlapping parts.
        """
        
        new, i = [], 0
        for i, it in enumerate(intervals):
            if newInterval[1] < it[0]:
                break  # 新区间在当前区间的右侧，停止遍历
            elif it[1] < newInterval[0]:
                new += it,  # 当前区间完全在新区间的左侧，直接添加到结果中
            else:
                newInterval = [min(it[0], newInterval[0]), max(it[1], newInterval[1])]  # 更新新区间以合并重叠部分
        
        return new + [newInterval] + intervals[i + 1:]  # 返回合并后的区间列表
