
class Solution:
    # 检查是否存在一个连续子数组，其和为k的倍数

    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # 如果k为0，则检查是否有两个相邻元素都为0的情况
        if not k:
            return any(nums[i] == nums[i - 1] == 0 for i in range(1, len(nums)))
        
        # 使用集合存储模k后的余数，sm记录当前子数组的累积和
        mods, sm = set(), 0
        
        # 遍历nums中的每个元素
        for i, num in enumerate(nums):
            sm = (sm + num) % k  # 更新累计和对k取模
            
            # 检查当前余数是否在集合中，且当前数字不为0或前一个数字不存在的情况
            if (sm in mods and num or (i and not nums[i - 1])) or (not sm and i):
                return True  # 如果满足条件，则返回True
            
            # 将当前余数加入集合
            mods |= {sm}
        
        # 遍历结束后未找到符合条件的子数组，返回False
        return False
