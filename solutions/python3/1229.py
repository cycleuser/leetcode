
class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], d: int) -> List[int]:
        """
        初始化s2排序，以便后续快速查找。
        :param s1: 第一个人的预约时间段列表
        :param s2: 第二个人的预约时间段列表
        :param d: 最小可用时长
        :return: 满足条件的时间段 [开始时间, 结束时间]
        """
        s2.sort()  # Sort s2 to enable quick lookup

        j = 0  # Pointer for iterating through sorted s2
        for start1, end1 in sorted(s1):  # Iterate through each slot of s1 after sorting
            while j < len(s2) - 1 and s2[j][1] < start1:
                j += 1  # Skip slots in s2 that end before the current slot in s1 starts

            if s2[j][0] <= end1:  # Check if there's an overlap with the current slot in s2
                left, right = max(start1, s2[j][0]), min(end1, s2[j][1])  # Determine overlapping interval
                if right - left >= d:  # If the interval is at least `d` units long
                    return [left, left + d]  # Return the available slot
