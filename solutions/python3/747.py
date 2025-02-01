
class Solution:
    # 定义一个Solution类，用于解决主要逻辑
    
    def dominantIndex(self, nums: List[int]) -> int:
        # 寻找数组nums中的最大值mx
        mx = max(nums)
        
        # 检查除了最大值外的所有元素是否都小于等于最大值的一半
        if all(num * 2 <= mx for num in nums if num < mx):
            # 如果满足条件，则返回最大值的索引
            return nums.index(mx)
        else:
            # 否则返回-1
            return -1
