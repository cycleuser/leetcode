
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化二分查找的边界
        low, high, mid = 0, len(nums) - 1, (len(nums) - 1) // 2
        
        # 当搜索区间大于1时继续循环
        while high - low > 1:
            # 更新mid位置，并统计范围内元素数量
            count, mid = 0, (high + low) // 2
            
            for k in nums:
                if mid < k <= high: 
                    count += 1
            
            # 根据计数结果调整搜索区间
            if count > high - mid:
                low = mid
            else:
                high = mid
        
        return high
