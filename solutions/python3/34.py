
class Solution(object):
    # 搜索目标值target在有序数组nums中的起始和结束位置

    def searchRange(self, nums, target):
        # 使用二分查找确定左边界
        l = bisect.bisect_left(nums, target)
        
        # 使用二分查找确定右边界，注意需要减1以获取正确的索引
        r = bisect.bisect_right(nums, target) - 1
        
        # 检查左右边界是否有效
        return [l, r] if 0 <= l <= r else [-1, -1]
