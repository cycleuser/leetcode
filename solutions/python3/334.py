
class Solution:
    # 检查是否存在一个严格递增的三元组
    def increasingTriplet(self, nums):
        mn = None  # 初始化最小值为None
        for i in range(len(nums)):
            if mn is None or nums[i] < mn: 
                mn = nums[i]
            # 更新nums数组，包含是否是严格递增的标志和当前元素值
            nums[i] = [False, nums[i]] if mn >= nums[i] else [True, nums[i]]
        
        mn = None  # 清空最小值变量
        for i in range(len(nums)):
            # 如果当前元素是严格递增且小于已记录的最小值，更新最小值
            if nums[i][0] and (mn is None or nums[i][1] < mn):
                mn = nums[i][1]
            # 检查是否存在一个严格递增的三元组
            elif mn is not None and mn < nums[i][1]:
                return True
        
        return False  # 如果没有找到，返回False
