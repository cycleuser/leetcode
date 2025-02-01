
class Solution:
    # 中文注释：定义一个名为Solution的类，包含单个数字查找方法singleNumber

    def singleNumber(self, nums):
        # 中文注释: 单个数字查找逻辑
        
        # 英文注释: Function to find the single number in a list of integers
        return ((sum(set(nums)) * 3) - sum(nums)) // 2
