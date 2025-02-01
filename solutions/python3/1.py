
class Solution:
    # 用于解决两数之和的问题

    def twoSum(self, nums, target):
        # 使用哈希表来存储已经遍历过的数字及其索引，以提高查找效率
        nums_hash = {}
        
        for i in range(len(nums)):
            # 检查目标值减去当前数值是否在哈希表中，如果存在则返回两个数的索引
            if target - nums[i] in nums_hash: 
                return [nums_hash[target - nums[i]], i]
            
            # 将当前数字及其索引存入哈希表
            nums_hash[nums[i]] = i
