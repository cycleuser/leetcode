
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # minMeetingRooms - 返回需要的最小会议室数量
    # @param intervals: List[Interval], 会议区间列表
    # @return: int, 最小会议室数量
    def minMeetingRooms(self, intervals):
        # 按照会议开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        # 使用最小堆记录当前使用中的会议结束时间
        heap, time, rooms = [], 0, 0
        
        for intr in intervals:
            # 弹出所有已经结束的会议，减少正在使用的会议室数量
            while heap and heap[0] <= intr.start:
                heapq.heappop(heap)
            
            # 将当前会议结束时间入堆，并增加使用中的会议室数量
            heapq.heappush(heap, intr.end)
            
            if len(heap) > rooms:
                rooms += 1
        
        return rooms

