
class Solution:
    # Python 解决方案类

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化左右指针和数组长度
        l, r, n = 0, len(nums) - 1, len(nums)
        
        # 使用二分查找进行优化
        while l <= r:
            mid = (l + r) // 2
            # 处理边界情况，获取前后元素值
            pre, after = mid == 0 and -float("inf") or nums[mid - 1], mid == n - 1 and -float("inf") or nums[mid + 1]
            
            # 当前元素为峰值返回其索引
            if pre < nums[mid] > after: return mid
            
            # 根据比较结果调整左右指针位置
            elif pre > nums[mid]: r = mid - 1
            else: l = mid + 1
