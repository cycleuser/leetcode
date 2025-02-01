# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
            
        # Sort by start time instead of end time
        intervals.sort(key=lambda x: x[0])
        
        res = []
        for interval in intervals:
            # If result is empty or no overlap with last interval
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If overlap, merge with last interval
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # Add new interval and use existing merge logic
        intervals.append(newInterval)
        return self.merge(intervals)