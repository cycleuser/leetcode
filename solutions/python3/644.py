
class Solution:
    # 寻找长度为k的子数组的最大平均值
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 辅助函数，检查给定mid是否满足条件
        def sub(mid):
            sm = pre = mn = 0
            # 初始化前k个元素的和与最小前缀和
            for i in range(k):
                sm += nums[i] - mid
            if sm >= 0:
                return True
            
            # 遍历剩余元素，维护滑动窗口内的和与最小前缀和
            for i in range(k, len(nums)):
                sm += nums[i] - mid
                pre += nums[i - k] - mid
                mn = min(mn, pre)
                if sm >= mn:
                    return True
            return False
        
        # 初始化二分查找的左右边界
        l, r = min(nums), max(nums)
        
        # 二分查找，找到满足条件的最大mid值
        while l + 1E-6 < r:
            mid = (l + r) / 2
            if sub(mid):
                l = mid
            else:
                r = mid
        
        return l
